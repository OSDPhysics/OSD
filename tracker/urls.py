from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('exams/new_exam', views.add_test1, name='new_exam1'),
]
