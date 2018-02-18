from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.splash, name='splash'),
    path('teachers/', views.teachers),
    path('students/', views.students),
    path('new_teacher/', views.new_teacher, name='new_teacher'),
    path('new_student/', views.new_student, name='new_student'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('teachers/add', views.add_teacher, name='add_teacher'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/logout', views.logged_out, name='logged_out'),

]
