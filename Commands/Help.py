import logging
from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import Constant

router = Router()

@router.message(F.text.lower() == "команды")
async def HelpCommands(ms: Message):
    try:
        text = ("назначить (роль)\nснять админку\nдать пред (на соо или по юзу)\n"
                "снять пред (на соо или по юзу)\nпосмотреть преды (на соо или по юзу)\nкик (на соо или по юзу)\nсписок участников\n"
                "цитата\nправда")
        await ms.reply(text)

    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await ms.reply(f"Произошла ошибка HelpCommands: {e}")