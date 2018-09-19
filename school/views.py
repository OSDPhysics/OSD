import logging
import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse

from .forms import *
from .functions.adddata import *
from osd.decorators import *
from tracker.models import Sitting, SyllabusTopic

from osd.decorators import admin_only, teacher_or_own_only, teacher_only

logger = logging.getLogger(__name__)


@login_required
def home(request):
    user = request.user
    return render(request, 'school/home.html', {'user': user})


@login_required
def splash(request):
    # Different splash pages are served depending on the type of user

    # TEACHERS splash page:

    if request.user.groups.filter(name='Teachers').exists():
        # Get the teacher's classes and assessments:
        classes = ClassGroup.objects.filter(groupteacher__user=request.user)
        assessments = Sitting.objects.filter(classgroup__groupteacher__user=request.user).order_by('-datesat')
        return render(request, 'school/splash_teacher.html', {'classes': classes,
                                                              'assessments': assessments})

    # STUDENTS spash page
    elif request.user.groups.filter(name='Students').exists():
        student = Student.objects.get(user=request.user)
        classgroups = student.classgroups.all()

        classgroup_data = []  # Holds key data about each class the student is a member of
        for classgroup in classgroups:
            current_group = {}  # A dictionary containing key info about the class
            current_group[
                'classgroup'] = classgroup  # Store the class object so we can access everything else (teacher etc) in views

            # Find the most recent 5 assessments
            recent_assessments = Sitting.objects.filter(classgroup=classgroup).order_by('-datesat')[:5]

            # Get the scores for each one:
            assessment_scores = []
            for assessment in recent_assessments:

                assessment_scores.append(str(assessment.student_total(student)) + "/" + str(assessment.exam.max_score()['maxscore__sum']))

            current_group['assessments'] = list(zip(recent_assessments, assessment_scores))

            # Find all the main topics of this class' syllabus
            current_group['topics'] = SyllabusTopic.objects.filter(syllabus__classgroup=classgroup)

            # Let's get the ratings for each one
            ratings = []  # List of all the ratings, in order of topic

            for topic in current_group['topics']:
                ratings.append(topic.studentAverageRating(student))

            # Put the topic ratings alongside  a reference to each topic
            current_group['topics'] = list(zip(current_group['topics'], ratings))

            # Send the final set of data to the rest of the data for all classes.
            classgroup_data.append(current_group)

        return render(request, 'school/splash_student.html', {'student': student,
                                                              'classgroup_data': classgroup_data})

    else:
        return render(request, 'school/splash.html', {})


@login_required
def school(request):
    return render(request, 'school/school.html', {})


@admin_only
def new_teacher(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TeacherForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            newteacher = addteacher(form.cleaned_data)
            return HttpResponseRedirect('/school/teachers/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TeacherForm()
    return render(request, 'school/new_teacher.html', {'form': form})


@login_required
def new_student(request):
    return render(request, 'school/404.html')


@login_required
def teachers(request):
    teachers = Teacher.objects.order_by('user__last_name')
    return render(request, 'school/teachers.html', {'teachers': teachers})


@login_required
def students(request):
    students = Student.objects.order_by('user__last_name').order_by('classgroups__groupname')
    return render(request, 'school/students.html', {'students': students})


@login_required
def accounts_profile(request):
    return render(request, 'school/accounts_profile.html')


@teacher_or_own_only
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'school/student_detail.html', {'student': student})


def logout_view(request):
    logout(request)


# Add students in bulk from CSV
@admin_only
def import_students(request):
    # Deal with getting a CSV file

    if request.method == 'POST':
        csvform = CSVDocForm(request.POST, request.FILES)
        if csvform.is_valid():
            file = csvform.save()
            path = file.document.path
            processstudent(path)
            os.remove(path)
            file.delete()
            return redirect(reverse('school:list_students'))
    else:
        csvform = CSVDocForm()
    return render(request, 'school/model_form_upload.html', {'csvform': csvform})


@admin_only
def import_teachers(request):
    # Deal with getting a CSV file

    if request.method == 'POST':
        csvform = CSVDocForm(request.POST, request.FILES)
        if csvform.is_valid():
            file = csvform.save()
            path = file.document.path
            processteacher(path)
            os.remove(path)
            file.delete()
            return redirect('list_students')
    else:
        csvform = CSVDocForm()
    return render(request, 'school/model_form_upload.html', {'csvform': csvform})


@teacher_only
def classes(request):
    classes = ClassGroup.objects.all().order_by('groupteacher').order_by('groupname')
    return render(request, 'school/classes.html', {'classes': classes})


# TODO: implement
@teacher_only
def teacher_details(request, *args, **kwargs):
    return render(request, 'tracker/404.html')


# TODO: implement
@teacher_only
def class_details(request, class_pk):
    classgroup = ClassGroup.objects.get(pk=class_pk)
    return render(request, 'school/class_detail.html', {'classgroup': classgroup})


@login_required
def student_class_overview(request, student_pk, class_pk):
    classgroup = ClassGroup.objects.get(pk=class_pk)
    student = Student.objects.get(pk=student_pk)
    recent_assessments = classgroup.assessments()[:5]
    scores = []
    for assessment in recent_assessments:
        scores.append(str(assessment.student_total(student)) + "/" + str(assessment.exam.max_score()['maxscore__sum']))
    recent_assessments = list(zip(recent_assessments, scores))

    # Build a set with topic, completion, score:
    topics = classgroup.topics()
    completion = []
    score = []
    for topic in topics:
        completion.append(topic.studentCompletion(student))
        score.append(topic.studentAverageRating(student))

    topics_data = list(zip(topics, completion, score))

    return render(request, 'school/student_class_overview.html', {'student': student,
                                                                   'classgroup': classgroup,
                                                                   'recent_assessments': recent_assessments,
                                                                   'topic_data': topics_data})