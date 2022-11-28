from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path('',views.index, name="index"),
    path('create/', views.article_create, name="create"),
    path('update/<int:article_pk>', views.article_update, name="update"),
    path('<int:article_pk>/',views.article_detail, name='detail'),
    path('delete/<int:article_pk>/',views.article_delete, name='delete'),
    path("main/", views.main, name="main"),
]