from django.shortcuts import render, redirect
from django.urls import reverse
from .models import StudentJournalEntry
from school.models import Student, Teacher
from tracker.models import SyllabusPoint, SyllabusTopic, SyllabusSubTopic
from osd.decorators import own_or_teacher_only
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def splash(request):
    if request.user.groups.filter(name='Students'):
        student = Student.objects.get(user=request.user)
        return redirect(reverse('full_journal', args=(student.pk,)))

    else:
        teacher = Teacher.objects.get(user=request.user)
        students = Student.objects.filter(classgroups__groupteacher=teacher)

        return render(request, 'journal/studentlist.html', {'students': students})


# Really, don't use this! It half-murders the database!
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

    journal_formset = journal_formset_factory(
        queryset=StudentJournalEntry.objects.filter(student=student).order_by('syllabus_point__number').order_by(
            'syllabus_point__topic'))

    # Now get topic ratings
    ratings = []
    for point in syllabus_points:
        ratings.append(round(point.get_student_rating(student) * 5, 1))

    data = list(zip(syllabus_points, ratings, journal_formset))

    return render(request, 'journal/all_student_entries.html', {'data': data,
                                                                'student': student,
                                                                'journal_formset': journal_formset})


# Should probably try to avoid this too, but it's less evil.
# Eventually we should move this all to sub-topics only.
def print_full_journal(request, student_pk):
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


@own_or_teacher_only
def view_topic(request, student_pk, topic_pk):
    student = Student.objects.get(pk=student_pk)
    topic = SyllabusTopic.objects.get(pk=topic_pk)

    syllabus_sub_topics = SyllabusSubTopic.objects.filter(topic=topic)

    syllabus_points = SyllabusPoint.objects.filter(topic=topic)

    sub_topic_ratings = []
    for sub_topic in syllabus_sub_topics:
        sub_topic_ratings.append(sub_topic.studentAverageRating(student))

    sub_topic_data = list(zip(syllabus_sub_topics, sub_topic_ratings))

    syllabus_ratings = []
    for syllabus_point in syllabus_points:
        syllabus_ratings.append(syllabus_point.get_student_rating(student))

    syllabus_point_data = list(zip(syllabus_points, syllabus_ratings))

    return render(request, 'journal/student_topic_overview.html', {'student': student,
                                                                   'sub_topic_data': sub_topic_data,
                                                                   'syllabus_point_data': syllabus_point_data,
                                                                   'topic': topic})
