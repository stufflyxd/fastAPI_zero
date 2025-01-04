from fastapi import FastAPI

app = FastAPI()


@app.get('/')  # O get funciona como "pegue esse caminho"
def read_root():
    return {'message': 'Yasmin minha gostosa.'}
