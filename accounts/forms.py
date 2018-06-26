from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignUp(UserCreationForm):
	profile_pic = forms.FileField(help_text='jpg,png')

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name','email','password1','password2','profile_pic',]

class UserEdit(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name','email',]
		exclude = ['username','password1','password2',]

class ProfileEdit(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['profile_pic',]