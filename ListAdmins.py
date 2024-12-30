import logging
from aiogram import Router, F
from aiogram.types import Message
import Constant
from Database import Connect

router = Router()

@router.message(F.text == "Прочитать роли",
                F.from_user.id == Constant.MY_ID)
async def GiveAdmins(ms: Message):
    try:
        res = await ms.chat.get_administrators()
        for user in res:
            if not user.user.is_bot:
                userid = user.user.id
                role = user.custom_title.title()
                print(role)
                db = Connect(userid, ms.chat.id)
                try:
                    db.AddUser(role)

                finally:
                    del db


    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await ms.reply(f"Произошла ошибка GiveAdmins: {e}")