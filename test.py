fancy_format = {
    "lower": "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",
    "upper": "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
}

def to_fancy_text(text: str):
    normal_lower = "abcdefghijklmnopqrstuvwxyz"
    normal_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""


    for char in text:
        if char.islower():
            index = normal_lower.index(char)
            result += fancy_format["lower"][index]
        elif char.isupper():
            index = normal_upper.index(char)
            result += fancy_format["upper"][index]
        else:
            result += char

    return result

print(to_fancy_text("own Sam/Peter" ))