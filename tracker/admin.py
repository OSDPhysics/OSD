from django.contrib import admin
from django import forms
from searchableselect.widgets import SearchableSelect



# Register your models here.


from .models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ()

        widgets = {
            'syllabuspoint': SearchableSelect(model='tracker.SyllabusPoint', search_field='syllabusText', many=True,
                                              limit=10)
        }


class QuestionInline(admin.TabularInline):
    model = Question

    class Meta:
        widgets = {
                'syllabuspoint': SearchableSelect(model='tracker.SyllabusPoint', search_field='syllabusText', many=True,
                                                  limit=10)
                 }

class ExamInLine(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]


class MarkInLine(admin.TabularInline):
    model = Mark




class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm

admin.site.register(Question)

admin.site.register(Examlevel)
admin.site.register(Examboard)
admin.site.register(Syllabus)
admin.site.register(SyllabusTopic)
admin.site.register(SyllabusPoint)
admin.site.register(Exam, ExamInLine)
#admin.site.register(Question)
admin.site.register(Mark)
admin.site.register(CSVDoc)
admin.site.register(Sitting)