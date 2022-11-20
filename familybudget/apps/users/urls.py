from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy

from apps.users.views import RegisterView

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "login/",
        LoginView.as_view(
            template_name="users/login.html",
            next_page=reverse_lazy("home"),
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(next_page=reverse_lazy("users:login")),
        name="logout",
    ),
]
