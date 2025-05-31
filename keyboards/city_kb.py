from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

city_kb_buttons = [
    [InlineKeyboardButton(text='Подтвердить город', callback_data='city_continue')],
    [InlineKeyboardButton(text='Назад', callback_data='menu')]
]

city_kb = InlineKeyboardMarkup(inline_keyboard=city_kb_buttons)

full_city_kb_buttons = [
    [InlineKeyboardButton(text='Назад', callback_data='city_continue')],
    [InlineKeyboardButton(text='В меню', callback_data='menu')]
]

full_city_kb = InlineKeyboardMarkup(inline_keyboard=full_city_kb_buttons)
