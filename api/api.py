import os
from dotenv import load_dotenv
from fastapi import Depends, Request, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from . import database, auth, models, security


load_dotenv()

router = APIRouter()

# Настройка сессий
SECRET_KEY = os.environ.get("SECRET_KEY")


@router.post('/register', response_model=models.User)
def register(user: models.UserCreate, db: Session = Depends(database.get_db)):
    db_user = auth.get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Такой пользователь уже зарегистрирован")
    created_user = auth.create_user(db, user=user)
    user_pydantic = models.User(id=created_user.id, username=created_user.username, full_name=created_user.full_name)
    return user_pydantic


@router.post('/token', response_model=models.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 db: Session = Depends(database.get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учетные данные",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = security.timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me", response_model=models.User)
async def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user


# @router.post("/bot", response_model=models.TelegramBotToken)
# async def telegram_bot_token(telegram_bot: models.TelegramBotToken,
#                                     db: Session = Depends(database.get_db),
#                                     current_user: database.User = Depends(auth.get_current_active_user)):
#     current_user.telegram_bot_token = telegram_bot.token
#     db.commit()
#     return {"message": "Telegram bot token updated successfully"}
