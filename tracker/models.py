from django.db import models
from school.models import Student, ClassGroup
import numpy

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


class SyllabusTopic(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.topic


class SyllabusPoint(models.Model):
    topic = models.ForeignKey(SyllabusTopic, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    syllabusText = models.TextField()

    LEVELS = (
        ('core', 'core'),
        ('extended', 'extended')
    )

    syllabusLevel = models.CharField(max_length=10, choices=LEVELS, blank=True, null=True)

    def __str__(self):
        return self.topic.topic + " " + self.number

    def get_student_rating(self, student):
        scores = Mark.objects.filter(question__syllabuspoint__in=self).filter(question__mark__student=student)
        numpy.mean(scores.score)


class Exam(models.Model):
    name = models.CharField(max_length=100)
    syllabus = models.ManyToManyField(Syllabus)

    def __str__(self):
        return self.name


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    qnumber = models.CharField(max_length=100)
    qorder = models.IntegerField()
    syllabuspoint = models.ManyToManyField(SyllabusPoint)
    maxscore = models.IntegerField()

    def __str__(self):
        return self.qnumber


class Sitting(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    classgroup = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    datesat = models.DateField()
    openForStudentRecording = models.BooleanField()


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.score)


# CSV Uploads


class CSVDoc(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
