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

            text_to_insert = "<p><strong>Entered from Assessment: " + str(reflection.sitting.exam) + " on " + str(reflection.sitting.datesat) + "</strong></p><p>" + reflection.notes + "</p>"

            print(text_to_insert)
            if journal_entry == text_to_insert:
                continue
            else:
                if journal_entry.entry:
                    journal_entry.entry = journal_entry.entry + text_to_insert
                else:
                    journal_entry.entry = text_to_insert

            journal_entry.save()