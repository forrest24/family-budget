import factory
from django.contrib.auth.hashers import make_password

from apps.users.models import CustomUser


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = "test_user"
    password = make_password("test_password")
    email = "test@testmail.com"
