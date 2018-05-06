from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
import logging
from .functions.adddata import *
import os

logger = logging.getLogger(__name__)


@login_required
def add_test1(request):
    '''Take the information for the first stage of a new test record'''

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewExamForm(request.POST)
        new_exam = form.save().pk

        return render(request, 'exam/' + str(new_exam), {'form': form,
                                                         'stage': 1})

    else:
        form = NewExamForm()
    return render(request, 'tracker/new_exam1.html', {'form': form})


@login_required
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

    return render(request, 'tracker/syllabusdetail.html', {'syllabus': syllabus,
                                                           'specpoints': allpoints})

# CSV Uplods


@login_required
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


@login_required
def create_questions(request):
    questionFormSet = formset_factory(questionsForm)
    newExamForm = examForm

    # Process POST data

    # If no post:

    return render(request, 'tracker/add_questions.html', {'questionFormSet': questionFormSet,})


@login_required
def list_exams(request):
    exams = Exam.objects.order_by('syllabus')
    return render(request, 'tracker/exams.html', {'exams': exams})


def construction(request, pk):
    return render(request, 'tracker/404.html', {})

@login_required
def tracker_overview(request):

    syllabuses = Syllabus.objects.order_by('examtype')
    sittings = Sitting.objects.order_by('datesat')[:10]

    return render(request, 'tracker/tracker_overview.html', {'syllabuses':syllabuses,
                                                             'sittings':sittings})


@login_required
def examDetails(request,pk):
    exam = Exam.objects.get(pk=pk)
    sittings = Sitting.objects.filter(exam=exam)
    questions = Question.objects.filter(exam=exam)
    return render(request, 'tracker/exam_details.html', {'exam': exam,
                                                         'sittings': sittings,
                                                         'questions': questions})


@login_required
def sitting_detail(request,pk):
    sitting = Sitting.objects.get(pk=pk)
    return render(request, 'tracker/404.html')
