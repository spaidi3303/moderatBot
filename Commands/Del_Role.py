import logging
from aiogram import Router, F
from aiogram.types import Message
import Constant
from Commands.GiveUsername import give_username
from Database import Connect

router = Router()


@router.message(F.text.lower().startswith("снять админку"),
                F.from_user.id.in_(Constant.admins),
                F.reply_to_message.from_user,)
async def DelRole(ms: Message):
    userid = ms.reply_to_message.from_user.id
    username = await give_username(ms)
    await promote_un_admin(ms, userid)
    db = Connect(userid, ms.chat.id)
    if db.IfUser() is None:
        await ms.answer(
            f'Пользователя нету в базе данных ')
        return
    await ms.answer(f"Роль пользователя: {db.ReadRole()}")
    db.DelRole()
    del db

    await ms.answer(
        f'С пользователя {username} была снята админка администратором @{ms.from_user.username}')


async def promote_un_admin(ms: Message, userid):
    await ms.chat.promote(
        user_id=userid,
        is_anonymous=False,
        can_manage_chat=False,
        can_delete_messages=False,
        can_manage_video_chats=False,
        can_restrict_members=False,
        can_promote_members=False,
        can_change_info=False,
        can_invite_users=False,
        can_post_stories=False,
        can_edit_stories=False,
        can_delete_stories=False,
        can_post_messages=True,
        can_edit_messages=True,
        can_pin_messages=False,
        can_manage_topics=False,
    )

@router.message(F.text.lower().startswith("удалить роль"), F.from_user.id.in_(Constant.admins))
async def DelROleRole(ms: Message):
    db = Connect(1, ms.chat.id)
    role = ms.text[13:]
    db.DelRoleRole(role)
    await ms.answer("Роль была успешно удалена!")