from django.shortcuts import render
from .models import Teacher
from django.contrib.auth.decorators import login_required
from .forms import TeacherForm
from .forms import UserDetails

# Create your views here.
def front_login(request):
    return render(request, 'tracker/front_login.html', {})

@login_required
def teachers(request):
    teachers = Teacher.objects.order_by('user__last_name')

    return render(request, 'tracker/teachers.html', {'teachers': teachers})

def add_teacher(request):
    form1 = TeacherForm()
    form2 = UserDetails()
    return render(request, 'tracker/edit_teacher.html', {'form1': form1, 'form2': form2})
