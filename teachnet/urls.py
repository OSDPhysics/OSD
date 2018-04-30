from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:pk>', views.profile, name='profile'),


]
