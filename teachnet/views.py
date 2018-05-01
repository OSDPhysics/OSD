from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from school.models import Teacher
import os


def can_view_profile(requester, user):
    if requester.pk == user.pk: # viewing own profile
        return True

    # check if the requester is the line manager of the user
    islinemanager = Teacher.objects.filter(line_manager=requester).count()

    if islinemanager >= 1:
        return True

    # We're not the user, or the line manager, so kick them out
    return False

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

    if can_view_profile(request.user,teacher):
        return render(request, 'teachnet/profile.html', {'teacher': teacher})

    else:
        return render(request, 'teachnet/forbidden.html')

@login_required
def teacherwithskill(request,pk):
    teachers = Teacher.objects.filter(skills__in=pk)
    return render(request, 'teachnet/teacher_skills.html', {'teachers': teachers})
