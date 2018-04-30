from django.db import models
from school.models import Teacher
# Create your models here.


class Objective(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    short_name = models.CharField(max_length=100)
    long_text = models.CharField()

    def __str__(self):
        return self.short_name


class Skill(models.Model):
    skill_name = models.CharField()
