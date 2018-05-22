from django.shortcuts import render, redirect, get_object_or_404
from school.models import Student, Teacher
from django.urls import reverse
from osd.decorators import *
from django.contrib.auth.decorators import login_required

from learningjournal.models import StudentJournalEntry
# Create your views here.

@login_required()
def splash(request):
    if request.user.groups.filter(name='Students'):
        return redirect(reverse('student_journal', request.user.pk))


@own_or_teacher_only
def student_journal(request, student_pk):

    student = Student.objects.get(pk=student_pk)
    entries = StudentJournalEntry.objects.filter(student=student).order_by('date_created')

    return render(request, 'learningjournal/student_journal.html', {'student': student,
                                                           'entries': entries})

