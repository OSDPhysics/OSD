from django import forms

from .models import Post

class UserForm(forms.ModelForm):
        class Meta:
        model = Post
        fields = ('title', 'text',)