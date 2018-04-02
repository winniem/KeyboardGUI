import update_keyboard as up
import json
import key_character as keychar
import json_operations as js

#Test
if __name__ == '__main__':
    char_list = js.read_char_list('bitmaps.json')
    key_list = char_list[12:24]
    up.update_keyboard(key_list, 'COM6', 270)