from tracker.models import MPTTSyllabus, Syllabus, Examlevel
from timetable.models import Lesson, LessonResources

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

    for resource in LessonResources.objects.filter(syllabus_points__isnull=False):
        resource.mptt_syllabus_points.clear()
        points = resource.syllabus_points.all()

        for point in points:
            equivalent = point.mptt_equivalent()
            if equivalent:
                resource.mptt_syllabus_points.add(point.mptt_equivalent())
            else:
                print("No equivalent found for point id", point.pk)
