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
        async for message in app.get_chat_history("-4210829020"):
            print(
                f"{message.from_user.first_name}: {message.text} | Айди пользователя: {message.from_user.id}"
                )
        async for member in app.get_chat_members("-4210829020"):
            print(member.user.id)
        


asyncio.run(main())
