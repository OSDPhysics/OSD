
from django import forms
from .models import *
from django.forms import formset_factory
from searchableselect.widgets import SearchableSelect


class CSVDetailsForm(forms.Form):
    topic = forms.ModelChoiceField(label='Topic', queryset=SyllabusTopic.objects.all())


class CSVDocForm(forms.ModelForm):
    class Meta:
        model = CSVDoc
        fields = ('description', 'document', )


class questionsForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ('',)
        widgets = {
            'syllabuspoint': SearchableSelect(model='tracker.SyllabusPoint', search_field='syllabusText', many=True, limit=10)
        }


class examForm(forms.ModelForm):
    class Meta:
        model = Exam
        exclude = ('',)