from django.urls import path
from . import views

app_name = "champions"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>/detail/", views.detail, name="detail"),
]
