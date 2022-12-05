from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.urls import reverse
from django.db import models
from django.conf import settings 
from datetime import datetime, timedelta,timezone
# Create your models here.
class CategorySelect(models.IntegerChoices):
    자유 = 0, '자유'
    유머 = 1, '유머'
    팬아트 = 2, '팬아트'
    유저찾기 = 3, '유저찾기'
    유저뉴스 = 4, '유저뉴스'
    팁과노하우 = 5, '팁과노하우'
    기획 = 6, '기획'
    사건사고 = 7, '사건사고'
    
# 카테고리 커스텀했을때 사용했음.
# class Category(models.Model):
#     title = models.CharField(max_length=255, default='자유')
#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse("articles:index")
        

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = ProcessedImageField(upload_to='images/', blank=True,null=True,
        processors=[ResizeToFill(100, 80)],
        format='JPEG',
        options={'quality': 80},)
    category = models.IntegerField(default=CategorySelect.자유,choices=CategorySelect.choices)
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
    def __str__(self):
        return self.title + ' | ' + str(self.user)
    
    def get_absolute_url(self):
        return reverse("articles:index")
    

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
    