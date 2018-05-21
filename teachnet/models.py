from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.


class Objective(models.Model):
    teacher = models.ForeignKey('school.Teacher', on_delete=models.CASCADE)

    short_name = models.CharField(max_length=100)
    long_text = RichTextField()

    date_created = models.DateField(null=True, auto_now_add=True)  # TODO: Change to FALSE for production

    date_approved = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.short_name


class Skill(models.Model):
    skill_name = models.TextField()
    experience = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.skill_name
