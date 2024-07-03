from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def auth_kb():
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(
            text="Поделиться контактом", 
            request_contact=True
            )
            )
    return builder.as_markup()
