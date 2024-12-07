from aiogram import Router

from Commands import Give_Role, Del_Role, MutAndAnmut, Kick, GivePred, List_Members
router = Router()
router.include_router(Give_Role.router)
router.include_router(Del_Role.router)
router.include_router(MutAndAnmut.router)
router.include_router(Kick.router)
router.include_router(GivePred.router)
router.include_router(List_Members.router)
