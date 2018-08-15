from django.urls import path
from . import views

app_name = "timetable"

urlpatterns = [
    path('', views.teacher_splash, name='teacher_splash'),
    path('<int:teacher_pk>/<int:week_number>', views.teacher_tt, name='teacher_tt')
]