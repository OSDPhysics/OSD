from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from osd.decorators import *
from django.urls import reverse
from django.db.models import Sum
from operator import itemgetter
from learningjournal.models import StudentJournalEntry
import datetime

from .models import *
import logging
from .functions.adddata import *
import os

logger = logging.getLogger(__name__)


@login_required()
def splash(request):
    if request.user.groups.filter(name='Students'):

        # For the first (classgroups) table
        student = Student.objects.get(user=request.user)
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
            points_learned = SyllabusPoint.objects.filter(topic__syllabus__in=syllabus).order_by('number').order_by('topic').order_by('topic__syllabus')

        student_ratings = []
        for point in points_learned:
            x = point.get_student_rating(student)
            student_ratings.append(round(x*100))

        syllabus_data = list(zip(points_learned, student_ratings))

        data['syllabus_data'] = syllabus_data

        return render(request, 'tracker/splash_student.html', data)

    if request.user.groups.filter(name='Teachers'):
        return render(request, 'tracker/splash_teacher.html')


@teacher_only
def add_test(request):
    '''Take the information for the first stage of a new test record'''

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewExamForm(request.POST)
        new_exam = form.save()

        return redirect(reverse('examDetail', args=(new_exam.pk,)))

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
    ratings = []
    for topic in topics:
        # get a list of topics, for each topic get all the syllabus points
        points = SyllabusPoint.objects.filter(topic=topic)
        for point in points:
            allpoints.append(point)


    return render(request, 'tracker/syllabusdetail.html', {'syllabus': syllabus,
                                                           'specpoints': allpoints})


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
def create_questions(request):
    questionFormSet = formset_factory(questionsForm)
    newExamForm = examForm

    # Process POST data

    # If no post:

    return render(request, 'tracker/add_questions.html', {'questionFormSet': questionFormSet, })


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
    sittings = Sitting.objects.filter(exam=exam)
    questions = Question.objects.filter(exam=exam)
    SetQuestionsFormset = formset_factory(SetQuestions, extra=10)

    if request.method == 'POST':
        qform = SetQuestionsFormset(request.POST)
        if qform.is_valid():
            for form in qform:
                form.exam = exam
                form.save()
                return redirect(reverse('examDetail', args=(pk,)))
        else:
            return render(request, 'tracker/404.html')

    else:
        return render(request, 'tracker/exam_details.html', {'exam': exam,
                                                             'sittings': sittings,
                                                             'questions': questions,
                                                             'qform': SetQuestionsFormset})


# Not in use: this was an attempt for an editable version, but it doesn't work.
# @teacher_only
# def examDetails(request, pk):
#     exam = Exam.objects.get(pk=pk)
#     questionFormset = formset_factory(SetQuestions)
#     formset = questionFormset()
#
#     if request.method == 'POST':
#         formset = questionFormset(request.POST)
#         if formset.is_valid():
#             for form in formset:
#                 newquestion = form.save(commit=False)
#                 newquestion.exam = exam
#                 form.save()
#                 form.save_m2m()
#                 return render(request, 'tracker/exam_details.html', {'formset': formset,
#                               'exam': exam})
#         else:
#             return render(request, 'tracker/exam_details.html', {'formset': formset,
#                           'exam': exam})
#
#     return render(request, 'tracker/exam_details.html', {'formset': formset,
#                                                          'exam': exam})


@teacher_only
def sitting_detail(request, pk):
    sitting = Sitting.objects.get(pk=pk)
    students = Student.objects.filter(classgroups__in=sitting.classgroup).order_by('pk').order_by('user__last_name')

    # collect total scores for this test
    scores = {}
    for student in students:
        total = Mark.objects.filter(sitting=sitting).filter(student=student).aggregate(Sum('score'))
        scores[student] = total

    return render(request, 'tracker/sitting_detail.html', {'sitting': sitting,
                                                           'scores': scores})

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
            return redirect(reverse('sitting_detail'))

        else:
            return render(request, 'tracker/new_sitting.html', {'sittingform': sittingform})

    return render(request, 'tracker/new_sitting.html', {'sittingform': sittingform})

@own_or_teacher_only
def input_marks(request, sitting_pk, student_pk):
    # Get the main data we'll need
    sitting = Sitting.objects.get(pk=sitting_pk)
    student = Student.objects.get(pk=student_pk)
    marks = Mark.objects.filter(sitting=sitting).filter(student=student).order_by('question__qorder')
    questions = Question.objects.filter(exam=sitting.exam).order_by('qorder')

    # Formset to enter the student's mark
    MarkFormset = modelformset_factory(Mark, fields=('score', 'notes'), extra=0, widgets={
          'score': forms.Textarea(attrs={'rows': 1, 'cols': 2}),
        })
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
                formset.save()

                if request.user.groups.filter(name='Students'):
                    return redirect(reverse('student_sitting_summary', (sitting_pk, student_pk)))

                if request.user.groups.filter(name='Teachers'):
                    return redirect(reverse('student_sitting_summary', (sitting_pk, student_pk)))

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


@own_or_teacher_only
def student_sitting_summary(request, sitting_pk, student_pk):

    student = Student.objects.get(pk=student_pk)
    sitting = Sitting.objects.get(pk=sitting_pk)

    marks = Mark.objects.filter(sitting=sitting).filter(student=student_pk).order_by('question__qorder')

    syllabus_point_tested = SyllabusPoint.objects.filter(question__mark__in=marks).distinct().order_by('number').order_by('topic')

    student_ratings = []
    for point in syllabus_point_tested:
        x = point.get_student_rating(student)
        student_ratings.append(round(x * 5, 1))

    point_notes = []
    for point in syllabus_point_tested:
        point_marks = Mark.objects.filter(student=student).filter(sitting=sitting).filter(question__syllabuspoint=point)
        single_note = []
        for mark in point_marks:
            single_note.append(mark.notes)
        single_note = list(filter(None, single_note))
        point_notes.append(single_note)

    syllabus_data = list(zip(syllabus_point_tested, student_ratings, point_notes))

    topics_tested = SyllabusTopic.objects.filter(syllabuspoint__question__mark__in=marks).distinct()
    topic_average_marks = []
    for topic in topics_tested:
        topic_average_marks.append(topic.studentAverageRating(student))

    topic_data = list(zip(topics_tested, topic_average_marks))

    return render(request, 'tracker/student_sitting_summary.html', {'student': student,
                                                                    'sitting': sitting,
                                                                    'marks': marks,
                                                                    'syllabus_data': syllabus_data,
                                                                    'topic_data': topic_data})
