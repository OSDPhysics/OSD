from django.shortcuts import render, redirect
from django.urls import reverse
from .models import StudentJournalEntry
from school.models import Student, Teacher
from tracker.models import SyllabusPoint
from osd.decorators import own_or_teacher_only
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def splash(request):
    if request.user.groups.filter(name='Students'):
        student = Student.objects.get(user=request.user)
        return redirect(reverse('full_journal', student.pk))

    else:
        teacher = Teacher.objects.get(user=request.user)
        students = Student.objects.filter(classgroups__groupteacher=teacher)

        return render(request, 'journal/studentlist.html', {'students': students})

@own_or_teacher_only
def full_journal(request, student_pk):

    student = Student.objects.get(pk=student_pk)
    student_classes = student.classgroups.all()
    syllabus_points = SyllabusPoint.objects.filter(topic__syllabus__classgroup__in=student.classgroups.all())

    # Make sure journal items exist:

    journal_entries = []
    for point in syllabus_points:
        entry, created = StudentJournalEntry.objects.get_or_create(student=student, syllabus_point=point)
        journal_entries.append(entry.entry)

    journal_formset_factory = modelformset_factory(StudentJournalEntry, extra=0, fields=('entry',))

    journal_formset = journal_formset_factory(queryset=StudentJournalEntry.objects.filter(student=student).order_by('syllabus_point__number').order_by('syllabus_point__topic'))

    # Now get topic ratings
    ratings = []
    for point in syllabus_points:
        ratings.append(round(point.get_student_rating(student)*5,1))

    data = list(zip(syllabus_points, ratings, journal_formset))

    return render(request, 'journal/all_student_entries.html', {'data': data,
                                                                'student': student,
                                                                'journal_formset': journal_formset})

def print_journal(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    student_classes = student.classgroups.all()
    syllabus_points = SyllabusPoint.objects.filter(topic__syllabus__classgroup__in=student.classgroups.all())

    # Make sure journal items exist:

    journal_entries = []
    for point in syllabus_points:
        entry, created = StudentJournalEntry.objects.get_or_create(student=student, syllabus_point=point)
        journal_entries.append(entry.entry)


    # Now get topic ratings
    ratings = []
    for point in syllabus_points:
        ratings.append(round(point.get_student_rating(student) * 5, 1))

    data = list(zip(syllabus_points, ratings, journal_entries))

    return render(request, 'journal/all_student_entries_print.html', {'data': data,
                                                                'student': student})
