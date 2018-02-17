from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('',views.splash),
    path('teachers/', views.teachers),
    path('students/', views.students),
    path('signup/', views.signup),
    path('login/', views.login)

]
