from aiogram import Router

from Events.Add_to_group import router as Event_Router
from Events.Leave_Join import router as Leave_Join_router

router = Router()

router.include_router(Event_Router)
router.include_router(Leave_Join_router)