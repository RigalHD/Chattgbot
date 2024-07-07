from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from typing import Any


class MainMenuCbData(CallbackData, prefix="pag"):
    action: str


class ParseChatCbData(CallbackData, prefix="pag"):
    action: str
    day_limit: int


class SendToGPTCbData(CallbackData, prefix="pag"):
    action: str
    query_id: int


def main_menu_kb(user_perms_lvl: int):
    builder = InlineKeyboardBuilder()
    if user_perms_lvl >= 1:
        builder.row(
            InlineKeyboardButton(
            text="Парсинг чата",
            callback_data=MainMenuCbData(action="Parse_chat_limit").pack()
            ),
        )
    builder.row(
        InlineKeyboardButton(
        text="Заглушка",
        callback_data=MainMenuCbData(action="-").pack()
        ),
    )
    return builder.as_markup()


def parse_chat_kb():
    builder = InlineKeyboardBuilder()
    day_limits = [360, 180, 90, 60, 30, 14, 7, 3, 2, 1, -1] # -1 = спарсит весь чат
    row_length = 3
    for i in range(len(day_limits) // row_length):
        row = []
        for el in day_limits[i * row_length : (i + 1) * row_length]:
            row.append(
                InlineKeyboardButton(
                    text=f"{el} д." if el != -1 else "Весь чат",
                    callback_data=ParseChatCbData(
                        action="Parse_chat",
                        day_limit=el,
                        ).pack()
                        ))
        builder.row(*row)

    row = []
    for el in day_limits[-(len(day_limits) % row_length):]:
        row.append(
            InlineKeyboardButton(
                text=f"{el} д." if el != -1 else "Весь чат",
                callback_data=ParseChatCbData(
                    action="Parse_chat",
                    day_limit=el,
                    ).pack()
                    ))
        
    builder.row(*row)

    return builder.as_markup()

def send_to_gpt_kb(query_id: int):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
        text="Отправить на обработку к ChatGPT",
        callback_data=SendToGPTCbData(action="Send_to_gpt", query_id=query_id).pack()
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