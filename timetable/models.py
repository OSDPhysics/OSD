from django.db import models
from school.models import ClassGroup, Teacher
from tracker.models import SyllabusPoint
from osd.settings.base import CALENDAR_START_DATE

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
        all_instances = all_instances.order_by('sequence')
        return list(all_instances).index(self) + 1


class Lesson(models.Model):
    lesson = models.ForeignKey(TimetabledLesson, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, null=True, blank=True)
    syllabus_points_covered = models.ManyToManyField(SyllabusPoint)
    title = models.CharField(max_length = 200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    sequence = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.lesson) + " lesson " + str(self.sequence)

    def resources(self):

        return LessonResources.objects.filter(lesson=self)

    def date(self):
        slots = TimetabledLesson.objects.filter(classgroup=self.lesson.classgroup)

        # Find the first day of term:
        start_date = get_monday_date_from_weekno(0)

        # Find total lessons per week
        lessons_per_week = int(TimetabledLesson.objects.filter(classgroup=self.lesson.classgroup).count())



        # Find which of this weeks lessons we're dealing with
        lesson_of_week = int(self.sequence % lessons_per_week)

        days_taught = []
        for slot in slots:
            days_taught.append(slot.lesson_slot.dow())

        # Find lesson of the week

        day_taught = days_taught[lessons_per_week % self.sequence]

        # Find in which week it appears
        weekno = self.sequence // lessons_per_week
        date = start_date + datetime.timedelta(weeks=weekno) + datetime.timedelta(days=day_taught)

        return date


class LessonResources(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    students_can_view_before = models.BooleanField()
    students_can_view_after = models.BooleanField()
