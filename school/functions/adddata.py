from django.contrib.auth.models import User, Group
from school.models import Student, Teacher, ClassGroup
from tracker.models import StandardisedResult, StandardisedData
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
                                                 )

    # created will be true if the user didn't already exist.

    if created:

        # New user won't have a password yet
        newuser.set_password(newstudent['password'])
        newuser.email = newstudent['email']
        newuser.first_name = newstudent['first_name']
        newuser.last_name = newstudent['last_name']
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


def process_student_wsst_dataset(path):
    with open(path, newline='') as csvfile:
        students = csv.reader(csvfile, delimiter=',', quotechar='|')
        newstudents = []  # list of all the newly-created students
        for row in students:
            newstudent = {'last_name': row[0],
                          'first_name': row[1],
                          'tutorgroup': row[2],
                          'gender': row[3], ## Must change to F or M
                          'learning_support': row[4],
                          'eal': row[5],
                          'catv': row[6],
                          'cat4q': row[7],
                          'cat4nv': row[8],
                          'cat4s': row[9],
                          'cat4mean': row[10],
                          'verbal_def': row[11],
                          'maths_car': row[12],
                          'reading_age': row[13],
                          'nrss': row[14],
                          'actual_age': row[15],
                          'pte_mean': row[16],
                          'english_achievement_mean': row[17],
                          'ptm_mean': row[18],
                          'maths_achievement': row[19],
                          'pts_mean': row[20],
                          'sci_achievement': row[21],
                          'av_achievement': row[22],
                          'pass_dom1': row[23],
                          'pass_dom2': row[24],
                          'pass_dom3': row[25],
                          'pass1': row[26],
                          'pass2': row[27],
                          'pass3': row[28],
                          'pass4': row[29],
                          'pass5': row[30],
                          'pass6': row[31],
                          'pass7': row[32],
                          'pass8': row[33],
                          'pass9': row[34],
                          ## IMPORTANT TO ADD!!
                          'student_id': row[35],
                          newstudents.append(addstudent_wsst_data(newstudent))

        return newstudents

def addstudent_wsst_data(newstudent):
    # Test to see whether the user exists yet

    newuser, created = User.objects.get_or_create(username=newstudent['username'],
                                                 )

    # created will be true if the user didn't already exist.

    if created:

        # New user won't have a password yet
        newuser.set_password("asdfoiqwefasidofu298bfkajs")
        newuser.email = str(newstudent['student_id']) + "@gardenschool.edu.my"
        newuser.first_name = newstudent['first_name']
        newuser.last_name = newstudent['last_name']
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

    # Add the students standardised data:

    for row in newstudent:
        if StandardisedData.objects.get(quickname=row.)

    return student

def add_student_standardised_data(student, result, target, point):

    # Remove this line in production; it's to make later stuff easier.
    point = StandardisedResult.objects.get_or_create(standardised_data=point, student=student)

    point.replace(new_result=result, new_target=target, reason="WSST Spreadsheet Import")
    return point
