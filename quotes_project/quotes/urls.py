from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name="main"),
    path('register/', views.register, name="register"),
    path('add_author/', views.add_author, name="add_author"),
    path('add_quote/', views.add_quote, name="add_quote"),
    path('add_tag/', views.add_tag, name="add_tag"),
    path('tag/<str:tag_name>/', views.quotes_by_tag, name="tag"),
]
