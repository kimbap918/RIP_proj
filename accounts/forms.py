from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from .models import *
from django.forms import ModelForm


class DateInput(forms.DateInput):
    input_type = "Date"


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "birthday",
            "agree",
            "nickname",
        )
        widgets = {"birthday": DateInput()}


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User()
        fields = ["nickname"]
        labels = {
            "nickname": "닉네임",
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile()
        fields = ["intro"]
