from os import getenv
from dotenv import load_dotenv
from asyncio import run

from .routes import main_router

from aiogram import Bot, Dispatcher

load_dotenv()

API_TOKEN: str | None = getenv("API_TOKEN")

async def start_bot() -> None:
    if API_TOKEN is not None:
        bot: Bot = Bot(API_TOKEN)

        dp = Dispatcher()

        dp.include_routers(main_router)

        await dp.start_polling(bot)

