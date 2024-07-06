from pyrogram import Client
from dotenv import load_dotenv
from pyrogram.types import Chat, Message, ChatMember
from os import getenv
import datetime
import json


class Parsed_Chat:
    def __init__(
            self, 
            members: list | tuple[ChatMember], 
            messages: list | tuple
            ) -> None:
        self._members: tuple[ChatMember] = tuple(members)
        self._messages: tuple[Message] = tuple(messages)
    
    def get_messages_text(self) -> str:
        """
        Возвращает строку, в которой находятся все сообщения
        """
        return "\n".join([message.text for message in self.messages if message.text])

    def make_text_file(self):
        """
        Создает текстовый файл, в котором находятся текста всех сообщений чата
        """
        with open("test_.txt", "w", encoding="utf-8") as file:
            # file.write("История сообщений чата: \n")
            for message in self.messages:
                if message.text:
                    file.write(message.text + "\n")

    def make_json_file(self):
        """
        Создаёт json файл, в котором хранится кортеж словарей,
        содержащих краткую информацию о сообщении
        (тг айди отправителя, время отправки, текст сообщения)
        """
        data = {
            "messages": tuple([{
                "user_id": message.from_user.id, 
                "datetime": message.date.strftime("%d-%m-%Y %H:%M:%S"), 
                "text": message.text
                } for message in self.messages if message.text]),
            }
        with open('result.json', 'w') as file:
            json.dump(data, file, indent=4)

    @property
    def members(self) -> tuple:
        return self._members
    
    @property
    def messages(self) -> tuple:
        return self._messages


async def parse_chat() -> Parsed_Chat:
    load_dotenv()
    api_id: int = int(getenv("api_id_"))
    api_hash: str = getenv("api_hash_")
    # result: dict = {
    #        "chat_history": [],
    #        "chat_members": [], 
    #     }
    messages = []
    members = []
    async with Client("my_account", api_id, api_hash) as app:
        # await app.send_message("me", "test")
        chat: Chat = await app.get_chat(getenv("chat_invite_link"))
        async for message in app.get_chat_history(chat.id):
            if all(
                (message.from_user, message.text, message.date < (datetime.datetime.now() - datetime.timedelta(days=180)))
                ):
                messages.append(message)
        async for member in app.get_chat_members(chat.id):
            if member:
                members.append(member)
        return Parsed_Chat(members=members, messages=messages)
