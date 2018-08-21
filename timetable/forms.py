from django import forms
from dal import autocomplete
from tracker.models import SyllabusPoint, Syllabus
from school.models import ClassGroup

from timetable.models import Lesson


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ["lesson_title", 'sequence', 'status', 'syllabus', 'syllabus_points_covered', 'description', 'requirements', 'lesson']

        widgets = {
            'syllabus_points_covered': autocomplete.ModelSelect2Multiple(
                                                                          url='tracker:syllabus-autocomplete2',
                                                                          forward=('syllabus',))
        }

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
        )


class LessonCopyForm(forms.Form):
    classgroup = forms.ModelChoiceField(ClassGroup.objects.all(),
                                        widget=autocomplete.ModelSelect2(url='tracker:classgroups-autocomplete'))
    lesson_to_copy_to = forms.ModelChoiceField(Lesson.objects.all())
