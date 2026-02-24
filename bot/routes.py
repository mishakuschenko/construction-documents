from aiogram import Router, F

from aiogram.filters import Command
from aiogram.types import Message

from spreadsheets import insert_data

main_router: Router = Router()

@main_router.message(Command("start"))
async def cmd_test(m: Message):
    await m.answer("start message")


@main_router.message(Command("help"))
async def cmd_help(m: Message):
    await m.answer("help message")

@main_router.message(F.text)
async def insert_data_handler(m: Message):
    data = m.text.split(",")
    insert_data(0, data)
    await m.answer("Данные успешно добавлены в таблицу!")