from django.urls import path
from . import views
urlpatterns = [
    path('', views.splash, name='splash'),
    path('<int:student_pk>/', views.full_journal, name='full_journal'),
path('<int:student_pk>/print', views.print_journal, name='print_journal'),
]