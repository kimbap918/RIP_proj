from django.urls import path, include
from . import views

app_name = "summoners"

urlpatterns = [
    path("test/", views.test, name="test"),
    path("", views.index, name="index"),
    path("result/", views.result, name="result"),
]
