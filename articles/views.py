from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from email import message
from .forms import *
from .models import *
# Create your views here.

# index (test용)
def index(request):
    article = Article.objects.order_by('-created_at')
    context = {
        'article': article
        }
    return render(request,'articles/index.html',context)

# 게시물 생성
# @login_required(login_url='accounts:login')
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

# 게시물 수정
# @login_required(login_url='accounts:login')
def article_update(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    # if request.user != article.author:
    #     message.error(request,'수정권한이 없습니다.')
    #     return redirect('articles:detail',pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)
    context = {
        'form':form
    }
    return render(request, 'articles/create.html', context)

def main(request):
    return render(request, "articles/main.html")

# articles 삭제
def article_detail(request, pk):
    # 특정 글을 가져온다.
    articles = get_object_or_404(articles, pk=pk)
    articles_form = ArticleForm()

    # template에 객체 전달
    context = {
        "articles": articles,
        # 역참조 (articles에 포함된 articles data를 전부 불러온다.)
        "articles": articles.articles_set.all(),
        "articles_form": articles_form,
    }
    return render(request, "articles/detail.html", context)


def article_delete(request, pk):
    Article.objects.get(pk=pk).delete()

    return redirect('articles:delete')