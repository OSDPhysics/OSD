from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .charts import CohortPointGraph, CohortSubTopicChart, StudentChart, StudentSubTopicGraph
from journal.forms import StudentJournalEntryLarge
from journal.functions import move_mark_reflection_to_journal_student_mptt
from osd.decorators import *
from django.urls import reverse, reverse_lazy
from journal.models import StudentJournalEntry
from django.contrib import messages
from timetable.models import Lesson, LessonResources
from school.models import PastoralStructure, AcademicStructure
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
        classgroups = ClassGroup.objects.filter(student=student)
        first_syllabus = classgroups[0].mptt_syllabustaught.all()[0]
        tree_root = first_syllabus.get_root()
        return redirect(reverse('tracker:student_ratings', args=(student.pk, tree_root.pk)))

    if request.user.groups.filter(name='Teachers'):
        teacher = Teacher.objects.get(user=request.user)

        # Show the teacher's students
        return redirect(reverse('tracker:new_teacher_overview', args=(teacher.pk,)))



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


def construction(request):
    return render(request, 'school/404.html', {})



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
    parent_form = MPTTSyllabusForm()
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
                                                             'qform': qform,
                                                             'parent_form': parent_form})


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
                    Mark.objects.get_or_create(student=student, question=question, sitting=sitting)
            return redirect(reverse('tracker:sitting_detail', args=[sitting.pk, ]))

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
                        messages.add_message(request, messages.ERROR, 'You have entered a score bigger than the maximum for at least one quesiton!')
                else:
                    formset[n].add_error('score', 'Please set a score')
                    messages.add_message(request, messages.ERROR,
                                         "You have left at least one score blank. Please enter 0 if you didn't get that mark")
                n = n + 1
            # Call is_valid() again. This will return false if we've added an error (from too high score) above.
            if formset.is_valid():
                formset.save() # Data is now saved.

                # Now we insert the notes into the journals.

                move_mark_reflection_to_journal_student_mptt(student, sitting)

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

@teacher_only
def classgroup_all_syllabuses_completion(request, classgroup_pk):
    """ REport how much of the syllabus has been taught and assessed """
    # Make sure we can teach multiple syllabuss


    classgroup = ClassGroup.objects.get(pk=classgroup_pk)
    classgroup_syllabuss = classgroup.syllabustaught.all()

    data = []

    for syllabus in classgroup_syllabuss:
        row = [syllabus]
        row.append(syllabus.classgroup_percentage_taught(classgroup))
        row.append(syllabus.classgroup_percentage_assessed(classgroup))
        data.append(row)


    return render(request, 'tracker/classgroup_all_syllabus_completion.html', {
        'classgroup': classgroup,
        'data': data
    })


def classgroup_sub_topic_completion(request, classgroup_pk, sub_topic_pk):
    classgroup = ClassGroup.objects.get(pk=classgroup_pk)
    sub_topic = SyllabusSubTopic.objects.get(pk=sub_topic_pk)

    syllabus_points = sub_topic.syllabus_points()
    data = []

    for point in syllabus_points:
        row = [point]

        if point.has_been_taught(classgroup):
            row.append(point.lessons_taught(classgroup))
        else:
            row.append(False)
        if point.has_been_assessed(classgroup):
            row.append(point.classgroup_assessments(classgroup))
        else:
            row.append(False)

        data.append(row)

    return render(request, 'tracker/classgroup_sub_topic_completion.html', {'classgroup': classgroup,
                                                                            'sub_topic': sub_topic,
                                                                       'data': data})


@teacher_only
def classgroup_topic_completion(request, classgroup_pk, topic_pk):
    classgroup = ClassGroup.objects.get(pk=classgroup_pk)
    topic = SyllabusTopic.objects.get(pk=topic_pk)

    sub_topics = topic.sub_topics()
    data = []
    for sub_topic in sub_topics:
        row = [sub_topic]
        row.append(sub_topic.classgroup_percent_taught(classgroup))
        row.append(sub_topic.classgroup_percent_assessed(classgroup))
        data.append(row)

    return render(request, 'tracker/classgroup_topic_completion.html', {'classgroup': classgroup,
                                                                        'topic': topic,
                                                                        'data': data})


def classgroup_syllabus_completion(request, classgroup_pk, syllabus_pk):
    classgroup = ClassGroup.objects.get(pk=classgroup_pk)
    syllabus = Syllabus.objects.get(pk=syllabus_pk)
    topics = SyllabusTopic.objects.filter(syllabus=syllabus)

    data = []
    for topic in topics:
        row = [topic]
        row.append(topic.classgroup_percentage_taught(classgroup))
        row.append(topic.classgroup_percentage_assessed(classgroup))
        data.append(row)
    return render(request, 'tracker/classgroup_syllabus_completion.html', {'classgroup': classgroup,
                                                                           'syllabus': syllabus,
                                                                           'data': data})

@admin_only
def chart_test(request):

    chart = CohortPointGraph()
    points = SyllabusPoint.objects.filter(topic__pk=1)
    chart.syllabus_areas = points
    chart.students = Student.objects.filter(classgroups__groupname="10B/Ph2")
    return render(request, 'tracker/chart_test.html', {'chart': chart})

@admin_only
def rating_ouput_check(request, classgroup_pk, topic_pk):
    classgroup = ClassGroup.objects.get(pk=classgroup_pk)
    students = Student.objects.filter(classgroups=classgroup)
    topic = SyllabusTopic.objects.get(pk=topic_pk)
    points = SyllabusSubTopic.objects.filter(topic=topic)

    data = []

    # Construct first row
    row = [""]
    for student in students:
        row.append(student)
    row.append("4-5")
    data.append(row)

    for point in points:
        row = []
        row.append(point)
        for student in students:
            row.append(point.get_student_rating(student).rating)
        row.append(point.cohort_rating_number(students, 4, 5))
        data.append(row)

    return render(request, 'tracker/rating_output_check.html', {'data': data})


@admin_only
def sub_topic_chart_test(request):

    chart = CohortSubTopicChart()
    points = SyllabusSubTopic.objects.filter(topic__pk=1)
    chart.syllabus_areas = points
    chart.students = Student.objects.filter(classgroups__groupname="10B/Ph2")
    return render(request, 'tracker/chart_test.html', {'chart': chart})


@teacher_only
def coverage_check(request, syllabus_pk):
    syllabus = Syllabus.objects.get(pk=syllabus_pk)

    classes = ClassGroup.objects.filter(syllabustaught=syllabus)

    points = SyllabusPoint.objects.filter(topic__syllabus=syllabus).order_by('sub_topic', 'number')

    data = []
    row = ["", ]

    for classgroup in classes:
        row.append(str(classgroup))

    data.append(row)

    for point in points:
        row = [str(point)]
        for classgroup in classes:
            if point.has_been_taught(classgroup):
                row.append("Y")
            else:
                row.append("N")
        data.append(row)

    return render(request, "tracker/coverage_check.html", {'syllabus': syllabus,
                                                           'data': data})


@own_or_teacher_only
def sub_topic_student_graph_check(request, student_pk, sub_topic_pk):
    student = Student.objects.filter(pk=student_pk)
    topic = SyllabusTopic.objects.get(pk=sub_topic_pk)
    points = SyllabusSubTopic.objects.filter(topic=topic)
    chart = StudentChart()
    chart.students = student
    chart.syllabus_areas = points

    return render(request, "tracker/student_s_topic_chart_test.html", {'student': student,
                                                       'sub_topic': topic,
                                                       'chart': chart})

@admin_only
def single_sub_topic_graph_check(request, student_pk, sub_topic_pk):
    student = Student.objects.filter(pk=student_pk)
    points = SyllabusSubTopic.objects.filter(pk=sub_topic_pk)
    chart = StudentSubTopicGraph()
    chart.students = student
    chart.syllabus_areas = points

    return render(request, "tracker/student_single_s_topic_chart.html", {'student': student,
                                                                       'sub_topic': points,
                                                                       'chart': chart})

@admin_only
def set_current_ratings(request):
    set_current_student_point_ratings()


@teacher_only
def new_teacher_overview(request, teacher_pk):
    """ New splash screen using MPTT Models """

    teacher = Teacher.objects.get(pk=teacher_pk)
    classgroups = ClassGroup.objects.filter(archived=False, groupteacher=teacher)

    classgroup_data = [] #format is: Classgruop, Syllabuses_taught, progress_dictionary
    for group in classgroups:
        row = []
        # Construct a table set:
        row.append(group)
        syllabuses = []
        progress_dics = []
        for syllabus in group.mptt_syllabustaught.all():
            syllabuses.append(syllabus)
            progress_dics.append(syllabus.group_ratings_data(group.students()))
        row.append(syllabuses)
        row.append(progress_dics)
        classgroup_data.append(row)

    sittings = Sitting.objects.filter(classgroup__in=classgroups).order_by('datesat').reverse()

    return render(request, "tracker/mptt_teacher_overview.html", {'teacher': teacher,
                                                          'classgroups': classgroups,
                                                          'sittings': sittings,
                                                          'classgroup_data': classgroup_data})

@teacher_only
def classgroup_ratings(request, classgroup_pk, syllabus_pk):
    """ Displays the ratings for a classroup for a given syllabus """

    classgroup = ClassGroup.objects.get(pk=classgroup_pk)
    syllabus = MPTTSyllabus.objects.get(pk=syllabus_pk)
    if not syllabus.is_root_node():
        parent = syllabus.get_ancestors(ascending=True)[0]
    else:
        parent = False

    students = classgroup.students()

    # Create the data for students:
    student_data = []
    for student in students:
        row = []
        data = syllabus.group_ratings_data(students=Student.objects.filter(pk=student.pk))
        row.append(student)
        row.append(student.tutorgroup)
        row.append(student.Gender)
        row.append(data)
        student_data.append(row)

    # Now let's do the topics they've been taught
    # We need two different takes here; one if we're at the bottom of a tree,
    # one if we're at a parent object.

    # For parents topics:

    if syllabus.get_descendant_count():
        sub_topic_data = []
        # We are not at the bottom:
        sub_points = syllabus.get_children()
        for point in sub_points:
            row = []
            row.append(point)
            row.append(point.group_ratings_data(students))
            sub_topic_data.append(row)
    else:
        # We are at the bottom of a row:
        sub_topic_data = [[syllabus, syllabus.group_ratings_data(students)],]



    return render(request, 'tracker/classgroup_ratings_mptt.html', {'classgroup': classgroup,
                                                                    'syllabus': syllabus,
                                                                    'students': students,
                                                                    'student_data': student_data,
                                                                    'sub_topic_data': sub_topic_data,
                                                                    'parent': parent})


@own_or_teacher_only
def student_ratings(request, student_pk, syllabus_pk):
    student = Student.objects.get(pk=student_pk)
    syllabus = MPTTSyllabus.objects.get(pk=syllabus_pk)

    # For the back buttons:

    if not syllabus.is_root_node():
        parent = syllabus.get_ancestors(ascending=True)[0]
    else:
        parent = False

    # Create a bunch of buttons for each classgroup the student is in,
    # so that a teacher can return to the overview for that group.

    classgroups = ClassGroup.objects.filter(student=student, mptt_syllabustaught__in=syllabus.get_ancestors(include_self=True), archived=False)
    # We only want to enable the group overview buttons for teachers:
    if request.user.groups.filter(name='Teachers').exists():
        isteacher = True
    else:
        isteacher = False

    student_as_queryset = Student.objects.filter(pk=student_pk)

    # Data for an overview bar:
    overview_data = syllabus.group_ratings_data(students=student_as_queryset)

    # Data for sub-point raings:

    sub_topic_data = []
    for point in syllabus.get_children():
        row = []
        row.append(point)

        row.append(point.group_ratings_data(student_as_queryset))

        # Add some lessons and resource:
        lessons = Lesson.objects.filter(mptt_syllabus_points=point, classgroup__in=student.classgroups.all())
        resources = []

        # Only allow students to see the correct resources:
        if isteacher:

            for lesson in lessons:
                resources.append(lesson.resources())
        else:
            for lesson in lessons:
                resources.append(lesson.student_viewable_resources())
        row.append(lessons)
        row.append(resources)

        sub_topic_data.append(row)

    # If we're at the second-to-last level, we will
    # have to display the journal etc.
    # If not, we just want the data on the topic.
    test = syllabus.get_descendant_count()
    if syllabus.get_children()[0].get_descendant_count() != 0:
        # We are not at the bottom, so no journal, and let's show assessments:

        assessments = Sitting.objects.filter(classgroup__student=student, classgroup__in=classgroups).order_by('datesat').reverse()
        assessment_data = []
        for assessment in assessments:
            row = []
            row.append(assessment)
            row.append(assessment.student_total(student))
            assessment_data.append(row)
        return render(request, 'tracker/student_ratings_mptt.html', {'student': student,
                                                                     'syllabus': syllabus,
                                                                     'sub_topic_data': sub_topic_data,
                                                                     'parent': parent,
                                                                     'isteacher': isteacher,
                                                                     'classgroups': classgroups,
                                                                     'assessment_data': assessment_data})
    else:
        # we are at the bottom, so need a journal.
        journal, created = StudentJournalEntry.objects.get_or_create(student=student, mptt_syllabus=syllabus)

        if request.method == 'POST':
            journal_form = StudentJournalEntryLarge(request.POST, instance=journal)
            if journal_form.is_valid():
                journal_entry = StudentJournalEntry.objects.get(student=student, mptt_syllabus=syllabus)
                journal_entry.entry = journal_form.cleaned_data['entry']
                journal_entry.save()
                messages.add_message(request, messages.SUCCESS, 'Journal saved.')
            else:
                messages.add(request, messages.ERROR, 'Something went wrong, and your journal has not been saved.')

        else:
            journal_form = StudentJournalEntryLarge(instance=journal)

        return render(request, 'tracker/student_ratings_mptt_w_journal.html', {'student': student,
                                                                     'syllabus': syllabus,
                                                                     'sub_topic_data': sub_topic_data,
                                                                     'parent': parent,
                                                                     'isteacher': isteacher,
                                                                     'classgroups': classgroups,
                                                                     'journal_form': journal_form})


@teacher_only
def student_standardised_data(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    standardised_data = []

    pass_parents = StandardisedData.objects.get(name="PASS")
    pass_data_objects = pass_parents.get_children()

    CAT4_parent = StandardisedData.objects.get(name="CAT4")
    CAT4_data_objects = CAT4_parent.get_children()

    pass_data = StandardisedResult.objects.filter(student=student, standardised_data__in=pass_data_objects)
    CAT4_data = StandardisedResult.objects.filter(student=student, standardised_data__in=CAT4_data_objects)


    standardised_data.append(pass_data)
    standardised_data.append(CAT4_data)

    assessments = Sitting.objects.filter(classgroup__student=student).order_by('datesat').reverse()

    return render(request, 'tracker/student_standardised_overview.html', {'student': student,
                      'standardised_data': standardised_data,
                                                                          'assessments': assessments})


@teacher_only
def cohort_standardised_data_vs_target(request, cohort_pk):
    cohort = Student.objects.all()
    IGCSE_parent = StandardisedData.objects.get(name="IGCSE Grades")
    IGCSE_data_objects = IGCSE_parent.get_children()

    IGCSE_graph_data = []
    for subject in IGCSE_data_objects:
        row = subject.cohort_target_vs_current_data(cohort)
        row.append("/" + str(row[0]) + "/")
        IGCSE_graph_data.append(row)

    return render(request, 'tracker/cohort_std_data_vs_tgt.html', {'IGCSE_graph_data': IGCSE_graph_data})


@teacher_only
def school_standardised_data_vs_target(request):
    pass
