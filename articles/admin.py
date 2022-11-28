from django.contrib import admin
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display  = ('title', 'created_at', 'updated_at')
# Register your models here.
admin.site.register(Article, ArticleAdmin)