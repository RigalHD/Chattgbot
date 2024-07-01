from pyrogram import Client
from dotenv import load_dotenv
from os import getenv
import asyncio

load_dotenv()
api_id = int(getenv("api_id"))
api_hash = getenv("api_hash")


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        pass
        # await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())
