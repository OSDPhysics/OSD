from django.db import models
from school.models import ClassGroup, Teacher
from tracker.models import SyllabusPoint, Syllabus
from osd.settings.base import CALENDAR_START_DATE, CALENDAR_END_DATE
from django.db.models import Q
from django.db.models import Max


import datetime

# Create your models here.

DAYS = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
)

PERIODS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
)

RESOURCE_TYPES = (
    ('Presentation', 'Presentation'),
    ('Worksheet', 'Worksheet'),
    ('Test', 'Test'),
    ('Mark Scheme', 'Mark Scheme'),
    ('Web Page', 'Web Page'),

)


def get_monday_date_from_weekno(week_number):
    start_date = CALENDAR_START_DATE + datetime.timedelta(weeks=week_number)
    return start_date


class LessonSlot(models.Model):
    day = models.CharField(max_length=10, choices=DAYS, blank=False, null=False)
    period = models.IntegerField(choices=PERIODS, blank=False, null=False)

    class Meta:
        unique_together = ['day', 'period']

    def __str__(self):
        return self.day + " P" + str(self.period)

    def dow(self):
        """Return the day of the week"""
        if self.day == "Monday":
            return 0
        if self.day == "Tuesday":
            return 1
        if self.day == "Wednesday":
            return 2
        if self.day == "Thursday":
            return 3
        if self.day == "Friday":
            return 4

    def teachers_lesson(self, teacher):
        """Return the TimetabledLesson assosciated with a teacher"""
        lesson = TimetabledLesson.objects.get(lesson_slot=self, classgroup__groupteacher=teacher)


class TimetabledLesson(models.Model):
    classgroup = models.ForeignKey(ClassGroup, on_delete=models.CASCADE, blank=True, null=True)
    lesson_slot = models.ForeignKey(LessonSlot, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        unique_together = ['classgroup', 'lesson_slot']

    def __str__(self):
        return str(self.classgroup) + " " + str(self.lesson_slot)

    def dow(self):
        return self.lesson_slot.day

    def total_lessons(self):
        lessons = int(TimetabledLesson.objects.filter(classgroup=self.classgroup).count())
        return lessons

    def order(self):
        all_instances = TimetabledLesson.objects.filter(classgroup=self.classgroup)
        return list(all_instances).index(self) + 1


class Lesson(models.Model):
    lessonslot = models.ForeignKey(TimetabledLesson, on_delete=models.CASCADE)
    classgroup = models.ForeignKey(ClassGroup, null=True, blank=False, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, null=True, blank=True)
    syllabus_points_covered = models.ManyToManyField(SyllabusPoint, blank=True)
    lesson_title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    sequence = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    syllabus = models.ForeignKey(Syllabus, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.lessonslot) + " lesson " + str(self.sequence)

    def resources(self):

        return LessonResources.objects.filter(lesson=self)

    def set_date(self):

        """ A slightly complicated method, which must set the date for the current lesson.

        In order for this to work, we will have to iterate over *every* lesson for the classgroup.
        This is so that we can check for any lesson suspensions. """

        all_lessons = Lesson.objects.filter(lessonslot__classgroup=self.lessonslot.classgroup).order_by('sequence')

        # Lesson slots where these appear.
        slots = TimetabledLesson.objects.filter(classgroup=self.lessonslot.classgroup)

        # Find the first day of term:
        start_date = get_monday_date_from_weekno(0)

        # Find total lessons per week
        lessons_per_week = int(TimetabledLesson.objects.filter(classgroup=self.lessonslot.classgroup).count())

        # we'll use *week* to track each week we're looking at.

        week = 0
        lesson_of_week = 0
        slot_number = 0
        date = CALENDAR_END_DATE


        def next_lesson(week, lesson_of_week, slot_number):
            if lesson_of_week == (lessons_per_week - 1):  # We just did the last lesson of the week
                week = week + 1
                lesson_of_week = 0

            else:
                lesson_of_week = lesson_of_week + 1

            if slot_number != slots.__len__() - 1:
                slot_number = slot_number + 1

            else:
                slot_number = 0

            return week, lesson_of_week, slot_number

        while date > CALENDAR_END_DATE:
            days_taught = []
            for slot in slots:
                days_taught.append(slot.lesson_slot.dow())

            # check if the date is a suspension day:

            suspensions = LessonSuspension.objects.filter(
                Q(whole_school=True) | Q(classgroups=self.lessonslot.classgroup))





    def save(self, date_to_set=False, *args, **kwargs):
        """Make sure we set all dates correctly. """
        if not date_to_set:

            if self.sequence is None:
                # Need to set a sequence number, otherwise the date will always be wrong
                classgroup = self.lessonslot.classgroup
                highest_sequence = Lesson.objects.filter(lessonslot__classgroup=classgroup).aggregate(Max('sequence'))

                if highest_sequence['sequence__max']:
                    self.sequence = highest_sequence['sequence__max'] + 1
                else:
                    self.sequence = 0

            super(Lesson, self).save(*args, **kwargs)
            self.set_date()

        else:

            self.date = date_to_set

            super(Lesson, self).save(*args, **kwargs)

        return self

    def lesson_resource_icons(self):
        icons = []
        resources = LessonResources.objects.filter(lesson=self)

        def generate_string(font_awesome_string, resource):
            string = "<a href=" + str(resource.link)
            string = string + 'data-toggle="tooltip" data-placement="top" title="'
            string = string + (str(resource.resource_name))
            string = string + '">'
            string = string + font_awesome_string
            string = string + "</i></a>"

            return string

        for resource in resources:
            if resource.resource_type == "Presentation":
                string = generate_string("<i class='fas fa-desktop'>", resource)

            elif resource.resource_type == "Web Page":
                string = generate_string("<i class='fas fa-tablet-alt'>", resource)

            elif resource.resource_type == "Worksheet":
                string = generate_string('<i class="far fa-newspaper">', resource)

            elif resource.resource_type == "Test":
                string = generate_string('<i class="fas fa-pencil-ruler">', resource)

            else:
                string = generate_string('<i class="far fa-question-circle">', resource)

            icons.append(string)

        return icons

class LessonResources(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=100, choices=RESOURCE_TYPES, null=False, blank=False)
    resource_name = models.CharField(max_length=100, null=True, blank=False)
    link = models.URLField(blank=True, null=True)
    students_can_view_before = models.BooleanField()
    students_can_view_after = models.BooleanField()


class LessonSuspension(models.Model):
    """Store suspensions and missing lessons"""
    whole_school = models.BooleanField(default=True)
    date = models.DateField(blank=False, null=False)
    reason = models.CharField(max_length=200, blank=False, null=True)
    classgroups = models.ManyToManyField(ClassGroup, blank=True, null=True)
    all_day = models.BooleanField(default=False)
    period = models.IntegerField(choices=PERIODS, blank=True, null=True)

    def save(self, *args, **kwargs):
        """When we save, we need to update the dates of all affected lessons. """

        affected_lessons = Lesson.objects.filter(date=self.date)
        for lesson in affected_lessons:
            lesson.set_date()
        super(LessonSuspension, self).save(*args, **kwargs)
