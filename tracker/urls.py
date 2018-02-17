from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.front_login, name='front_login'),
    path('teachers', views.teachers),
    path('teachers/add', views.add_teacher, name='add_teacher' ),
]
