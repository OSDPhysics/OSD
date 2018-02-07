from django.contrib import admin

# Register your models here.

from .models import Teacher
from .models import TutorGroup
from .models import ClassGroup
from. models import Student

admin.site.register(Teacher)
admin.site.register(TutorGroup)
admin.site.register(ClassGroup)
admin.site.register(Student)
