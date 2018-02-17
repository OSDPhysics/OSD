from django import forms

from .models import User, Teacher, Student

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ()

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ()



