from aiogram import Router, F
from aiogram.types import Message
import random
import json

router = Router()


def read_json_ss(js_name):
    with open(f'play/{js_name}', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


@router.message(F.text.lower() == "цитата")
async def citaty(ms: Message):
    js_name = 'quotes.json'
    data = read_json_ss(js_name)
    max_number = len(data)
    num = random.randint(0, max_number)
    await ms.answer(data[num])


@router.message(F.text.lower() == "правда")
async def questions(ms: Message):
    js_name = 'questions.json'
    data = read_json_ss(js_name)
    max_number = len(data)
    num = random.randint(0, max_number)
    await ms.answer(data[num])
