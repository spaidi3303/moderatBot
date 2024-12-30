import logging
from aiogram import Router, F
from aiogram.types import Message
import Constant
from Commands.GiveUsername import give_username
from Database import Connect
from I_AM_GOD import I_AM_GOD

router = Router()

@router.message(F.text.lower().startswith("назначить"),
                F.from_user.id.in_(Constant.admins),
                F.reply_to_message.from_user,
                F.text.len() > 9)
async def Give_role_func(ms: Message):
    try:
        userid = ms.reply_to_message.from_user.id
        if userid == Constant.MY_ID:
            await I_AM_GOD(ms)
            return
        db = Connect(userid, ms.chat.id)
        if db.IfUser():
            await ms.answer("Пользователь уже есть в базе данных")
            return
        del db

        role = await to_fancy_text(ms.text[10:], ms.chat.id)

        await promote_admin(ms, ms.reply_to_message.from_user.id)
        db = Connect(userid, ms.chat.id)
        db.AddUser(role)

        await ms.chat.set_administrator_custom_title(ms.reply_to_message.from_user.id, role)
        username = await give_username(ms)
        await ms.answer(
            f"Администратор @{ms.from_user.username} дал {username} роль {role}")
        await ms.answer_sticker(
            sticker="CAACAgIAAyEFAASGBTcIAAMvZsZuCOgeBPzNzSZ8r05Mly2rsyAAAkUiAAKWaHFKuh9vhlNg01M1BA")

    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await ms.reply(f"Произошла ошибка Give_role_func: {e}")


async def promote_admin(ms: Message, userid):
    await ms.chat.promote(
        user_id=userid,
        is_anonymous=False,
        can_manage_chat=False,
        can_delete_messages=False,
        can_manage_video_chats=True,
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


fancy_format = {
    -1002260554438: {
        "lower": "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",
        "upper": "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
    },
    -1002291981486: {
        "lower": "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛",
        "upper": "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁"
    }
}

async def to_fancy_text(text: str, chatid):

    normal_lower = "abcdefghijklmnopqrstuvwxyz"
    normal_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""


    for char in text:
        if char.islower():
            index = normal_lower.index(char)
            result += fancy_format[chatid]["lower"][index]
        elif char.isupper():
            index = normal_upper.index(char)
            result += fancy_format[chatid]["upper"][index]
        else:
            result += char

    return result