from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('syllabus', views.list_syllabuses, name='syllabuses'),
    path('syllabus/<int:pk>', views.syllabus_detail, name='syllabus_detail'),
    path('exams/new_exam', views.add_test, name='new_exam1'),
    path('syllabus/import', views.import_spec_points, name = 'syllabusimport'),
    path('questions/new', views.create_questions, name = 'create_exam_questions'),
    path('exams/<int:pk>', views.examDetails, name='examDetail'),
    path('exams/', views.list_exams, name='listExams'),
    path('exams/new', views.add_test, name='new_test'),
    path('sittings/', views.construction, name='sittings'),
    path('sittings/<int:pk>', views.sitting_detail, name='sitting_detail'),
    path('', views.tracker_overview, name='tracker_overview'),

]
