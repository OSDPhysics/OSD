"""osd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout
from school import views as school_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tracker/', include('tracker.urls', namespace='tracker')),
    path('school/', include('school.urls', namespace='school')),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('searchableselect/', include('searchableselect.urls')),
    path('', school_views.splash, name='splash'),
    path('accounts/profile/', school_views.accounts_profile, name='accounts_profile'),
    path('teachnet/', include('teachnet.urls', namespace='teachnet')),
    path('journal/', include('journal.urls', namespace='journal')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

