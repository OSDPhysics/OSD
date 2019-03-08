from django.db import models
from tracker.models import MPTTSylabus
from mptt.models import TreeForeignKey
from school.models import Teacher, Student

# Create your models here.


class RevisionSession(models.Model):
    syllabus_subject = TreeForeignKey(blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    teachers_in_charge = models.ManyToManyField(Teacher)
    date = models.DateField(null=False, blank=False)

    booking_until = models.DateTimeField(blank=False, null=False)

    students_attending = models.ManyToManyField(Student)

    def __str__(self):
        return self.title + str(self.date)
