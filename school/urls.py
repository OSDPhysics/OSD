from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='school_home'),
    path('teachers/', views.teachers),
    # not defined yet: path('teachers/<int:pk>', views.teacher_details, name='teacher_details'),
    path('teachers/new/', views.new_teacher, name='new_teacher'),
    path('teachers/import', views.import_teachers, name='import_teachers'),
    path('students/', views.students, name='list_students'),
    path('students/import', views.import_students, name='import_students'),
    path('students/new_student/', views.new_student, name='new_student'),
    path('student/<int:pk>', views.student_detail, name='student_detail'),
    path('', views.school, name='school'),
]
