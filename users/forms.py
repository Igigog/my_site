from django import forms
from .models import UserProfileData
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserProfileDataForm(forms.ModelForm):
    class Meta:
        model = UserProfileData
        fields = ('portfolio_site', 'profile_pic')
