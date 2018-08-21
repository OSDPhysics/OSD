from django.db import models
from school.models import ClassGroup, Teacher
from tracker.models import SyllabusPoint, Syllabus
from osd.settings.base import CALENDAR_START_DATE
from django.db.models import Q

import datetime

# Create your models here.

DAYS = (
    ('Monday', 'Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
        )

PERIODS = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
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
    lesson = models.ForeignKey(TimetabledLesson, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, null=True, blank=True)
    syllabus_points_covered = models.ManyToManyField(SyllabusPoint)
    title = models.CharField(max_length = 200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    sequence = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    syllabus = models.ForeignKey(Syllabus, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.lesson) + " lesson " + str(self.sequence)

    def resources(self):

        return LessonResources.objects.filter(lesson=self)

    def set_date(self):

        """ A slightly complicated method, which must set the date for the current lesson.

        In order for this to work, we will have to iterate over *every* lesson for the classgroup.
        This is so that we can check for any lesson suspensions. """

        all_lessons = Lesson.objects.filter(lesson__classgroup=self.lesson.classgroup)

        # Lesson slots where these appear.
        slots = TimetabledLesson.objects.filter(classgroup=self.lesson.classgroup)

        # Find the first day of term:
        start_date = get_monday_date_from_weekno(0)

        # Find total lessons per week
        lessons_per_week = int(TimetabledLesson.objects.filter(classgroup=self.lesson.classgroup).count())

        # we'll use *week* to track each week we're looking at.

        week = 0

        for lesson in all_lessons:

            # Find which of this weeks lessons we're dealing with
            lesson_of_week = int(lesson.sequence % lessons_per_week)

            days_taught = []
            for slot in slots:
                days_taught.append(slot.lesson_slot.dow())

            # Find lesson of the week

            day_taught = days_taught[lessons_per_week % self.sequence]

            # Find in which week it should appear
            weekno = week
            date = start_date + datetime.timedelta(weeks=weekno) + datetime.timedelta(days=day_taught)

            # check if the date is a suspension day:

            suspensions = LessonSuspension.objects.filter(Q(whole_school=True)|Q(classgroups=lesson.lesson.classgroup))

            for suspension in suspensions: # Check for a suspension
                if date == suspension.date and suspension.all_day is True:
                    continue

                elif date == suspension.date and suspension.period == lesson.lesson.lesson_slot.period:
                    continue

                else: # lesson isn't suspended, so save it.
                    lesson.date = date
                    lesson.save() # TODO: Add a kwarg to disable the self.set_date in the overriden save() method to prevent infinite recurision.

    def save(self, *args, **kwargs):
        """Make sure we set all dates correctly. """
        self.set_date()
        super(Lesson, self).save(*args, **kwargs)


class LessonResources(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=100)
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