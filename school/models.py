from django.db import models
from django.contrib.auth.models import User
from teachnet.models import Skill
from django.apps import apps
from numpy import average
from itertools import chain
from mptt.models import TreeManyToManyField, MPTTModel, TreeForeignKey, TreeOneToOneField
from osd.settings.base import ACADEMIC_YEARS


# Remove before starting server - this is to help PyCharm auto syntax completion!
# from tracker.models import *
# from timetable.models import Lesson

# Create your models here.
class Teacher(models.Model):
    TITLES = (
        ('Miss', 'Miss'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Mr', 'Mr'),
        ('Dr', 'Dr'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    title = models.CharField(max_length=20, choices=TITLES, blank=True)
    staffcode = models.CharField(max_length=10, blank=True)
    skills = models.ManyToManyField(Skill)
    line_manager = models.ForeignKey(User, related_name='line_manager', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        space = ' '
        fullname = self.title + space + self.user.first_name + space + self.user.last_name + space + '(' + self.staffcode + ')'
        # fullname = 'temporary'
        return fullname

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Teacher.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.teacher.save()


class ClassGroup(models.Model):
    groupname = models.CharField(max_length=50)
    groupteacher = models.ForeignKey('school.Teacher', on_delete=models.CASCADE, null=True, blank=True)
    syllabustaught = models.ManyToManyField('tracker.Syllabus')
    mptt_syllabustaught = TreeManyToManyField('tracker.MPTTSyllabus')
    archived = models.BooleanField(blank=True, default=False)
    academic_position = TreeForeignKey('school.AcademicStructure', null=True, on_delete=models.SET_NULL)
    year_taught = models.IntegerField(null=False, blank=False)
    rollover_classgroup = models.ForeignKey('school.ClassGroup', blank=True, null=True, on_delete=models.SET_NULL)


    def __str__(self):

        return self.groupname + " " +\
               ACADEMIC_YEARS[self.year_taught]

    def assessments(self):

        # Avoid a circular import
        sitting_model = apps.get_model(app_label='tracker', model_name='Sitting')

        return sitting_model.objects.filter(classgroup=self).order_by('-datesat')

    def topics(self):
        # Avoid a circular import
        SyllabusTopic = apps.get_model(app_label='tracker', model_name='SyllabusTopic')

        return SyllabusTopic.objects.filter(syllabus__in=self.syllabustaught.all())

    def class_topics_w_ratings(self):

        SyllabusTopic = apps.get_model(app_label='tracker', model_name='SyllabusTopic')
        topics_taught = SyllabusTopic.objects.filter(syllabus__in=self.syllabustaught.all())

        ratings = []
        for topic in topics_taught:
            ratings.append(topic.classAverageRating(self))

        data = list(zip(topics_taught, ratings))

        return data

    def class_topics_completion(self):

        SyllabusTopic = apps.get_model(app_label='tracker', model_name='SyllabusTopic')
        topics_taught = SyllabusTopic.objects.filter(syllabus__in=self.syllabustaught.all())

        completion = []
        for topic in topics_taught:
            completion.append(topic.classAverageCompletion(self))

        data = list(zip(topics_taught, completion))

        return data

    def classgroup_average_rating(self):
        ratings = []
        for syllabus in self.syllabustaught.all():
            ratings.append(syllabus.classgroup_average_rating(self))
        return round(average(ratings),1)

    def classgroup_average_completion(self):
        pcs = []
        for syllabus in self.syllabustaught.all():
            pcs.append(syllabus.classgroup_completion(self))
        return round(average(pcs), 1)

    def class_topic_all_data(self):

        SyllabusTopic = apps.get_model(app_label='tracker', model_name='SyllabusTopic')
        topics_taught = SyllabusTopic.objects.filter(syllabus__in=self.syllabustaught.all())

        ratings = []
        for topic in topics_taught:
            ratings.append(topic.classAverageRating(self))

        completion = []
        for topic in topics_taught:
            completion.append(topic.classAverageCompletion(self))

        data = list(zip(topics_taught, completion, ratings))

        return data

    def students(self):
        return Student.objects.filter(classgroups=self)

    def all_students_completion_data(self):

        students = self.students()

        ratings = []
        journaled = []
        for student in students:
            individual_ratings = []
            individual_journaled = []
            for syllabus in self.syllabustaught.all():
                individual_ratings.append(syllabus.studentAverageRating(student))
                individual_journaled.append(syllabus.student_completion(student))
            ratings.append(average(individual_ratings))
            journaled.append(average(individual_journaled))

        data = list(zip(students, journaled, ratings))
        return data

    def percentage_topics_taught(self):

        # Avoid circular import:
        SyllabusPoint = apps.get_model(app_label='tracker', model_name='SyllabusPoint')
        # Get total number of syllabus points
        total_points = SyllabusPoint.objects.filter(sub_topic__topic__syllabus__in=self.syllabustaught.all())
        total_points = total_points.distinct().count()

        # Find how many individual points we've taught:

        # Get all lessons:
        Lesson = apps.get_model(app_label='timetable', model_name='Lesson')
        all_lessons = Lesson.objects.filter(classgroup=self)
        taught_points = SyllabusPoint.objects.filter(lesson__in=all_lessons)


        if taught_points == 0 or total_points == 0:
            return 0
        else:
            taught_points = taught_points.distinct().count()

            return round(taught_points/total_points * 100, 0)


class TutorGroup(models.Model):
    tgname = models.CharField(max_length=5)
    tgtutor = models.ForeignKey('school.Teacher', on_delete=models.CASCADE, blank=True, null=True)
    pastoral_link = TreeOneToOneField('school.PastoralStructure', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.tgname


class Student(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Undisclosed', 'Undisclosed'),
    )

    LS_TYPES = (
        ('S', 'S'),
        ('SA', 'SA'),
        ('M', 'M'),
        ('SS', 'SS'),
        ('N', 'N'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Gender = models.CharField(max_length=20, choices=GENDER, blank=True)
    idnumber = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    classgroups = models.ManyToManyField('school.ClassGroup')
    tutorgroup = models.ForeignKey('school.TutorGroup', blank=True, null=True, on_delete=models.SET_NULL)
    academic_tutorgroup = TreeForeignKey('school.PastoralStructure', on_delete=models.SET_NULL, null=True, blank=True)
    learning_support = models.CharField(max_length=5, choices=LS_TYPES, blank=True, null=True)
    eal = models.BooleanField(blank=False, null=False, default=False)
    dob = models.DateField(blank=True, null=True)
    SIMS_name = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        space = ' '
        fullname = self.user.first_name + space + self.user.last_name  # + space + '(' + self.tg.tgname + ')'
        # fullname = 'temporary'
        return fullname

    def age(self):
        if self.dob:
            import datetime
            return datetime.date.today() - self.dob

# For CSV Imports:

class CSVDoc(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class PastoralStructure(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    leaders = models.ManyToManyField(Teacher, blank=True)
    kpis = models.ManyToManyField('tracker.StandardisedData', blank=True)
    classgroups = models.ManyToManyField(ClassGroup, blank=True)
    kpi_pairs = models.ManyToManyField('tracker.KPIPair', blank=True)

    def all_leaders(self):
        superiors = self.get_ancestors(include_self=True)
        return Teacher.objects.filter(pastoralstructure__leaders__in=superiors)

    def all_kpis(self):
        ancestors = self.get_ancestors(include_self=True)

        StandardisedData = apps.get_model(app_label='tracker', model_name='StandardisedData')
        return StandardisedData.objects.filter(pastoralstructure__in=ancestors)

    def students(self):
        return Student.objects.filter(academic_tutorgroup__in=self.get_descendants(include_self=True))



class AcademicStructure(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    leaders = models.ManyToManyField(Teacher, blank=True)
    kpis = models.ManyToManyField('tracker.StandardisedData', blank=True)
    classgroups = models.ManyToManyField(ClassGroup, blank=True)
    kpi_pairs = models.ManyToManyField('tracker.KPIPair', blank=True)

    def __str__(self):
        return self.name

    def all_leaders(self):
        superiors = self.get_ancestors(include_self=True)
        return Teacher.objects.filter(academicstructure__leaders__in=superiors)

    def all_kpis(self):
        ancestors = self.get_ancestors(include_self=True)

        StandardisedData = apps.get_model(app_label='tracker', model_name='StandardisedData')
        return StandardisedData.objects.filter(academicstructure__in=ancestors)

    def students(self):
        return Student.objects.filter(classgroups__academicstructure=self.get_descendants(include_self=True))
