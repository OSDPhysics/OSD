from django.contrib import admin
from .models import *
from django import forms
from searchableselect.widgets import SearchableSelect
from mptt.admin import MPTTModelAdmin

from.models import Skill
# Register your models here.


admin.site.register(TutorGroup)
admin.site.register(ClassGroup)
admin.site.register(Student)
admin.site.register(AcademicStructure, MPTTModelAdmin)
admin.site.register(PastoralStructure, MPTTModelAdmin)


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ()

        widgets = {
            'skills': SearchableSelect(model='teachnet.Skill', search_field='skill_name', many=True,
                                              limit=10)
        }


class TeacherAdmin(admin.ModelAdmin):
    form = TeacherForm


admin.site.register(Teacher, TeacherAdmin)