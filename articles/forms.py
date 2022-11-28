from django.forms import ModelForm
from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content']
        labels = {
            'title': '제목',
            'content': '내용',
        }
        widgets = {
            'content': SummernoteWidget(attrs={'summernote':{'width':'100%','height':'400px'}})
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content',]