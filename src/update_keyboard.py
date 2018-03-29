# Update keyboard function to send the updated keycodes and bitmaps to a microcontroller
# Transfers the data using the python XMODEM library

# Inputs: key_list - a list of key_character objects
# Outputs: Sends the key_character data in the keylist to the connected microcontroller

# TODO: Tal look into how COM ports are recognized and addressed
#       ideally this would involve reading all the device COM ports
#       and finding the one that matches the device name. Ask David
#       for the device name
#       If COM port stuff is complicated enough we may want to look into making it user-selectable
#       Add in a reasonable time-out while the data is transferred

from xmodem import XMODEM
import serial
key_identifier = 0xDEAD
key_width = 50
key_height = 50
rotation = 90
offset = (0,0)

def update_keyboard(keylist, port, offset):

    #Generate the file to send
    #Apply offset and rotation to the image
    for keys in keylist:

    #Send the file
    ser = serial.Serial(port)

def generate_binary(keylist, offset):

#offset is a tuple that signals where to start the image (0,0) is the top left
def offset_rotate(keylist, offset, rotation):

