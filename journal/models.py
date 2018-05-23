from django.db import models
from school.models import Student
from tracker.models import SyllabusPoint
from ckeditor.fields import RichTextField
# Create your models here.

class StudentJournalEntry(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    syllabus_point = models.ForeignKey(SyllabusPoint, on_delete=models.SET_NULL, blank=True, null=True)
    entry = RichTextField(null=True, blank=True)

    class Meta:
        unique_together = ('student', 'syllabus_point')
