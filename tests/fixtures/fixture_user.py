import pytest


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        email='bobmar@index.com',
        first_name='Bob',
        last_name='Marley',
        username='bobmar',
        password='bombibom89',
    )


@pytest.fixture
def another_user(django_user_model):
    return django_user_model.objects.create_user(
        email='krol@index.com',
        first_name='Krol',
        last_name='Travozhadniy',
        username='krol',
        password='kroltrav89',
    )


@pytest.fixture
def token(user):
    from rest_framework.authtoken.models import Token
    token = Token.objects.get_or_create(user=user)

    return token
