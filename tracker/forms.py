
from django import forms
from .models import *


class CSVDetailsForm(forms.Form):
    topic = forms.ModelChoiceField(label='Topic', queryset=SyllabusTopic.objects.all())


class CSVDocForm(forms.ModelForm):
    class Meta:
        model = CSVDoc
        fields = ('description', 'document', )

