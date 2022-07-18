import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


class TestAuth:
    url_login = '/api/auth/token/login/'
    url_logout = '/api/auth/token/logout/'

    @pytest.mark.django_db(transaction=True)
    def test_auth_login__invalid_request_data(self, client, user):
        url = self.url_login
        response = client.post(url)
        code_expected = 400
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected}'
        )
        non_field = 'non_field_errors'
        assert non_field in response.json().keys(), (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected} с сообщением о том, '
            'при обработке каких полей возникла ошибка.'
            f'Не найдено поле {non_field}'
        )

        username_invalid = 'invalid_username_not_exists'
        password_invalid = 'invalid pwd'
        data_invalid = {
            'email': username_invalid,
            'password': password_invalid
        }
        response = client.post(url, data=data_invalid)
        code_expected = 400
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected}'
        )
        field = {'non_field_errors':
                     ['Unable to log in with provided credentials.']}
        assert field['non_field_errors'] in response.json().values(), (
            f'Убедитесь, что при запросе `{url}` с некорректным username, '
            f'возвращается код {code_expected} с соответствующим сообщением '
            f'в поле {field}'
        )
        username_valid = user.email
        data_invalid = {
            'email': username_valid,
            'password': password_invalid
        }
        response = client.post(url, data=data_invalid)
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected}'
        )
        field = {'non_field_errors':
                     ['Unable to log in with provided credentials.']}
        assert field['non_field_errors'] in response.json().values(), (
            f'Убедитесь, что при запросе `{url}` с некорректным password, '
            f'возвращается код {code_expected} с соответствующим сообщением '
            f'в поле {field}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_auth_login__valid_request_data(self, client, user):
        url = self.url_login
        valid_data = {
            'email': user.email,
            'password': 'bombibom89'
        }
        response = client.post(url, data=valid_data)
        code_expected = 200
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с валидными данными, '
            f'возвращается код {code_expected}'
        )
        field_in_response = 'auth_token'
        assert field_in_response in response.json().keys(), (
            f'Убедитесь, что при запросе `{url}` с валидными данными, '
            f' в ответе возвращается код {code_expected} с ключом '
            f'{field_in_response}, где содержится токен'
        )

    @pytest.mark.django_db(transaction=True)
    def test_auth_logout__invalid_request_data(self, client, token):
        url = self.url_logout
        response = client.post(url)
        code_expected = 401
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с некорректными данными, '
            f'возвращается код {code_expected}'
        )
        field_in_response = 'detail'
        assert field_in_response in response.json().keys(), (
            f'Убедитесь, что при запросе `{url}` с некорректными данными, '
            f' в ответе возвращается код {response} с ключом '
            f'{field_in_response}, где содержится {response.json().keys()}'
        )
