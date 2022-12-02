from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.article_create, name="create"),
    path("<int:article_pk>/update", views.article_update, name="update"),
    path("<int:pk>/", views.article_detail, name="detail"),
    path("<int:pk>/delete", views.article_delete, name="delete"),
    # 댓글 생성
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    # 댓글 삭제
    path(
        "<int:pk>/comment_delete/<int:comment_pk>",
        views.comment_delete,
        name="comment_delete",
    ),
    # 게시글 좋아요
    path("<int:pk>/like/", views.like, name="like"),
    # 댓글 좋아요
    path(
        "<int:article_pk>/like/<int:comment_pk>/",
        views.comment_like,
        name="comment_like",
    ),
    # 게시물 북마크
    path("<int:pk>/bookmark/", views.bookmark, name="bookmark"),
]
