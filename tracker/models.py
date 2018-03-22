from django.db import models
from school.models import Student
# Create your models here.


class Examboard(models.Model):
    board = models.CharField(max_length=20)

    def __str__(self):
        return self.board


class Examlevel(models.Model):
    examtype = models.CharField(max_length=20)

    def __str__(self):
        return self.examtype


class Syllabus(models.Model):
    board = models.ForeignKey(Examboard, on_delete=models.CASCADE)
    examtype = models.ForeignKey(Examlevel, on_delete=models.CASCADE)
    syllabusname = models.CharField(max_length=50)

    def __str__(self):
        return self.syllabusname


class Syllabuspoint(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
    shortpoint = models.CharField(max_length=10, null=True, blank=True)
    topic = models.CharField(max_length=10, null=True, blank=True)
    syllabustext = models.CharField(max_length=500)

    LEVELS = (
        ('core', 'core'),
        ('extended', 'extended')
    )

    syllabuslevel = models.CharField(max_length=10, choices=LEVELS, blank=True, null=True)

    def __str__(self):
        return self.syllabustext


class Exam(models.Model):
    name = models.CharField(max_length=100)
    syllabus = models.ManyToManyField(Syllabus)

    def __str__(self):
        return self.name


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    qnumber = models.CharField(max_length=100)
    qorder = models.IntegerField()
    syllabuspoint = models.ManyToManyField(Syllabuspoint, blank=True)
    maxscore = models.IntegerField()

    def __str__(self):
        return self.qnumber


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return self.score
