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
            'content': SummernoteWidget(attrs={'summernot':{'width':'100%','height':'400px'}})
        }