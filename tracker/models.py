from django.db import models
from school.models import Student, ClassGroup
import numpy
from django.db.models import Sum
from ckeditor.fields import RichTextField
from django.apps import apps
from datetime import datetime


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
            return int(round(completed_points.count() / all_points.count() * 100, 0))
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
        marks = Mark.objects.filter(question__syllabuspoint__topic__syllabus=self).filter(
            sitting__classgroup=classgroup)
        return mark_queryset_to_rating(marks)

    def all_topics(self):
        return SyllabusTopic.objects.filter(syllabus=self)

    def all_sub_topics(self):
        return SyllabusSubTopic.objects.filter(topic__syllabus=self)

    def all_syllabus_points(self):
        return SyllabusPoint.objects.filter(sub_topic__topic__syllabus=self)

    def classgroup_percentage_taught(self, classgroup):
        all_points = SyllabusPoint.objects.filter(sub_topic__topic__syllabus=self).order_by('sub_topic')
        total_points = all_points.count()

        if not total_points:
            return 0

        points_taught = 0

        for point in all_points:
            if point.lessons_taught(classgroup):
                points_taught = points_taught +1

        percentage_taught = points_taught / total_points * 100
        return round(percentage_taught)

    def classgroup_percentage_assessed(self, classgroup):
        all_points = SyllabusPoint.objects.filter(sub_topic__topic__syllabus=self).order_by('sub_topic')
        total_points = all_points.count()
        if not total_points:
            return 0
        points_assessed = 0
        for point in all_points:
            if point.has_been_assessed(classgroup):
                points_assessed = points_assessed + 1

        percentage_assessed = points_assessed / total_points * 100
        return round(percentage_assessed)

class SyllabusTopic(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(str(self.syllabus) + " " + self.topic)

    def studentAverageRating(self, student):
        # check if we have already calculated this:
        ratings = StudentTopicRating.objects.filter(student=student, syllabus_topic=self).order_by('date')
        if ratings.count() > 0:
            return ratings.reverse()[0].rating

        else:

            recorded_rating = self.calculate_student_rating(student)

            return recorded_rating.rating

    def calculate_student_rating(self, student):
        points = SyllabusPoint.objects.filter(topic=self)
        marks = Mark.objects.filter(question__syllabuspoint__in=points).filter(student=student)
        rating = mark_queryset_to_rating(marks)
        rating, created = StudentTopicRating.objects.get_or_create(student=student,
                                                                   syllabus_topic=self,
                                                                   rating=rating,
                                                                   date=datetime.today())
        return rating

    def studentCompletion(self, student):
        possible = SyllabusPoint.objects.filter(topic=self).distinct()
        with_score = possible.filter(question__mark__student=student)

        if possible.count() > 0:
            return round(with_score.count() / possible.count() * 100)
        else:
            return 0

    def studentSubTopicData(self, student):
        sub_topics = SyllabusSubTopic.objects.filter(topic=self)
        ratings = []
        for topic in sub_topics:
            ratings.append(topic.studentAverageRating(student))
        return list(zip(sub_topics, ratings))

    def groupAverageRating(self, students):
        marks = Mark.objects.filter(question__syllabuspoint__topic=self).filter(student__in=students)
        return mark_queryset_to_rating(marks)

    def groupPercentRatingsWithinBounds(self, students, upper, lower, max=5):

        ''' Calculate number of scores that are within a boundary. The max is what the rating is out of (default 5)'''
        all_marks = Mark.objects.filter(student__in=students, question__syllabuspoint__topic=self)
        upper_percentage = upper/max
        lower_percentage = lower / max

        elibible = 0
        for mark in all_marks:
            mark_percentage = mark.score / mark.question.maxscore
            if mark_percentage >= lower_percentage:
                if mark.score <= upper_percentage:
                    elibible = elibible + 1

        return elibible / all_marks.count()

    def classAverageRating(self, classgroup):
        students = classgroup.students()
        return self.groupAverageRating(students)

    def GoupAverageCompletion(self, students):
        possible = SyllabusPoint.objects.filter(topic=self).distinct()
        with_score = possible.filter(question__mark__student__in=students)
        if possible.count() > 0:
            return round(with_score.count() / possible.count() * 100)
        else:
            return 0

    def classAverageCompletion(self, classgroup):

        students = classgroup.students()
        score = self.GroupAverageCompletion(self, students)
        return score

    def lessons_taught(self, classgroup):
        """ return all the lessons in which this point has been taught to this classgroup"""

        Lesson = apps.get_model(app_label='timetable', model_name='Lesson')
        lessons = Lesson.objects.filter(syllabus_points_covered__sub_topic__topic=self, classgroup=classgroup)
        return lessons.distinct()

    def sub_topics(self):
        return SyllabusSubTopic.objects.filter(topic=self)

    def classgroup_percentage_taught(self, classgroup):
        all_points = SyllabusPoint.objects.filter(sub_topic__topic=self).order_by('sub_topic')
        total_points = all_points.count()
        if not total_points:
            return 0

        points_taught = 0
        for point in all_points:
            if point.lessons_taught(classgroup):
                points_taught = points_taught +1

        percentage_taught = points_taught / total_points * 100
        return round(percentage_taught)

    def classgroup_percentage_assessed(self, classgroup):
        all_points = SyllabusPoint.objects.filter(sub_topic__topic=self).order_by('sub_topic')
        total_points = all_points.count()
        if not total_points:
            return 0

        points_assessed = 0
        for point in all_points:
            if point.has_been_assessed(classgroup):
                points_assessed = points_assessed + 1

        percentage_assessed = points_assessed / total_points * 100
        return round(percentage_assessed)


class SyllabusSubTopic(models.Model):
    topic = models.ForeignKey(SyllabusTopic, on_delete=models.CASCADE)
    sub_topic = models.CharField(max_length=100)

    def __str__(self):
        return str(self.topic) + ': ' + str(self.sub_topic)

    def syllabus_points(self):
        return SyllabusPoint.objects.filter(sub_topic=self)

    def studentAverageRating(self, student):
        # check if we have already calculated this:
        ratings = StudentSubTopicRating.objects.filter(student=student, syllabus_sub_topic=self).order_by('date')
        if ratings.count() > 0:
            return ratings.reverse()[0].rating

        else:

            recorded_rating = self.calculate_student_rating(student)

            return recorded_rating.rating

    def calculate_student_rating(self, student):
        points = SyllabusPoint.objects.filter(sub_topic=self)
        marks = Mark.objects.filter(question__syllabuspoint__in=points).filter(student=student)
        rating = mark_queryset_to_rating(marks)
        rating, created = StudentSubTopicRating.objects.get_or_create(student=student,
                                                                      syllabus_sub_topic=self,
                                                                      rating=rating,
                                                                      date=datetime.today())
        return rating

    def student_sub_topic_data(self, student):

        syllabus_points = SyllabusPoint.objects.filter(sub_topic=self)
        ratings = []
        assessments = []
        lessons = []
        resources = []
        Lesson = apps.get_model(app_label='timetable', model_name='Lesson')
        for point in syllabus_points:
            # None of these can be blank, or zip() will fail

            ratings.append(point.get_student_rating(student))  # already gives 0 if no data

            assessment_queryset = Exam.objects.filter(question__mark__student=student,
                                                      question__syllabuspoint=point).distinct()

            if assessment_queryset.count() > 0:
                assessments.append(assessment_queryset)
            else:
                assessments.append('None')

            relevant_lessons = Lesson.objects.filter(syllabus_points_covered=point,
                                                     classgroup__in=student.classgroups.all())

            if relevant_lessons.count() > 0:
                lessons.append(relevant_lessons)
                for lesson in relevant_lessons:
                    resources.append(lesson.student_viewable_resources())
            else:
                lessons.append('None')
                resources.append('None')

        return list(zip(syllabus_points, ratings, assessments, lessons, resources))

    def lessons_taught(self, classgroup):
        """ return all the lessons in which this point has been taught to this classgroup"""

        Lesson = apps.get_model(app_label='timetable', model_name='Lesson')
        lessons = Lesson.objects.filter(syllabus_points_covered__sub_topic=self, classgroup=classgroup)
        return lessons.distinct()

    def classgroup_percent_taught(self, classgroup):
        points = self.syllabus_points()
        total = points.count()

        if not total:
            return 0
        taught = 0
        for point in points:
            if point.lessons_taught(classgroup):
                taught = taught + 1

        return round(taught/total*100)

    def classgroup_percent_assessed(self, classgroup):
        points = self.syllabus_points()
        total = points.count()

        if not total:
            return 0

        assessed = 0
        for point in points:
            if point.has_been_assessed(classgroup):
                assessed = assessed + 1

        return round(assessed / total * 100)

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

    def calculate_student_rating(self, student):
        marks = Mark.objects.filter(question__syllabuspoint=self).filter(student=student)
        rating = mark_queryset_to_rating(marks)
        rating, created = StudentPointRating.objects.get_or_create(student=student,
                                                          syllabus_point=self,
                                                          rating=rating,
                                                          date=datetime.today())

        return rating

    def get_student_rating(self, student):
        # check if we have already calculated this:
        ratings = StudentPointRating.objects.filter(student=student, syllabus_point=self).order_by('date')
        if ratings.count() > 0:
            return ratings.reverse()[0].rating

        else:

            recorded_rating = self.calculate_student_rating(student)

            return recorded_rating.rating

    def student_assesments(self, student):
        assessments = Exam.objects.filter(question__syllabuspoint=self).distinct()

        sittings = Sitting.objects.filter(classgroup__student=student).filter(exam__in=assessments)
        return sittings

    def lessons_taught(self, classgroup):
        """ return all the lessons in which this point has been taught to this classgroup"""

        Lesson = apps.get_model(app_label='timetable', model_name='Lesson')
        lessons = Lesson.objects.filter(syllabus_points_covered=self, classgroup=classgroup)
        return lessons.distinct()

    def has_been_taught(self, classgroup):
        if self.lessons_taught(classgroup):
            return True
        else:
            return False

    def classgroup_assessments(self, classgroup):
        assessments = Sitting.objects.filter(exam__question__syllabuspoint=self, classgroup=classgroup).distinct()
        return assessments

    def has_been_assessed(self, classgroup):
        assessments = Sitting.objects.filter(exam__question__syllabuspoint=self, classgroup=classgroup).distinct()
        if assessments.count():
            return True
        else:
            return False

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

        return round(numpy.std(scores), 1)

    def class_topic_performance(self):
        topics = self.exam.topics_tested().all()

        topic_ratings = []
        for topic in topics:
            questions = Question.objects.filter(syllabuspoint__topic=topic, exam=self.exam)
            markset = Mark.objects.filter(question__in=questions, student__in=self.students())
            topic_ratings.append(mark_queryset_to_rating(markset))

        topic_data = list(zip(topics, topic_ratings))

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


class StudentRating(models.Model):
    """ A model that stores computed point ratings to speed up render time, and allow for tracking over time."""

    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False, null=False)

    date = models.DateTimeField(null=False, blank=False, default=datetime.now)
    type = models.CharField(max_length=100, blank=False, null=False, default='Calculated')
    rating = models.DecimalField(blank=False, null=False, max_digits=5, decimal_places=2)

    class Meta:
        abstract = True


class StudentPointRating(StudentRating):
    syllabus_point = models.ForeignKey(SyllabusPoint, on_delete=models.CASCADE, blank=False, null=False)


class StudentSubTopicRating(StudentRating):
    """ A model that stores computed sub-topic ratings to speed up render time, and allow for tracking over time."""

    syllabus_sub_topic = models.ForeignKey(SyllabusSubTopic,
                                           on_delete=models.CASCADE,
                                           blank=False,
                                           null=False)


class StudentTopicRating(StudentRating):
    syllabus_topic = models.ForeignKey(SyllabusTopic,
                                       on_delete=models.CASCADE,
                                       blank=False,
                                       null=False)


class StudentSyllabusRating(StudentRating):
    syllabus = models.ForeignKey(Syllabus,
                                 on_delete=models.CASCADE,
                                 null=False)


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
