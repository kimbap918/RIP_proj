from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    birthday = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_length=100)
    agree = models.BooleanField(null=False, default=False)

# 마이페이지 프로필
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    intro = models.TextField(blank=True)  # 소개글

    def __str__(self):
        return self.email

