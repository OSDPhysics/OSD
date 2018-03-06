from django.contrib.auth.models import User
from django import forms
from .models import User, Teacher, Student


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class TeacherForm(forms.Form):
    TITLES = (
        ('Miss', 'Miss'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Mr', 'Mr'),
        ('Dr', 'Dr'),
    )

    # newteacher = {}
    # newteacher['last_name'] = forms.CharField(label='Surname', max_length=100)
    # newteacher['first_name'] = forms.CharField(label='Forename', max_length=100)
    # newteacher['title'] = forms.ChoiceField(choices='TITLES', label='Title')
    # newteacher['email'] = forms.EmailField()
    # newteacher['username'] = forms.CharField(label='Username', max_length=100)
    # newteacher['staffcode'] = forms.CharField(label='Staff code', max_length=4)
    # newteacher['password'] = forms.CharField(widget=forms.PasswordInput, label='Default Password', max_length=100)


    last_name = forms.CharField(label='Surname', max_length=100)
    first_name = forms.CharField(label='Forename', max_length=100)
    title = forms.ChoiceField(choices=TITLES, label='Title')
    email = forms.EmailField()
    username = forms.CharField(label='Username', max_length=100)
    staffcode = forms.CharField(label='Staff code', max_length=4)
    password = forms.CharField(widget=forms.PasswordInput, label='Default Password', max_length=100)


class UserDetails(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ()
