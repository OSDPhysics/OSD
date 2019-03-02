from tracker.models import MPTTSyllabus, Syllabus, Examlevel, Question, Mark, Sitting
from journal.models import StudentJournalEntry
from timetable.models import Lesson, LessonResources
from school.models import ClassGroup

def convert_to_mptt():
    """ Take our existing syllabus structure and convert to MPTT type. """
    # Steps are as follows;
    # 0. Delete all existing ones to prevent duplication
    # 1. Get all the Levels.
    # 2. Get all the syllabus'
    # 3. For each syllabus, get its topics
    # 4. For each topic, get all the sub topics
    # 5. Create a point for each one.

    # 0 Delete all existing:
    MPTTSyllabus.objects.all().delete()
    # 1. Get and create each level:

    levels = Examlevel.objects.all()
    for level in levels:
        current_level = MPTTSyllabus.objects.create(text=level.examtype)
        syllabuses = Syllabus.objects.filter(examtype=level)

        for syllabus in syllabuses:
            print("Currently on: ", syllabus)
            mptt_syllabus = MPTTSyllabus.objects.create(text=syllabus.syllabusname, parent=current_level,
                                                        related_syllabus=syllabus)
            topics = syllabus.all_topics()
            for topic in topics:
                print("Currently on: ", topic)
                mptt_topic = MPTTSyllabus.objects.create(text=topic.topic, parent=mptt_syllabus, related_topic=topic,
                                                         related_syllabus=syllabus)
                sub_topics = topic.sub_topics()
                for sub_topic in sub_topics:
                    mptt_sub_topic = MPTTSyllabus.objects.create(parent=mptt_topic, text=sub_topic.sub_topic,
                                                                 related_sub_topic=sub_topic, related_topic=topic,
                                                                 related_syllabus=syllabus)
                    points = sub_topic.syllabus_points()
                    for point in points:
                        MPTTSyllabus.objects.create(parent=mptt_sub_topic, text=point.syllabusText,
                                                    tier=point.syllabusLevel, related_point=point, number=point.number,
                                                    related_sub_topic=sub_topic, related_topic=topic,
                                                    related_syllabus=syllabus)

    # Now add MPTTSyllabus items where needed:

    # LESSONS
    print("Updating lessons to use MPTTSyllabus")
    for lesson in Lesson.objects.filter(lesson_title__isnull=False):
        lesson.mptt_syllabus_points.clear()
        spoints = lesson.syllabus_points_covered.all()
        for point in spoints:
            equivalent = point.mptt_equivalent()
            if equivalent:
                lesson.mptt_syllabus_points.add(equivalent)
            else:
                print("No equivalent found for point id", point.pk)
    # RESOURCES

    print("Updating resources to use MPTT syllabus")
    for resource in LessonResources.objects.filter(syllabus_points__isnull=False):
        resource.mptt_syllabus_points.clear()
        points = resource.syllabus_points.all()

        for point in points:
            equivalent = point.mptt_equivalent()
            if equivalent:
                resource.mptt_syllabus_points.add(point.mptt_equivalent())
            else:
                print("No equivalent found for point id", point.pk)

    # QUESTIONS
    print("Now updating questions to use new MPTTSyllabus")
    for question in Question.objects.filter(syllabuspoint__isnull=False):
        question.MPTTsyllabuspoint.clear()
        points = question.syllabuspoint.all()

        for point in points:
            question.MPTTsyllabuspoint.add(point.mptt_equivalent())

    # MARKS
    print("Now updaitng marks to have calculated fields")
    for mark in Mark.objects.filter(score__isnull=False):
        mark.set_calculated_values()

    # Ratings

    print("Now creating student ratings")
    for sitting in Sitting.objects.all():
        print("Currently on: " + str(sitting))
        sitting.create_ratings()

    convert_classgroup_syllabai()
    convert_journal_entries()

def calculate_sitting_ratings():
    print("Now creating student ratings")
    for sitting in Sitting.objects.all():
        print("Currently on: " + str(sitting))
        sitting.create_ratings()

def convert_classgroup_syllabai():
    print ("Now converting classgroup Syllabai")
    for classgroup in ClassGroup.objects.all():
        print("Now on classgroup: " + str(classgroup))
        for syllabus in classgroup.syllabustaught.all():
            print("Now on syllabus: " + str(syllabus))
            equivalent = MPTTSyllabus.objects.get(related_syllabus=syllabus, related_topic__isnull=True)
            classgroup.mptt_syllabustaught.add(equivalent)


def convert_journal_entries():
    print("Now converting student Journal entries")

    for entry in StudentJournalEntry.objects.filter(syllabus_point__isnull=True):
        print("Now on: " + str(entry.student))
        equivalent = MPTTSyllabus.objects.get(related_sub_topic=entry.syllabus_sub_topic, related_point__isnull=True)
        entry.mptt_syllabus = equivalent
        entry.save()
