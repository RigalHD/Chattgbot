from pyrogram import Client
from dotenv import load_dotenv
from pyrogram.types import Chat, Message, ChatMember
from os import getenv
import os
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

    def make_json_file(self, file_name: str):
        """
        Создаёт json файл, в котором хранится кортеж словарей,
        содержащих краткую информацию о сообщении
        (тг айди отправителя, время отправки, текст сообщения)
        """
        # all_replied_messages = [(i.reply_to_message_id, i.id) for i in self._messages if i.reply_to_message_id]
        # print(all_replied_messages)
        
        data = {}
        # {
        #         "user_id": message.from_user.id, 
        #         "datetime": message.date.strftime("%d-%m-%Y %H:%M:%S"), 
        #         "text": message.text
        #         } for message in self._messages if message.text])
        for message in self._messages:
            try:
                data[message.id] = {
                    "user_id": message.from_user.id if message.from_user else message.sender_chat.id, 
                    "datetime": message.date.strftime("%d-%m-%Y %H:%M:%S"), 
                    "text": message.text,
                    "messages_replied_to_this_ids": [msg.id for msg in self._messages if msg.reply_to_message_id == message.id]
                    }
            except AttributeError:
                print(message)
        if not os.path.isdir("bot_temp_files/"):
            os.makedirs("bot_temp_files/")
        with open(f'bot_temp_files/{file_name}.json', 'w') as file:
            json.dump(data, file, indent=4)

    @property
    def members(self) -> tuple:
        return self._members
    
    @property
    def messages(self) -> tuple:
        return self._messages


async def parse_chat(limit_of_days: int = 180) -> Parsed_Chat:
    """
    :param limit_of_days: парсит чат до 
        <сегодняшняя дата> - limit_of_days дней.
        Если limit_of_days == -1, то произойдет парсинг всего чата
    """
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
            conditions = [
                message.from_user or message.sender_chat, 
                message.text,
                ]
            if all(conditions):
                if limit_of_days == -1\
                      or message.date > (datetime.datetime.now() - datetime.timedelta(days=limit_of_days)):
                    messages.append(message)
                    
        async for member in app.get_chat_members(chat.id):
            if member:
                members.append(member)
        return Parsed_Chat(members=members, messages=messages)
