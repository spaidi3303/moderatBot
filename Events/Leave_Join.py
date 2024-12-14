import logging

from aiogram import Router, F
from aiogram.types import Message

from Constant import MY_ID, DEAN
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
            f"➳ Любимый фильм/сериал\n➳ Что любишь, а что ненавидешь\n"
            f"{DEAN.admins_us.value}")

    return text


@router.message(F.new_chat_members)
async def JoinUser(ms: Message):
    try:
        for new_member in ms.new_chat_members:
            if new_member.id == MY_ID:
                await I_AM_GOD(ms)
                await ms.answer("Добро пожаловать, хозяин!")
            if ms.from_user.id == new_member.id:
                text = await Saluts(ms.from_user)
                await ms.answer(text)

            else:
                text = await Saluts(new_member)
                await ms.answer(text)

    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await ms.reply(f"Произошла ошибка JoinUser: {e}")
        

@router.message(F.left_chat_member)
async def LeaveUser(ms: Message):
    try:
        left_user = ms.left_chat_member

        if ms.from_user.id == left_user.id:
            user = left_user
            await Lefts(user, ms)
        else:
            user = left_user
            await Lefts(user, ms)

    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await ms.reply(f"Произошла ошибка LeaveUser: {e}")

async def Lefts(user, ms: Message):
    userid = user.id
    if user.username:
        mention_text = f"@{user.username}"
    else:
        mention_text = f"<a href='tg://user?id={user.id}'>{user.full_name}</a>"

    db = Connect(userid)
    try:
        user = db.IfUser()
        if not user:
            await ms.answer(
                f"{mention_text} покинул группу. Но его не было в базе данных. {DEAN.admins_us.value}")
            return
    finally:
        del db

    db = Connect(userid)
    try:
        role = db.ReadRole()
        await ms.answer(f"{mention_text} покинул группу. Роль {role}. {DEAN.admins_us.value}")
        db.DelRole()
    finally:
        del db