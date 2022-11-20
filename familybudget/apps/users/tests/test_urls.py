from django.contrib.auth.views import LoginView, LogoutView
from django.urls import resolve, reverse
from pytest_django.asserts import assertURLEqual

from apps.users.views import RegisterView


def test_register_url_is_resolved():
    url = reverse("users:register")
    assertURLEqual(resolve(url).func.view_class, RegisterView)


def test_login_url_is_resolved():
    url = reverse("users:login")
    assertURLEqual(resolve(url).func.view_class, LoginView)


def test_logout_url_is_resolved():
    url = reverse("users:logout")
    assertURLEqual(resolve(url).func.view_class, LogoutView)
