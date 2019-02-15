from django import forms
from dal import autocomplete
from django.forms.widgets import CheckboxSelectMultiple
from tracker.models import SyllabusPoint, Syllabus, MPTTSyllabus
from school.models import ClassGroup
from mptt.forms import TreeNodeMultipleChoiceField

from timetable.models import Lesson, LessonResources


class LessonForm(forms.ModelForm):
    syllabus_points = TreeNodeMultipleChoiceField(queryset=MPTTSyllabus.objects.all(), widget=CheckboxSelectMultiple)

    class Meta:
        model = Lesson
        fields = ["lesson_title",  'syllabus', 'description', 'requirements', ]

        # widgets = {
        #     'syllabus_points_covered': autocomplete.ModelSelect2Multiple(
        #                                                                   url='tracker:syllabus-autocomplete2',
        #                                                                   forward=('syllabus',))
        # }

        widgets = {
            'mptt_syllabus_points': CheckboxSelectMultiple()
        }

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
        )


class LessonCopyForm(forms.Form):
    classgroup = forms.ModelChoiceField(ClassGroup.objects.all(),
                                        widget=autocomplete.ModelSelect2(url='tracker:classgroups-autocomplete'),
                                        )
    lesson_to_copy_to = forms.ModelChoiceField(Lesson.objects.all(),
                                               widget=autocomplete.ModelSelect2(url='tracker:lesson_autocomplete',
                                                                               forward=('classgroup', )))

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
        )


class LessonResourceForm(forms.ModelForm):
    """ Resource linked to a particular lesson """
    class Meta:
        model = LessonResources
        fields = {'resource_type',
                  'resource_name',
                  'link',
                  'students_can_view_before',
                  'students_can_view_after',
                  'available_to_all_classgroups',
                  }


class ResourceNoLessonForm(forms.Form):

    """ Resource that can be viewed by all students, not linked to a lesson """

    class Meta:
        model = LessonResources
        fields = {'resource_type',
                  'resource_name',
                  'link',
                  }

class AddLessonSuspensions(forms.Form):

    reason = forms.CharField(max_length=100, required=True)
    all_classgroups = ClassGroup.objects.all()
    start_date = forms.DateField(label='Start date', widget=forms.SelectDateWidget(years=(2018, 2019, 2020)))
    end_date = forms.DateField(label = 'End date', widget=forms.SelectDateWidget(years=(2018, 2019, 2020)))
    whole_school = forms.BooleanField(label = 'Whole school?', required=False)
    classgroups = forms.ModelMultipleChoiceField(widget=autocomplete.ModelSelect2Multiple(url='tracker:classgroups-autocomplete'), queryset=all_classgroups, required=False)
