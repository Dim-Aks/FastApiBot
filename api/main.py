from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


# Модель Pydantic
class User(BaseModel):
    id: int
    login: str
    name: str


@app.get('/home')
def get_home():
    return 'Hello'


@app.post('/register')
def register():
    return User


@app.post('/login')
def register():
    return User


# @app.post('/bot')
# def bot():
#     return 'Bot'
