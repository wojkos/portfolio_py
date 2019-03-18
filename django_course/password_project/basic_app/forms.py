from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfilefileInfo

class UserForm(form.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfilefileInfo
        fields = ('portfolio_site', 'profile_pic')