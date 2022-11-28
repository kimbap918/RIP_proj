from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path('',views.index, name="index"),
    path('create/', views.article_create, name="create"),
    path('update/<int:article_pk>', views.article_update, name="update"),
    path("main/", views.main, name="main"),
]