# Generates a JSON file with bitmap objects

from PIL import Image, ImageDraw, ImageFont

import parse_usb_hid_keys_h as parse
import sys
import json

#Adds a set of keys in a new languages
#Input: information about the new language & list of keys (format to be determined)
#       file to be modified
#Output: Modified file

img_width = 50
img_height = 50
font_file = 'arialbd.ttf'
big_pt = 22
small_pt = 16
mode = 'L'
base_colour = 'white'
text_colour = 'black'
bitmap_file = 'bitmaps.json'
data = {}
origin = (4, 0)

#def bitmap_generator()
    
    #JSON: language modifier, keycode, width, height, string of numbers
    #24-bit RGB
    
if __name__ == '__main__':
    #Parses a file with HID keycodes and key characters
    keylist = parse.parse_file()
    data['keys'] = []

    for keys in keylist:
        base = Image.new(mode, (img_width, img_height), base_colour)
        if len(keys.get_letter()) > 1:
            fnt = ImageFont.truetype(font=font_file, size=small_pt)
        else:
            fnt = ImageFont.truetype(font=font_file, size=big_pt)
        draw = ImageDraw.Draw(base)
        font_width, font_height = draw.textsize(keys.get_letter())
        draw.text(origin, keys.get_letter(), font=fnt, fill=text_colour)
        # Shows you the images
        base.show()
        # Will print out the strings
        #bytestring = str(base.tobytes())
        #print(bytestring)
        #
        # temp_bytes = base.tobytes()
        # temp_hex = temp_bytes.hex()
        # new_bytes = bytes.fromhex(temp_hex)

        # temp_str = temp_bytes.decode().encode()
        # Image.frombytes(data=temp_bytes, size=(50, 50), mode='L').show()


        data['keys'].append({
            'keycode': keys.get_keycode(),
            'height': img_height,
            'width': img_width,
            'letter': keys.get_letter(),
            'bitmap': base.tobytes().hex()
        })

    with open(bitmap_file, 'w') as outfile:
        json.dump(data, outfile)