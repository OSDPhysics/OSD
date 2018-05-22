from django.db import models
from tracker.models import SyllabusPoint, SyllabusTopic, Mark
from school.models import Student
from ckeditor.fields import RichTextField

# Create your models here.


class StudentJournalEntry(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_created = models.DateField()

    mark = models.ForeignKey(Mark, blank=True, null=True, on_delete=models.CASCADE)

    syllabus_point = models.ManyToManyField(SyllabusPoint)
    syllabus_topic = models.ManyToManyField(SyllabusTopic)
    entry = RichTextField()

    def __str__(self):
        return str(self.student) + ' ' + str(self.date_created) + ' ' + str(self.pk)
