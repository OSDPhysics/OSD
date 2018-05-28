from django.db import models
from school.models import Student
from tracker.models import SyllabusPoint, SyllabusSubTopic
from ckeditor.fields import RichTextField
# Create your models here.


class StudentJournalEntry(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    syllabus_point = models.ForeignKey(SyllabusPoint, on_delete=models.SET_NULL, blank=True, null=True)
    syllabus_sub_topic = models.ForeignKey(SyllabusSubTopic, on_delete=models.SET_NULL, blank=True, null=True)
    entry = RichTextField(null=True, blank=True)

    class Meta:
        unique_together = (('student', 'syllabus_point'),
                           ('student', 'syllabus_sub_topic'))
