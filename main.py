import asyncio
import logging
from aiogram import Dispatcher
from aiogram.methods import DeleteWebhook
from aiogram import Bot
from all_routers import router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import Message
from Constant import TOKEN
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()
dp.include_router(router)


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
