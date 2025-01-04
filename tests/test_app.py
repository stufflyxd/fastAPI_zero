from http import HTTPStatus

from fastapi.testclient import TestClient

# O último app está importando o objeto (app)
# O "fast.app" está referenciando o arquivo.
from fastz.app import app

client = TestClient(app)


def test_read_root_deve_retornar_OK_e_yasmin():
    client = TestClient(app)  # Fase Arrange (Organização)

    response = client.get('/')  # Act (ação) executa o bloco de código

    # (garanta que o status code da resposta...)
    assert response.status_code == HTTPStatus.OK

    # A chamada do servidor é retornado em um json
    assert response.json() == {'mensage': 'Yasmin é minha gostosa.'}


# Exercicio
def test_saudacao_deve_retornar_OK_e_ola_mundo():
    client = TestClient(app)
    response = client.get('/ola_mundo')

    assert response.status_code == HTTPStatus.OK

    assert "Olá, mundo!" in response.text
