from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import StudentForm, TeacherForm, UserForm, UserDetails
from .models import Teacher

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
    return render(request, 'tracker/teachers.html', {})

def students(request):
    return render(request, 'tracker/students.html', {})
    teachers = Teacher.objects.order_by('user__last_name')
    return render(request, 'tracker/teachers.html', {'teachers': teachers})

@login_required
def profile(request):
    return render(request, 'registration/profile.html',{})
