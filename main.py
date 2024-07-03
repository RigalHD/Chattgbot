import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from os import getenv

import main_menu.callbacks
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
    dp.include_routers(main_menu.callbacks.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

