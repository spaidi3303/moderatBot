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

def to_fancy_text(text: str, chatid):

    normal_lower = "abcdefghijklmnopqrstuvwxyz"
    normal_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""


    for char in text:
        if char.islower():
            index = normal_lower.index(char)
            result += fancy_format[chatid]["lower"][index]
        elif char.isupper():
            index = normal_upper.index(char)
            result += fancy_format[chatid]["upper"][index]
        else:
            result += char

    return result

text = "oleg"
res = to_fancy_text(text, -1002291981486)
print(res)