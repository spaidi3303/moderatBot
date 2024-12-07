import logging
from aiogram import Router, F
from aiogram.types import Message
import Constant
from Commands.GiveUsername import give_username
from Database import Connect

router = Router()

@router.message(F.text.lower() == "кик",
                F.from_user.id.in_(Constant.DEAN.admins.value),
                F.reply_to_message.from_user)
async def KickUser(ms: Message):
    try:
        userid = ms.reply_to_message.from_user.id
        await ms.chat.ban(userid)
        db = Connect(userid)
        user = db.IfUser()
        del db
        if user:
            db = Connect(userid)
            role = db.ReadRole()
            await ms.answer(f"Роль Пользователя: {role}")
            db.DelRole()
            del db

    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await ms.reply(f"Произошла ошибка KickUser: {e}")