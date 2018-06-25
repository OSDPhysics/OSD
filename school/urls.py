from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_name = "school"

urlpatterns = [
    path('', views.home, name='school_home'),
    path('teachers/', views.teachers,name = 'teachers'),
    path('teachers/<int:pk>', views.teacher_details, name='teacher_details'),
    path('teachers/new/', views.new_teacher, name='new_teacher'),
    path('teachers/import', views.import_teachers, name='import_teachers'),
    path('students/', views.students, name='list_students'),
    path('students/import', views.import_students, name='import_students'),
    path('students/new_student/', views.new_student, name='new_student'),
    path('student/<int:pk>', views.student_detail, name='student_detail'),
    path('class/', views.classes, name='classes'),
    path('class/<int:class_pk>', views.class_details, name='class_details'),
    path('class/<int:student_pk>/<int:class_pk>', views.student_class_overview, name='student_class_overview'),
    path('', views.school, name='school'),
]
