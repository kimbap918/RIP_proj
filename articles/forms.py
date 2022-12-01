from django.forms import ModelForm
from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content','photo','category']
        labels = {
            'title': '제목',
            'content': '내용',
            'photo': '이미지',
        }
        widgets = {
            'content': SummernoteWidget(attrs={'summernote':{'width':'100%','height':'400px'}})
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content',]
        labels = {
            'content': '바르고 고운 말을 사용하세요! 댓글은 당신의 얼굴입니다.'
        }