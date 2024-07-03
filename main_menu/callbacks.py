from aiogram.types import CallbackQuery
from aiogram import Router, F

from keyboards.inline import MainMenuCbData


router = Router()


@router.callback_query(MainMenuCbData.filter(F.action == "Info_view"))
async def info_view_handler(query: CallbackQuery, callback_data: MainMenuCbData):
    await query.bot.answer_callback_query(callback_query_id=query.id, text="test")
