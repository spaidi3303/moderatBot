from aiogram import Router

import Commands.Command_Router
import Events.Event_Router
import ListAdmins
import play.main
import error

router = Router()
router.include_router(Events.Event_Router.router)
router.include_router(Commands.Command_Router.router)
router.include_router(play.main.router)
router.include_router(ListAdmins.router)
router.include_router(error.router)