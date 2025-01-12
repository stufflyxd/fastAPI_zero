from http import HTTPStatus

# Utilizando para reduzir as linhas de código
# client = TestClient(app)
# O último app está importando o objeto (app)
# O "fast.app" está referenciando o arquivo.


def test_read_root_deve_retornar_OK_e_yasmin(client):
    # Utilizando para reduzir as linhas de código

    response = client.get('/')  # Act (ação) executa o bloco de código

    # (garanta que o status code da resposta...)
    assert response.status_code == HTTPStatus.OK

    # A chamada do servidor é retornado em um json
    assert response.json() == {'message': 'Yasmin é minha gostosa.'}


# Criado 1:
def test_create_user_retornar_OK_e_JSON_RESPONSE(client):
    # UserSchema
    response = client.post(
        '/users/',
        json={
            'username': 'testeusername',
            'email': 'teste@teste.com',
            'password': 'cabritinho',
        },
    )

    assert response.status_code == HTTPStatus.CREATED

    # Validar UserPublic
    assert response.json() == {
        'username': 'testeusername',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'users': [
            {
                'username': 'testeusername',
                'email': 'teste@teste.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'ai meu bumbumm',
            'email': 'teste@teste.com',
            'id': 1,
            'password': '123',
        },
    )

    assert response.json() == {
        'username': 'ai meu bumbumm',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}


# Exercicio 1: Aula 2
def test_saudacao_deve_retornar_OK_e_ola_mundo(client):
    response = client.get('/ola_mundo')

    assert response.status_code == HTTPStatus.OK

    assert 'Olá, mundo!' in response.text


# Exercicio 2: Aula 3
def test_not_found_user_put(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'Gih',
            'email': 'gih@cabecuda.com',
            'id': 2,
            'password': '12345',
        },
    )

    assert response.json() == {'detail': 'User not found'}


# Exercicio 3: 404 para o endpoint DELETE
def test_not_found_user_delete(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found!'}


# Exercicio 4: 404 para o endpoint read_user_id
def test_get_user_shoud_return_not_found__exercicio(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found!'}


# Criado apenas para o exercicio


def test_create_user_retornar_OK_e_JSON_RESPONSE__EXERCICIO(client):
    # UserSchema
    response = client.post(
        '/users/',
        json={
            'username': 'testeusername',
            'email': 'teste@teste.com',
            'password': 'cabritinho',
        },
    )

    assert response.status_code == HTTPStatus.CREATED

    # Validar UserPublic
    assert response.json() == {
        'username': 'testeusername',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_get_user__exercicio(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testeusername',
        'email': 'teste@teste.com',
        'id': 1
    }
