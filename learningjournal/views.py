from django.shortcuts import render, redirect, get_object_or_404
from tracker.models import SyllabusPoint, SyllabusTopic, Syllabus
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

@own_or_teacher_only
def student_journal_syllabus(request, student_pk, syllabus_pk):

    student = Student.objects.get(pk=student_pk)
    entries = StudentJournalEntry.objects.filter(student=student)
    syllabus = Syllabus.objects.get(pk=syllabus_pk)

    syllabus_points_taught = SyllabusPoint.objects.filter(topic__syllabus=syllabus).order_by('number', 'topic')

    ratings = []
    for topic in syllabus_points_taught:
        ratings.append(round(topic.get_student_rating(student) * 5, 1))

    topic_data = list(zip(syllabus_points_taught, ratings))

    return render(request, 'learningjournal/student_journal_syllabus.html', {'student': student,
                                                                        'topic_data': topic_data,
                                                                             'syllabus': syllabus})

