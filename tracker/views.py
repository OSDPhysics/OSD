from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import StudentForm, TeacherForm, UserForm


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

def new_student(request):
    form = StudentForm()
    return render(request, 'tracker/new_student.html', {'form': form})

def login(request): 
    return render(request, 'tracker/login.html', {})

def teachers(request):
    return render(request, 'tracker/teachers.html', {})

def students(request):
    return render(request, 'tracker/students.html', {})
