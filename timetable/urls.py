from django.urls import path
from . import views

app_name = "timetable"

urlpatterns = [
    path('', views.teacher_splash, name='teacher_splash'),
    path('<int:teacher_pk>/<int:week_number>', views.teacher_tt, name='teacher_tt'),
    path('class/<int:classgroup_pk>', views.class_lesson_list, name='class_lesson_list'),
    path('class/<int:classgroup_pk>/check', views.class_lesson_check, name='class_lesson_check'),
    path('copy/<int:lesson_pk>', views.copy_lesson, name='copy_lesson'),
    path('delete/<int:lesson_pk>/<int:class_pk>', views.delete_lesson, name='delete_lesson'),
    path('confirm_delete/<int:lesson_pk>/<int:class_pk>', views.confirm_delete_lesson, name='confirm_delete_lesson'),
    path('insert/<int:lesson_pk>', views.insert_lesson, name='insert_lesson'),
    path('move_up/<int:lesson_pk>', views.move_lesson_up, name='move_lesson_up'),
    path('move_down/<int:lesson_pk>', views.move_lesson_down, name='move_lesson_down'),
    path('lessons/<int:lesson_pk>', views.lesson_details, name='lesson_details'),
    path('lessons/<int:lesson_pk>/edit', views.edit_lesson, name='edit_lesson'),
    path('lessons/<int:lesson_pk>/add_resource/<int:resource_pk>', views.edit_lesson_resource, name='edit_lesson_resource')
]