from pyrogram import Client
from dotenv import load_dotenv
from pyrogram.types import Chat
from os import getenv


class Parsed_Chat:
    def __init__(
            self, 
            chat: Chat,
            members: list | tuple, 
            messages: list | tuple
            ):
        print(chat.id)
        self._members: tuple = tuple(members)
        self._messages: tuple = tuple(messages)
        self._chat: int = chat

    @property
    def members(self) -> tuple:
        return self._members
    
    @property
    def messages(self) -> tuple:
        return self._messages
    
    @property
    def chat(self) -> Chat:
        return self._chat


async def parse_chat() -> Parsed_Chat:
    load_dotenv()
    api_id = int(getenv("api_id_"))
    api_hash = getenv("api_hash_")
    # result: dict = {
    #        "chat_history": [],
    #        "chat_members": [], 
    #     }
    messages = []
    members = []
    async with Client("my_account", api_id, api_hash) as app:
        # await app.send_message("me", "test")
        chat: Chat = await app.get_chat("https://t.me/+cyVZuxr5T7xhMTM6")
        async for message in app.get_chat_history(chat.id):
            if message.from_user:
                messages.append(message)
        async for member in app.get_chat_members(chat.id):
            if member:
                members.append(member)
        return Parsed_Chat(members=members, messages=messages, chat=chat)
