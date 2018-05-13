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

    return render(request, 'tracker/add_questions.html', {'questionFormSet': questionFormSet,})


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

    return render(request, 'tracker/tracker_overview.html', {'syllabuses':syllabuses,
                                                             'sittings':sittings})


# @teacher_only
# def examDetails(request,pk):
#     exam = Exam.objects.get(pk=pk)
#     sittings = Sitting.objects.filter(exam=exam)
#     questions = Question.objects.filter(exam=exam)
#     SetQuestionsFormset = formset_factory(SetQuestions, extra=10)
#
#     if request.method == 'POST':
#         qform = SetQuestionsFormset(request.POST)
#         if qform.is_valid():
#             for form in qform:
#                 form.exam = exam
#                 form.save()
#                 return redirect(reverse('examDetail', args=(pk,)))
#         else:
#             return render(request, 'tracker/404.html')
#
#     else:
#         return render(request, 'tracker/exam_details.html', {'exam': exam,
#                                                              'sittings': sittings,
#                                                              'questions': questions,
#                                                              'qform': SetQuestionsFormset})


@teacher_only
def examDetails(request, pk):
    exam = Exam.objects.get(pk=pk)
    form = SetQuestions()

    if request.method == 'POST':
        form = SetQuestions(request.POST)
        if form.is_valid():
            newquestion = form.save(commit=False)
            newquestion.exam = exam
            form.save()
            form.save_m2m()
            return render(request, 'tracker/exam_details.html', {'qform': form,
                          'exam': exam})
        else:
            return render(request, 'tracker/exam_details.html', {'qform': form,
                          'exam': exam})

    return render(request, 'tracker/exam_details.html', {'qform': form,
                                                         'exam': exam})


@teacher_only
def sitting_detail(request,pk):
    sitting = Sitting.objects.get(pk=pk)
    return render(request, 'tracker/404.html')
