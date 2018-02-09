from django.shortcuts import render
from .models import Teacher
from django.contrib.auth.decorators import login_required


# Create your views here.
def front_login(request):
    return render(request, 'tracker/front_login.html', {})

@login_required
def teachers(request):
    teachers = Teacher.objects.order_by('user__last_name')

    return render(request, 'tracker/teachers.html', {'teachers': teachers})
