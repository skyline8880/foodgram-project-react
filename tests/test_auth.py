import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


class TestJWT:
    url_create = '/api/auth/jwt/create/'
    url_refresh = '/api/auth/jwt/refresh/'
    url_verify = '/api/auth/jwt/verify/'
    url_logout = '/api/auth/jwt/logout/'

    @pytest.mark.django_db(transaction=True)
    def test_jwt_create__invalid_request_data(self, client, user):
        url = self.url_create
        response = client.post(url)
        code_expected = 400
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected}'
        )
        fields_invalid = ['email', 'password']
        for field in fields_invalid:
            assert field in response.json().keys(), (
                f'Убедитесь, что при запросе `{url}` без параметров, '
                f'возвращается код {code_expected} с сообщением о том, '
                'при обработке каких полей возникла ошибка.'
                f'Не найдено поле {field}'
            )

        username_invalid = 'invalid_username_not_exists'
        password_invalid = 'invalid pwd'
        data_invalid = {
            'email': username_invalid,
            'password': password_invalid
        }
        response = client.post(url, data=data_invalid)
        code_expected = 401
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected}'
        )
        field = 'detail'
        assert field in response.json(), (
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
        field = 'detail'
        assert field in response.json(), (
            f'Убедитесь, что при запросе `{url}` с некорректным password, '
            f'возвращается код {code_expected} с соответствующим сообщением '
            f'в поле {field}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_jwt_create__valid_request_data(self, client, user):
        url = self.url_create
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
        fields_in_response = ['refresh', 'access']
        for field in fields_in_response:
            assert field in response.json().keys(), (
                f'Убедитесь, что при запросе `{url}` с валидными данными, '
                f' в ответе возвращается код {code_expected} с ключами '
                f'{fields_in_response}, где содержатся токены'
            )

    @pytest.mark.django_db(transaction=True)
    def test_jwt_refresh__invalid_request_data(self, client):
        url = self.url_refresh

        response = client.post(url)
        code_expected = 400
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected}'
        )
        data_invalid = {
            'refresh': 'invalid token'
        }
        response = client.post(url, data=data_invalid)
        code_expected = 401
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с невалидным значением параметра refresh, '
            f'возвращается код {code_expected}'
        )
        fields_expected = ['detail', 'code']
        for field in fields_expected:
            assert field in response.json(), (
                f'Убедитесь, что при запросе `{url}` с невалидным значением параметра refresh, '
                f'возвращается код {code_expected} с соответствующим сообщением '
                f'в поле {field}'
            )

    @pytest.mark.django_db(transaction=True)
    def test_jwt_refresh__valid_request_data(self, client, user):
        url = self.url_refresh
        valid_data = {
            'email': user.email,
            'password': 'bombibom89'
        }
        response = client.post(self.url_create, data=valid_data)
        token_refresh = response.json().get('refresh')
        code_expected = 200
        response = client.post(url, data={'refresh': token_refresh})
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с валидным параметром refresh, '
            f'возвращается код {code_expected}'
        )
        field = 'access'
        assert field in response.json(), (
            f'Убедитесь, что при запросе `{url}` с валидным параметром refresh, '
            f'возвращается код {code_expected} и параметр access, в котором передан новый токен'
        )

    @pytest.mark.django_db(transaction=True)
    def test_jwt_verify__valid_request_data(self, client, user):
        url = self.url_verify
        valid_data = {
            'email': user.email,
            'password': 'bombibom89'
        }
        response = client.post(self.url_create, data=valid_data)
        token_access = response.json().get('access')
        token_refresh = response.json().get('refresh')
        code_expected = 200
        response = client.post(url, data={'token': token_access})
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с валидным параметром token, '
            f'возвращается код {code_expected}. '
            'Валидацию должны проходить как refresh, так и access токены'
        )
        response = client.post(url, data={'token': token_refresh})
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с валидным параметром token, '
            f'возвращается код {code_expected}. '
            'Валидацию должны проходить как refresh, так и access токены'
        )

    @pytest.mark.django_db(transaction=True)
    def test_jwt_verify__invalid_request_data(self, client):
        url = self.url_verify

        response = client.post(url)
        code_expected = 400
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected}'
        )
        data_invalid = {
            'token': 'invalid token'
        }
        response = client.post(url, data=data_invalid)
        code_expected = 401
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с невалидным значением параметра token, '
            f'возвращается код {code_expected}'
        )
        fields_expected = ['detail', 'code']
        for field in fields_expected:
            assert field in response.json(), (
                f'Убедитесь, что при запросе `{url}` с невалидным значением параметра token, '
                f'возвращается код {code_expected} с соответствующим сообщением '
                f'в поле {field}'
            )

    @pytest.mark.django_db(transaction=True)
    def test_jwt_logout__valid_request_data(self, user_client, user):
        url = self.url_logout
        valid_data = {
            'email': user.email,
            'password': 'bombibom89'
        }
        response = user_client.post(self.url_create, data=valid_data)
        token_access = response.json().get('access')
        token_refresh = response.json().get('refresh')
        code_expected = 200
        response = user_client.post(url, data={'token': token_access})
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с валидным параметром token, '
            f'возвращается код {code_expected}. '
            'Валидацию должны проходить как refresh, так и access токены'
        )
        response = user_client.post(url, data={'token': token_refresh})
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с валидным параметром token, '
            f'возвращается код {code_expected}. '
            'Валидацию должны проходить как refresh, так и access токены'
        )

    @pytest.mark.django_db(transaction=True)
    def test_jwt_logout__invalid_request_data(self, client):
        url = self.url_logout

        response = client.post(url)
        code_expected = 401
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected}'
        )
        data_invalid = {
            'token': 'invalid token'
        }
        response = client.post(url, data=data_invalid)
        code_expected = 401
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` с невалидным значением параметра token, '
            f'возвращается код {code_expected}'
        )
        field_expected = 'detail'
        assert field_expected in response.json(), (
            f'Убедитесь, что при запросе `{url}` с невалидным значением параметра token, '
            f'возвращается код {code_expected} с соответствующим сообщением '
            f'в поле {field_expected}'
            )
