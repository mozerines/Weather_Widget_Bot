from typing import Dict

# Хранилище ID сообщений виджета
widget_messages: Dict[int, int] = {}

def get_stored_message_id(chat_id: int) -> int:
    """Получить сохраненный ID сообщения"""
    return widget_messages.get(chat_id)

def save_message_id(chat_id: int, message_id: int):
    """Сохранить ID сообщения"""
    widget_messages[chat_id] = message_id