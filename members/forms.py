from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.safestring import mark_safe




class RegisterUserForm(UserCreationForm):
     
    class Meta:
        model = User
        fields = ('username','password1', 'password2')
	   

