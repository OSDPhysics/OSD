from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Teacher(models.Model):
    TITLES = (
            ('Miss', 'Miss'),
            ('Mrs', 'Mrs'),
            ('Ms', 'Ms'),
            ('Mr', 'Mr'),
            ('Dr', 'Dr'),
        )

    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    title = models.CharField(max_length=20, choices=TITLES, blank=True)
    staffcode = models.CharField(max_length=10, blank=True)

    def __str__(self):
        space = ' '
        fullname = self.title + space + self.user.first_name + space + self.user.last_name + space + '(' + self.staffcode + ')'
        #fullname = 'temporary'
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
    groupteacher = models.ForeignKey('tracker.Teacher',on_delete=models.CASCADE)

    def __str__(self):
        return self.groupname

class TutorGroup(models.Model):
    tgname = models.CharField(max_length=5)
    tgtutor = models.ForeignKey('tracker.Teacher',on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.tgname

class Student(models.Model):
    GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Undisclosed', 'Undisclosed'),
        )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Gender = models.CharField(max_length=20, choices=GENDER, blank=True)
    idnumber = models.IntegerField(blank=True,null=True)
    tg = models.ForeignKey('tracker.TutorGroup',blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        space = ' '
        fullname =  self.user.first_name + space + self.user.last_name #+ space + '(' + self.tg.tgname + ')'
        #fullname = 'temporary'
        return fullname

    #Currently broken - if we log in any user, it wants to be linked to a student, too!

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Student.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.student.save()

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
    syllabustext = models.CharField(max_length=500)

    def __str__(self):
        return self.syllabustext

class Exam(models.Model):
    name = models.CharField(max_length=100)
    level = models.ForeignKey(Examlevel, on_delete=models.CASCADE)
    syllabus = models.ManyToManyField(Syllabus)

    def __str__(self):
        return self.name

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    qnumber = models.CharField(max_length=100)
    qorder = models.IntegerField()
    syllabuspoint = models.ForeignKey(Syllabuspoint, on_delete=models.CASCADE, blank=True, null=True)
    maxscore = models.IntegerField()

    def __str__(self):
        return self.qnumber

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return self.score
