from django.urls import path
from tracker.autocomplete import *
from django.contrib import admin
from django.contrib.auth import views as auth_views
# from tracker import views

from tracker.views import common, students, teachers

app_name = "tracker"

urlpatterns = [
    path('', common.splash, name='splash'),
    path('splash/<int:teacher_pk>', teachers.new_teacher_overview, name='new_teacher_overview'),

    path('<int:student_pk>/', common.student_profile, name='student_profile'),

    path('syllabus', teachers.list_syllabuses, name='syllabuses'),
    path('syllabus/<int:pk>', common.syllabus_detail, name='syllabus_detail'),

    path('check/<classgroup_pk>', teachers.classgroup_all_syllabuses_completion, name='classgroup_all_syllabuses_completion'),
    path('check/syllabus/<int:syllabus_pk>/<classgroup_pk>', common.classgroup_syllabus_completion, name='classgroup_syllabus_completion'),
    path('check/topic/<int:topic_pk>/<classgroup_pk>', teachers.classgroup_topic_completion, name='classgroup_topic_completion'),

    path('classgroups-autocomplete/', ClaassgroupAutocomplete.as_view(), name='classgroups-autocomplete'),

    path('topics/<int:topic_pk>/<int:student_pk>', common.student_topic_overview, name='student_topic_overview'),

    path('sub-topic/<int:sub_topic_pk>/<classgroup_pk>', common.classgroup_sub_topic_completion, name='classgroup_sub_topic_completion'),
    path('subtopics/<int:sub_topic_pk>/<int:student_pk>', common.student_sub_topic_overview, name='student_sub_topic_overview'),

    path('exams/new_exam', teachers.add_test, name='new_exam1'),

    path('syllabus/import', common.import_spec_points, name ='syllabusimport'),

    path('exams/<int:pk>', teachers.examDetails, name='examDetail'),
    path('exams/', teachers.list_exams, name='listExams'),
    path('exams/new', teachers.add_test, name='new_test'),

    path('sittings/', common.construction, name='sittings'),
    path('sittings/new/<int:exampk>', teachers.new_sitting, name='new_sitting'),
    path('sittings/<int:pk>', teachers.sitting_detail, name='sitting_detail'),
    path('sittings/<int:sitting_pk>/classmarks', teachers.input_class_marks, name='input_class_marks'),
    path('sittings/<int:pk>/toggle', teachers.sitting_toggle_open_for_recording, name='sitting_toggle_open_for_recording'),
    path('sittings/<int:sitting_pk>/detail', teachers.sitting_by_q, name='sitting_by_q'),
    path('sittings/<int:sitting_pk>/<int:student_pk>/scores', common.input_marks, name='input_marks'),
    path('sittings/<int:sitting_pk>/<int:student_pk>', common.student_sitting_summary, name='student_sitting_summary'),\


    path('syllabuspoints/<int:point_pk>/<int:student_pk>', common.small_assessment_list, name='small_assessment_list'),
    path('syllabus-point-autocomplete/', SyllabusPointAutocomplete.as_view(), name='syllabus-point-autocomplete'),
    path('syllabus-autocomplete/', SyllabusAutocomplete.as_view(), name='syllabus-autocomplete'),
    path('syllabus-autocomplete2/', SyllabusPointAutocomplete2.as_view(), name='syllabus-autocomplete2'),

    path('lesson_autocomplete/', LessonAutocomplete.as_view(), name='lesson_autocomplete'),

    path('mptt_syllabus_autocomplete/', MPTTSyllabusAutocomplete.as_view(), name='mptt_syllabus_autocomplete'),

    path('chart_test/', common.chart_test, name='chart_test'),
    path('chart_test2/', common.sub_topic_chart_test, name='sub_topic_test_chart'),

    path('output_check/<int:classgroup_pk>/<int:topic_pk>', common.rating_ouput_check, name='rating_output_check'),

    path('coverage_check/<int:syllabus_pk>', teachers.coverage_check, name='coverage_check'),

    path('student_s_topic_graph/<int:student_pk>/<int:sub_topic_pk>', common.sub_topic_student_graph_check, name='student_s_topic_chart'),
    path('student_single_graph/<int:student_pk>/<int:sub_topic_pk>', common.single_sub_topic_graph_check, name='student_single_graph_check'),

    path('class/<int:classgroup_pk>/<int:syllabus_pk>', teachers.classgroup_ratings, name='classgroup_ratings',),

    path('student/<int:student_pk>/<int:syllabus_pk>', common.student_ratings, name='student_ratings'),
    path('student_standardised/<int:student_pk>', teachers.student_standardised_data, name='student_standardised_data'),

    path('cohort_standardised/<int:cohort_pk>', teachers.cohort_standardised_data_vs_target, name='cohort_std_data_vs_tgt')
]
