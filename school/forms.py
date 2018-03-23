from django import forms
from school.models import *

class TeacherForm(forms.Form):
    last_name = forms.CharField(label='Surname', max_length=100)
    first_name = forms.CharField(label='Forename', max_length=100)
    title = forms.ChoiceField(choices=Teacher.TITLES, label='Title')
    email = forms.EmailField()
    username = forms.CharField(label='Username', max_length=100)
    staffcode = forms.CharField(label='Staff code', max_length=4)
    password = forms.CharField(widget=forms.PasswordInput, label='Default Password', max_length=100)




class CSVDocForm(forms.ModelForm):
    class Meta:
        model = CSVDoc
        fields = ('description', 'document', )

