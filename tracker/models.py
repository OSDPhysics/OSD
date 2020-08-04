from django.db import models
from django.utils import timezone
import pytz
from school.models import Student, ClassGroup, PastoralStructure, AcademicStructure
import numpy
from django.db.models import Sum, Avg, F
from ckeditor.fields import RichTextField
from django.apps import apps
from datetime import datetime
from django.utils import timezone
from .charts import StudentSubTopicGraph
import pytz
from django.utils import timezone
from django.contrib.auth.models import User

from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField, TreeManager


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
                points_taught = points_taught + 1

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

    def mptt_equivalent(self):
        if MPTTSyllabus.objects.get(related_syllabus=self).exists():
            return MPTTSyllabus.objects.get(related_syllabus=self)
        else:
            return False


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

    def cohort_rating_number(self, cohort, min_rating, max_rating):
        """ Takes a queryset of students (cohort) and returns the number of
        ratings that are between min_rating and max_rating """

        points = self.syllabus_points()

        total = StudentPointRating.objects.filter(student__in=cohort,
                                                  syllabus_point__in=points,
                                                  rating__gt=min_rating,
                                                  rating__lte=max_rating,
                                                  current=True).count()

        return total

    def calculate_student_rating(self, student):
        points = SyllabusPoint.objects.filter(topic=self)
        marks = Mark.objects.filter(question__syllabuspoint__in=points).filter(student=student)
        rating = mark_queryset_to_rating(marks)
        rating, created = StudentTopicRating.objects.get_or_create(student=student,
                                                                   syllabus_topic=self,
                                                                   rating=rating,
                                                                   date=timezone.now())

        if created:
            # Check no others are set to 'current':
            others = StudentTopicRating.objects.filter(student=student,
                                                       syllabus_topic=self,
                                                       current=True)
            for other in others:
                other.current = False
                other.save()

            rating.current = True
            rating.save()

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
        classgroup = ClassGroup.objects.filter(student=student,
                                               syllabustaught__syllabustopic=self,
                                               archived=False)
        ratings = []
        assessments = []
        lessons = []
        resources = []
        charts = []
        for topic in sub_topics:
            ratings.append(topic.studentAverageRating(student))
            assessments.append("")
            lessons.append("")
            resources.append("")
            chart = StudentSubTopicGraph()
            chart.students = Student.objects.filter(pk=student.pk)
            chart.syllabus_areas = SyllabusSubTopic.objects.filter(pk=topic.pk)
            charts.append(chart)
        return list(zip(sub_topics, ratings, assessments, lessons, resources, charts))

    def groupAverageRating(self, students):
        marks = Mark.objects.filter(question__syllabuspoint__topic=self).filter(student__in=students)
        return mark_queryset_to_rating(marks)

    def groupPercentRatingsWithinBounds(self, students, upper, lower, max=5):

        ''' Calculate number of scores that are within a boundary. The max is what the rating is out of (default 5)'''
        all_marks = Mark.objects.filter(student__in=students, question__syllabuspoint__topic=self)
        upper_percentage = upper / max
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

    def GroupAverageCompletion(self, students):
        possible = SyllabusPoint.objects.filter(topic=self).distinct()
        with_score = possible.filter(question__mark__student__in=students)
        if possible.count() > 0:
            return round(with_score.count() / possible.count() * 100)
        else:
            return 0

    def classAverageCompletion(self, classgroup):

        students = classgroup.students()
        score = self.GroupAverageCompletion(students)
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
                points_taught = points_taught + 1

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

    def syllabus_points(self):
        return SyllabusPoint.objects.filter(topic=self)

    def mptt_equivalent(self):
        return MPTTSyllabus.objects.get(related_topic=self)


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
                                                                      date=timezone.now())
        if created:
            # Check no others are set to 'current':
            others = StudentSubTopicRating.objects.filter(student=student,
                                                          syllabus_sub_topic=self,
                                                          current=True)
            for other in others:
                other.current = False
                other.save()

            rating.current = True
            rating.save()

        return rating

    def get_student_rating(self, student):
        # check if we have already calculated this:
        try:
            rating = StudentSubTopicRating.objects.get(student=student,
                                                       syllabus_sub_topic=self,
                                                       current=True)
        except StudentPointRating.DoesNotExist:
            rating = self.calculate_student_rating(student)

        return rating

    def cohort_rating_number(self, cohort, min_rating, max_rating):
        """ Takes a queryset of students (cohort) and returns the number of
        ratings that are between min_rating and max_rating """

        points = self.syllabus_points()

        total = StudentPointRating.objects.filter(student__in=cohort,
                                                  syllabus_point__in=points,
                                                  rating__gt=min_rating,
                                                  rating__lte=max_rating,
                                                  current=True).count()

        return total

    def student_sub_topic_data(self, student):

        syllabus_points = SyllabusPoint.objects.filter(sub_topic=self)
        ratings = []
        assessments = []
        lessons = []
        resources = []
        charts = []
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

            chart = StudentSubTopicGraph()
            chart.students = Student.objects.filter(pk=student.pk)
            chart.syllabus_areas = point
            charts.append(chart)

        return list(zip(syllabus_points, ratings, assessments, lessons, resources, charts))

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

        return round(taught / total * 100)

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

    def mptt_equivalent(self):
        return MPTTSyllabus.objects.get(related_sub_topic=self)


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
                                                                   date=timezone.now())

        if created:
            # Check no others are set to 'current':
            others = StudentPointRating.objects.filter(student=student,
                                                       syllabus_point=self,
                                                       current=True)
            for other in others:
                other.current = False
                other.save()

            rating.current = True
            rating.save()

        return rating

    def get_student_rating(self, student):
        # check if we have already calculated this:
        try:
            rating = StudentPointRating.objects.get(student=student,
                                                    syllabus_point=self,
                                                    current=True)
        except StudentPointRating.DoesNotExist:
            rating = self.calculate_student_rating(student)

        return rating

    def cohort_rating_number(self, cohort, min_rating, max_rating):
        """ Takes a queryset of students (cohort) and returns the number of
        ratings that are between min_rating and max_rating """

        total = 0

        total = StudentPointRating.objects.filter(student__in=cohort,
                                                  syllabus_point=self,
                                                  rating__gt=min_rating,
                                                  rating__lte=max_rating,
                                                  current=True).count()

        return total

    def generate_cohort_ratings_dictionary(self, cohort):
        """ For a queryset of students, return a dictionary of the number of ratings for each score level. """

        points = {'point': self,
                  'number_zero_to_one': self.cohort_rating_number(cohort, 0, 1),
                  'number_one_to_two': self.cohort_rating_number(cohort, 1, 2),
                  'number_two_to_three': self.cohort_rating_number(cohort, 2, 3),
                  'number_three_to_four': self.cohort_rating_number(cohort, 3, 4),
                  'number_four_to_five': self.cohort_rating_number(cohort, 4, 5)}

        return points

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

    def mptt_equivalent(self):
        try:
            equivalent = MPTTSyllabus.objects.get(related_point=self)
        except(models.ObjectDoesNotExist):
            print("No equivalent found for point id", self.pk)
            equivalent = False
        if equivalent:
            return equivalent
        else:
            return False

    def mptt_rating(self, students):
        ''' Find the rating for a group of students '''
        marks = Mark.objects.filter(student__in=students, question__syllabuspoint=self)
        average = marks.aggregate(Avg('percent'))
        return round(average * 5, 1)

    def mptt_weighted_rating(self, students):
        marks = Mark.objects.filter(student__in=students, question__syllabuspoint=self)


class Exam(models.Model):
    name = models.CharField(max_length=100)
    syllabus = models.ManyToManyField(Syllabus)
    root_syllabus = models.ForeignKey('MPTTSyllabus', blank=False, null=True, on_delete=models.SET_NULL)
    weighting = models.FloatField(default=1, blank=False, null=False)

    def __str__(self):
        return self.name

    def max_score(self):
        return Question.objects.filter(exam=self).aggregate(Sum('maxscore'))['maxscore__sum']

    def topics_tested(self):
        questions = Question.objects.filter(exam=self)
        topics = SyllabusTopic.objects.filter(syllabussubtopic__syllabuspoint__question__in=questions).distinct()
        topics = MPTTSyllabus.objects.filter(question__in=questions)
        return topics

    def coverage_check(self, points_to_check):
        """ Takes a queryset of syllabus points and checks each one to see if it appears in this test"""
        points = []
        # load once to save memory
        self_points = self.topics_tested()
        for point in points_to_check:
            row = {'point': point,
                   'tested': False}
            if point in self_points:
                row['tested'] = True
            points.append(row)

        return points


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    qnumber = models.CharField(max_length=100)
    qorder = models.DecimalField(decimal_places=2, max_digits=6)
    syllabuspoint = models.ManyToManyField(SyllabusPoint, blank=True)
    maxscore = models.IntegerField()
    weighting = models.FloatField(default=1.0, blank=False, null=False)
    MPTTsyllabuspoint = TreeManyToManyField('MPTTSyllabus')

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
        return str(self.class_average_score_int()) + '/' + str(self.exam.max_score())

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
            questions = Question.objects.filter(MPTTsyllabuspoint__in=topic.get_descendants(include_self=True),
                                                exam=self.exam)
            markset = Mark.objects.filter(question__in=questions, student__in=self.students())
            topic_ratings.append(mark_queryset_to_rating(markset))

        topic_data = list(zip(topics, topic_ratings))

        return topic_data

    def toggle_open_for_recording(self):
        # clever trick to switch Bool
        self.openForStudentRecording = not self.openForStudentRecording

    def create_ratings(self):
        single_points = MPTTSyllabus.objects.filter(question__exam__sitting=self)

        points = MPTTSyllabus.objects.get_queryset_ancestors(queryset=single_points, include_self=True)
        for student in self.students():
            for point in points:
                rating, zero_to_one, one_to_two, two_to_three, three_to_four, \
                four_to_five, total_contributions = point.calculate_student_rating(student, eff_date=self.datesat)
                if not rating:
                    # Rating will be Null if no points exist yet.
                    continue
                # Check if we've done a rating including this sitting before
                # (This would occur if we've updated a mark)
                ratings = MPTTRating.objects.filter(student=student,
                                                    syllabus=point,
                                                    created=self.datesat)
                if ratings.count() > 0:
                    # The rating has already been done; so we're just updating it.
                    rating_instance = ratings[0]
                else:
                    rating_instance = MPTTRating.objects.create(student=student,
                                                                created=self.datesat,
                                                                syllabus=point)

                rating_instance.assessment.add(self)

                rating_instance.rating = rating
                rating_instance.zero_to_one = zero_to_one
                rating_instance.one_to_two = one_to_two
                rating_instance.two_to_three = two_to_three
                rating_instance.three_to_four = three_to_four
                rating_instance.four_to_five = four_to_five
                rating_instance.total_contributions = total_contributions

                rating_instance.save()


class Mark(models.Model):
    # TODO: This should be updated whenever a sitting is modified
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField(blank=True, null=True)
    sitting = models.ForeignKey(Sitting, on_delete=models.CASCADE)
    notes = RichTextField(null=True, blank=True, config_name='small')

    # Calculated fields

    percent = models.IntegerField(blank=True, null=True)
    maximum = models.IntegerField(blank=True, null=True)
    weighted_maximum = models.IntegerField(blank=True, null=True)
    weighted_percent = models.FloatField(blank=True, null=True)

    # Used so we can force an update, triggering all the signals when changing an exam or question.
    updates = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return str(self.question.exam) + ' ' + str(self.student) + ' ' + str(self.question) + '(' + str(
            self.score) + ')'

    def calculate_percentage(self):

        if self.score:
            percent = round(self.score / self.question.maxscore * 100, 2)
        elif self.score == 0:
            percent = 0
        else:
            percent = None
        return percent

    def calculate_weighted_percent(self):
        if self.score:
            weighting = self.question.weighting * self.question.exam.weighting
            weighted_score = weighting * self.score
            weighted_percent = round(weighted_score / self.calculate_weighted_max() * 100, 0)
        else:
            weighted_percent = None
        return weighted_percent

    def calculate_weighted_max(self):
        weighting = self.question.weighting * self.question.exam.weighting
        return self.question.maxscore * weighting

    def get_maxscore(self):
        return self.question.maxscore

    def set_calculated_values(self):
        self.maximum = self.get_maxscore()
        self.percent = self.calculate_percentage()
        self.weighted_maximum = self.calculate_weighted_max()
        self.weighted_percent = self.calculate_weighted_percent()
        self.save()

    class Meta:
        unique_together = (("student", "question", "sitting"),)


class StudentRating(models.Model):
    """ A model that stores computed point ratings to speed up render time, and allow for tracking over time."""

    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False, null=False)

    date = models.DateTimeField(null=False, blank=False, default=datetime.now)
    type = models.CharField(max_length=100, blank=False, null=False, default='Calculated')
    rating = models.DecimalField(blank=False, null=False, max_digits=5, decimal_places=2)

    current = models.BooleanField(blank=True, default=False)

    class Meta:
        abstract = True


class StudentPointRating(StudentRating):
    syllabus_point = models.ForeignKey(SyllabusPoint, on_delete=models.CASCADE, blank=False, null=False)


def set_current_student_point_ratings():
    all_ratings = StudentPointRating.objects.filter(date__lte=datetime.today())
    points = SyllabusPoint.objects.all()
    students = Student.objects.all()
    for point in points:
        for student in students:
            point.get_student_rating(student)
            rating = all_ratings.filter(syllabus_point=point,
                                        student=student).order_by('date').reverse()
        rating[0].current = True
        rating[0].update()


def set_current_student_stopic_ratings():
    all_ratings = StudentSubTopicRating.objects.filter(date__lte=timezone.now())
    points = SyllabusSubTopic.objects.all()
    students = Student.objects.all()
    for point in points:
        for student in students:
            point.calculate_student_rating(student)


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


def set_current_student_stopic_ratings():
    all_ratings = StudentSubTopicRating.objects.filter(date__lte=timezone.now())
    points = SyllabusSubTopic.objects.all()
    students = Student.objects.all()
    for point in points:
        print("Now on points: ", point)

        for student in students:
            point.calculate_student_rating(student)
        print("Last point for student:", student)


# There are the models required for django MPTT:


class MPTTSyllabus(MPTTModel):
    text = models.CharField(max_length=500, unique=False)
    tier = models.CharField(max_length=50, unique=False, blank=True, null=True)
    number = models.CharField(max_length=20, unique=False, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    related_syllabus = models.ForeignKey(Syllabus, on_delete=models.SET_NULL, blank=True, null=True)
    related_topic = models.ForeignKey(SyllabusTopic, on_delete=models.SET_NULL, blank=True, null=True)
    related_sub_topic = models.ForeignKey(SyllabusSubTopic, on_delete=models.SET_NULL, blank=True, null=True)
    related_point = models.ForeignKey(SyllabusPoint, on_delete=models.SET_NULL, blank=True, null=True)


    class MPTTMeta:
        order_insertion_by = ['number', 'text']

    def __str__(self):
        return self.text

    def get_group_ratings(self, students):

        '''Return a rating / 5 for a cohort, not weighted '''
        # We need to search not just this instance, but all children too (so we get a complete view of it.
        points = self.get_descendants(include_self=True)
        marks = Mark.objects.filter(question__MPTTsyllabuspoint__in=points, student__in=students)
        marks.aggregate(average=Avg('percent'))

    def calculate_student_rating(self, student, eff_date=datetime.today()):
        points = self.get_descendants(include_self=True)
        marks = Mark.objects.filter(question__MPTTsyllabuspoint__in=points, student=student,
                                    sitting__datesat__lte=eff_date, score__isnull=False)

        if marks.count() == 0:
            return None, None, None, None, None, None, None
        percent = marks.aggregate(average=Avg('percent'))['average']
        if percent:
            rating = round(percent / 20, 1)

            zero_to_one = marks.filter(percent__gte=0, percent__lt=20).count()
            one_to_two = marks.filter(percent__gte=20, percent__lt=40).count()
            two_to_three = marks.filter(percent__gte=40, percent__lt=60).count()
            three_to_four = marks.filter(percent__gte=60, percent__lt=80).count()
            four_to_five = marks.filter(percent__gte=80, percent__lte=100).count()
            total_contributions = marks.count()

        else:
            return None, None, None, None, None, None, None

        return rating, zero_to_one, one_to_two, two_to_three, three_to_four, four_to_five, total_contributions

    def calculate_group_rating(self, students, eff_date=datetime.today()):
        points = self.get_descendants(include_self=True)
        marks = Mark.objects.filter(question__MPTTsyllabuspoint__in=points, student__in=students,
                                    sitting__datesat__lte=eff_date, score__isnull=False)

        if marks.count() == 0:
            return None, None, None, None, None, None, None
        percent = marks.aggregate(average=Avg('percent'))['average']
        if percent:
            rating = round(percent / 20, 1)

            zero_to_one = marks.filter(percent__gte=0, percent__lt=20).count()
            one_to_two = marks.filter(percent__gte=20, percent__lt=40).count()
            two_to_three = marks.filter(percent__gte=40, percent__lt=60).count()
            three_to_four = marks.filter(percent__gte=60, percent__lt=80).count()
            four_to_five = marks.filter(percent__gte=80, percent__lte=100).count()
            total_contributions = marks.count()



        else:
            return None, None, None, None, None, None, None

        return rating, zero_to_one, one_to_two, two_to_three, three_to_four, four_to_five, total_contributions

    def group_ratings_data(self, students):
        rating, zero_to_one, one_to_two, two_to_three, three_to_four, four_to_five, total = self.calculate_group_rating(
            students=students)
        self_assessment = self.group_most_recent_self_rating(students)
        data = {'rating': rating,
                'zero_to_one': zero_to_one,
                'one_to_two': one_to_two,
                'two_to_three': two_to_three,
                'three_to_four': three_to_four,
                'four_to_five': four_to_five,
                'total': total,
                'self_assessment': self_assessment}
        return data

    def group_most_recent_self_rating(self, students):
        ratings = MPTTManualRating.objects.filter(student__in=students,
                                                  syllabus=self)
        if ratings:
            return ratings.order_by('-created')[0]
        else:
            children = self.get_descendants()
            ratings = MPTTManualRating.objects.filter(student__in=students,
                                                      syllabus__in=children)
            if ratings:
                return ratings.aggregate(average=Avg('rating'))['average']
            else:
                return 0

    def knowledge_organiser(self):
        return KnowledgeOrganiser.objects.filter(syllabus_point=self)


class MPTTRating(models.Model):
    syllabus = TreeForeignKey(MPTTSyllabus, null=False, blank=False, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    rating = models.FloatField(null=True, blank=True)

    # these store the total instance of a score in each range
    # These should store the count of each in this range
    zero_to_one = models.IntegerField(null=True, blank=True)
    one_to_two = models.IntegerField(null=True, blank=True)
    two_to_three = models.IntegerField(null=True, blank=True)
    three_to_four = models.IntegerField(null=True, blank=True)
    four_to_five = models.IntegerField(null=True, blank=True)
    total_contributions = models.IntegerField(null=False, default=0)

    created = models.DateTimeField(blank=False, null=False, default=datetime.now)
    reason = models.CharField(blank=False, null=False, default="Assessment", max_length=100)
    assessment = models.ManyToManyField(Sitting)

    def __str__(self):
        return str(self.syllabus) + ": " + str(self.student) + str(self.created) + "(" + str(self.rating) + ")"


class MPTTManualRating(models.Model):
    syllabus = TreeForeignKey(MPTTSyllabus, null=False, blank=False, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    rating = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(blank=False, null=False, default=datetime.now)
    reason = models.CharField(blank=False, null=False, default="Student Assessment", max_length=100)

    def __str__(self):
        return str(self.syllabus) + ": " + str(self.student) + str(self.created) + "(" + str(self.rating) + ")"


class StandardisedData(MPTTModel):
    name = models.CharField(max_length=50)
    max_value = models.DecimalField(max_digits=5, decimal_places=1)
    min_value = models.DecimalField(max_digits=5, decimal_places=1)
    step = models.DecimalField(max_digits=5, decimal_places=1)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    quickname = models.CharField(blank=True, null=True, max_length=20)

    def __str__(self):
        return self.name

    def cohort_average_residual(self, cohort):
        residuals = StandardisedResult.objects.filter(student__in=cohort,
                                                      standardised_data=self)
        average = residuals.aggregate(average=Avg('residual'))
        return average['average']

    def cohort_average_result(self, cohort):
        results = StandardisedResult.objects.filter(student__in=cohort,
                                                    standardised_data=self)
        average = results.aggregate(average=Avg('result'))
        return average['average']

    def cohort_average_target(self, cohort):
        results = StandardisedResult.objects.filter(student__in=cohort,
                                                    standardised_data=self)
        average = results.aggregate(average=Avg('target'))
        return average['average']

    def cohort_target_vs_current_data(self, cohort):
        data = [self,
                self.cohort_average_target(cohort),
                self.cohort_average_result(cohort)]
        return data


class StandardisedResultQueryset(models.QuerySet):
    def add_residuals(self, target=StandardisedData.objects.none()):
        return self.annotate(calc_residual=F('result') - F('target'))


class StandardisedResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False, null=False)
    standardised_data = TreeForeignKey(StandardisedData, on_delete=models.CASCADE)
    result = models.DecimalField(max_digits=5, decimal_places=1)
    target = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    date_created = models.DateField(blank=True, null=True, default=timezone.now)
    reason_created = models.TextField(blank=True, null=True)
    residual = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    normalised_residual = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    objects = StandardisedResultQueryset.as_manager()

    def __str__(self):
        return self.standardised_data.name + str(self.student) + str(self.result)

    def replace(self,
                new_result=False,
                new_target=False,
                new_date=datetime.today(),
                new_reason=False):

        PastStandardisedResult.objects.create(
            student=self.student,
            standardised_data=self.standardised_data,
            result=self.result,
            target=self.target,
            date_created=self.date_created,
            reason_created=self.reason_created,
            residual=self.residual
        )

        if new_result:
            self.result = new_result

        if new_date:
            self.date_created = new_date

        if new_target:
            self.target = new_target

        if new_reason:
            self.reason_created = new_reason
        self.save()

        return self

    def save(self, *args, **kwargs):
        self.target = self.find_missing_result_or_target()
        self.residual = self.calculate_residual()
        self.normalised_residual = self.calculate_normalised_residual()

        super(StandardisedResult, self).save(*args, **kwargs)

    def calculate_residual(self):
        if self.result:
            if self.target:
                return float(self.result) - float(self.target)

    def calculate_normalised_residual(self):
        if self.residual:
            return self.residual / float(self.standardised_data.max_value)

    def find_missing_result_or_target(self):
        # Check if this is a result in the kpi_pairs:
        pairs = KPIPair.objects.filter(student_result=self.standardised_data)
        for pair in pairs:
            # Now get the target
            result_target = pair.sudent_target
            if StandardisedResult.objects.filter(student=self.student,
                                                 standardised_data=result_target).exists():
                target_data = StandardisedResult.objects.get(student=self.student,
                                                             standardised_data=result_target)

                return target_data.result


class PastStandardisedResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False, null=False)
    standardised_data = TreeForeignKey(StandardisedData, on_delete=models.CASCADE)
    result = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    target = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True, default=timezone.now)
    reason_created = models.TextField(blank=True, null=True)
    residual = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.standardised_data.name + str(self.student) + str(self.result)


class KPIPair(models.Model):
    sudent_target = TreeForeignKey(StandardisedData, on_delete=models.CASCADE, related_name='student_target')
    student_result = TreeForeignKey(StandardisedData, on_delete=models.CASCADE, related_name='student_result')
    name = models.CharField(max_length=100, blank=False, null=False)

    def calculate_residual(self, student):
        difference = self.student_taget - self.student_result
        normalised_difference = difference / self.student_result.standar

    def __str__(self):
        return self.name


class KnowledgeOrganiser(models.Model):
    syllabus_point = models.ForeignKey(MPTTSyllabus, blank=False, null=False, on_delete=models.CASCADE)
    question = models.TextField(blank=False, null=False)
    teacher_answer = models.TextField(blank=False, null=False)
    created_by = models.ForeignKey(User, blank=False, null=True, on_delete=models.SET_NULL)



class StudentKnowledgeNotes(models.Model):
    knowledge_organiser = models.ForeignKey(KnowledgeOrganiser, blank=False, null=False, on_delete=models.CASCADE)

