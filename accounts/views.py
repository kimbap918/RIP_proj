from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from .forms import CustomUserCreationForm
from django.http import HttpResponseRedirect


# Create your views here.
def login(request):
    # if request.user.is_anonymous:
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect("articles:main")
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
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return redirect("articles:main")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


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
            profile_form = ProfileForm()
            change_form = CustomUserChangeForm(instance=user)

    context = {
        "profile_form": profile_form,
        "change_form": change_form,
    }

    return render(request, "accounts/update.html", context)
