import logging

from aiogram import Router, F
from aiogram.types import Message

from Constant import MY_ID, admins_us
from I_AM_GOD import I_AM_GOD
from Database import Connect

router = Router()

async def Saluts(user):

    if user.username:
        mention_text = f"@{user.username}"
    else:
        mention_text = f"<a href='tg://user?id={user.id}'>{user.full_name}</a>"
    text = (f"{mention_text}, Добро пожаловать. Ответьте на вопросы:\n"
            f"➳ Когда у тебя день рождения\n➳ Чем любишь заниматься\n"
            f"➳ Любимый фильм/сериал\n➳ Что любишь, а что ненавидешь\n")

    return text


@router.message(F.new_chat_members)
async def JoinUser(ms: Message):
    for new_member in ms.new_chat_members:
        if new_member.id == MY_ID:
            await I_AM_GOD(ms)
            await ms.answer("Добро пожаловать, хозяин!")
        if ms.from_user.id == new_member.id:
            text = await Saluts(ms.from_user)
            await ms.answer(text)

        else:
            text = await Saluts(new_member)
            text+=f"{admins_us[ms.chat.id]}"
            await ms.answer(text)


@router.message(F.left_chat_member)
async def LeaveUser(ms: Message):
    left_user = ms.left_chat_member

    if ms.from_user.id == left_user.id:
        user = left_user
        await Lefts(user, ms)
    else:
        user = left_user
        await Lefts(user, ms)


async def Lefts(user, ms: Message):
    userid = user.id
    if user.username:
        mention_text = f"@{user.username}"
    else:
        mention_text = f"<a href='tg://user?id={user.id}'>{user.full_name}</a>"

    db = Connect(userid, ms.chat.id)
    try:
        user = db.IfUser()
        if not user:
            await ms.answer(
                f"{mention_text} покинул группу. Но его не было в базе данных. {admins_us[ms.chat.id]}")
            return
    finally:
        del db

    db = Connect(userid, ms.chat.id)
    try:
        role = db.ReadRole()
        await ms.answer(f"{mention_text} покинул группу. Роль {role}. {admins_us[ms.chat.id]}")
        db.DelRole()
    finally:
        del db