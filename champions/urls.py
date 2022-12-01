from django.urls import path
from . import views

app_name = "champions"

urlpatterns = [

    path('index/', views.index, name='index'),
    # path('index/<str:lane_name>', views.lane_name, name='lane_name'),

]