from aiogram import Router
from aiogram.types import Message
import datetime
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.methods.send_contact import SendContact
import os

router = Router()


class AuthState(StatesGroup):
    contact = State()


@router.message(AuthState.contact)
async def process_auth_contact(message: Message, state: FSMContext) -> None:
    await state.update_data(contact=message.text)
    await message.answer(text="")
