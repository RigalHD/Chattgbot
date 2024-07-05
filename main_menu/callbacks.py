from aiogram.types import CallbackQuery
from aiogram import Router, F

from Neuro.chat import neuro_marketing
from parser.bot import parse_chat
from keyboards import inline
from utils.database import UsersTable

router = Router()


@router.callback_query(inline.MainMenuCbData.filter(F.action == "Parse_chat"))
async def parse_chat_handler(query: CallbackQuery, callback_data: inline.MainMenuCbData):
    await query.message.edit_text(text="Парсинг чата может занять некоторое время")
    try:
        chat = await parse_chat()
        await query.message.edit_text(
            text="Парсинг прошел успешно. Хотите отправить данные на обработку в ChatGPT?", 
            reply_markup=inline.send_to_gpt_kb()
            )
        # print(chat.members)
        # print(neuro_marketing(chat.get_messages_text()))
    except Exception as e:
        print(e)
        await query.message.edit_text(text="Произошла ошибка", reply_markup=inline.back_to_main_menu_kb())
    # print(*chat.members)
    # print([i.text for i in chat.messages])
    # print(chat.messages)
    # print(chat.messages[0])
    # print(neuro_marketing(chat.get_messages_text()))


@router.callback_query(inline.MainMenuCbData.filter(F.action == "Send_to_gpt"))
async def send_to_gpt_handler(query: CallbackQuery, callback_data: inline.MainMenuCbData):
    await query.message.edit_text(text="Обработка данных может занять некоторое время")
    try:
        chat = await parse_chat()
        message_text=neuro_marketing(chat.get_messages_text())
    except Exception as e:
        print(e)
        message_text="Произошла ошибка"
    finally:
        await query.message.edit_text(text=str(message_text), reply_markup=inline.back_to_main_menu_kb())


@router.callback_query(inline.MainMenuCbData.filter(F.action == "Back_to_main_menu"))
async def back_to_main_menu_handler(query: CallbackQuery, callback_data: inline.MainMenuCbData):
    db = UsersTable()
    permissions_level = await db.get_user_permissions_level(query.from_user.id)
    await query.message.edit_text(text="Главное меню", reply_markup=inline.main_menu_kb(permissions_level))
