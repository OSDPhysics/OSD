from django.shortcuts import render
from .models import StudentJournalEntry
from school.models import Student
from tracker.models import SyllabusPoint
from osd.decorators import own_or_teacher_only
from django.forms import modelformset_factory
# Create your views here.

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

    data = list(zip(syllabus_points, journal_formset))

    return render(request, 'journal/all_student_entries.html', {'data': data,
                                                                'student': student})
