from django.urls import path
from .views import baseviews,articleviews,commentviews

app_name = "articles"

urlpatterns = [
    path('', baseviews.index, name="index"),
    # 카테고리
    path('category/<int:pk>/', baseviews.category, name="category"),
    # 아티클
    path('create/', articleviews.article_create, name="create"),
    path('<int:article_pk>/update', articleviews.article_update, name="update"),
    path('<int:pk>/',articleviews.article_detail, name='detail'),
    path('<int:pk>/delete',articleviews.article_delete, name='delete'),
    # 신고
    path('<int:pk>/report',articleviews.article_report, name='article_report'),
    # 댓글 생성
    path('<int:pk>/comments/', commentviews.comment_create, name='comment_create'),
    # 댓글 삭제
    path('<int:pk>/comment_delete/<int:comment_pk>', commentviews.comment_delete, name ='comment_delete'),
    # 게시글 좋아요
    path('<int:pk>/like/', articleviews.like, name='like'),
    # 댓글 좋아요
    path("<int:article_pk>/like/<int:comment_pk>/", commentviews.comment_like, name="comment_like"),
    # 게시물 북마크
    path('<int:pk>/bookmark/', articleviews.bookmark, name='bookmark'),
]
