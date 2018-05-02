from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='teachnet_home'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('profile/<int:pk>/objectives', views.objectives, name='objectives'),
    path('skills', views.teacherskills,name='teacherskills'),
    path('skills/<int:pk>', views.teacherwithskill, name='teacherwithskill'),
]
