from django.urls import path
from . import views

app_name = "champions"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>/detail/", views.detail, name="detail"),
    path("goin/", views.goin, name="goin"),
    path("search/",views.search,name="search"),
]
