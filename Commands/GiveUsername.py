from aiogram.types import Message


async def give_username(ms: Message):
    if ms.reply_to_message:
        user = ms.reply_to_message.from_user
        if user.username:
            username = f"@{user.username}"
        else:
            username = f"<a href='tg://user?id={user.id}'>{user.full_name}</a>"
    else:
        username1 = ms.text.split()[-1]
        if username1[-1] == '@':
            username = username1
        else:
            userid = await user_name(ms, username1)
            username = f"<a href='tg://user?id={userid}'>{username1}</a>"
    return username


async def user_name(ms, username):
    res = await ms.chat.get_administrators()
    for i in res:
        if not i.user.is_bot:
            if username[0] == '@':
                us = f"@{i.user.username}"
            else:
                us = i.user.full_name
            if us == username:
                userid = i.user.id
                return userid
                