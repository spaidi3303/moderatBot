import logging
from aiogram import Router, F
from aiogram.types import Message
import Constant
from Commands.GiveUsername import give_username, user_name
from Database import Connect

router = Router()

@router.message(F.text.lower().startswith("дать пред"),
                F.from_user.id.in_(Constant.admins),)
async def give_pred(ms: Message):
    if ms.reply_to_message:
        username = await give_username(ms)
        userid = ms.reply_to_message.from_user.id
    else:
        username = ms.text.split()[-1]
        userid = await user_name(ms, username)

    db = Connect(userid, ms.chat.id)
    user = db.IfUser()
    del db
    if not user:
        await ms.answer(
            f'Пользователя нету в базе данных ')
        return
    db = Connect(userid, ms.chat.id)
    count = int(db.ReadCountPreds())
    db.AddPred(count + 1)
    await ms.answer(
        f"Пользователю {username} был выдан пред {count + 1} из 3 администратором @{ms.from_user.username}.")
    if count + 1 == 3:
        await ms.chat.ban(userid)
        role = db.ReadRole()
        await ms.answer(f"Роль Пользователя: {role}")
        db.DelRole()
        await ms.answer(
            f'Пользователь {username} был кикнут по достижению 3-х предов.')

@router.message(F.text.lower().startswith("снять пред"),
                F.from_user.id.in_(Constant.admins),)
async def DelOnePred(ms: Message):
    if ms.reply_to_message:
        username = await give_username(ms)
        userid = ms.reply_to_message.from_user.id
    else:
        username = ms.text.split()[-1]
        userid = await user_name(ms, username)
    db = Connect(userid, ms.chat.id)
    user = db.IfUser()
    del db

    if not user:
        await ms.answer(
            f'Пользователя нету в базе данных ')
        return

    db = Connect(userid, ms.chat.id)
    count = int(db.ReadCountPreds())
    if count == 0:
        await ms.answer("У пользователя нет предов")
        return
    await ms.answer(
        f"С пользователя {username} был снят пред администратором @{ms.from_user.username}.")
    db.AddPred(count - 1)

@router.message(F.text.lower().startswith("посмотреть преды"),
                F.from_user.id.in_(Constant.admins),)
async def ReadPredsUser(ms: Message):
    if ms.reply_to_message:
        username = await give_username(ms)
        userid = ms.reply_to_message.from_user.id
    else:
        username = ms.text.split()[-1]
        userid = await user_name(ms, username)
    db = Connect(userid, ms.chat.id)
    user = db.IfUser()
    del db

    if not user:
        await ms.answer(
            f'Пользователя нету в базе данных ')
        return

    db = Connect(userid, ms.chat.id)
    count = int(db.ReadCountPreds())
    print(count)
    if count is None:
        count = 0
    if count == 0:
        await ms.answer("У пользователя нет предов")
        return
    await ms.answer(f"У пользователя {count} преда")