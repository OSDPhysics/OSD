from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm, TeacherForm, UserForm, UserDetails
from .models import Teacher, Student
from .functions.adddata import *
import csv
import codecs
import os

# Create your views here.
def splash(request):
    return render(request, 'tracker/splash.html', {})

def new_teacher(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            form.save()
            return redirect('splash')
    else:
       form = UserForm()
    return render(request, 'tracker/new_teacher.html', {'form': form})

def add_teacher(request):
    form1 = TeacherForm()
    form2 = UserDetails()
    return render(request, 'tracker/edit_teacher.html', {'form1': form1, 'form2': form2})


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

def students(request):
    students = Student.objects.order_by('user__last_name').order_by('classgroups__groupname')
    return render(request, 'tracker/students.html', {'students': students})


@login_required
def profile(request):
    return render(request, 'registration/profile.html',{})

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'tracker/student_detail.html', {'student': student})

@login_required
def import_students(request):
    if request.POST and request.FILES:
        #csvfile = request.FILES['csv_file'].read()
        settings_dir = os.path.dirname(__file__)
        PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

        STATIC_FOLDER = os.path.join(PROJECT_ROOT, 'tracker/static/')
        csvfile = open(STATIC_FOLDER + 'input.csv','r')
        #ndialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        #csvfile.open()
        reader = csv.reader(csvfile,  delimiter=',')
        processstudent(reader)



    return render(request, "tracker/import_students.html", locals())
