from django.contrib.auth.models import User
from django import forms
from .models import User, Teacher, Student

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('title', 'staffcode', 'user')

class UserDetails(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ()
