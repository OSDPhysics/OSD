from django.db import models

# Create your models here.

class Teacher(models.Model):
    TITLES = (
            ('Miss', 'Miss'),
            ('Mrs', 'Mrs'),
            ('Ms', 'Ms'),
            ('Mr', 'Mr'),
            ('Dr', 'Dr'),
        )
    
    forename = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    title = models.CharField(max_length=20, choices=TITLES)
    staffcode = models.CharField(max_length=10)

    def __str__(self):
        space = ' '
        fullname = self.title + space + self.forename + space + self.surname + space + '(' + self.staffcode + ')'
        return fullname

class Group(models.Model):
    groupname = models.CharField(max_length=50)
    groupteacher = models.ForeignKey('tracker.Teacher',on_delete=models.CASCADE)

    def __str__(self):
        return self.groupname
