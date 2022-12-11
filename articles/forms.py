from django.forms import ModelForm
from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget

# choices = Category.objects.all().values_list('title','title')

# choice_list = []

# for item in choices:
#     choice_list.append(item)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "photo", "category", "top_fixed"]
        labels = {
            "title": "제목",
            "content": "내용",
            "photo": "이미지",
        }
        widgets = {
            "content": SummernoteWidget(
                attrs={"summernote": {"width": "100%", "height": "400px"}}
            ),
            # 'category':forms.Select(choices=choice_list)
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
        labels = {"content": "바르고 고운 말을 사용하세요! 댓글은 당신의 얼굴입니다."}

class ReportForm(forms.ModelForm):
    class Meta:
        model = Reported
        fields = [
            'category','content'
        ]