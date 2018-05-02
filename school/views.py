from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required, user_passes_test
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

def is_teacher(user):
    return user.groups.filter(name='Teachers').exists()


@login_required
def home(request):
    user = request.user
    return render(request, 'school/home.html', {'user': user})


def splash(request):
    return render(request, 'school/splash.html', {})


@login_required
def school(request):
    return render(request, 'school/school.html', {})

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


@login_required
def new_student(request):
    return render(request, 'school/404.html')


@login_required
def teachers(request):
    teachers = Teacher.objects.order_by('user__last_name')
    return render(request, 'school/teachers.html', {'teachers': teachers})


@login_required
def students(request):
    students = Student.objects.order_by('user__last_name').order_by('classgroups__groupname')
    return render(request, 'school/students.html', {'students': students})


@login_required
def accounts_profile(request):
    return render(request, 'school/accounts_profile.html')


@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'school/student_detail.html', {'student': student})


def logout_view(request):
    logout(request)


# Add students in bulk from CSV
@user_passes_test(is_teacher)
def import_students(request):
    # Deal with getting a CSV file

    if request.method == 'POST':
        csvform = CSVDocForm(request.POST, request.FILES)
        if csvform.is_valid():
            file = csvform.save()
            path = file.document.path
            processstudent(path)
            os.remove(path)
            file.delete()
            return redirect('list_students')
    else:
        csvform = CSVDocForm()
    return render(request, 'school/model_form_upload.html', {'csvform': csvform})


@login_required
def import_teachers(request):
    # Deal with getting a CSV file

    if request.method == 'POST':
        csvform = CSVDocForm(request.POST, request.FILES)
        if csvform.is_valid():
            file = csvform.save()
            path = file.document.path
            processteacher(path)
            os.remove(path)
            file.delete()
            return redirect('list_students')
    else:
        csvform = CSVDocForm()
    return render(request, 'school/model_form_upload.html', {'csvform': csvform})
