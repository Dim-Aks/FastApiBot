import os
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine


load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")  # Измените на свои значения

# Создаем движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# Создаем сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    full_name = Column(String)
    telegram_bot_token = Column(String, nullable=True)


def create_db_and_tables():
    Base.metadata.create_all(engine)


# Получение сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
