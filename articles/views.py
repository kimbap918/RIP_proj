from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from email import message
from .forms import *
from .models import *
from django.http import JsonResponse,HttpResponseForbidden
from django.http import JsonResponse
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

# 게시물 디테일
def article_detail(request, pk):
    # 특정 글을 가져온다.
    article = get_object_or_404(Article, pk=pk)
    article_form = ArticleForm()
    comments_form = CommentForm()
    comments = Comment.objects.filter(article_id=pk).order_by("-created_at")
    # template에 객체 전달
    context = {
        "article": article,
        # 역참조 (articles에 포함된 comments data를 전부 불러온다.)
        "articles_form": article_form,
        "comments_form": comments_form,
        "comments": comments,
    }
    return render(request, "articles/detail.html", context)

# 게시물 삭제
def article_delete(request, article_pk):
    Article.objects.get(pk=article_pk).delete()

    return redirect('articles:index')

# 댓글 생성
def comment_create(request, pk):
    print(request.POST)
    article = get_object_or_404(Article, pk=pk)
    # 위에서 선언된 article의 pk값 저장
    article_pk = article.pk
    # 요청 유저의 pk값 저장
    user = request.user.pk

    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    # 맨 마지막에 생성된 댓글순으로 comment정보를 저장
    temp = Comment.objects.filter(article_id=pk).order_by("-created_at")
    # 저장된 comment를 담을 리스트
    comment_data = []

    # temp에서 순회하면서 유저의 id, 댓글의 pk, 내용, 생성일자, 닉네임을 각각 comment_data에 담음 
    for t in temp:
        t.created_at = t.created_at.strftime("%Y-%m-%d %H:%M")
        comment_data.append(
            {
                "user_id": t.user_id,
                "commentPK": t.pk,
                "content": t.content,
                "created_at": t.created_at,
                "profile_name": t.user.nickname,
            }
        )
    # context(data)에 commentData, article의 pk, 요청유저의 pk를 담아서
    data = {
        "commentData": comment_data,
        "articlePK": article_pk,
        "user": user
    }
    # json으로 리턴
    return JsonResponse(data)
    #return redirect("articles:detail", pk)

# 댓글 삭제
def comment_delete(request, comment_pk, pk): # 마지막에 특정 리뷰에 대한 pk가 필요함
    comment = Comment.objects.get(pk=comment_pk)
    if request.user.is_authenticated and request.user == comment.user:
        comment.delete()
        return redirect("articles:detail", pk)

# 게시글 좋아요
def like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 만약에 로그인한 유저가 이 글을 좋아요를 눌렀다면,
    # if article.like_users.filter(id=request.user.id).exists():
    if request.user in article.like_users.all(): 
        # 좋아요 삭제하고
        article.like_users.remove(request.user)
        is_liked = False
    else:
        # 좋아요 추가하고 
        article.like_users.add(request.user)
        is_liked = True
    # 상세 페이지로 redirect
    context = {'isLiked': is_liked, 'likeCount': article.like_users.count()}
    return JsonResponse(context)

# 댓글 좋아요
def comment_like(request, review_pk, comment_pk):
    is_like = False
    temp = Comment.objects.filter(review_id=review_pk)
    for i in temp:
        if i.pk == comment_pk:
            if request.user not in i.like_users.all():
                i.like_users.add(request.user)
                is_like = True
            else:
                i.like_users.remove(request.user)
                is_like = False
            data = {
                "review.pk": review_pk,
                "comment_pk": comment_pk,
                "isLike": is_like,
            }
            return JsonResponse(data)


# 게시물 북마크
def bookmark(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 만약에 로그인한 유저가 이 글을 북마크를 눌렀다면,
    # if answer.like_users.filter(id=request.user.id).exists():
    if request.user in article.bookmark_users.all():
        # 북마크 삭제하고
        article.bookmark_users.remove(request.user)
        is_bookmark = False
    else:
        # 북마크 추가하고
        article.bookmark_users.add(request.user)
        is_bookmark = True
    # 상세 페이지로 redirect
    data = {"is_bookmark": is_bookmark,}
    return JsonResponse(data)