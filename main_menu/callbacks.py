from aiogram.types import CallbackQuery
from aiogram import Router, F
from aiogram.fsm.context import FSMContext

from keyboards.inline import MainMenuCbData
from . import states

router = Router()


@router.callback_query(MainMenuCbData.filter(F.action == "Info_view"))
async def info_view_handler(query: CallbackQuery, callback_data: MainMenuCbData, state: FSMContext):
    await query.bot.answer_callback_query(callback_query_id=query.id, text="test")
    await state.set_state(states.AuthState.contact)
    await query.message.answer(text="Поделись контактом")
    await query.bot.send_contact()

