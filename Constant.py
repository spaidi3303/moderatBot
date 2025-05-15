import os
from dotenv import load_dotenv
load_dotenv("secrets.env")
TOKEN = os.getenv("token")

host = os.getenv('host')
user = os.getenv('user')
database = os.getenv('database')
password = os.getenv('password')

rk = {
    -1002260554438: "bunker_rk",
    -1002291981486: "spiderworld_rk"
}
admins_us = {
    -1002260554438: "@impalapie67 @sammylwm",
}

admins = {2098644058, 752640376, 1576223619}

MY_ID = 2098644058

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