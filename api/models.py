from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    """Схема для создания пользователя (регистрация)"""
    username: str
    password: str
    full_name: str


class User(BaseModel):
    """Схема для отображения пользователя"""
    id: int
    username: str
    full_name: str
    telegram_id: Optional[int] = None

    class Config:
        from_attributes = True # говорит Pydantic, что можно получать данные из ORM моделей


class Token(BaseModel):
    """Схема для создания токена"""
    access_token: str
    token_type: str


class TelegramId(BaseModel):
    """Схема для создания telegram id"""
    telegram_id: Optional[int] = None
