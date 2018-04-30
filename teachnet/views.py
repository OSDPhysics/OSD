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
def profile(request):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teachnet/profile.html', {'teacher': teacher})