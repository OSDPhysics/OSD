from django.urls import path
from . import views
urlpatterns = [
    path('<int:student_pk>/', views.full_journal, name='full_journal')
]