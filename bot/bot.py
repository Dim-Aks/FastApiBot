import os
import asyncio
from FastApiBot.api.database import User, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

load_dotenv()


TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
DATABASE_URL = os.environ.get("DATABASE_URL")

dp = Dispatcher()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """ `/start` command """
    await message.reply(f"Привет, {html.bold(message.from_user.full_name)}!")
    user_id = message.from_user.id
    # Получение Telegram ID
    await message.answer("Пожалуйста, перейдите на сайт и свяжите свой аккаунт Telegram, указав свой Telegram ID.")
    await message.answer(f"Ваш ID: {user_id}")


@dp.message()
async def echo_handler(message: Message) -> None:
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.telegram_id == message.from_user.id).first()
        if user:
            await message.answer(f"Вы отправили сообщение длиной {len(message.text)} символов.")
        else:
            await message.answer("Бот не подключен ни к одному аккаунту или не настроен.")
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Бот принимает только текст и возвращает количество символов.")
    finally:
        db.close()


async def start() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    Base.metadata.create_all(engine)
    await dp.start_polling(bot)

asyncio.run(start())
