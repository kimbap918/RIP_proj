from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    birthday = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_length=100)
    agree = models.BooleanField(null=False, default=False)
    nickname = models.CharField(max_length=10, default='')
    
