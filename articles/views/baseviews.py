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
def index(request):
    page = request.GET.get("page", "1")
    article = Article.objects.order_by("-created_at")
    kw = request.GET.get("kw", "")
    search_kind = request.GET.get("searchKind", "전체")
    sort = request.GET.get("sort", "")
    list1 = []
    for articles in article:
        if articles.top_fixed == True:
            list1.append(articles)
    # 추천순
    if sort == "1":
        article = (
            Article.objects.all()
            .annotate(like_cnt=Count("like_user"))
            .order_by("-like_cnt")
        )
    # 답글많은 순
    elif sort == "2":
        article = (
            Article.objects.all()
            .annotate(comments=Count("comment"))
            .order_by("-comments")
        )
    elif sort == "3":
        article = user.article_set.all()
    # 내가 와드 한 글
    elif sort == "4":
        article = user.bookmark_post.all()
    # 내가 좋아요 한 글
    elif sort == "5":
        article = user.like_post.all()
    if kw:
        if search_kind == "전체":
            article = article.filter(
                Q(title__icontains=kw)
                | Q(content__icontains=kw)  # 제목 검색
                | Q(user__username__icontains=kw)  # 내용 검색
            ).distinct()  # 질문 글쓴이 검색
        elif search_kind == "제목":
            article = article.filter(Q(title__icontains=kw)).distinct()  # 제목 검색
        elif search_kind == "내용":
            article = article.filter(Q(content__icontains=kw)).distinct()  # 내용 검색
        elif search_kind == "작성자":
            article = article.filter(
                Q(user__username__icontains=kw)  # 내용 검색
            ).distinct()
    if request.user.is_authenticated:
        user = get_user_model().objects.get(pk=request.user.pk)
    paginator = Paginator(article, 10)
    page_obj = paginator.get_page(page)
    categories = ["자유", "유머", "팬아트", "유저찾기", "유저뉴스", "팁과노하우", "기획", "사건사고"]
    
    context = {
        "sort": sort,
        "article": page_obj,
        "page": page,
        "categories": categories,
        "kw": kw,
        "top_fixed": list1,
    }

    return render(request, "articles/index.html", context)

def category(request, pk):
    sort = request.GET.get("sort", "")
    page = request.GET.get("page", "1")
    article = Article.objects.filter(category=pk)
    kw = request.GET.get("kw", "")
    search_kind = request.GET.get("searchKind", "전체")
    # 추천순
    if sort == "1":
        article = (
            Article.objects.filter(category=pk)
            .annotate(like_cnt=Count("like_user"))
            .order_by("-like_cnt")
        )
    # 답글많은 순
    elif sort == "2":
        article = (
            Article.objects.filter(category=pk)
            .annotate(comments=Count("comment"))
            .order_by("-comments")
        )
    # 내가 쓴 글
    elif sort == "3":
        user = get_user_model().objects.get(pk=request.user.pk)
        article = user.article_set.all()
    # 내가 와드 한 글
    elif sort == "4":
        user = get_user_model().objects.get(pk=request.user.pk)
        article = user.bookmark_post.all()
    # 내가 좋아요 한 글
    elif sort == "5":
        user = get_user_model().objects.get(pk=request.user.pk)
        article = user.like_post.all()

    if kw:
        if search_kind == "전체":
            article = article.filter(
                Q(title__icontains=kw)
                | Q(content__icontains=kw)  # 제목 검색
                | Q(user__username__icontains=kw)  # 내용 검색
            ).distinct()  # 질문 글쓴이 검색
        elif search_kind == "제목":
            article = article.filter(Q(title__icontains=kw)).distinct()  # 제목 검색
        elif search_kind == "내용":
            article = article.filter(Q(content__icontains=kw)).distinct()  # 내용 검색
        elif search_kind == "작성자":
            article = article.filter(
                Q(user__username__icontains=kw)  # 내용 검색
            ).distinct()
    paginator = Paginator(article, 10)
    page_obj = paginator.get_page(page)
    categories = ["자유", "유머", "팬아트", "유저찾기", "유저뉴스", "팁과노하우", "기획", "사건사고"]
    category_name = categories[pk]
    context = {
        "sort": sort,
        "pk": pk,
        "article": page_obj,
        "categories": categories,
        "category_name": category_name,
        "page": page,
        "kw": kw,
    }
    return render(request, "articles/category.html", context)
