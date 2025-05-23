# Учебная практика, проект "Погодный виджет" ☀️☂️
import asyncio

from handlers.handlers import *


async def main():
    print('Бот запущен!')
    await dp.start_polling(Weather_widget_bot)


if __name__ == '__main__':
    asyncio.run(main())
