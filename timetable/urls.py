from django.urls import path
from . import views

app_name = "timetable"

urlpatterns = [
    path('', views.teacher_splash, name='teacher_splash'),
    path('<int:teacher_pk>/<int:week_number>', views.teacher_tt, name='teacher_tt'),
    path('class/<int:classgroup_pk>', views.class_lesson_list, name='class_lesson_list'),
    path('class/<int:classgroup_pk>/check', views.class_lesson_check, name='class_lesson_check'),
    path('copy/<int:lesson_pk>', views.copy_lesson, name='copy_lesson'),
]