from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

developer_kb_buttons = [
    [InlineKeyboardButton(text='В меню', callback_data='menu')]
]

developer_kb = InlineKeyboardMarkup(inline_keyboard=developer_kb_buttons)