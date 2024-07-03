from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class MainMenuCbData(CallbackData, prefix="pag"):
    action: str


def main_menu_kb():
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(
        text="Информация",
        callback_data=MainMenuCbData(action="Info_view").pack()
        ),
    )

    return builder.as_markup()
