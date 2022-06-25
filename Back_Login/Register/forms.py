from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):
	#email = forms.EmailField(required=True)
	#bio = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), max_length=500, required=False)
	#image = forms.ImageField(required=False)
	class Meta:
		model = get_user_model()
		fields = ['username', 'password1', 'email']