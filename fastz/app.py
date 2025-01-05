from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastz.schemas import (
    Message,  # Documenta direitinho dizendo o que vai ser retornado
)

app = FastAPI()


# O get funciona como "pegue esse caminho"
# (Cria um caminho que aceita verbos get)
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'mensage': 'Yasmin é minha gostosa.'}


# Exercicio: Novo end point
@app.get('/ola_mundo', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def saudacao():
    return """
    <html>
    <head>
        <title>Mano, tmj.</title>
    </head>
    <body>
        <h1>Olá, mundo!</h1>
    </body>
    </html>
"""

# Ain, bolsonaro