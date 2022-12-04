from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),  # 회원가입
    path("logout/", views.logout, name="logout"),  # 로그아웃
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:user_pk>/mypage/", views.mypage, name="mypage"),  # 마이페이지
    path("password/", views.password, name="password"),  # 비밀번호 변경
    path("delete/", views.delete, name="delete"),  # 회원탈퇴
    path("<int:pk>/update/", views.update, name="update"),  # 회원정보수정
    path("member/",views.member, name="member"), # 프로그래스바
    path("login/kakao", views.kakao_request, name="kakao"),
    path("login/kakao/callback/", views.kakao_callback),
]
