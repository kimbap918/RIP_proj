import random
import requests
from django.shortcuts import render, redirect, get_object_or_404
# from articles.models import Grade
from .forms import CustomUserCreationForm, ProfileForm
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail.message import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
)
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.shortcuts import resolve_url

UserModel = get_user_model()
INTERNAL_RESET_URL_TOKEN = "set-password"
INTERNAL_RESET_SESSION_TOKEN = "_password_reset_token"


# Create your views here.
def login(request):
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
    print(context)
    return render(request, "accounts/login.html", context)


# else:
#    return HttpResponseRedirect("")


def logout(request):
    auth_logout(request)
    return redirect("main")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # 프로필 생성
            auth_login(
                request, user, backend="django.contrib.auth.backends.ModelBackend"
            )
            return redirect("main")

    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    articles = user.article_set.all()
    like_articles = user.like_post.all()
    bookmark_articles = user.bookmark_post.all()
    grade = ''

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
        "grade":grade,
        "user": user,
        "articles": articles,
        "like_articles": like_articles,
        "bookmark_articles": bookmark_articles,
    }
    return render(request, "accounts/detail.html", context)


# 마이 페이지 (회원 정보로 이동, 비밀번호 변경, 로그아웃, 회원탈퇴)
@login_required
def mypage(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    articles = user.article_set.all()
    like_articles = user.like_post.all()
    bookmark_articles = user.bookmark_post.all()

    # 업데이트
    if request.user.profile:
        profile = request.user.profile

        if request.method == "POST":
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
            change_form = CustomUserChangeForm(request.POST, instance=user)

            if profile_form.is_valid() and change_form.is_valid():
                profile_form.save()
                change_form.save()
                # return redirect('accounts:detail', request.user.pk)
                return redirect("accounts:mypage", request.user.pk)
        else:
            profile_form = ProfileForm(instance=profile)
            change_form = CustomUserChangeForm(instance=user)

    # 최초 생성
    else:
        if request.method == "POST":
            profile_form = ProfileForm(request.POST, request.FILES)
            change_form = CustomUserChangeForm(request.POST, instance=user)

            if profile_form.is_valid() and change_form.is_valid():
                profile_form.save()
                change_form.save()
                # return redirect('accounts:detail', request.user.pk)
                return redirect("accounts:mypage", request.user.pk)

        else:
            profile_form = ProfileForm
            change_form = CustomUserChangeForm(instance=user)

    context = {
        "profile_form": profile_form,
        "change_form": change_form,
        "user": user,
        "articles": articles,
        "like_articles": like_articles,
        "bookmark_articles": bookmark_articles,
    }

    return render(request, "accounts/mypage.html", context)


# 비밀번호 변경
@login_required
def password(request, user_pk):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # 로그인 유지
            return redirect("accounts:mypage", user_pk)

    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }

    return render(request, "accounts/password.html", context)


# 회원 탈퇴


def pre_delete(request, user_pk):
    return render(request, "accounts/pre_delete.html")


def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)

    return redirect("articles:index")


# 회원 프로필 (프로필 사진, 소개글) (+ 닉네임?)
@login_required
def update(request, pk):
    user = get_user_model().objects.get(pk=pk)
    articles = user.article_set.all()
    like_articles = user.like_post.all()
    bookmark_articles = user.bookmark_post.all()

    # 업데이트
    if request.user.profile:
        profile = request.user.profile

        if request.method == "POST":
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
            change_form = CustomUserChangeForm(request.POST, instance=user)

            if profile_form.is_valid() and change_form.is_valid():
                profile_form.save()
                change_form.save()
                # return redirect('accounts:detail', request.user.pk)
                return redirect("accounts:update", request.user.pk)
        else:
            profile_form = ProfileForm(instance=profile)
            change_form = CustomUserChangeForm(instance=user)

    # 최초 생성
    else:
        if request.method == "POST":
            profile_form = ProfileForm(request.POST, request.FILES)
            change_form = CustomUserChangeForm(request.POST, instance=user)

            if profile_form.is_valid() and change_form.is_valid():
                profile_form.save()
                change_form.save()
                # return redirect('accounts:detail', request.user.pk)
                return redirect("accounts:update", request.user.pk)

        else:
            profile_form = ProfileForm
            change_form = CustomUserChangeForm(instance=user)

    context = {
        "profile_form": profile_form,
        "change_form": change_form,
        "user": user,
        "articles": articles,
        "like_articles": like_articles,
        "bookmark_articles": bookmark_articles,
    }

    return render(request, "accounts/update.html", context)

    # 최초 생성
    # else:
    # if request.method == "POST":
    #     profile_form = ProfileForm(request.POST, request.FILES)
    #     change_form = CustomUserChangeForm(request.POST, instance=user)

    #     if profile_form.is_valid() and change_form.is_valid():
    #         profile_form.save()
    #         change_form.save()
    #         # return redirect('accounts:detail', request.user.pk)
    #         return redirect("accounts:mypage", request.user.pk)

    # else:
    #     profile_form = ProfileForm()
    #     change_form = CustomUserChangeForm(instance=user)


@login_required
def report(request, pk):
    # 프로필에 해당하는 유저를 로그인한 유저가!
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.user == user:
        messages.warning(request, "스스로 신고 할 수 없습니다.")
        return redirect("accounts:detail", pk)
    if request.user in user.reported.all():
        messages.warning(request, "이미 신고한 게시글입니다.")
    else:
        user.reported.add(request.user)
    return redirect("accounts:detail", pk)


def send_email(request):
    subject = "RIP.gg 비밀번호 재설정"
    message = render_to_string("password_reset_email.html")
    send_email = EmailMessage(subject, message)
    send_email.send()


def member(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # 프로필 생성
            auth_login(
                request, user, backend="django.contrib.auth.backends.ModelBackend"
            )
            return redirect("main")

    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/member.html", context)


@login_required
def articles(request, pk):
    articles = all.Articles.objects.filter(user=request.user).order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "accounts/articles.html", context)


import secrets

state_token = secrets.token_urlsafe(16)


def kakao_request(request):
    kakao_api = "https://kauth.kakao.com/oauth/authorize?"
    redirect_uri = "http://ripggbean-env.eba-tprx3bfx.ap-northeast-2.elasticbeanstalk.com/accounts/login/kakao/callback"
    client_id = "39c09c3e2d2a0741405cf64373d6a60a"  # # rest_api_key
    return redirect(
        f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
    )


def kakao_callback(request):
    data = {
        "grant_type": "authorization_code",
        "client_id": "39c09c3e2d2a0741405cf64373d6a60a",  # rest_api_key
        "redirect_uri": "http://ripggbean-env.eba-tprx3bfx.ap-northeast-2.elasticbeanstalk.com/accounts/login/kakao/callback",
        "code": request.GET.get("code"),
    }
    kakao_token_api = "https://kauth.kakao.com/oauth/token"
    access_token = requests.post(kakao_token_api, data=data).json()["access_token"]

    headers = {"Authorization": f"bearer ${access_token}"}
    kakao_user_api = "https://kapi.kakao.com/v2/user/me"
    kakao_user_information = requests.get(kakao_user_api, headers=headers).json()

    kakao_id = kakao_user_information["id"]
    kakao_nickname = kakao_user_information["properties"]["nickname"]
    kakao_email = kakao_user_information["kakao_account"]["email"]

    # 유저 모델에 프로필 사진 추가시 사용
    # kakao_profile_image = kakao_user_information["properties"]["profile_image"]
    if get_user_model().objects.filter(kakao_id=kakao_id).exists():
        kakao_user = get_user_model().objects.get(kakao_id=kakao_id)
        # Profile.objects.create(user=kakao_user)  # 프로필 생성
        # Grade.objects.create(user=kakao_user)


    else:
        kakao_login_user = get_user_model()()
        kakao_login_user.username = kakao_nickname
        kakao_login_user.kakao_id = kakao_id
        kakao_login_user.kakao_email = kakao_email
        kakao_login_user.password = str(state_token)
        kakao_login_user.save()
        kakao_user = get_user_model().objects.get(kakao_id=kakao_id)
        Profile.objects.create(user=kakao_user)  # 프로필 생성


    auth_login(request, kakao_user, backend="django.contrib.auth.backends.ModelBackend")
    return redirect(request.GET.get("next") or "articles:index")


# 비밀번호 초기화, 찾기 이메일
class UserPasswordResetView(PasswordResetView):
    template_name = "accounts/password_reset.html"
    email_template_name = "accounts/password_reset_email.html"
    success_url = reverse_lazy("password_reset_done")
    form_class = PasswordResetForm

    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            return render(self.request, "accounts/password_reset_done_fail.html")


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = SetPasswordForm
    reset_url_token = "set-password"
    success_url = reverse_lazy("password_reset_complete")

    def form_valid(self, form):
        return super().form_valid(form)


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_url"] = resolve_url(settings.LOGIN_URL)
        return context
