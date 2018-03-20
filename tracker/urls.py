from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('syllabus', views.list_syllabuses, name='syllabuses'),
    path('syllabus/<int:pk>', views.syllabus_detail, name='syllabus_detail'),
    path('exams/new_exam', views.add_test1, name='new_exam1'),
]
