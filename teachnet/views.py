from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from school.models import Teacher
import os



@login_required
def home(request):

    return render(request, 'teachnet/home.html')

@login_required
def teacherskills(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachnet/teacher_skills.html', {'teachers': teachers})

@login_required
def profile(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teachnet/profile.html', {'teacher': teacher})

@login_required
def teacherwithskill(request,pk):
    teachers = Teacher.objects.filter(skills__in=pk)
    return render(request, 'teachnet/teacher_skills.html', {'teachers': teachers})
