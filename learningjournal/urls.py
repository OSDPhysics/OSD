from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('<int:student_pk>', views.student_journal, name='student_journal'),
    path('<int:student_pk>/<int:syllabus_pk>', views.student_journal_syllabus, name='journal_all'),
]