from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Examlevel)
admin.site.register(Examboard)
admin.site.register(Syllabus)
admin.site.register(SyllabusTopic)
admin.site.register(SyllabusPoint)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Mark)
