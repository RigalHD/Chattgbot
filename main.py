import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
from os import getenv

import main_menu.callbacks
from keyboards.inline import main_menu_kb
from keyboards.reply import auth_kb
from main_menu.states import AuthState
import main_menu.states

load_dotenv()
bot = Bot(
    getenv("TOKEN"), 
    default=DefaultBotProperties(parse_mode="HTML")
    )
dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer(
        "Приветствуем! Для продолжения использования данного бота "
        "Вам нужно авторизоваться с помощью Вашей контактной информации (номер телефона и т.д.)",
        reply_markup=auth_kb()
        )
    await state.set_state(AuthState.contact)


async def main():
    dp.include_routers(main_menu.callbacks.router, main_menu.states.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

