# Various JSON operations:
# Read all key characters from a json file
# Write key characters to a json file
# Read all key lists from a json file
# Write all key lists to a json file

import json
import key_character as keychar

# Inputs: A JSON file that contains key characters under the category 'keys'
#         Each key character should contain 'keycode', 'height', 'width', 'bitmap'
#         and 'letter' tags
# Outputs: Returns all key characters in the file as a list of key characters

def read_char_list(filename):
    char_list = []
    with open(filename) as json_file:
        data = json.load(json_file)
        for key in data['keys']:
            newkey = keychar.key_character(keycode=key['keycode'], height=key['height'],
                                           width=key['width'], bitmap=key['bitmap'], letter=key['letter'])
            char_list.append(newkey)
    return char_list

# Inputs:  A JSON file that contains all layout names with the category "Layout Names" and
#          key character lists with the category tag as the list name
#          Each key character should contain 'keycode', 'height', 'width', 'bitmap'
#          and 'letter' tags
# Outputs: Returns a list of tuples formatted as ('name', key_list)
# Warning: If the file already exists it will be rewritten

def read_key_lists(filename):
    key_lists = []

    with open(filename) as json_file:
        data = json.load(json_file)

        for name in data['Layout Names']:
            layout_list = []
            str_name = name['name']
            for key in data[str_name]:
                newkey = keychar.key_character(keycode=key['keycode'], height=key['height'],
                                               width=key['width'], bitmap=key['bitmap'], letter=key['letter'])
                layout_list.append(newkey)
            key_lists.append((str_name, layout_list))
    return key_lists

# Inputs: A list of key characters and a filename with a '.json' extension
# Outputs: A JSON file that contains key characters under the category 'keys'
#          Each key character should contain 'keycode', 'height', 'width', 'bitmap'
#          and 'letter' tags
# Warning: If the file already exists it will be rewritten

def write_char_list(char_list, filename):
    data = []

    for key in char_list:
        data['keys'].append({
            'keycode': key.get_keycode(),
            'height': key.get_height(),
            'width': key.get_width(),
            'letter': key.get_letter(),
            'bitmap': key.get_bitmap()
        })

    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

# Inputs: A list of tuples formatted as ('name', key_list)
# Outputs: A JSON file that contains all layout names with the category "Layout Names" and
#          key character lists with the category tag as the list name
#          Each key character should contain 'keycode', 'height', 'width', 'bitmap'
#          and 'letter' tags
# Warning: If the file already exists it will be rewritten
def write_key_lists(key_lists, filename):
    data = {}

    data['Layout Names'] = []
    for name, key_list in key_lists:
        data['Layout Names'].append({
            'name': name
        })

    for name, key_list in key_lists:
        data[name] = []
        for key in key_list:
            data[name].append({
                'keycode': key.get_keycode(),
                'height': key.get_height(),
                'width': key.get_width(),
                'letter': key.get_letter(),
                'bitmap': key.get_bitmap()
            })
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)