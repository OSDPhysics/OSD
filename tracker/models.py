from django.db import models
from school.models import Student, ClassGroup
import numpy
from django.db.models import Sum
from ckeditor.fields import RichTextField


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

    def studentAverageRating(self, student):
        marks = Mark.objects.filter(question__syllabuspoint__topic=self).filter(student=student)
        pcs = []
        for mark in marks:
            if mark.score is not None:
                pcs.append(mark.score / mark.question.maxscore)
        return round(numpy.mean(pcs) * 5, 1)


class SyllabusSubTopic(models.Model):
    topic = models.ForeignKey(SyllabusTopic, on_delete=models.CASCADE)
    sub_topic = models.CharField(max_length=100)

    def __str__(self):
        return str(self.topic) + ': ' + str(self.sub_topic)

    def studentAverageRating(self, student):
        points = SyllabusPoint.objects.filter(sub_topic=self)
        marks = Mark.objects.filter(question__syllabuspoint__in=points, student=student)
        return mark_queryset_to_rating(marks)


class SyllabusPoint(models.Model):
    topic = models.ForeignKey(SyllabusTopic, on_delete=models.CASCADE)
    sub_topic = models.ForeignKey(SyllabusSubTopic, on_delete=models.CASCADE, null=True)
    number = models.CharField(max_length=10)
    syllabusText = models.TextField()

    LEVELS = (
        ('core', 'core'),
        ('extended', 'extended')
    )

    syllabusLevel = models.CharField(max_length=10, choices=LEVELS, blank=True, null=True)

    def __str__(self):
        return self.topic.topic + " " + self.number + " " + self.syllabusText

    def get_student_rating(self, student):
        marks = Mark.objects.filter(question__syllabuspoint=self).filter(student=student)
        return mark_queryset_to_rating(marks)


class Exam(models.Model):
    name = models.CharField(max_length=100)
    syllabus = models.ManyToManyField(Syllabus)

    def __str__(self):
        return self.name

    def max_score(self):
        return Question.objects.filter(exam=self).aggregate(Sum('maxscore'))


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

    def student_total(self, student):
        total = Mark.objects.filter(sitting=self).filter(student=student).aggregate(Sum('score'))

        return total['score__sum']

    def class_average_score_int(self):
        students = Student.objects.filter(classgroups=self.classgroup)
        scores = []
        for student in students:
            if self.student_total(student):
                scores.append(self.student_total(student))
        return round(numpy.average(scores))

    def class_average_score_str(self):
        return str(self.class_average_score_int()) + '/' + str(self.exam.max_score()['maxscore__sum'])

    def __str__(self):
        return self.exam.name + " " + self.classgroup.groupname

    def class_score_range(self):
        students = Student.objects.filter(classgroups=self.classgroup)
        scores = []
        for student in students:
            if self.student_total(student):
                scores.append(self.student_total(student))
        score_range = numpy.max(scores) - numpy.min(scores)
        return score_range

    def class_score_std(self):
        students = Student.objects.filter(classgroups=self.classgroup)
        scores = []
        for student in students:
            if self.student_total(student):
                scores.append(self.student_total(student))

        return round(numpy.std(scores),1)


class Mark(models.Model):
    # TODO: This should be updated whenever a sitting is modified
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField(blank=True, null=True)
    sitting = models.ForeignKey(Sitting, on_delete=models.CASCADE)
    notes = RichTextField(null=True, blank=True)

    def __str__(self):
        return str(self.question.exam) + ' ' + str(self.student) + ' ' + str(self.question) + '(' + str(
            self.score) + ')'

    def percentage(self):

        if self.score:
            return round(self.score / self.question.maxscore * 100, 2)
        # CSV Uploads
        else:
            return False


class CSVDoc(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


def mark_queryset_to_rating(marks):
    """ take a queryset of marks and return a student rating for it."""
    pcs = []
    for mark in marks:
        if mark.score is not None:
            pcs.append(mark.score / mark.question.maxscore)
    return round(numpy.mean(pcs) * 5, 1)
