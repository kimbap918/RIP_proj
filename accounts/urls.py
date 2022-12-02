from django.urls import path

# 비밀번호 초기화, 재설정
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy

app_name = "accounts"

urlpatterns = [
    path("", views.login, name="login"),
    path("signup/", views.signup, name="signup"),  # 회원가입
    path("logout/", views.logout, name="logout"),  # 로그아웃
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:user_pk>/mypage/", views.mypage, name="mypage"),  # 마이페이지
    path("password/", views.password, name="password"),  # 비밀번호 변경
    path("delete/", views.delete, name="delete"),  # 회원탈퇴
    path("<int:pk>/update/", views.update, name="update"),  # 회원정보수정
    path(
        "password_reset/",
        views.UserPasswordResetView.as_view(
            template_name="accounts/password_reset.html",
            email_template_name="accounts/password_reset_email.html",
            success_url=reverse_lazy("accounts:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password_reset_done/",
        views.UserPasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("send_email/", views.send_email, name="send_email"),
]
