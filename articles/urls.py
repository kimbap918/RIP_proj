from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("main/", views.main, name="main"),
]