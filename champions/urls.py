from django.urls import path
from . import views

app_name = "champions"

urlpatterns = [
    path('index/', views.index, name='index'),
]