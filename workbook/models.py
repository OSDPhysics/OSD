from django.db import models
from timetable.models import Lesson
from school.models import Student
from tracker.models import MPTTSyllabus
# Create your models here.

class WorkTemplate(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=150, blank=False, null=False)
    template = models.URLField(blank=True, null=True)
    instructions = models.URLField(blank=True, null=True)
    syllabus_points = models.ManyToManyField(MPTTSyllabus, blank=True)
    max_mark = models.FloatField(blank=True, null=True)
    min_mark = models.FloatField(blank=True, null=True)


class StudentWork(models.Model):
    template = models.ForeignKey(WorkTemplate, on_delete=models.CASCADE, blank=False, null=False)
    student = models.ForeignKey(Student, blank=False, null=False, on_delete=models.CASCADE)
    mark = models.FloatField(blank=True, null=True)
    teacher_comments = models.TextField(blank=True, null=True)
    linked_folder = models.URLField(blank=True, null=True)