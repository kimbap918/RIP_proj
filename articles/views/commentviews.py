from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import *
from ..models import *
from accounts.models import *
from django.http import JsonResponse, HttpResponseForbidden
# Create your views here.

# 댓글 생성
def comment_create(request, pk):
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
                "profile_name": t.user.username,
            }
        )
    # context(data)에 commentData, article의 pk, 요청유저의 pk를 담아서
    data = {"commentData": comment_data, "articlePK": article_pk, "user": user}
    # json으로 리턴
    return JsonResponse(data)
    # return redirect("articles:detail", pk)


# 댓글 삭제
def comment_delete(request, pk, comment_pk):
    # article의 pk값 저장
    article_pk = Article.objects.get(pk=pk).pk
    # 요청 유저의 pk값 저장
    user = request.user.pk
    comment = Comment.objects.get(pk=comment_pk)

    if comment.user == request.user:
        comment.delete()

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
                "profile_name": t.user.username,
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




# 댓글 좋아요
def comment_like(request, article_pk, comment_pk):
    temp = Comment.objects.filter(article_id=article_pk)
    for i in temp:
        if i.pk == comment_pk:
            if request.user not in i.like_user.all():
                i.like_user.add(request.user)
                is_like = True
            else:
                i.like_user.remove(request.user)
                is_like = False
            data = {
                "article_pk": article_pk,
                "comment_pk": comment_pk,
                "isLike": is_like,
                'likeCount': i.like_user.count()
            }
            # print(data)
            return JsonResponse(data)