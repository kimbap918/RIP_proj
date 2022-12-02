from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from ..forms import *
from ..models import *
from accounts.models import *
from django.http import HttpResponseForbidden
from django.db.models import Q, Avg, Count
# Create your views here.

# index 
def index(request):
    # 추천순
    sort = request.GET.get('sort','')
    if sort == '1':
        page = request.GET.get("page", "1")
        article = Article.objects.all().annotate(like_cnt=Count('like_user')).order_by('-like_cnt')
        paginator = Paginator(article, 20)
        page_obj = paginator.get_page(page)
        context = {"article": page_obj}
        return render(request,"articles/index.html",context)
    # 답글많은 순
    elif sort == '2':
        page = request.GET.get("page", "1")
        article = Article.objects.all().annotate(comments=Count('comment')).order_by('-comments')
        paginator = Paginator(article, 20)
        page_obj = paginator.get_page(page)
        context = {"article": page_obj}
        return render(request,"articles/index.html",context)
    # 내가 쓴 글
    elif sort == '3':
        user = get_user_model().objects.get(pk=request.user.pk)
        page = request.GET.get("page", "1")
        article = user.article_set.all()
        paginator = Paginator(article, 20)
        page_obj = paginator.get_page(page)
        context = {"article": page_obj}
        return render(request,"articles/index.html",context)
    # 내가 와드 한 글
    elif sort == '4':
        user = get_user_model().objects.get(pk=request.user.pk)
        page = request.GET.get("page", "1")
        article = user.bookmark_post.all()
        paginator = Paginator(article, 20)
        page_obj = paginator.get_page(page)
        context = {"article": page_obj}
        return render(request,"articles/index.html",context)
    # 내가 좋아요 한 글
    elif sort == '5':
        user = get_user_model().objects.get(pk=request.user.pk)
        page = request.GET.get("page", "1")
        article = user.like_post.all()
        paginator = Paginator(article, 20)
        page_obj = paginator.get_page(page)
        context = {"article": page_obj}
        return render(request,"articles/index.html",context)
    # 자유
    elif sort == '6':
        page = request.GET.get("page", "1")
        article = Article.objects.filter(category=1).order_by('-created_at')
        paginator = Paginator(article, 20)
        page_obj = paginator.get_page(page)
        context = {"article": page_obj}
        return render(request,"articles/index.html",context)
    # 유머
    elif sort == '7':
        page = request.GET.get("page", "1")
        article = Article.objects.filter(category=2).order_by('-created_at')
        paginator = Paginator(article, 20)
        page_obj = paginator.get_page(page)
        context = {"article": page_obj}
        return render(request,"articles/index.html",context)
    # 팬아트
    elif sort == '8':
        page = request.GET.get("page", "1")
        article = Article.objects.filter(category=3).order_by('-created_at')
        paginator = Paginator(article, 20)
        page_obj = paginator.get_page(page)
        context = {"article": page_obj}
        return render(request,"articles/index.html",context)
    # 유저찾기
    elif sort == '9':
        page = request.GET.get("page", "1")
        article = Article.objects.filter(category=4).order_by('-created_at')
        paginator = Paginator(article, 20)
        page_obj = paginator.get_page(page)
        context = {"article": page_obj}
        return render(request,"articles/index.html",context)
    # 유저뉴스
    elif sort == '10':
        page = request.GET.get("page", "1")
        article = Article.objects.filter(category=5).order_by('-created_at')
        paginator = Paginator(article, 20)
        page_obj = paginator.get_page(page)
        context = {"article": page_obj}
        return render(request,"articles/index.html",context)
    # 팁과 노하우
    elif sort == '11':
        page = request.GET.get("page", "1")
        article = Article.objects.filter(category=6).order_by('-created_at')
        paginator = Paginator(article, 20)
        page_obj = paginator.get_page(page)
        context = {"article": page_obj}
        return render(request,"articles/index.html",context)
    # 기획
    elif sort == '12':
        page = request.GET.get("page", "1")
        article = Article.objects.filter(category=7).order_by('-created_at')
        paginator = Paginator(article, 20)
        page_obj = paginator.get_page(page)
        context = {"article": page_obj}
        return render(request,"articles/index.html",context)
    # 사건 사고
    elif sort == '13':
        page = request.GET.get("page", "1")
        article = Article.objects.filter(category=8).order_by('-created_at')
        paginator = Paginator(article, 20)
        page_obj = paginator.get_page(page)
        context = {"article": page_obj}
        return render(request,"articles/index.html",context)
    else:
        page = request.GET.get("page", "1")
        article = Article.objects.order_by("-created_at")
        paginator = Paginator(article, 20)
        page_obj = paginator.get_page(page)
        context = {"article": page_obj}
        return render(request, "articles/index.html", context)