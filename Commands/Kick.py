import logging
from aiogram import Router, F
from aiogram.types import Message
import Constant
from Commands.GiveUsername import give_username, user_name
from Database import Connect

router = Router()

@router.message(F.text.lower().startswith("кик"),
                F.from_user.id.in_(Constant.admins),)
async def KickUser(ms: Message):
    if ms.reply_to_message:
        userid = ms.reply_to_message.from_user.id
    else:
        username = ms.text.split()[-1]
        userid = await user_name(ms, username)

    await ms.chat.ban(userid)
    db = Connect(userid, ms.chat.id)
    user = db.IfUser()
    del db
    
