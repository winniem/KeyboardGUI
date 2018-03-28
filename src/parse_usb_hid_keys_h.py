import key_character as keychar

def parse_file():
    file = open("usb_hid_keys.h", "r")
    keylist = []
    height = 0
    width = 0

    for line in file:
        goodline = line[8:].split(" ")
        if line.startswith("#define ") and len(goodline)>1:
            key1 = goodline[0]
            key = key1.split("_")[1]
            value = ""
            for i in range(1, len(goodline)):
                if goodline[i] == "":
                    continue
                else:
                    value = goodline[i].rsplit()[0]
                    break

            # do whatever you wanna do with the scancode name, and its hex value
            # Debug purposes
            # print("\"{}\": \"{}\",".format(key, value))

            newkey = keychar.key_character(keycode=value, height=height, width=width, bitmap="", letter=key)

            keylist.append(newkey)

    return keylist
