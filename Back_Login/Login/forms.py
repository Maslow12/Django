from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import ModelForm
from django.forms import PasswordInput
from Register.models import User

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username']
        self.fields['password']
        class Meta:
            model = User
            fields = ['username', 'password']