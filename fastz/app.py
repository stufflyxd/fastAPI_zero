from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fastz.schemas import (
    Message,  # Documenta direitinho dizendo o que vai ser retornado
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()

database = []


# O get funciona como "pegue esse caminho"
# (Cria um caminho que aceita verbos get)
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Yasmin é minha gostosa.'}


@app.post('/users/', response_model=UserPublic, status_code=HTTPStatus.CREATED)
# UserSchema (Entrada): O que a API espera receber
# UserPublic (Response): O que deve sair como resposta
def create_user(user: UserSchema):
    user_with_id = UserDB(
        id=len(database) + 1,  # É somando 1, pois inicial vale 0
        **user.model_dump(),
    )

    database.append(user_with_id)
    return user_with_id  # Isso é a resposta


# Pegando o cadastro dos usuarios
@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


# Alterna o registro
@app.put('/users/{user_id}', response_model=UserPublic)
# user_id = aceita inteiro
# user: UserSchema: necessário para fazer o update (tem a senha)
# respose_model=UserPublic -> Retorna o público (sem a senha)
def update_user(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    user_with_id = UserDB(id=user_id, **user.model_dump())
    # Coloca no banco de dados o novo registro
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found!'
        )

    del database[user_id - 1]

    return {'message': 'User deleted!'}


# Exercicio: Novo endpoint
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


# Exercicio: Novo endpoint que só retorna o id
@app.get('/users/{id}', response_model=UserPublic)
def read_user_id(id: int):
    if id > len(database) or id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found!'
        )

    return database[id - 1]
