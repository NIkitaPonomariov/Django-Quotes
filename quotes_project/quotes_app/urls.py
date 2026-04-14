from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = "quotes_app"

urlpatterns = [
    path('', views.main, name="main"),
   
]
