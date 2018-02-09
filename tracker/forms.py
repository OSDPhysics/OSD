from django import forms
from django.contrib.auth.models import User

from .models import Teacher

class TeacherForm(forms.ModelForm):


    class Meta:
        model = Teacher
        fields = ('title', 'staffcode', 'user')

class UserDetails(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
