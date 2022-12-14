from django.urls import path

# 비밀번호 초기화, 재설정
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy

app_name = "accounts"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),  # 회원가입
    path("logout/", views.logout, name="logout"),  # 로그아웃
    path("<int:pk>/", views.detail, name="detail"),
    path('<int:pk>/report/', views.report, name='report'),
    path("<int:user_pk>/mypage/", views.mypage, name="mypage"),  # 마이페이지
    path("<int:user_pk>/password/", views.password, name="password"),  # 비밀번호 변경
    path("delete/", views.delete, name="delete"),  # 회원탈퇴
    path("<int:user_pk>/pre_delete/", views.pre_delete, name="pre_delete"),  # 회원탈퇴
    path("<int:pk>/update/", views.update, name="update"),  # 회원정보수정
    path(
        "password/reset/",
        views.UserPasswordResetView.as_view(
            template_name="accounts/password_reset.html",
            email_template_name="accounts/password_reset_email.html",
            success_url=reverse_lazy("accounts:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password/reset/done/",
        views.UserPasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password/reset/confirm/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url=reverse_lazy("accounts:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password/reset/confirm/complete/",
        views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("send_email/", views.send_email, name="send_email"),
    path("member/", views.member, name="member"),  # 프로그래스바
    path("login/kakao", views.kakao_request, name="kakao"),
    path("login/kakao/callback/", views.kakao_callback, name="kakao_callback"),
]
