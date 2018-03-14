from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import StudentForm, TeacherForm, NewExamForm
from .models import Teacher, Student
from .functions.adddata import *
import csv
import codecs
import os


# Create your views here.
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
            return HttpResponseRedirect('tracker/teachers/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TeacherForm()
    return render(request, 'tracker/new_teacher.html', {'form': form})


def new_student(request):
    form = StudentForm()
    return render(request, 'tracker/new_student.html', {'form': form})


def login(request):
    return render(request, 'tracker/login.html', {})


def logged_out(request):
    return render(request, 'registration/logged_out.html', {})


@login_required
def teachers(request):
    teachers = Teacher.objects.order_by('user__last_name')
    return render(request, 'tracker/teachers.html', {'teachers': teachers})


def teacher_details(request):
    return


def students(request):
    students = Student.objects.order_by('user__last_name').order_by('classgroups__groupname')
    return render(request, 'tracker/students.html', {'students': students})


@login_required
def profile(request):
    return render(request, 'registration/profile.html', {})


@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'tracker/student_detail.html', {'student': student})


@login_required
def import_students(request):
    if request.POST and request.FILES:
        # csvfile = request.FILES['csv_file'].read()
        settings_dir = os.path.dirname(__file__)
        PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

        STATIC_FOLDER = os.path.join(PROJECT_ROOT, 'tracker/static/')
        csvfile = open(STATIC_FOLDER + 'input.csv', 'r')
        # ndialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        # csvfile.open()
        reader = csv.reader(csvfile, delimiter=',')
        processstudent(reader)

    return render(request, "tracker/import_students.html", locals())


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
