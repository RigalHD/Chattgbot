from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from Neuro.chat import neuro_marketing

from parser_bot.bot import parse_chat
from keyboards.inline import MainMenuCbData
from . import states

router = Router()


@router.callback_query(MainMenuCbData.filter(F.action == "Info_view"))
async def info_view_handler(query: CallbackQuery, callback_data: MainMenuCbData):
    await query.message.answer(text="Мы - ну, мы, ну, да, мы")
    chat = await parse_chat()
    # print(*chat.members)
    # print([i.text for i in chat.messages])
    # print(chat.messages)
    # print(chat.messages[0])
    print(neuro_marketing(chat.get_messages_text()))