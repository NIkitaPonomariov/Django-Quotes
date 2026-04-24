from . import views
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from .forms import LoginForm
from . import views


app_name = "users"

urlpatterns = [
    path('signin/', LoginView.as_view(template_name="users/lohin.html", form_class=LoginForm), name="signin"),
    path('logout/', LogoutView.as_view(template_name="users/logout.html"), name="logout"),

    path('signup/', views.RegisterView.as_view(), name="signup"),
]
