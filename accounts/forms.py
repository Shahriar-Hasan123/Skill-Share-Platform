from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "location", "website", "avatar"]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4}),
        }


