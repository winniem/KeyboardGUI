# Update keyboard function to send the updated keycodes and bitmaps to a microcontroller
# Transfers the data using the python XMODEM library

# Inputs: key_list - a list of key_character objects, port, image rotation (counterclockwise, in degrees)
# Outputs: Sends the key_character data in the keylist to the connected microcontroller
# TODO: Implement some sort of check/behaviour if the image is too large (50x50 should be the max)
#       recommendation is the PIL.ImagesOps.fit() function

from xmodem import XMODEM
import serial
from PIL import Image
import time

def update_keyboard(keylist, port, rotation):
    key_identifier = bytearray.fromhex('DEAD')
    key_data = []
    binary_file = 'binary_file.bin'
    max_keys = 12

    # key_data has (keycode, width, height, bitmap)
    for keys in keylist:
        key_data.append((keys.get_keycode(), keys.get_width(), keys.get_height(),
                         Image.frombytes(mode='L', data=bytes.fromhex(keys.get_bitmap()),
                                         size=(keys.get_width(), keys.get_height())).rotate(rotation)))

    # Generate the binary file to send
    with open(binary_file, 'wb') as f:          # Should erase existing files when it's opened for writing
        count = 0
        for index, image in zip(range(max_keys), key_data):
            f.write(key_identifier)
            f.write(count.to_bytes(1, 'big'))
            count += 1
            f.write((int(image[0], 16)).to_bytes(1, 'big'))
            f.write(image[1].to_bytes(1, 'big'))
            f.write(image[2].to_bytes(1, 'big'))
            f.write(image[3].tobytes())

    # Send the file
    ser = serial.Serial(port, timeout=1,  baudrate=115200)

    # Not reading
    def getc(size, timeout=1):
        return ser.read(size)

    # Data to send
    def putc(data, timeout=1):
        ser.write(data)
        time.sleep(0.001)  # delay for safety reasons

    modem = XMODEM(getc, putc)
    stream = open(binary_file, 'rb')
    print(modem.send(stream, timeout=2))

    ser.close()
