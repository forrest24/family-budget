import pytest

from apps.users.forms import CustomUserCreationForm


@pytest.mark.parametrize(
    "username,email,password1,password2,expected_result",
    [
        ("user", "user_email@gmail.com", "test_password", "test_password", True),
        ("", "user_email@gmail.com", "test_password", "test_password", False),
        ("user", "", "test_password", "test_password", False),
        ("user", "user_email@gmail.com", "", "test_password", False),
        ("user", "user_email@gmail.com", "test_password", "", False),
    ],
)
@pytest.mark.django_db
def test_custom_user_creation_form(
    username, email, password1, password2, expected_result
):
    form_data = {
        "username": username,
        "email": email,
        "password1": password1,
        "password2": password2,
    }

    form = CustomUserCreationForm(data=form_data)
    assert form.is_valid() == expected_result

