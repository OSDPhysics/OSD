
from django.shortcuts import render, redirect, get_object_or_404
#from .forms import NewExamForm
from .models import Syllabus, SyllabusPoint, SyllabusTopic
import logging

logger = logging.getLogger(__name__)

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


def list_syllabuses(request):
    syllabuses = Syllabus.objects.order_by('examtype')
    return render(request, 'tracker/syllabus.html', {'syllabuses': syllabuses})


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