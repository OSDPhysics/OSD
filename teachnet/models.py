from django.db import models
#from school.models import Teacher as myTeacher
# Create your models here.


class Objective(models.Model):
    teacher = models.ForeignKey('school.Teacher', on_delete=models.CASCADE)

    short_name = models.CharField(max_length=100)
    long_text = models.TextField()

    def __str__(self):
        return self.short_name


class Skill(models.Model):
    skill_name = models.TextField()
