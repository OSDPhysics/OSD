from django.contrib import admin
from timetable.models import *

# Register your models here.
admin.site.register(LessonSlot)
admin.site.register(TimetabledLesson)
admin.site.register(Lesson)
admin.site.register(LessonResources)