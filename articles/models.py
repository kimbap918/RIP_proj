from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models
from django.conf import settings 

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # image = ProcessedImageField(
    #     upload_to='images/', 
    #     blank=True,
    #     processors=[ResizeToFill(1200, 960)],
    #     format='JPEG',
    #     options={'quality': 80},
    # )
    like_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_post"
    )
    bookmark_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="bookmark_post"
    )

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    