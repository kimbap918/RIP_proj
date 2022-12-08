from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from articles.models import *
from accounts.models import *
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


def main(request):
    # if request.user.is_anonymous:
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect("home")

    else:
        login_form = AuthenticationForm()

    context = {
        "login_form": login_form,
    }
    return render(request, "main.html", context)


def base(request):
    return render(request, 'base.html')


def home(request):
    # 게시물 최근 순
    lately_a = Article.objects.order_by("-pk")[:10]
    # 게시물 좋아요 순
    # 에러 'Article' object has no attribute 'like_users'
    # best_a = Article.objects.all()
    # best_a = sorted(best_a, key=lambda a: -a.like_users.count())[:10]
    context = {
        "lately_a": lately_a,
        # "best_a": best_a,
    }
    return render(request, "home.html", context)
