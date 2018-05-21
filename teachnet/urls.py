from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='teachnet_home'),
    path('profile/<int:teacher_pk>', views.profile, name='profile'),
    path('profile/<int:teacher_pk>/objectives', views.objectives, name='objectives'),
    path('profile/<int:teacher_pk>/update_objective', views.new_objectives, name='set_objective'),
    path('profile/<int:teacher_pk>/edit_objective/<int:objective_pk>', views.edit_objective, name='edit_objective'),
    path('skills', views.teacherskills,name='teacherskills'),
    path('skills/<int:pk>', views.teacherwithskill, name='teacherwithskill'),
]
