from journal.models import *
from tracker.models import *


def move_mark_reflection_to_journal():
    # Get all mark reflections
    reflections = Mark.objects.exclude(notes__isnull=True).exclude(notes__exact='')
    for reflection in reflections:
        student = reflection.student
        mark_points = reflection.question.syllabuspoint.all()
        for mark_point in mark_points:

            journal_entry, created = StudentJournalEntry.objects.get_or_create(student=student, syllabus_sub_topic=mark_point.sub_topic)

            text_to_insert = "<p><strong>Entered from Assessment: " + str(reflection.sitting.exam) + " on " + str(reflection.sitting.datesat) + "<a href='/tracker/sittings/"+ str(reflection.sitting.pk) + "/" +str(reflection.student.pk) + "'> Question  " + str(reflection.question) + "</a></strong></p>" + reflection.notes

            print(text_to_insert)
            if text_to_insert in journal_entry.entry:
                continue
            else:
                if journal_entry.entry:
                    journal_entry.entry = journal_entry.entry + text_to_insert
                else:
                    journal_entry.entry = text_to_insert

            journal_entry.save()

def move_mark_reflection_to_journal_student(student , sitting):

    # Get all mark reflections
    reflections = Mark.objects.filter(student=student, sitting=sitting).exclude(notes__isnull=True).exclude(notes__exact='')
    for reflection in reflections:
        student = reflection.student
        mark_points = reflection.question.syllabuspoint.all()
        for mark_point in mark_points:

            journal_entry, created = StudentJournalEntry.objects.get_or_create(student=student, syllabus_sub_topic=mark_point.sub_topic)

            text_to_insert = "<p><strong>Entered from Assessment: " + str(reflection.sitting.exam) + " on " + str(reflection.sitting.datesat) + "<a href='/tracker/sittings/"+ str(reflection.sitting.pk) + "/" +str(reflection.student.pk) + "'> Question  " + str(reflection.question) + "</a></strong></p>" + reflection.notes

            print(text_to_insert)

            if journal_entry.entry:
                if text_to_insert in journal_entry.entry:
                    continue
                else:
                    if journal_entry.entry:
                        journal_entry.entry = journal_entry.entry + text_to_insert
                    else:
                        journal_entry.entry = text_to_insert
            else:
                journal_entry.entry = text_to_insert

            journal_entry.save()
