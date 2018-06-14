from django.contrib.auth.models import User, Group
from school.models import Student, Teacher, ClassGroup
import csv
import codecs

def processstudent(path):
    with open(path, newline='') as csvfile:
        students = csv.reader(csvfile, delimiter=',', quotechar='|')
        newstudents=[] # list of all the newly-created students
        for row in students:
            newstudent = {}
            newstudent['last_name'] = row[0]
            newstudent['first_name'] = row[1]
            newstudent['tutorgroup'] = row[2]
            newstudent['Gender'] = row[3]
            newstudent['email'] = row[4]
            newstudent['username'] = row[5]
            newstudent['studentid'] = row[6]
            newstudent['password'] = row[7]
            newstudent['classgroup'] = row[8]

            newstudents.append(addstudent(newstudent))

        return newstudents

def processteacher(reader):
    for row in reader:
        newteacher = {}
        newteacher['last_name'] = row[0]
        newteacher['first_name'] = row[1]
        newteacher['title'] = row[2]
        newteacher['email'] = row[3]
        newteacher['username'] = row[4]
        newteacher['staffcode'] = row[5]
        newteacher['password'] = row[6]

        addteacher(newteacher)


def addstudent(newstudent):
    # Test to see whether the user exists yet

    newuser, created = User.objects.get_or_create(username=newstudent['username'],
                                       email=newstudent['email'],
                                       password=newstudent['password'],
                                       first_name=newstudent['first_name'],
                                       last_name=newstudent['last_name']
                                       )

    if created:
        newuser.set_password(newstudent['password'])

    # created will be true if the user didn't already exist.

    if created:

        # Place new user in the Students Auth group

        students_user_group = Group.objects.get(name='Students')
        students_user_group.user_set.add(newuser)

        student = Student.objects.create(user=newuser,
                                         Gender=newstudent['Gender'],
                                         idnumber=newstudent['studentid'],
                                         #year=int(newstudent['year'])

                                         )
    else:
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
    teacher = Teacher.objects.create(user=newuser,
                                     staffcode=newteacher['staffcode'],
                                     title=newteacher['title']

                                     )
    return teacher
