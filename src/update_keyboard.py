# Update keyboard function to send the updated keycodes and bitmaps to a microcontroller
# Transfers the data using the python XMODEM library

# Inputs: key_list - a list of key_character objects
# Outputs: Sends the key_character data in the keylist to the connected microcontroller

# TODO: Tal look into how COM ports are recognized and addressed
#       ideally this would involve reading all the device COM ports
#       and finding the one that matches the device name. Ask David
#       for the device name
#       If COM port stuff is complicated enough we may want to look into making it user-selectable

def update_keyboard(key_list)
    