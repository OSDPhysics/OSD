from django.shortcuts import render
from school.models import Teacher
# Create your views here.


def markbook(request):

    teacher = Teacher.objects.get(user=request.user)
    return render(request, 'DataDashboard/markbook.html', {'teacher': teacher})