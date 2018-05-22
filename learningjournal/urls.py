from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('<int:student_pk>', views.student_journal, name='student_journal')
]