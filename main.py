# Учебная практика, проект "Погодный виджет" ☀️☂️
import asyncio

from PIL import *
from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from keys import BOT_KEY, API_KEY

dp = Dispatcher()
Weather_widget_bot = Bot(token=BOT_KEY)

@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Введите желаемый город: ')


async def main():
    await dp.start_polling(Weather_widget_bot)

if __name__ == '__main__':
    asyncio.run(main())
