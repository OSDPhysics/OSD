from django.urls import path
from tracker.autocomplete import *
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_name = "tracker"

urlpatterns = [
    path('', views.splash, name='splash'),
    path('<int:student_pk>/', views.student_profile, name='student_profile'),
    path('syllabus', views.list_syllabuses, name='syllabuses'),
    path('syllabus/<int:pk>', views.syllabus_detail, name='syllabus_detail'),
    path('exams/new_exam', views.add_test, name='new_exam1'),
    path('syllabus/import', views.import_spec_points, name = 'syllabusimport'),
    path('exams/<int:pk>', views.examDetails, name='examDetail'),
    path('exams/', views.list_exams, name='listExams'),
    path('exams/new', views.add_test, name='new_test'),
    path('sittings/', views.construction, name='sittings'),
    path('sittings/new/<int:exampk>', views.new_sitting, name='new_sitting'),
    path('sittings/<int:pk>', views.sitting_detail, name='sitting_detail'),
    path('sittings/<int:pk>/detail', views.sitting_by_q, name='sitting_by_q'),
    path('', views.tracker_overview, name='tracker_overview'),
    path('sittings/<int:sitting_pk>/<int:student_pk>/scores', views.input_marks, name='input_marks'),
    path('sittings/<int:sitting_pk>/<int:student_pk>', views.student_sitting_summary, name='student_sitting_summary'),
    path('topics/<int:topic_pk>/<int:student_pk>', views.student_topic_overview, name='student_topic_overview'),
    path('subtopics/<int:sub_topic_pk>/<int:student_pk>', views.student_sub_topic_overview, name='student_sub_topic_overview'),
    path('syllabus-point-autocomplete/', SyllabusPointAutocomplete.as_view(), name='syllabus-point-autocomplete'),
    path('classgroups-autocomplete/', ClaassgroupAutocomplete.as_view(), name='classgroups-autocomplete'),
    path('syllabus-autocomplete/', SyllabusAutocomplete.as_view(), name='syllabus-autocomplete')

]
