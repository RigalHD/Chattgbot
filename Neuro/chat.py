import openai
from dotenv import load_dotenv
from os import getenv
import os
import json


def neuro_marketing(query_id: int) -> tuple[str]:
    if isinstance(query_id, int):
        # Следующий код нужно раскомментировать, после получения доступа к api chatgpt
        # load_dotenv()
        # openai_key = getenv("openai_api_token")
        # openai.api_key = openai_key
        # prompt =\
        #     "Ты профессиональный маркетолог."\
        #     "Выбираешь самые важные смыслы из текста чата, в котором общаются люди."\
        #     "Найди топ-10 темы для создания рекламной стратегии."
        # В prompt нужно вставить основной промпт для gpt, чтобы он понял свою роль
        with open(f'bot_temp_files/{query_id}.json', 'r') as file:
            data = json.load(file)
        # os.remove(f'bot_temp_files/{query_id}.json')
        chat_messages_text = "\n".join(
            [data[key]["text"] for key in data.keys() if data[key]["text"]]
            )

        chat_gpt_answers: list[str] = []
        # print(len(chat_messages_text))
        requests_count: int = len(chat_messages_text) // 50000 + 1 \
            if len(chat_messages_text) % 50000 != 0 else len(chat_messages_text) // 50000
        # Так как один промпт ограничен по токенам, будет сделано несколько промптов
        for n in range(requests_count):
            """
            Следующий код нужно раскомментировать, после получения доступа к api chatgpt,
            а так же нужно после этого удалить/закомментировать последнюю строку
            """
            # result = openai.ChatCompletion.create(
            #     model="gpt-4o",
            #     messages=[
            #             {"role": "system", "content": prompt},
            #             {"role": "user", "content": chat_messages_text[n * 50000 : (n + 1) * 50000]}
            #         ],
            #     temperature = 0
            #     )

            # chat_gpt_answers.append(result['choices'][0]['message']['content'])
            chat_gpt_answers.append(f"text_{n}") # заглушка
        
        return tuple(chat_gpt_answers)
