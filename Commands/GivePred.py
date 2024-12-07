import logging
from aiogram import Router, F
from aiogram.types import Message
import Constant
from Commands.GiveUsername import give_username
from Database import Connect

router = Router()

@router.message(F.text.lower() == "дать пред",
                F.from_user.id.in_(Constant.DEAN.admins.value),
                F.reply_to_message)
async def give_pred(ms: Message):
    try:
        userid = ms.reply_to_message.from_user.id
        username = await give_username(ms)
        db = Connect(userid)
        user = db.IfUser()
        del db
        if not user:
            await ms.answer(
                f'Пользователя нету в базе данных ')
            return
        db = Connect(userid)
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

    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await ms.reply(f"Произошла ошибка give_pred: {e}")

@router.message(F.text.lower() == "снять пред",
                F.from_user.id.in_(Constant.DEAN.admins.value),
                F.reply_to_message)
async def DelOnePred(ms: Message):
    try:
        userid = ms.reply_to_message.from_user.id
        username = await give_username(ms)
        db = Connect(userid)
        user = db.IfUser()
        del db

        if not user:
            await ms.answer(
                f'Пользователя нету в базе данных ')
            return

        db = Connect(userid)
        count = int(db.ReadCountPreds())
        if count == 0:
            await ms.answer("У пользователя нет предов")
            return
        await ms.answer(
            f"С пользователя {username} был снят пред администратором @{ms.from_user.username}.")
        db.AddPred(count - 1)

    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await ms.reply(f"Произошла ошибка DelOnePred: {e}")

@router.message(F.text.lower() == "посмотреть преды",
                F.from_user.id.in_(Constant.DEAN.admins.value),
                F.reply_to_message)
async def ReadPredsUser(ms: Message):
    try:
        userid = ms.reply_to_message.from_user.id
        db = Connect(userid)
        user = db.IfUser()
        del db

        if not user:
            await ms.answer(
                f'Пользователя нету в базе данных ')
            return

        db = Connect(userid)
        count = int(db.ReadCountPreds())
        if count is None:
            count = 0
        if count == 0:
            await ms.answer("У пользователя нет предов")
            return
        await ms.answer(f"У пользователя {count} преда")

    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await ms.reply(f"Произошла ошибка ReadPredsUser: {e}")