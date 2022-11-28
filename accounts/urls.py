from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.login, name="login"),
    path("logout/", views.logout, name="logout"), # 로그아웃
    path("signup/", views.signup, name="signup"), # 회원가입
    path("<int:user_pk>/mypage/", views.mypage, name="mypage"),  # 마이페이지
    path("password/", views.password, name="password"),  # 비밀번호 변경
    path("delete/", views.delete, name="delete"),  # 회원탈퇴
    path("<int:pk>/update/", views.update, name="update"),
]

