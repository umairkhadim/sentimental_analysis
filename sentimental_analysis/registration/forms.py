from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelformset_factory


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,)

    class Meta:
        model = User
        fields = ['username', 'password']

