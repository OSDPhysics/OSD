from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import *
from .models import Teacher, Student
from .functions.adddata import *
import csv
import codecs
import os
import logging

logger = logging.getLogger(__name__)


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


def new_student(request):
    return render(request, 'school/404.html')


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


# Add students in bulk from CSV
def import_students(request):
    # Deal with getting a CSV file

    if request.method == 'POST':
        csvform = CSVDocForm(request.POST, request.FILES)
        if csvform.is_valid():
            file = csvform.save()
            path = file.document.path
            logger.error(path)
            processstudent(path)

            return redirect('list_students')
    else:
        csvform = CSVDocForm()
    return render(request, 'school/model_form_upload.html', {'csvform': csvform})
