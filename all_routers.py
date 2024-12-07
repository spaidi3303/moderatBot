from aiogram import Router

import Commands.Command_Router
import Events.Event_Router
import play.main

router = Router()
router.include_router(Events.Event_Router.router)
router.include_router(Commands.Command_Router.router)
router.include_router(play.main.router)