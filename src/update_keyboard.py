# Update keyboard function to send the updated keycodes and bitmaps to a microcontroller
# Transfers the data using the python XMODEM library

# Inputs: key_list - a list of key_character objects, port, image rotation (counterclockwise, in degrees)
# Outputs: Sends the key_character data in the keylist to the connected microcontroller

# TODO: Tal look into how COM ports are recognized and addressed
#       ideally this would involve reading all the device COM ports
#       and finding the one that matches the device name. Ask David
#       for the device name
#       If COM port stuff is complicated enough we may want to look into making it user-selectable
#       Add in a reasonable time-out while the data is transferred

from xmodem import XMODEM
import serial
from PIL import Image
import time
from io import StringIO
from io import BytesIO



def update_keyboard(keylist, port, rotation):
    key_identifier = bytearray.fromhex('DEAD')
    key_data = []
    binary_file = 'binary_file.bin'
    max_keys = 12

    # key_data has (keycode, width, height, bitmap)
    for keys in keylist:
        # bitmap_string = keys.get_bitmap().replace('\\', ' ')
        # bitmap_string.split(sep=' ', maxsplit=1)
        # bitmap_bytes = bytearray.fromhex(bitmap_string)
        # bytes.fromhex(keys.get_bitmap())
        key_data.append((keys.get_keycode(), keys.get_width(), keys.get_height(),
                         Image.frombytes(mode='L', data=bytes.fromhex(keys.get_bitmap()),
                                         size=(keys.get_width(), keys.get_height())).rotate(rotation)))
        # with StringIO(keys.get_bitmap()) as imgfile:
        #     key_data.append((keys.get_keycode(), keys.get_width(), keys.get_height(),
        #                      Image.open(imgfile).rotate(rotation)))
        # with BytesIO(bytearray(keys.get_bitmap(), encoding='utf-8')) as imgfile:
        #     key_data.append((keys.get_keycode(), keys.get_width(), keys.get_height(),
        #                      Image.open(imgfile).rotate(rotation)))
        # images.append(Image.open(io.BytesIO(keys.getbitmap())).rotate(rotation))
        # keycodes.append(keys.get_keycodes())
        # key_height.append(keys.get_height())
        # key_width.append(keys.get_width())

    # Generate the binary file to send
    with open(binary_file, 'wb') as f:          # Should erase existing files when it's opened for writing
        #write_data.append(key_identifier)
        #f.write(key_identifier)
        #print(bytes(key_identifier))

        count = 0
        for index, image in zip(range(max_keys), key_data):
            f.write(key_identifier)
            f.write(count.to_bytes(1, 'big'))
            count += 1
            f.write((int(image[0], 16)).to_bytes(1, 'big'))
            f.write(image[1].to_bytes(1, 'big'))
            f.write(image[2].to_bytes(1, 'big'))
            f.write(image[3].tobytes())
            #image[3].show()
            #f.write(image[i])
            #for i in range(0, 4):
            # for i, item in enumerate(image, 0):
            #     #f.write(bytes(image[i]))
            #     #write_data = write_data.join(bytes(image[i]))
            #     print(bytes(image[i]), encoding='utf-8')

    # Send the file
    ser = serial.Serial(port, timeout=0)

    # Not reading
    def getc(size, timeout=1):
        return None

    # Data to send
    def putc(data, timeout=1):
        ser.write(data)
        time.sleep(0.001)  # delay for safety reasons

    modem = XMODEM(getc, putc)
    stream = open(binary_file, 'rb')
    modem.send(stream)