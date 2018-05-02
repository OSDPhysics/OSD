from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('skills', views.teacherskills,name='teacherskills'),
    path('skills/<int:pk>', views.teacherwithskill, name='teacherwithskill'),
]
