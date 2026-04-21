from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = "quotes_app"

urlpatterns = [
    path('', views.main, name="main"),
    path('author/<int:author_id>/', views.about_author, name="about"),
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('quote/', views.add_quote, name='quote')
]
