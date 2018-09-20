from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from journal.forms import StudentJournalEntryLarge
from journal.functions import move_mark_reflection_to_journal_student
from osd.decorators import *
from django.urls import reverse, reverse_lazy
from journal.models import StudentJournalEntry
from django.db.models import Sum
from operator import itemgetter
import datetime

from .models import *
import logging
from .functions.adddata import *
import os

logger = logging.getLogger(__name__)


@login_required()
def splash(request):
    if request.user.groups.filter(name='Students'):
        student = Student.objects.get(user=request.user)

        return redirect(reverse('tracker:student_profile', args=(student.pk,)))

    if request.user.groups.filter(name='Teachers'):
        teacher = Teacher.objects.get(user=request.user)

        # Show the teacher's students
        students = Student.objects.filter(classgroups__groupteacher=teacher).order_by('user__last_name').order_by('classgroups__groupname')

        # Show the teacher's exams

        sittings = Sitting.objects.filter(classgroup__groupteacher=teacher)

        return render(request, 'tracker/splash_teacher.html', {'teacher': teacher,
                                                               'students': students,
                                                               'sittings': sittings})


@own_or_teacher_only
def student_profile(request, student_pk):
    # For the first (classgroups) table
    student = Student.objects.get(pk=student_pk)
    classes = student.classgroups.all()
    data = {'student': student,
            'sittings': Sitting.objects.filter(classgroup__in=classes),
            'classes': classes}

    # To get the assessments the student has sat:

    sittings = Sitting.objects.filter(classgroup__in=classes)
    scores = []
    for sitting in sittings:
        scores.append(sitting.student_total(student))
    sitting_data = list(zip(sittings, scores))
    data['sitting_data'] = sitting_data

    # Get syllabus ratings:

    syllabuss_learned = []
    for classgroup in student.classgroups.all().distinct():
        syllabuss_learned.append(classgroup.syllabustaught.all())

    for syllabus in syllabuss_learned:
        points_learned = SyllabusPoint.objects.filter(topic__syllabus__in=syllabus).order_by('number').order_by(
            'topic').order_by('topic__syllabus')

    student_ratings = []
    for point in points_learned:
        x = point.get_student_rating(student)
        student_ratings.append(x)

    syllabus_data = list(zip(points_learned, student_ratings))

    data['syllabus_data'] = syllabus_data

    return render(request, 'tracker/splash_student.html', data)


@teacher_only
def add_test(request):
    '''Take the information for the first stage of a new test record'''

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewExamForm(request.POST)
        if form.is_valid():
            new_exam = form.save()

            return redirect(reverse('tracker:examDetail', args=(new_exam.pk,)))

        else:
            return render(request, 'tracker/new_exam1.html', {'form': form})

    else:
        form = NewExamForm()
    return render(request, 'tracker/new_exam1.html', {'form': form})


@teacher_only
def list_syllabuses(request):
    syllabuses = Syllabus.objects.order_by('examtype')
    return render(request, 'tracker/syllabus.html', {'syllabuses': syllabuses})


@login_required
def syllabus_detail(request, pk):

    syllabus = get_object_or_404(Syllabus, pk=pk)
    topics = SyllabusTopic.objects.filter(syllabus=syllabus)
    allpoints = []
    for topic in topics:
        # get a list of topics, for each topic get all the syllabus points
        points = SyllabusPoint.objects.filter(topic=topic)
        for point in points:
            allpoints.append(point)

    if request.user.groups.filter(name='Students'):

        return render(request, 'tracker/syllabusdetail.html', {'syllabus': syllabus,
                                                               'specpoints': allpoints})

    if request.user.groups.filter(name='Teachers'):

        students = Student.objects.all().filter(classgroups__syllabustaught=syllabus).order_by('user__last_name')

        ratings = []
        for topic in topics:
            row = []
            for student in students:
                row.append(topic.studentAverageRating(student))
            ratings.append(row)
        student_topic_data = list(zip(topics, ratings))

        return render(request, 'tracker/syllabus_teacher_detail.html', {'syllabus': syllabus,
                                                               'specpoints': allpoints,
                                                                        'student_topic_data': student_topic_data,
                                                                        'students': students})

# CSV Uplods
@admin_only
def import_spec_points(request):
    # Deal with getting a CSV file

    if request.method == 'POST':
        csvform = CSVDocForm(request.POST, request.FILES)
        if csvform.is_valid():
            file = csvform.save()
            path = file.document.path
            processSpecification(path)
            os.remove(path)
            file.delete()
            return redirect('syllabuses')
    else:
        csvform = CSVDocForm()
    return render(request, 'school/model_form_upload.html', {'csvform': csvform})


@teacher_only
def list_exams(request):
    exams = Exam.objects.all()
    return render(request, 'tracker/exams.html', {'exams': exams})


def construction(request, pk):
    return render(request, 'tracker/404.html', {})


@teacher_only
def tracker_overview(request):
    syllabuses = Syllabus.objects.order_by('examtype')
    sittings = Sitting.objects.order_by('datesat')[:10]

    return render(request, 'tracker/tracker_overview.html', {'syllabuses': syllabuses,
                                                             'sittings': sittings})


@teacher_only
def examDetails(request, pk):
    exam = Exam.objects.get(pk=pk)
    syllabus = exam.syllabus.all()
    sittings = Sitting.objects.filter(exam=exam)
    questions = Question.objects.filter(exam=exam)
    SetQuestionsFormset = modelformset_factory(Question,  form=SetQuestions, extra=10)

    if request.method == 'POST':
        qform = SetQuestionsFormset(request.POST)

        # Quite a nasty hack to remove the hidden 'exam' field from only those forms without data.

        for form in qform:
            if form['qorder'].value == '' and form['qnumber'].value == '' and form['syllabuspoint'].value =='' and form['maxsore'].value == '':
                form.data['exam'].value = '' # set the exam to nothing.

        #if qform.is_valid():
        for form in qform:
            form.is_valid()
            # Only process formsets with data in them
            if 'qorder' in form.cleaned_data.keys():
                question = form.save(commit=False)
                question.exam = exam
                if question.qorder == 0:
                    question.delete()
                else:
                    question.save()
                    form.save_m2m()

        # Now sort of the field ordering: decimals may have been used to insert fields.

        questions = Question.objects.filter(exam=exam).order_by('qorder')
        n = 1
        for question in questions:
            question.qorder = n
            question.save()
            n = n+1

        return redirect(reverse('tracker:examDetail', args=(pk,)))

        #else:
            #return render(request, 'tracker/exam_details.html', {'exam': exam,
                                                                 #'sittings': sittings,
                                                                 #'questions': questions,
                                                                 #'qform': qform})

    else:
        qform = SetQuestionsFormset(queryset=Question.objects.filter(exam=exam).order_by('qorder'))

        for form in qform:
            form.initial['exam'] = exam.pk


        return render(request, 'tracker/exam_details.html', {'exam': exam,
                                                             'sittings': sittings,
                                                             'questions': questions,
                                                             'qform': qform})


@teacher_only
def sitting_detail(request, pk):
    sitting = Sitting.objects.get(pk=pk)
    students = Student.objects.filter(classgroups=sitting.classgroup).order_by('pk').order_by('user__last_name')

    # collect total scores for this test
    scores = []
    for student in students:
        total = Mark.objects.filter(sitting=sitting).filter(student=student).aggregate(Sum('score'))
        scores.append(total['score__sum'])

    data = list(zip(students, scores))

    # Get the topic ratings:
    topic_data = sitting.class_topic_performance()
    return render(request, 'tracker/sitting_detail.html', {'sitting': sitting,
                                                           'scores': scores,
                                                           'data': data,
                                                           'topic_data': topic_data})

@teacher_only
def new_sitting(request, exampk):
    # TODO: USE THE FORMAT for x, y in z
    #       by using 'zip'.
    exam = Exam.objects.get(pk=exampk)
    questions = Question.objects.filter(exam=exam)
    sittingform = NewSittingForm()
    if request.method == 'POST':
        sittingform = NewSittingForm(request.POST)
        if sittingform.is_valid():

            classgroup = sittingform.cleaned_data['classgroup']
            sitting = Sitting.objects.create(exam=exam, classgroup=classgroup, datesat=sittingform.cleaned_data['date'],
                                             openForStudentRecording=True)
            students = Student.objects.filter(classgroups=classgroup)
            for student in students:
                for question in questions:
                    Mark.objects.create(student=student, question=question, sitting=sitting)
            return (reverse('tracker:sitting_detail', args=[sitting.pk,]))

        else:
            return render(request, 'tracker/new_sitting.html', {'sittingform': sittingform})

    return render(request, 'tracker/new_sitting.html', {'sittingform': sittingform})


@teacher_only
def sitting_toggle_open_for_recording(request, sitting_pk):
    sitting = Sitting.objects.get(pk=sitting_pk)
    classgroup = sitting.classgroup
    sitting.toggle_open_for_recording()
    return redirect(reverse('school:class_detail', args=[classgroup.pk,]))


@own_or_teacher_only
def input_marks(request, sitting_pk, student_pk):
    # Get the main data we'll need
    sitting = Sitting.objects.get(pk=sitting_pk)
    student = Student.objects.get(pk=student_pk)

    questions = Question.objects.filter(exam=sitting.exam).order_by('qorder')
    marks = []
    for question in questions:
        marks.append(Mark.objects.get_or_create(sitting=sitting, student=student, question=question))
    # Formset to enter the student's mark
    MarkFormset = modelformset_factory(Mark, fields=('score', 'notes'), extra=0, widgets={
          'score': forms.Textarea(attrs={'rows': 1, 'cols': 2}),
        })

    marks = Mark.objects.filter(student=student, sitting=sitting).order_by('question__qorder')
    formset = MarkFormset(queryset=marks)

    if request.method == 'POST':

        formset = MarkFormset(request.POST)

        if formset.is_valid():
            formset.save(commit=False)
            n = 0 # Loop counter

            for mark in marks: #TODO: move this to the __clean__ method of formset
                # Check marks are correct:
                if formset[n].cleaned_data['score'] is not None:
                    if formset[n].cleaned_data['score'] > mark.question.maxscore:
                        formset[n].add_error('score', 'Score is greater than the maximum for this question')
                else:
                    formset[n].add_error('score', 'Please set a score')
                n = n + 1
            # Call is_valid() again. This will return false if we've added an error (from too high score) above.
            if formset.is_valid():
                formset.save() # Data is now saved.

                # Now we insert the notes into the journals.

                move_mark_reflection_to_journal_student(student, sitting)

                if request.user.groups.filter(name='Students'):
                    return redirect(reverse('tracker:student_sitting_summary', args=[sitting_pk, student_pk]))

                if request.user.groups.filter(name='Teachers'):
                    return redirect(reverse('tracker:student_sitting_summary', args=[sitting_pk, student_pk]))

            else:   # Either an initial validation error or the mark checking picked up too high a score
                data = list(zip(questions, formset))
                return render(request, 'tracker/exam_scores.html', {'data': data,
                                                                    'sitting': sitting,
                                                                    'marks': marks,
                                                                    'student': student,
                                                                    'formset': formset}, )

        else:
            data = list(zip(questions, formset))
            return render(request, 'tracker/exam_scores.html', {'data': data,
                                                                'sitting': sitting,
                                                                'marks': marks,
                                                                'student': student,
                                                                'formset': formset}, )

    else:
        data = list(zip(questions, formset))
        return render(request, 'tracker/exam_scores.html', {'data': data,
                                                            'sitting': sitting,
                                                            'marks': marks,
                                                            'student': student,
                                                            'formset': formset}, )

@teacher_only
def input_class_marks(request, sitting_pk):
    # Get the main data we'll need
    sitting = Sitting.objects.get(pk=sitting_pk)
    students = Student.objects.filter(classgroups=sitting.classgroup).order_by('user__last_name', 'user__first_name', 'pk')
    questions = Question.objects.filter(exam=sitting.exam).order_by('qorder')

    # make sure that all the marks exist

    for student in students:
        for question in questions:
            Mark.objects.get_or_create(student=student, sitting=sitting, question=question)

    MarkFormset = modelformset_factory(Mark, fields=('score',), extra=0, widgets={
        'score': forms.Textarea(attrs={'rows': 1, 'cols': 2}),
    })

    # marks = Mark.objects.filter(student__in=students, sitting=sitting).order_by('question__qorder')
    # formset = MarkFormset(queryset=marks)

    # experimental

    formsets = []
    n = 0

    if request.method == 'GET':
        for question in questions:
            marks = Mark.objects.filter(student__in=students, sitting=sitting, question=question).order_by('student__user__last_name', 'student__user__first_name', 'student__pk')
            formset = MarkFormset(queryset=marks, prefix=n)
            formsets.append(formset)
            n = n+1

        entry_rows = list(zip(questions, formsets))

        return render(request, 'tracker/input_class_marks.html', {'entry_rows': entry_rows,
                                                                  'sitting': sitting,
                                                                  'students': students})

    if request.method == 'POST':
        n = 0
        for question in questions:
            formset = MarkFormset(request.POST, prefix=n)
            if formset.is_valid():
                formset.save()

            else:
                entry_rows = list(zip(questions, formsets))
                return render(request, 'tracker/input_class_marks.html', {'entry_rows': entry_rows,
                                                               'sitting': sitting,
                                                               'students': students})
            n = n + 1


        entry_rows = list(zip(questions, formsets))

        return render(request, 'tracker/input_class_marks.html', {'entry_rows': entry_rows,
                                                                  'sitting': sitting,
                                                                  'students': students})



@own_or_teacher_only
def student_sitting_summary(request, sitting_pk, student_pk):
    student = Student.objects.get(pk=student_pk)
    sitting = Sitting.objects.get(pk=sitting_pk)

    marks = Mark.objects.filter(sitting=sitting).filter(student=student_pk).order_by('question__qorder')

    syllabus_point_tested = SyllabusPoint.objects.filter(question__mark__in=marks).distinct().order_by(
        'number').order_by('topic')

    student_ratings = []
    for point in syllabus_point_tested:
        x = point.get_student_rating(student)
        student_ratings.append(x)

    point_notes = []
    for point in syllabus_point_tested:
        point_marks = Mark.objects.filter(student=student).filter(sitting=sitting).filter(
            question__syllabuspoint=point)
        single_note = []
        for mark in point_marks:
            single_note.append(mark.notes)
        single_note = list(filter(None, single_note))
        point_notes.append(single_note)

    point_journal = []

    for point in syllabus_point_tested:
        journal_entry, created = StudentJournalEntry.objects.get_or_create(student=student, syllabus_point=point)

    # Create a formset to store the journal items in.
    journal_formset = modelformset_factory(StudentJournalEntry, extra=0, fields=('entry',))

    if request.method == 'POST':

        # Populate the formset with POSTed data:
        point_journal_formset = journal_formset(request.POST)

        if point_journal_formset.is_valid():
            point_journal_formset.save()

            return redirect(reverse('tracker:tracker_overview'))

        else:

            syllabus_data = list(zip(syllabus_point_tested, student_ratings, point_notes, point_journal_formset))

            topics_tested = SyllabusTopic.objects.filter(syllabuspoint__question__mark__in=marks).distinct()
            topic_average_marks = []
            for topic in topics_tested:
                topic_average_marks.append(topic.studentAverageRating(student))

            topic_data = list(zip(topics_tested, topic_average_marks))

            return render(request, 'tracker/student_sitting_summary.html', {'student': student,
                                                                            'sitting': sitting,
                                                                            'marks': marks,
                                                                            'syllabus_data': syllabus_data,
                                                                            'topic_data': topic_data,
                                                                            'point_journal_formset': point_journal_formset})

    else:


        point_journal_formset = journal_formset(
            queryset=StudentJournalEntry.objects.filter(student=student,
                                                        syllabus_point__in=syllabus_point_tested).order_by(
                'syllabus_point__number') .order_by('syllabus_point__topic'))

        syllabus_data = list(zip(syllabus_point_tested, student_ratings, point_notes, point_journal_formset))

        topics_tested = SyllabusTopic.objects.filter(syllabuspoint__question__mark__in=marks).distinct()
        topic_average_marks = []
        for topic in topics_tested:
            topic_average_marks.append(topic.studentAverageRating(student))

        topic_data = list(zip(topics_tested, topic_average_marks))

        return render(request, 'tracker/student_sitting_summary.html', {'student': student,
                                                                        'sitting': sitting,
                                                                        'marks': marks,
                                                                        'syllabus_data': syllabus_data,
                                                                        'topic_data': topic_data,
                                                                        'point_journal_formset': point_journal_formset})


@teacher_only
def sitting_by_q(request, pk):
    sitting = Sitting.objects.get(pk=pk)
    students = Student.objects.filter(classgroups=sitting.classgroup).order_by('pk').order_by('user__last_name')
    questions = Question.objects.filter(exam__sitting=sitting).order_by('qorder')

    # create a row of percentage scores for each mark
    scores = []
    for question in questions:
        row = []
        for student in students:
            mark, created = Mark.objects.get_or_create(sitting=sitting, student=student, question=question)
            row.append(mark.percentage())
        scores.append(row)

    score_data = list(zip(questions, scores))

    return render(request, 'tracker/sitting_detail_by_q.html', {'sitting': sitting,
                                                           'scores': scores,
                                                           'score_data': score_data,
                                                                'students': students})


@own_or_teacher_only
def student_topic_overview(request, topic_pk, student_pk):
    student = Student.objects.get(pk=student_pk)
    topic = SyllabusTopic.objects.get(pk=topic_pk)

    sub_topic_data = topic.studentSubTopicData(student)

    return render(request, 'tracker/student_topic_overview.html', {'student': student,
                  'topic': topic,
                  'sub_topic_data': sub_topic_data})


@own_or_teacher_only
def student_sub_topic_overview(request, sub_topic_pk, student_pk):
    student = Student.objects.get(pk=student_pk)
    sub_topic = SyllabusSubTopic.objects.get(pk=sub_topic_pk)

    point_data = sub_topic.student_sub_topic_data(student)
    # Remember, get_or_create returns a tuple; the object, and a TRUE or FALSE depending on whether it was created.
    journal, created = StudentJournalEntry.objects.get_or_create(student=student, syllabus_sub_topic=sub_topic)

    if request.method == 'POST':
        journal_form = StudentJournalEntryLarge(request.POST)
        if journal_form.is_valid():
            journal_entry = StudentJournalEntry.objects.get(student=student, syllabus_sub_topic=sub_topic)
            journal_entry.entry = journal_form.cleaned_data['entry']
            journal_entry.save()
            parent_topic_pk = sub_topic.topic.pk
            return redirect(reverse('tracker:student_topic_overview', args=(parent_topic_pk, student_pk )))

        else:
            return render(request, 'tracker/student_sub_topic_overview.html', {'student': student,
                                                                               'sub_topic': sub_topic,
                                                                               'point_data': point_data,
                                                                               'journal_form': journal_form})

    else:

        journal_form = StudentJournalEntryLarge(instance=journal)

        return render(request, 'tracker/student_sub_topic_overview.html', {'student': student,
                                                                           'sub_topic': sub_topic,
                                                                           'point_data': point_data,
                                                                           'journal_form': journal_form})


@own_or_teacher_only
def small_assessment_list(request, point_pk, student_pk):
    '''Create a small window showing which assessments are testing a certain syllabus point.'''

    student = Student.objects.get(pk=student_pk)
    point = SyllabusPoint.objects.get(pk=point_pk)

    assessments = point.student_assesments(student)

    return render(request, 'tracker/small_assessment_list.html', {'student': student,
                                                                  'point': point,
                                                                  'assessments': assessments})
