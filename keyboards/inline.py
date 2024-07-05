from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from typing import Any


class MainMenuCbData(CallbackData, prefix="pag"):
    action: str


def main_menu_kb(user_perms_lvl: int):
    builder = InlineKeyboardBuilder()
    if user_perms_lvl >= 1:
        builder.row(
            InlineKeyboardButton(
            text="Парсинг чата",
            callback_data=MainMenuCbData(action="Parse_chat").pack()
            ),
        )
    builder.row(
        InlineKeyboardButton(
        text="Заглушка",
        callback_data=MainMenuCbData(action="-").pack()
        ),
    )
    return builder.as_markup()


def send_to_gpt_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
        text="Отправить на обработку к ChatGPT",
        callback_data=MainMenuCbData(action="Send_to_gpt").pack()
        ),
    )
    builder.row(
        InlineKeyboardButton(
        text="Отмена",
        callback_data=MainMenuCbData(action="Back_to_main_menu").pack()
        ),
    )

    return builder.as_markup()


def back_to_main_menu_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
        text="В главное меню",
        callback_data=MainMenuCbData(action="Back_to_main_menu").pack()
        ),
    )

    return builder.as_markup()