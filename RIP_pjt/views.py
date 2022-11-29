from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponseForbidden
from articles.models import *
def main(request):
    return render(request, "main.html")

def base(request):
    return render(request, 'base.html')

def home(request):
    # 게시물 최근 순
    lately_a = Article.objects.order_by("-pk")[:4]
    # 게시물 좋아요 순
    # 에러 'Article' object has no attribute 'like_users'
    # best_a = Article.objects.all()
    # best_a = sorted(best_a, key=lambda a: -a.like_users.count())[:4]
    context = {
        "lately_a": lately_a,
        # "best_a": best_a,
    }
    return render(request, "home.html", context)