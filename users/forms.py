from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        #particular user gets affected
        model=User
        #order of contents in the form
        fields=['username','email','password1','password2']
