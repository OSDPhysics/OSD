from dal import autocomplete
from tracker.models import SyllabusPoint, Syllabus
from school.models import ClassGroup
from timetable.models import Lesson
from django import forms
from dal import forward

class LessonForm(forms.ModelForm):
    syllabus = forms.ModelChoiceField(queryset=Syllabus.objects.all(),
                                      widget=autocomplete.ModelSelect2(
                                          url='tracker:syllabus-autocomplete'))

    syllabus_points_covered = forms.ModelMultipleChoiceField(queryset=SyllabusPoint.objects.all(),
                                            widget=autocomplete.ModelSelect2Multiple(url='tracker:syllabus-autocomplete2',
                                                                                     forward=('syllabus',)))


class LessonCopyForm(forms.Form):
    classgroup = forms.ModelChoiceField(ClassGroup.objects.all(),
                                        widget=autocomplete.ModelSelect2(url='tracker:classgroups-autocomplete'))
    lesson_to_copy_to = forms.ModelChoiceField(Lesson.objects.all())

