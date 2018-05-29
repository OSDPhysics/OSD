from django.urls import path
from . import views

app_name = "journal"

urlpatterns = [
    path('', views.splash, name='splash'),
    path('<int:student_pk>/', views.full_journal, name='full_journal'),
path('<int:student_pk>/print', views.print_full_journal, name='print_full_journal'),
]