from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = "quotes_app"

urlpatterns = [
    path('', views.main, name="main"),
    path('author/<int:author_id>/', views.about_author, name="about"),
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #adding urls
    path('quote/', views.add_quote, name='quote'),
    path('tag/', views.add_tag, name='tag'),
    path('author/', views.add_author, name='author'),

    #by tag
    path('tag/<str:tag>/', views.by_tag, name='by_tag'),

    #scrape data from base url
    path('scrape/', views.scrape_data_from_cite, name="scrape")
]
