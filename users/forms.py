from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        #particular user gets affected
        model=User
        #order of contents in the form
        fields=['username','email','password1','password2']

#updating username and email
class UserUpdateForm(forms.ModelForm):
        email=forms.EmailField()

        class Meta:
            #model to work with
            model=User
            fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']