from django.contrib.auth.models import User, Group
from school.models import Student, Teacher, ClassGroup
import csv
import codecs


def processstudent(path):
    with open(path, newline='') as csvfile:
        students = csv.reader(csvfile, delimiter=',', quotechar='|')
        newstudents = []  # list of all the newly-created students
        for row in students:
            newstudent = {'last_name': row[0],
                          'first_name': row[1],
                          'tutorgroup': row[2],
                          'Gender': row[3],
                          'email': row[4],
                          'username': row[5],
                          'studentid': row[6],
                          'password': row[7],
                          'classgroup': row[8]}

            newstudents.append(addstudent(newstudent))

        return newstudents


def processteacher(reader):
    for row in reader:
        newteacher = {'last_name': row[0],
                      'first_name': row[1],
                      'title': row[2],
                      'email': row[3],
                      'username': row[4],
                      'staffcode': row[5],
                      'password': row[6]}

        addteacher(newteacher)


def addstudent(newstudent):
    # Test to see whether the user exists yet

    newuser, created = User.objects.get_or_create(username=newstudent['username'],
                                                  email=newstudent['email'],
                                                  password=newstudent['password'],
                                                  first_name=newstudent['first_name'],
                                                  last_name=newstudent['last_name']
                                                  )

    # created will be true if the user didn't already exist.

    if created:

        # New user won't have a password yet
        newuser.set_password(newstudent['password'])
        newuser.save()

        # Place new user in the Students Auth group

        students_user_group = Group.objects.get(name='Students')
        students_user_group.user_set.add(newuser)

        student = Student.objects.create(user=newuser,
                                         Gender=newstudent['Gender'],
                                         idnumber=newstudent['studentid'],
                                         # year=int(newstudent['year'])

                                         )
    else:
        # This will execute if 'created' is False
        # which would mean that the student already existed
        # and has been set to the matching student.
        student = Student.objects.get(user=newuser)

    # Add student to CLASS GROUP (NOT USER GROUP)
    newclassgroupname = newstudent['classgroup']
    newclassgroup = ClassGroup.objects.get(groupname=newclassgroupname)
    student.classgroups.add(newclassgroup)

    return student


def addteacher(newteacher):
    newuser = User.objects.create_user(username=newteacher['username'],
                                       email=newteacher['email'],
                                       password=newteacher['password'],
                                       first_name=newteacher['first_name'],
                                       last_name=newteacher['last_name']
                                       )

    # New user won't have a password yet
    newuser.set_password(newteacher['password'])
    newuser.save()

    # Place new user in the Students Auth group

    teachers_user_group = Group.objects.get(name='Teachers')
    teachers_user_group.user_set.add(newuser)

    teacher = Teacher.objects.create(user=newuser,
                                     staffcode=newteacher['staffcode'],
                                     title=newteacher['title']

                                     )
    return teacher
