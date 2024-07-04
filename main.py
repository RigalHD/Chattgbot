from pyrogram import Client
from dotenv import load_dotenv
from os import getenv
# from secret_data import api_id, api_hash
import asyncio

load_dotenv()
api_id = int(getenv("api_id_"))
api_hash = getenv("api_hash_")

# ---

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        # await app.send_message("me", "test")
        with open("test_.txt", "w", encoding="utf-8") as file:
            file.write("История сообщений чата: \n")
            async for message in app.get_chat_history("-1002211055178"):
                if message.from_user:
                    file.write(f"{message.from_user.first_name}: {message.text} | Айди пользователя: {message.from_user.id}\n")
            file.write("Участники чата: \n")
            async for member in app.get_chat_members("-1002211055178"):
                file.write(f"{member.user.first_name}: | Айди пользователя: {member.user.id}\n")


asyncio.run(main())
