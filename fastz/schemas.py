from pydantic import BaseModel


class Message(BaseModel):
    # Isso tem a ver com:
    # {"message": "Alguma coisa..."}
    # "message" precisa ser o mesmo nome
    mensage: str
