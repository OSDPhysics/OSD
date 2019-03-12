from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *
from tracker.forms import SetQuestions
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    form = SetQuestions

class QuestionsInLine(admin.TabularInline):
    model = Question
    form = SetQuestions

class ExamInLine(admin.ModelAdmin):
    inlines = [
        QuestionsInLine,
    ]


class SyllabusPointInLine(admin.TabularInline):
    model = SyllabusPoint


class SyllabusTopicAdmin(admin.ModelAdmin):
    inlines = [SyllabusPointInLine,]



class MarkInLine(admin.TabularInline):
    model = Mark


admin.site.register(Question)

admin.site.register(Examlevel)
admin.site.register(Examboard)
admin.site.register(Syllabus)
admin.site.register(SyllabusTopic, SyllabusTopicAdmin)
admin.site.register(SyllabusSubTopic)
admin.site.register(SyllabusPoint)
admin.site.register(Exam, ExamInLine)
#admin.site.register(Question)
admin.site.register(Mark)
admin.site.register(CSVDoc)
admin.site.register(Sitting)
admin.site.register(StudentPointRating)
admin.site.register(MPTTSyllabus, MPTTModelAdmin)
admin.site.register(MPTTRating)
admin.site.register(StandardisedData, MPTTModelAdmin)
admin.site.register(StandardisedResult)

#admin.site.register(PastStandardisedResult)
#admin.site.register(StandardisedTarget)