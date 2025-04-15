import logging
from aiogram import Router, F
from aiogram.types import Message
import Constant
from Database import Connect

router = Router()

@router.message(F.text.lower() == "список участников",
                F.from_user.id.in_(Constant.admins),)
async def ListMembers(ms: Message):
    db = Connect(1, ms.chat.id)
    array = {}
    res = db.ReadAllId()
    ids = []
    for Array in res:
        ids.append(Array["userid"])
    del db

    for userid in ids:
        username = await read_username_id(ms, userid)
        db = Connect(userid, ms.chat.id)
        try:
            role = db.ReadRole()
            array[username] = role
        finally:
            del db
    text = ''
    num = 1
    for i, j in array.items():
        text += f"{num}. {i} : {j}\n"
        num += 1

    await ms.answer(text)

async def read_username_id(ms: Message, userid):
        res = await ms.chat.get_member(userid)
        if res.user.username:
            username = '@' + f"{res.user.username}"
        else:
            username = f"<a href='tg://user?id={userid}'>{res.user.full_name}</a>"
        return username