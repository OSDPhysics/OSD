from django.contrib import admin
from timetable.models import *
from timetable.forms import LessonForm
# Register your models here.


class ResourcesInLine(admin.TabularInline):
    model = LessonResources

class LessonAdmin(admin.ModelAdmin):
    form = LessonForm
    inlines = [
        ResourcesInLine,
    ]


admin.site.register(LessonSlot)
admin.site.register(TimetabledLesson)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonResources)
admin.site.register(LessonSuspension)