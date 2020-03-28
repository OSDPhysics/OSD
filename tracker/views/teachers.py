from django.contrib.auth.decorators import login_required
from tracker.charts import CohortPointGraph, CohortSubTopicChart, StudentChart, StudentSubTopicGraph
from journal.forms import StudentJournalEntryLarge
from journal.functions import move_mark_reflection_to_journal_student_mptt
from journal.models import StudentJournalEntry
from django.contrib import messages
from timetable.models import Lesson, LessonResources
from django.db.models import Sum
from operator import itemgetter
import datetime
from tracker.models import *
import os

from django.shortcuts import render, redirect, get_object_or_404
from tracker.forms import *
from osd.decorators import *
from django.urls import reverse, reverse_lazy
from school.models import PastoralStructure, AcademicStructure
import logging
from tracker.functions.adddata import *


logger = logging.getLogger(__name__)


@teacher_only
def add_test(request):
    '''Take the information for the first stage of a new test record'''

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewExamForm(request.POST)
        if form.is_valid():
            new_exam = form.save()

            return redirect(reverse('tracker:examDetail', args=(new_exam.pk,)))

        else:
            return render(request, 'tracker/new_exam1.html', {'form': form})

    else:
        form = NewExamForm()
    return render(request, 'tracker/new_exam1.html', {'form': form})


@teacher_only
def list_syllabuses(request):
    syllabuses = MPTTSyllabus.objects.all()
    return render(request, 'tracker/syllabus.html', {'syllabuses': syllabuses})


@teacher_only
def list_exams(request):
    exams = Exam.objects.all()
    return render(request, 'tracker/exams.html', {'exams': exams})


@teacher_only
def tracker_overview(request):
    syllabuses = Syllabus.objects.order_by('examtype')
    sittings = Sitting.objects.order_by('datesat')[:10]

    return render(request, 'tracker/tracker_overview.html', {'syllabuses': syllabuses,
                                                             'sittings': sittings})


@teacher_only
def examDetails(request, pk):
    exam = Exam.objects.get(pk=pk)
    syllabus = exam.syllabus.all()
    sittings = Sitting.objects.filter(exam=exam)
    questions = Question.objects.filter(exam=exam)
    setquestionsformset = modelformset_factory(Question, form=SetQuestions, extra=10)
    parent_form = MPTTSyllabusForm()
    if request.method == 'POST':
        qform = setquestionsformset(request.POST)

        # Quite a nasty hack to remove the hidden 'exam' field from only those forms without data.

        for form in qform:
            if form['qorder'].value == '' and form['qnumber'].value == '' and form['syllabuspoint'].value == '' and \
                    form['maxsore'].value == '':
                form.data['exam'].value = ''  # set the exam to nothing.

        # if qform.is_valid():
        for form in qform:
            form.is_valid()
            # Only process formsets with data in them
            if 'qorder' in form.cleaned_data.keys():
                question = form.save(commit=False)
                question.exam = exam
                if question.qorder == 0:
                    question.delete()
                else:
                    question.save()
                    form.save_m2m()

        # Now sort of the field ordering: decimals may have been used to insert fields.

        questions = Question.objects.filter(exam=exam).order_by('qorder')
        n = 1
        for question in questions:
            question.qorder = n
            question.save()
            n = n + 1

        return redirect(reverse('tracker:examDetail', args=(pk,)))

        # else:
        # return render(request, 'tracker/exam_details.html', {'exam': exam,
        # 'sittings': sittings,
        # 'questions': questions,
        # 'qform': qform})

    else:
        qform = setquestionsformset(queryset=Question.objects.filter(exam=exam).order_by('qorder'))

        for form in qform:
            form.initial['exam'] = exam.pk

        return render(request, 'tracker/exam_details.html', {'exam': exam,
                                                             'sittings': sittings,
                                                             'questions': questions,
                                                             'qform': qform,
                                                             'parent_form': parent_form
                                                               })


@teacher_only
def sitting_detail(request, pk):
    sitting = Sitting.objects.get(pk=pk)
    students = Student.objects.filter(classgroups=sitting.classgroup).order_by('pk').order_by('user__last_name')

    # collect total scores for this test
    scores = []
    percentages = []
    exam_total = sitting.exam.max_score()
    for student in students:
        total = Mark.objects.filter(sitting=sitting).filter(student=student).aggregate(Sum('score'))
        scores.append(total['score__sum'])
        studnet_total = total['score__sum']
        if studnet_total:
            percentage = studnet_total / exam_total *100

        else:
            percentage = False
        percentages.append(percentage)

    data = list(zip(students, scores, percentages))

    # Get the topic ratings:
    topic_data = sitting.class_topic_performance()
    return render(request, 'tracker/sitting_detail.html', {'sitting': sitting,
                                                           'scores': scores,
                                                           'data': data,
                                                           'topic_data': topic_data})


@teacher_only
def new_sitting(request, exampk, ):

    exam = Exam.objects.get(pk=exampk)
    questions = Question.objects.filter(exam=exam)

    requesting_teacher = Teacher.objects.get(user=request.user)
    currentdate = datetime.today()
    sittingform = NewSittingForm(initial={"teacher":requesting_teacher,
                                          "date":currentdate, })

    if request.method == 'POST':
        sittingform = NewSittingForm(request.POST)

        if sittingform.is_valid():

            classgroup = sittingform.cleaned_data['classgroup']
            sitting = Sitting.objects.create(exam=exam, classgroup=classgroup, datesat=sittingform.cleaned_data['date'],
                                             openForStudentRecording=True)
            students = Student.objects.filter(classgroups=classgroup)
            for student in students:
                for question in questions:
                    Mark.objects.get_or_create(student=student, question=question, sitting=sitting)
            return redirect(reverse('tracker:sitting_detail', args=[sitting.pk, ]))

        else:
            return render(request, 'tracker/new_sitting.html', {'sittingform': sittingform})

    return render(request, 'tracker/new_sitting.html', {'sittingform': sittingform})


@teacher_only
def sitting_toggle_open_for_recording(request, sitting_pk):
    sitting = Sitting.objects.get(pk=sitting_pk)
    classgroup = sitting.classgroup
    sitting.toggle_open_for_recording()
    return redirect(reverse('school:class_detail', args=[classgroup.pk, ]))


@teacher_only
def input_class_marks(request, sitting_pk):
    # Get the main data we'll need
    sitting = Sitting.objects.get(pk=sitting_pk)
    students = Student.objects.filter(classgroups=sitting.classgroup).order_by('user__last_name', 'user__first_name',
                                                                               'pk')
    questions = Question.objects.filter(exam=sitting.exam).order_by('qorder')

    # make sure that all the marks exist

    for student in students:
        for question in questions:
            Mark.objects.get_or_create(student=student, sitting=sitting, question=question)

    MarkFormset = modelformset_factory(Mark, fields=('score',), extra=0, widgets={
        'score': forms.Textarea(attrs={'rows': 1, 'cols': 2}),
    })

    # marks = Mark.objects.filter(student__in=students, sitting=sitting).order_by('question__qorder')
    # formset = MarkFormset(queryset=marks)

    # experimental

    formsets = []
    n = 0

    if request.method == 'GET':
        for question in questions:
            marks = Mark.objects.filter(student__in=students, sitting=sitting, question=question).order_by(
                'student__user__last_name', 'student__user__first_name', 'student__pk')
            formset = MarkFormset(queryset=marks, prefix=n)
            formsets.append(formset)
            n = n + 1

        entry_rows = list(zip(questions, formsets))

        return render(request, 'tracker/input_class_marks.html', {'entry_rows': entry_rows,
                                                                  'sitting': sitting,
                                                                  'students': students})

    if request.method == 'POST':
        n = 0
        for question in questions:
            formset = MarkFormset(request.POST, prefix=n)
            if formset.is_valid():
                formset.save()

            else:
                entry_rows = list(zip(questions, formsets))
                return render(request, 'tracker/input_class_marks.html', {'entry_rows': entry_rows,
                                                                          'sitting': sitting,
                                                                          'students': students})
            n = n + 1

        entry_rows = list(zip(questions, formsets))

        return render(request, 'tracker/input_class_marks.html', {'entry_rows': entry_rows,
                                                                  'sitting': sitting,
                                                                  'students': students})


@teacher_only
def sitting_by_q(request, pk):
    sitting = Sitting.objects.get(pk=pk)
    students = Student.objects.filter(classgroups=sitting.classgroup).order_by('pk').order_by('user__last_name')
    questions = Question.objects.filter(exam__sitting=sitting).order_by('qorder')

    # create a row of percentage scores for each mark
    scores = []
    for question in questions:
        row = []
        for student in students:
            mark, created = Mark.objects.get_or_create(sitting=sitting, student=student, question=question)
            row.append(mark.percentage())
        scores.append(row)

    score_data = list(zip(questions, scores))

    return render(request, 'tracker/sitting_detail_by_q.html', {'sitting': sitting,
                                                                'scores': scores,
                                                                'score_data': score_data,
                                                                'students': students})


@teacher_only
def classgroup_all_syllabuses_completion(request, classgroup_pk):
    """ REport how much of the syllabus has been taught and assessed """
    # Make sure we can teach multiple syllabuss

    classgroup = ClassGroup.objects.get(pk=classgroup_pk)
    classgroup_syllabuss = classgroup.syllabustaught.all()

    data = []

    for syllabus in classgroup_syllabuss:
        row = [syllabus]
        row.append(syllabus.classgroup_percentage_taught(classgroup))
        row.append(syllabus.classgroup_percentage_assessed(classgroup))
        data.append(row)

    return render(request, 'tracker/classgroup_all_syllabus_completion.html', {
        'classgroup': classgroup,
        'data': data
    })


@teacher_only
def classgroup_topic_completion(request, classgroup_pk, topic_pk):
    classgroup = ClassGroup.objects.get(pk=classgroup_pk)
    topic = SyllabusTopic.objects.get(pk=topic_pk)

    sub_topics = topic.sub_topics()
    data = []
    for sub_topic in sub_topics:
        row = [sub_topic]
        row.append(sub_topic.classgroup_percent_taught(classgroup))
        row.append(sub_topic.classgroup_percent_assessed(classgroup))
        data.append(row)

    return render(request, 'tracker/classgroup_topic_completion.html', {'classgroup': classgroup,
                                                                        'topic': topic,
                                                                        'data': data})


@teacher_only
def coverage_check(request, syllabus_pk):
    syllabus = Syllabus.objects.get(pk=syllabus_pk)

    classes = ClassGroup.objects.filter(syllabustaught=syllabus)

    points = SyllabusPoint.objects.filter(topic__syllabus=syllabus).order_by('sub_topic', 'number')

    data = []
    row = ["", ]

    for classgroup in classes:
        row.append(str(classgroup))

    data.append(row)

    for point in points:
        row = [str(point)]
        for classgroup in classes:
            if point.has_been_taught(classgroup):
                row.append("Y")
            else:
                row.append("N")
        data.append(row)

    return render(request, "tracker/coverage_check.html", {'syllabus': syllabus,
                                                           'data': data})


@teacher_only
def new_teacher_overview(request, teacher_pk):
    """ New splash screen using MPTT Models """

    teacher = Teacher.objects.get(pk=teacher_pk)
    classgroups = ClassGroup.objects.filter(archived=False, groupteacher=teacher,)

    classgroup_data = []  # format is: Classgroup, Syllabuses_taught, progress_dictionary, latest_assessment
    for group in classgroups:
        row = []
        # Construct a table set:
        row.append(group)
        syllabuses = []
        progress_dics = []
        for syllabus in group.mptt_syllabustaught.all():
            syllabuses.append(syllabus)
            progress_dics.append(syllabus.group_ratings_data(group.students()))
        row.append(syllabuses)
        row.append(progress_dics)
        row.append(group.latest_assessment())
        classgroup_data.append(row)


    sittings = Sitting.objects.\
        filter(classgroup__in=classgroups,
               classgroup__archived=False).\
        order_by('datesat').reverse()

    return render(request, "tracker/mptt_teacher_overviewV2.html", {'teacher': teacher,
                                                                  'classgroups': classgroups,
                                                                  'sittings': sittings,
                                                                  'classgroup_data': classgroup_data})


@teacher_only
def classgroup_ratings(request, classgroup_pk, syllabus_pk):
    """ Displays the ratings for a classroup for a given syllabus """

    classgroup = ClassGroup.objects.get(pk=classgroup_pk)
    syllabus = MPTTSyllabus.objects.get(pk=syllabus_pk)
    if not syllabus.is_root_node():
        parent = syllabus.get_ancestors(ascending=True)[0]
    else:
        parent = False

    students = classgroup.students()

    # Create the data for students:
    student_data = []
    for student in students:
        row = []
        data = syllabus.group_ratings_data(students=Student.objects.filter(pk=student.pk))
        row.append(student)
        row.append(student.tutorgroup)
        row.append(student.Gender)
        row.append(data)
        student_data.append(row)

    # Now let's do the topics they've been taught
    # We need two different takes here; one if we're at the bottom of a tree,
    # one if we're at a parent object.

    # For parents topics:

    if syllabus.get_descendant_count():
        sub_topic_data = []
        # We are not at the bottom:
        sub_points = syllabus.get_children()
        for point in sub_points:
            row = []
            row.append(point)
            row.append(point.group_ratings_data(students))
            sub_topic_data.append(row)
    else:
        # We are at the bottom of a row:
        sub_topic_data = [[syllabus, syllabus.group_ratings_data(students)], ]

    return render(request, 'tracker/classgroup_ratings_mptt2.html', {'classgroup': classgroup,
                                                                    'syllabus': syllabus,
                                                                    'students': students,
                                                                    'student_data': student_data,
                                                                    'sub_topic_data': sub_topic_data,
                                                                    'parent': parent})


@teacher_only
def student_standardised_data(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    standardised_data = []

    pass_parents = StandardisedData.objects.get(name="PASS")
    pass_data_objects = pass_parents.get_children()

    CAT4_parent = StandardisedData.objects.get(name="CAT4")
    CAT4_data_objects = CAT4_parent.get_children()

    pass_data = StandardisedResult.objects.filter(student=student, standardised_data__in=pass_data_objects)
    CAT4_data = StandardisedResult.objects.filter(student=student, standardised_data__in=CAT4_data_objects)

    standardised_data.append(pass_data)
    standardised_data.append(CAT4_data)

    assessments = Sitting.objects.filter(classgroup__student=student).order_by('datesat').reverse()

    return render(request, 'tracker/student_standardised_overview.html', {'student': student,
                                                                          'standardised_data': standardised_data,
                                                                          'assessments': assessments})


@teacher_only
def cohort_standardised_data_vs_target(request, cohort_pk):
    cohort = Student.objects.all()
    IGCSE_parent = StandardisedData.objects.get(name="IGCSE Grades")
    IGCSE_data_objects = IGCSE_parent.get_children()

    IGCSE_graph_data = []
    for subject in IGCSE_data_objects:
        row = subject.cohort_target_vs_current_data(cohort)
        row.append("/" + str(row[0]) + "/")
        IGCSE_graph_data.append(row)

    return render(request, 'tracker/cohort_std_data_vs_tgt.html', {'IGCSE_graph_data': IGCSE_graph_data})


@teacher_only
def school_standardised_data_vs_target(request, pastoral_pk, academic_pk):
    """ Display clickable radial graphs for a cohort, as narrowed by both their pastoral and academic position in the data structure. """
    # Set up containers for our two charts:
    pastoral_data = []
    academic_data = []

    # 1. GET THE SUB-LEVELS FOR EACH REQUESTED VIEW: **
    pastoral_level = PastoralStructure.objects.get(pk=pastoral_pk)

    academic_level = AcademicStructure.objects.get(pk=academic_pk)

    return dashboard(request,
              academic_level=academic_level,
              pastoral_level=pastoral_level)


def dashboard(request,
              student=Student.objects.none(),
              academic_level=AcademicStructure.objects.none(),
              pastoral_level=AcademicStructure.objects.none()):

    pastroal_sub_levels = pastoral_level.get_descendants(include_self=True)
    academic_sub_levels = academic_level.get_descendants(include_self=True)

    if student.exists():
        # This happens if we've been sent a single student.
        students = Student.objects.filter(pk=student.pk)

        student_tutorgroup = student.tutorgroup
        pastoral_level = PastoralStructure.objects.get(name=student_tutorgroup.tgname)
        academic_level = PastoralStructure.objects.get(name="Garden International School")


    else:
        students = Student.objects.filter(classgroups__academicstructure__in=academic_sub_levels,
                                          classgroups__pastoralstructure__in=pastroal_sub_levels)

    academic_kpis = academic_level.all_kpis()
    pastoral_kpis = pastoral_level.all_kpis()

    # 4. Grenerate graph data with urls to next view
    def generate_kpi_radar_data(kpis=StandardisedData.objects.none(), cohort=Student.objects.none()):
        data = []
        for kpi in kpis:
            dataset = StandardisedResult.objects.filter(student__in=cohort, standardised_data=kpi)
            avgs = dataset.aggregate(av_target=Avg('target'), av_result=Avg('result'))
            row = []
            row.append(kpi)
            row.append(avgs['av_target'])
            row.append(avgs['av_result'])
            data.append(row)
        return data

    def generate_residual_radar_data(pastoral_level=PastoralStructure.objects.none()):
        pastoral_sub_levels = pastoral_level.get_children()
        data = []
        for level in pastoral_sub_levels:
            row = [level]
            students = Student.objects.filter(academic_tutorgroup__in=level.get_descendants(include_self=True))

            residual = StandardisedResult.objects.filter(student__in=students).aggregate(average_residual=Avg('residual'))['average_residual']
            row.append(residual)
            data.append(row)
        return data

    pass_data = StandardisedData.objects.filter(name__contains='PASS')
    def generate_pass_radar(pass_data=pass_data, cohort=Student.objects.all()):
        data = []
        for point in pass_data:
            row = [point]
            average_pass = StandardisedResult.objects.filter(student__in=cohort, standardised_data=point).aggregate(result=Avg('result'))['result']
            row.append(average_pass)
            data.append(row)

        return data

    academic_data = generate_kpi_radar_data(kpis=academic_kpis, cohort=students)

    pastoral_data = generate_kpi_radar_data(kpis=pastoral_kpis, cohort=students)

    pass_data = generate_pass_radar(cohort=students)

    residuals = generate_residual_radar_data(pastoral_level)

    # 5. Render the page.

    return render(request, 'tracker/cohort_std_data_vs_tgt_plotly.html', {'pastoral_level': pastoral_level,
                                                                          'academic_level': academic_level,
                                                                          'academic_data': academic_data,
                                                                          'pastroal_data': pastoral_data,
                                                                          'residuals': residuals,
                                                                          'pass_data': pass_data})


@admin_only
def mpttselect(request):
    form = mpttSyllabusPointSelect()
    return render(request, 'tracker/mpttselect.html', {'form': form})
