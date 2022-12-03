from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display  = ('title', 'created_at', 'updated_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)