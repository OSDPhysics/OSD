from django.contrib import admin

# Register your models here.

from .models import Teacher
from .models import Group


admin.site.register(Teacher)
admin.site.register(Group)
