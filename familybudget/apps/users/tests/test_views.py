import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains, assertRedirects, assertTemplateUsed

from apps.users.models import CustomUser
from apps.users.tests.factories import CustomUserFactory


@pytest.fixture
@pytest.mark.django_db
def authenticated_user(client):
    user = CustomUserFactory()
    client.force_login(user)
    return user


@pytest.mark.django_db
def test_register_view_get_when_user_is_not_authenticated(client):
    response = client.get(reverse("users:register"))
    assertTemplateUsed(response, "users/register.html")


@pytest.mark.django_db
def test_register_view_get_when_user_is_authenticated(client, authenticated_user):
    response = client.get(reverse("users:register"))
    assertRedirects(response, reverse("home"))


@pytest.mark.django_db
def test_register_view_post_with_valid_input(client):
    data = {
        "username": "test_user",
        "email": "test@testmail.com",
        "password1": "test_password",
        "password2": "test_password",
    }
    response = client.post(reverse("users:register"), data=data, follow=True)

    user = CustomUser.objects.first()
    assert user.username == "test_user"
    assert user.check_password("test_password")

    assertContains(response, "Account was created successfully")
    assertTemplateUsed(response, "users/login.html")


@pytest.mark.parametrize(
    "username,email,password1,password2,user_exists",
    [
        ("", "test@testmail.com", "test_password", "test_password", False),
        ("test_user", "", "test_password", "test_password", False),
        ("test_user", "test@testmail.com", "", "test_password", False),
        ("test_user", "test@testmail.com", "test_password", "", False),
        ("test_user", "test@testmail.com", "test_password1", "test_password2", False),
        ("test_user", "test2@testmail.com", "test_password", "test_password", True),
        ("test_user2", "test@testmail.com", "test_password", "test_password", True),
    ],
)
@pytest.mark.django_db
def test_register_view_post_with_invalid_input(
        client, username, email, password1, password2, user_exists
):
    if user_exists:
        CustomUserFactory()

    data = {
        "username": username,
        "email": email,
        "password1": password1,
        "password2": password2,
    }
    response = client.post(reverse("users:register"), data=data, follow=True)

    assert response.status_code == 200
    assert CustomUser.objects.count() == user_exists


@pytest.mark.django_db
def test_login_view_get_when_user_is_authenticated(client, authenticated_user):
    response = client.get(reverse("users:login"))
    assertRedirects(response, reverse("home"))
