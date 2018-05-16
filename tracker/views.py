from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from osd.decorators import teacher_only, admin_only
from django.urls import reverse
from .models import *
import logging
from .functions.adddata import *
import os

logger = logging.getLogger(__name__)


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


@teacher_only
def syllabus_detail(request, pk):
    syllabus = get_object_or_404(Syllabus, pk=pk)
    topics = SyllabusTopic.objects.filter(syllabus=syllabus)
    allpoints = []
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
    return render(request, 'tracker/sitting_detail.html', {'sitting': sitting})


def new_sitting(request, exampk):
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
            return render(request, 'tracker/new_sitting.html.html', {'sittingform': sittingform})

    return render(request, 'tracker/new_sitting.html', {'sittingform': sittingform})


def input_marks(request, sitting_pk, student_pk):
    sitting = Sitting.objects.get(pk=sitting_pk)
    student = Student.objects.get(pk=student_pk)
    marks = Mark.objects.filter(sitting=sitting).filter(student=student).order_by('question__qorder')

    # Todo:  create a formset
    MarkFormset = modelformset_factory(Mark, fields=('score', 'question'), extra=0)
    formset = MarkFormset(
        queryset=Mark.objects.filter(sitting=sitting).filter(student=student).order_by('question__qorder'))

    if request.method == 'POST':

        formset = MarkFormset(request.POST)
        if formset.is_valid():
            formset.save(commit=False)
            n = 0
            for mark in marks:
                # Override any naughty changes to the question order by POST hacking
                formset[n].question = marks[n].question
                # Set our form to the correct student TODO: Is this needed?
                formset[n].student = student

                # Check marks are correct:
                if formset[n].cleaned_data['score']:
                    if formset[n].cleaned_data['score'] > mark.question.maxscore:
                        formset[n].add_error('score', 'Score is greater than the maximum for this question')

                n = n + 1
            # Call is_valid() again to check if we've added any errors.
            if formset.is_valid():
                formset.save()
                return redirect('tracker')

            else:
                return render(request, 'tracker/exam_scores.html', {'formset': formset,
                                                                'sitting': sitting,
                                                                'marks': marks,
                                                                'student': student})

        else:
            return render(request, 'tracker/exam_scores.html', {'formset': formset,
                                                                'sitting': sitting,
                                                                'marks': marks,
                                                                'student': student})

    else:
        return render(request, 'tracker/exam_scores.html', {'formset': formset,
                                                            'sitting': sitting,
                                                            'marks': marks,
                                                            'student': student}, )

    # Todo:  send that formset to the view
    # Todo:  process the completed formset.
