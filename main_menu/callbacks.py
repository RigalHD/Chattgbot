from aiogram.types import CallbackQuery, FSInputFile
from aiogram import Router, F

from Neuro.chat import neuro_marketing
from parser.bot import parse_chat
from keyboards import inline

router = Router()


@router.callback_query(inline.MainMenuCbData.filter(F.action == "Parse_chat_limit"))
async def parse_chat_limit_handler(query: CallbackQuery, callback_data: inline.MainMenuCbData):
    await query.message.edit_text(text="Парсинг чата может занять некоторое время")
    try:
        await query.message.edit_text(
            text="Выберите лимит парсинга (Пример: 30 д. - парситься будет полследний месяц)", 
            reply_markup=inline.parse_chat_kb()
            )
    except Exception as e:
        print(e)
        await query.message.edit_text(
            text="Произошла ошибка", 
            reply_markup=inline.back_to_main_menu_kb()
            )


@router.callback_query(inline.ParseChatCbData.filter(F.action == "Parse_chat"))
async def parse_chat_handler(query: CallbackQuery, callback_data: inline.ParseChatCbData):
    await query.message.edit_text(text="Парсинг чата может занять некоторое время")
    try:
        chat = await parse_chat(callback_data.day_limit)
        chat.make_json_file(query.id)
        await query.message.answer_document(
            document=FSInputFile(
                f'bot_temp_files/{query.id}.json', 
                filename="data.json"
                ),
            caption='Файл с историей чата'
        )
        await query.message.edit_text(
            text="Парсинг прошел успешно. Хотите отправить данные на обработку в ChatGPT?", 
            reply_markup=inline.send_to_gpt_kb(query.id)
            )
        
    except Exception as e:
        print(e)
        await query.message.edit_text(
            text="Произошла ошибка", 
            reply_markup=inline.back_to_main_menu_kb()
            )
        

@router.callback_query(inline.SendToGPTCbData.filter(F.action == "Send_to_gpt"))
async def send_to_gpt_handler(query: CallbackQuery, callback_data: inline.SendToGPTCbData):
    await query.message.edit_text(text="Обработка данных может занять некоторое время")
    try:
        message_text=neuro_marketing(query_id=callback_data.query_id)
    except Exception as e:
        print(e)
        message_text="Произошла ошибка"
    finally:
        await query.message.edit_text(
            text=str(message_text), 
            reply_markup=inline.back_to_main_menu_kb()
            )


@router.callback_query(inline.MainMenuCbData.filter(F.action == "Back_to_main_menu"))
async def back_to_main_menu_handler(query: CallbackQuery, callback_data: inline.MainMenuCbData):
    db = UsersTable()
    permissions_level = await db.get_user_permissions_level(query.from_user.id)
    await query.message.edit_text(
        text="Главное меню", 
        reply_markup=inline.main_menu_kb(permissions_level)
        )
