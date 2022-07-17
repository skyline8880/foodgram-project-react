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
def user_2(django_user_model):
    return django_user_model.objects.create_user(
        email='vaskin@index.com',
        first_name='Vasiliy',
        last_name='Tyorkin',
        username='vaskin',
        password='vakivaki89',
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
    from rest_framework_simplejwt.tokens import RefreshToken
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@pytest.fixture
def user_client(token):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
    return client
