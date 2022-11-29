from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models
from django.conf import settings 
from datetime import datetime, timedelta,timezone
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_post"
    )
    bookmark_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="bookmark_post"
    )
    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_comment")

    # @property
    # def created_string(self):
    #     time = datetime.now(tz=timezone.utc) - self.created

    #     if time < timedelta(minutes=1):
    #         return '방금 전'
    #     elif time < timedelta(hours=1):
    #         return str(int(time.seconds / 60)) + '분 전'
    #     elif time < timedelta(days=1):
    #         return str(int(time.seconds / 3600)) + '시간 전'
    #     elif time < timedelta(days=7):
    #         time = datetime.now(tz=timezone.utc).date() - self.created.date()
    #         return str(time.days) + '일 전'
    #     else:
    #         return False
    