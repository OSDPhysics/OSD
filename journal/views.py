from django.shortcuts import render
from .models import StudentJournalEntry
from school.models import Student
from tracker.models import SyllabusPoint
from osd.decorators import own_or_teacher_only
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

    data = list(zip(syllabus_points, journal_entries))

    return render(request, 'journal/all_student_entries.html', {'data': data,
                                                                'student': student})
