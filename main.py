from pyrogram import Client
from pyrogram.types import Message, User
from dotenv import load_dotenv
from os import getenv
import asyncio

load_dotenv()
api_id = int(getenv("api_id"))
api_hash = getenv("api_hash")


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        with open("test_.txt", "w", encoding="utf-8") as file:
            file.write("История сообщений чата: \n")
            async for message in app.get_chat_history("-4210829020"):
                file.write(f"{message.from_user.first_name}: {message.text} | Айди пользователя: {message.from_user.id}\n")
            file.write("Участники чата: \n")
            async for member in app.get_chat_members("-4210829020"):
                file.write(f"{member.user.first_name}: | Айди пользователя: {member.user.id}\n")

asyncio.run(main())
