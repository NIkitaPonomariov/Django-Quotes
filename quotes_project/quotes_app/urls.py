from . import views
from django.urls import path, include

app_name = "quotes_app"

urlpatterns = [
    path('', views.main, name="main")
]
