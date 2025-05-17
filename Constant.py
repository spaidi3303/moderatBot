import os
from dotenv import load_dotenv
load_dotenv("secrets.env")
TOKEN =os.getenv("TOKEN")

host = os.getenv('host')
user = os.getenv('user')
database = os.getenv('database')
password = os.getenv('password')

rk = {
    "id": "name",
}
admins_us = {
   "id": "admins"
}

admins = {"ids"}

MY_ID = 'myid'

fancy_format = {
    "id": {
        "lower": "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",
        "upper": "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
    },
}