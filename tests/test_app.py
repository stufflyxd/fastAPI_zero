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
    assert response.json() == {'message': 'Yasmin minha gostosa.'}
