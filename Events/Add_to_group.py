import logging

from aiogram import Router, F
from aiogram.filters import JOIN_TRANSITION, ChatMemberUpdatedFilter
from aiogram.types import Message, ChatMemberUpdated

from Constant import MY_ID

router = Router()

@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
async def bot_added(event: ChatMemberUpdated):
    print(event.chat.id)
    print(event.from_user.id)
    # if event.from_user.id != MY_ID:
    #     await event.answer("Право добавлять Бота в группу имеет только создатель бота.")
    #     await event.bot.leave_chat(event.chat.id)