from aiogram import Router

from aiogram.filters import Command
from aiogram.types import Message

main_router: Router = Router()

@main_router.message(Command("start"))
async def cmd_test(m: Message):
    await m.answer("Hello!")