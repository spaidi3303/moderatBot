import asyncio
import logging
from aiogram import Router, F
from aiogram.types import Message, ChatPermissions
import Constant
from datetime import datetime, timedelta

from Commands.GiveUsername import give_username, user_name
from Commands.Give_Role import promote_admin
from Database import Connect

router = Router()

@router.message(F.text.lower().startswith("мут"),
                F.from_user.id.in_(Constant.admins),
                F.reply_to_message.from_user,)
async def Mut(ms: Message):
    minute = 0
    if len(ms.text.split()) > 1:
        time_1 = int(ms.text.split()[1])
        time_2 = ms.text.split()[2]
        if time_2.lower() in ["неделя", "недели", 'недель']:
            minute = 10080 * time_1
        elif time_2.lower() in ['день', 'дней']:
            minute = 1440 * time_1
        elif time_2.lower() in ['час', 'часа', 'часов']:
            minute = 60 * time_1
        elif time_2.lower() in ['минута', 'минут']:
            minute = time_1
        time1 = ms.text.split()[1]
        time2 = ms.text.split()[2]
    else:
        minute = 1440
        time1 = 1
        time2 = 'день'

    userid = ms.reply_to_message.from_user.id

    now = datetime.utcnow()
    offset = timedelta(hours=3)
    local_time = now + offset

    until_date = local_time + timedelta(minutes=minute)
    await ms.chat.restrict(
        user_id=userid,
        permissions=ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_polls=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False
        ),
        until_date=until_date
    )

    username = await give_username(ms)

    db = Connect(userid, ms.chat.id)
    res = db.IfUser()
    del db
    if res is None:
        await ms.answer(
            f"Пользователю {username} был выдан мут администратором @{ms.from_user.username} на {time1} {time2}. Подумайте о своём поведении!")
    else:

        await ms.answer(
            f"Пользователю {username} был выдан мут администратором @{ms.from_user.username} на {time1} {time2}. Подумайте о своём поведении!")

        await asyncio.sleep(minute * 60)

        db = Connect(userid, ms.chat.id)
        role = db.ReadRole()
        del db

        await promote_admin(ms, userid)
        await ms.chat.set_administrator_custom_title(ms.reply_to_message.from_user.id, role)
        await ms.answer(
            f"с пользователя {username} был снять мут, и впредь следите за своим языком!")
        
@router.message(F.text.lower().startswith("анмут"),
                F.from_user.id.in_(Constant.admins),)
async def UnMut(ms: Message):
    if ms.reply_to_message:
        username = await give_username(ms)
        userid = ms.reply_to_message.from_user.id
    else:
        username = ms.text.split()[-1]
        userid = await user_name(ms, username)

    await ms.chat.restrict(
        user_id=ms.reply_to_message.from_user.id,
        permissions=ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_polls=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False
        )
    )

    db = Connect(userid, ms.chat.id)
    user = db.IfUser()
    del db

    if not user:
        await ms.answer(
            f"с пользователя {username} был снять мут, и впредь следите за своим языком!")
    else:
        await ms.answer(
            f"с пользователя {username} был снять мут, и впредь следите за своим языком!")

        db = Connect(ms.reply_to_message.from_user.id, ms.chat.id)
        try:
            role = db.ReadRole()
        finally:
            del db

        await promote_admin(ms, ms.reply_to_message.from_user.id)
        await ms.chat.set_administrator_custom_title(ms.reply_to_message.from_user.id, role)