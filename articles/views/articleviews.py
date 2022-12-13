from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import *
from ..models import *
from accounts.models import *
from django.http import JsonResponse, HttpResponseForbidden
from django.views.generic import ListView
from django.contrib.auth import get_user_model

# Create your views here.
# 게시물 생성
# @login_required(login_url='accounts:login')
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/create.html", context)


# 게시물 수정
# @login_required(login_url='accounts:login')
def article_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # if request.user != article.author:
    #     message.error(request,'수정권한이 없습니다.')
    #     return redirect('articles:detail',pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect("articles:index")
    else:
        form = ArticleForm(instance=article)
    context = {"form": form}
    return render(request, "articles/update.html", context)


# def main(request):
#     return render(request, "articles/main.html")

# 게시물 디테일
def article_detail(request, pk):
    # 특정 글을 가져온다.
    article = get_object_or_404(Article, pk=pk)
    # user = User.objects.get(pk=request.user.id)
    # user_articles = user.article_set.all()
    article_form = ArticleForm()
    comments_form = CommentForm()
    report_form = ReportForm()
    comments = Comment.objects.filter(article_id=pk).order_by("-created_at")
    # template에 객체 전달

    grade = ''
    if request.user.is_authenticated:
        user = get_user_model().objects.get(pk=request.user.pk)
        article_set = user.article_set.all()
        comment_set = user.comment_set.all()
        a_count = article_set.count()
        c_count = comment_set.count()

        if c_count > 20 and a_count > 10:
            grade = '썩은물'
        elif c_count > 10 and a_count > 4:
            grade = '고인물'
        elif c_count > 2 and a_count > 2:
            grade = '탁한물'
        elif c_count > 2 or a_count > 0:
            grade = '맑은물'
        elif c_count <= 2 or a_count == 0:
            grade = '신선한물'
            
    context = {
        "article": article,
        # 역참조 (articles에 포함된 comments data를 전부 불러온다.)
        "articles_form": article_form,
        "comments_form": comments_form,
        "report_form": report_form,
        "comments": comments,
        "categories": ["자유", "유머", "팬아트", "유저찾기", "유저뉴스", "팁과노하우", "기획", "사건사고"],
        # "user_articles":user_articles,
        # "user":user,
        "grade" : grade,
    }
    return render(request, "articles/detail.html", context)


# 게시물 삭제
def article_delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        if request.user == article.user:
            article.delete()
            messages.success(request, "삭제되었습니다.")
    return redirect("articles:index")


# 게시글 좋아요
def like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user in article.like_user.all():
        article.like_user.remove(request.user)
        is_liked = False
    else:
        article.like_user.add(request.user)
        is_liked = True
    context = {"isLiked": is_liked, "likeCount": article.like_user.count()}
    return JsonResponse(context)


@login_required
def article_report(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        messages.warning(request, "스스로 신고 할수 없습니다.")
        return redirect("articles:detail", pk)
    else:
        article.report.add(request.user)
        messages.success(request, "신고완료")
    return redirect("articles:detail", pk)


# 게시물 북마크
def bookmark(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 만약에 로그인한 유저가 이 글을 북마크를 눌렀다면,
    # if answer.like_users.filter(id=request.user.id).exists():
    if request.user in article.bookmark_user.all():
        # 북마크 삭제하고
        article.bookmark_user.remove(request.user)
        isBookmark = False
    else:
        # 북마크 추가하고
        article.bookmark_user.add(request.user)
        isBookmark = True
    # 상세 페이지로 redirect
    context = {"isBookmark": isBookmark, "bookMarkCount": article.bookmark_user.count()}
    print(context)
    return JsonResponse(context)
