from django.db import models
from school.models import Student, ClassGroup
import numpy
from django.db.models import Sum
from ckeditor.fields import RichTextField
from django.apps import apps


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

    def student_completion(self, student):
        """Find the % of entire syllabus a student has marks entered for"""
        all_points = SyllabusPoint.objects.filter(topic__syllabus=self)

        all_marks = Mark.objects.filter(student=student, score__isnull=False)
        completed_points = all_points.filter(question__mark__in=all_marks).distinct()
        if completed_points.count() != 0:
            return int(round(completed_points.count()/all_points.count()*100,0))
        else:
            return 0


    def studentAverageRating(self, student):
        marks = Mark.objects.filter(question__exam__syllabus=self).filter(student=student)
        return mark_queryset_to_rating(marks)

    def classgroup_completion(self, classgroup):
        points = SyllabusPoint.objects.filter(topic__syllabus=self)
        students = Student.objects.filter(classgroups=classgroup)
        entered = SyllabusPoint.objects.filter(question__mark__student__in=students,
                                               question__syllabuspoint__in=points).distinct().count()

        if points.count() > 0:
            return int(round(entered / points.count() * 100, 0))
        else:
            return 0


    def classgroup_average_rating(self, classgroup):
        marks = Mark.objects.filter(question__syllabuspoint__topic__syllabus=self).filter(sitting__classgroup=classgroup)
        return mark_queryset_to_rating(marks)

class SyllabusTopic(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.topic

    def studentAverageRating(self, student):
        marks = Mark.objects.filter(question__syllabuspoint__topic=self).filter(student=student)
        return mark_queryset_to_rating(marks)

    def studentCompletion(self, student):
        possible = SyllabusPoint.objects.filter(topic=self).distinct()
        with_score = possible.filter(question__mark__student=student)

        if possible.count() > 0:
            return round(with_score.count() / possible.count() *100)
        else:
            return 0

    def studentSubTopicData(self, student):
        sub_topics = SyllabusSubTopic.objects.filter(topic=self)
        ratings = []
        for topic in sub_topics:
            ratings.append(topic.studentAverageRating(student))
        return list(zip(sub_topics, ratings))

    def classAverageRating(self, classgroup):
        marks = Mark.objects.filter(question__syllabuspoint__topic=self).filter(sitting__classgroup=classgroup)
        return mark_queryset_to_rating(marks)

    def classAverageCompletion(self, classgroup):
        possible = SyllabusPoint.objects.filter(topic=self).distinct()
        students = classgroup.students()
        with_score = possible.filter(question__mark__student__in=students)
        if possible.count() > 0:
            return round(with_score.count() / possible.count() *100)
        else:
            return 0

    def lessons_taught(self, classgroup):
        """ return all the lessons in which this point has been taught to this classgroup"""

        Lesson = apps.get_model(app_label='timetable', model_name='Lesson')
        lessons = Lesson.objects.filter(syllabus_points_covered__sub_topic__topic=self, classgroup=classgroup)
        return lessons.distinct()


class SyllabusSubTopic(models.Model):
    topic = models.ForeignKey(SyllabusTopic, on_delete=models.CASCADE)
    sub_topic = models.CharField(max_length=100)

    def __str__(self):
        return str(self.topic) + ': ' + str(self.sub_topic)

    def studentAverageRating(self, student):
        points = SyllabusPoint.objects.filter(sub_topic=self)
        marks = Mark.objects.filter(question__syllabuspoint__in=points, student=student)
        return mark_queryset_to_rating(marks)

    def student_sub_topic_data(self, student):

        syllabus_points = SyllabusPoint.objects.filter(sub_topic=self)
        ratings = []
        assessments = []
        lessons = []
        resources = []
        Lesson = apps.get_model(app_label='timetable', model_name='Lesson')
        for point in syllabus_points:
            ratings.append(point.get_student_rating(student))

            assessments.append(Exam.objects.filter(question__mark__student=student, question__syllabuspoint=point).distinct())
            relevant_lessons = Lesson.objects.filter(syllabus_points_covered=point, classgroup__in=student.classgroups.all())
            lessons.append(relevant_lessons)
            for lesson in relevant_lessons:

                resources.append(lesson.student_viewable_resources())
        return list(zip(syllabus_points, ratings, assessments, lessons, resources))

    def lessons_taught(self, classgroup):
        """ return all the lessons in which this point has been taught to this classgroup"""

        Lesson = apps.get_model(app_label='timetable', model_name='Lesson')
        lessons = Lesson.objects.filter(syllabus_points_covered__sub_topic=self, classgroup=classgroup)
        return lessons.distinct()


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

    def student_assesments(self, student):
        assessments = Exam.objects.filter(question__syllabuspoint=self).distinct()

        sittings = Sitting.objects.filter(classgroup__student=student).filter(exam__in=assessments)
        return sittings

    def lessons_taught(self, classgroups):
        """ return all the lessons in which this point has been taught to this classgroup"""

        Lesson = apps.get_model(app_label='timetable', model_name='Lesson')
        lessons = Lesson.objects.filter(syllabus_points_covered=self, classgroup__in=classgroups)
        return lessons.distinct()


class Exam(models.Model):
    name = models.CharField(max_length=100)
    syllabus = models.ManyToManyField(Syllabus)

    def __str__(self):
        return self.name

    def max_score(self):
        return Question.objects.filter(exam=self).aggregate(Sum('maxscore'))

    def topics_tested(self):
        questions = Question.objects.filter(exam=self)
        topics = SyllabusTopic.objects.filter(syllabussubtopic__syllabuspoint__question__in=questions).distinct()

        return topics


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    qnumber = models.CharField(max_length=100)
    qorder = models.DecimalField(decimal_places=2, max_digits=6)
    syllabuspoint = models.ManyToManyField(SyllabusPoint)
    maxscore = models.IntegerField()

    def __str__(self):
        return self.qnumber

    class Meta:
        unique_together = (("exam", "qorder"),)


class Sitting(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    classgroup = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    datesat = models.DateField()
    openForStudentRecording = models.BooleanField()

    def students(self):
        return Student.objects.filter(classgroups=self.classgroup)

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

        if len(scores) > 0:
            score_range = numpy.max(scores) - numpy.min(scores)
            return score_range

        else:
            return 0

    def class_score_std(self):
        students = Student.objects.filter(classgroups=self.classgroup)
        scores = []
        for student in students:
            if self.student_total(student):
                scores.append(self.student_total(student))

        return round(numpy.std(scores),1)

    def class_topic_performance(self):
        topics = self.exam.topics_tested().all()

        topic_ratings = []
        for topic in topics:
            questions = Question.objects.filter(syllabuspoint__topic=topic, exam=self.exam)
            markset = Mark.objects.filter(question__in=questions, student__in=self.students())
            topic_ratings.append(mark_queryset_to_rating(markset))

        topic_data= list(zip(topics,topic_ratings))

        return topic_data

    def toggle_open_for_recording(self):
        # clever trick to switch Bool
        self.openForStudentRecording = not self.openForStudentRecording


class Mark(models.Model):
    # TODO: This should be updated whenever a sitting is modified
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField(blank=True, null=True)
    sitting = models.ForeignKey(Sitting, on_delete=models.CASCADE)
    notes = RichTextField(null=True, blank=True, config_name='small')

    def __str__(self):
        return str(self.question.exam) + ' ' + str(self.student) + ' ' + str(self.question) + '(' + str(
            self.score) + ')'

    def percentage(self):

        if self.score:
            return round(self.score / self.question.maxscore * 100, 2)
        # CSV Uploads
        else:
            return False

    class Meta:
        unique_together = (("student", "question", "sitting"),)


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

    if len(pcs) > 0:
        return round(numpy.mean(pcs) * 5, 1)
    else:
        return 0  # If we have no marks recorded, don't try to round - give zero.
