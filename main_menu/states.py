from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from utils.database import UsersTable

router = Router()


class AuthState(StatesGroup):
    contact = State()


@router.message(AuthState.contact)
async def process_auth_contact(message: Message, state: FSMContext) -> None:
    if message.contact:
        await state.update_data(contact=message.contact)
        await message.answer(
            text="Авторизация прошла успешно!"
            )
        await state.clear()

        db = UsersTable()
        first_name = message.from_user.first_name if message.from_user.first_name else None
        last_name = message.from_user.last_name if message.from_user.last_name else None
        username = message.from_user.username if message.from_user.username else None

        await db.register_user(
            telegram_id=message.from_user.id,
            first_name=first_name,
            last_name=last_name,
            username=username,
            phone_number=message.contact.phone_number,
            )
    else:
        await message.answer(
            text="Необходимо отправить ваш контакт с помощью кнопки на клавиатуре"
        )
    