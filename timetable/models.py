from django.db import models
from school.models import ClassGroup, Teacher
from tracker.models import SyllabusPoint

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


class LessonSlot(models.Model):
    day = models.CharField(max_length=10, choices=DAYS, blank=False, null=False)
    period = models.IntegerField(choices=PERIODS, blank=False, null=False)

    class Meta:
        unique_together = ['day', 'period']


class TimetabledLesson(models.Model):
    classgroup = models.ForeignKey(ClassGroup, on_delete=models.CASCADE, blank=True, null=True)
    lesson_slot = models.ForeignKey(LessonSlot, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        unique_together = ['classgroup', 'lesson_slot']


class Lesson(models.Model):
    date = models.DateField()
    lesson = models.ForeignKey(TimetabledLesson, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, null=True, blank=True)
    syllabus_points_covered = models.ForeignKey(SyllabusPoint, on_delete=models.SET_NULL, blank=True, null=True)


class LessonResources(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    students_can_view_before = models.BooleanField()
    students_can_view_after = models.BooleanField()
