from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from .models import *
from django.forms import ModelForm


class ProfileForm(ModelForm):
    class Meta:
        model = Profile()
        fields = ["intro"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User()
        fields = ["nickname"]
        labels = {
            "nickname": "닉네임",
        }
