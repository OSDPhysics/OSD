from django.contrib import admin
from django import forms
from searchableselect.widgets import SearchableSelect

# Register your models here.
from .models import *

admin.site.register(Objective)
admin.site.register(Skill)