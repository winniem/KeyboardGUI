import update_keyboard as up
import json
import key_character as keychar

def read_charlist(filename):
    charlist = []
    with open(filename) as json_file:
        data = json.load(json_file)
        for key in data['keys']:
            newkey = keychar.key_character(keycode=key['keycode'], height=key['height'],
                                           width=key['width'], bitmap=key['bitmap'], letter=key['letter'])
            charlist.append(newkey)
    return charlist

#Test
if __name__ == '__main__':
    char_list = read_charlist('bitmaps.json')
    key_list = char_list[12:24]
    up.update_keyboard(key_list, 'COM9', 270)