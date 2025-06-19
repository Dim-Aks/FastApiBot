from pydantic import BaseModel


class UserCreate(BaseModel):
    """Схема для создания пользователя (регистрация)"""
    username: str
    password: str
    full_name: str


class User(BaseModel):
    id: int
    username: str
    full_name: str
    telegram_bot_token: str | None

    class Config:
        from_attributes = True # говорит Pydantic, что можно получать данные из ORM моделей


# Модель для аутентификации (логин)
class Token(BaseModel):
    access_token: str
    token_type: str


class TelegramBotToken(BaseModel):
    """Схема для подключения Telegram"""
    telegram_bot_token: str
