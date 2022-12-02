from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
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
    return render(request, "accounts/login.html", context)


# else:
#    return HttpResponseRedirect("")


def logout(request):
    auth_logout(request)
    return redirect("accounts:login")


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

    context = {
        "user": user,
        "articles": articles,
        "like_articles": like_articles,
        "bookmark_articles": bookmark_articles,
    }
    return render(request, "accounts/detail.html", context)


# 마이 페이지 (회원 정보로 이동, 비밀번호 변경, 로그아웃, 회원탈퇴)
@login_required
def mypage(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)

    if request.user != user:
        return redirect("articles:index")

    context = {
        "user": user,
    }

    return render(request, "accounts/mypage.html", context)


# 비밀번호 변경
@login_required
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # 로그인 유지
            return redirect("accounts:mypage", request.user.pk)

    else:
        form = PasswordChangeForm(request.user)

    context = {
        "form": form,
    }

    return render(request, "accounts/password.html", context)


# 회원 탈퇴
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)

    return redirect("articles:index")


# 회원 프로필 (프로필 사진, 소개글) (+ 닉네임?)
@login_required
def update(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)

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


def send_email(request):
    subject = "RIP.gg 비밀번호 재설정"
    message = render_to_string("password_reset_email.html")
    send_email = EmailMessage(subject, message)
    send_email.send()


@login_required
def articles(request, pk):
    articles = all.Articles.objects.filter(user=request.user).order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "accounts/articles.html", context)


class UserPasswordResetView(PasswordResetView):
    template_name = "accounts/password_reset.html"
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
    post_reset_login = False
    post_reset_login_backend = None
    reset_url_token = "set-password"
    success_url = reverse_lazy("accounts/password_reset_complete.html")
    template_name = "accounts/password_reset_confirm.html"
    email_template_name = "accounts/password_reset.html"

    def form_valid(self, form):
        return super().form_valid(form)


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_url"] = resolve_url(settings.LOGIN_URL)
        return context
