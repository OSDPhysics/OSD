from django.db import models
import tracker


# Create your models here.


class Question(models.Model):
    syllabus = models.ForeignKey(tracker.models.Syllabus, on_delete=models.CASCADE)
    qimage = models.ImageField(upload_to='qimages')
    year = models.IntegerField()
    paper = models.CharField(max_length = 10)
    qnumber = models.IntegerField()
    aimage = models.ImageField(upload_to='aimages')


