from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    # Isso tem a ver com:
    # {"message": "Alguma coisa..."}
    # "message" precisa ser o mesmo nome
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserList(BaseModel):
    users: list[UserPublic]  # users - Chave definida


class UserDB(UserSchema):
    id: int


# Exercicio (acho que precisa) - Apenas o id será buscado
class UserID(BaseModel):
    id: int
