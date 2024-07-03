import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import Message
from dotenv import load_dotenv
from os import getenv

import callbacks.main_menu
from keyboards.inline import main_menu_kb
import callbacks

load_dotenv()
bot = Bot(
    getenv("TOKEN"), 
    default=DefaultBotProperties(parse_mode="HTML")
    )
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Hello!",
        reply_markup=main_menu_kb()
        )


async def main():
    dp.include_routers(callbacks.main_menu.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

