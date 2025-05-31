from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_widget_keyboard():
    """Клавиатура для управления виджетом"""
    builder = InlineKeyboardBuilder()
    builder.button(text="🔄 Обновить", callback_data="refresh_widget")
    return builder.as_markup()