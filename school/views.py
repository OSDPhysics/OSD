from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import TeacherForm
from .models import Teacher, Student
from .functions.adddata import *
import csv
import codecs
import os

def splash(request):
    return render(request, 'tracker/splash.html', {})


def new_teacher(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TeacherForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            newteacher = addteacher(form.cleaned_data)
            return HttpResponseRedirect('/school/teachers/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TeacherForm()
    return render(request, 'school/new_teacher.html', {'form': form})


def teachers(request):
    teachers = Teacher.objects.order_by('user__last_name')
    return render(request, 'school/teachers.html', {'teachers': teachers})


def students(request):
    students = Student.objects.order_by('user__last_name').order_by('classgroups__groupname')
    return render(request, 'school/students.html', {'students': students})


@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'school/student_detail.html', {'student': student})


# EXPERIMENTAL AND DUMB:
def import_students(request):
    if request.POST and request.FILES:
        # csvfile = request.FILES['csv_file'].read()
        settings_dir = os.path.dirname(__file__)
        PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

        STATIC_FOLDER = os.path.join(PROJECT_ROOT, 'school/static/')
        csvfile = open(STATIC_FOLDER + 'input.csv', 'r')
        # ndialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        # csvfile.open()
        reader = csv.reader(csvfile, delimiter=',')
        processstudent(reader)

    return render(request, "school/import_students.html", locals())

