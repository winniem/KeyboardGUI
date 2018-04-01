# Keyboard GUI

import sys
from PyQt5.QtWidgets import *
import serial
import json_operations as js
import update_keyboard as up

charfile = 'bitmaps.json'
keyfile = 'keylists.json'

# TODO: Implement saving layouts
# TODO: Implement saving with a new name (Add one last tab / new button)
# TODO: Implement deleting layouts
# TODO: Add COM ports
# TODO: (Bonus) Change push buttons text to images

class GUI(QWidget):

    def __init__(self):
        super().__init__()
        self.charlist = js.read_char_list(charfile)
        self.keylist = js.read_key_lists(keyfile)
        self.names = []
        self.buttons = []
        self.keyboard_list = QComboBox()
        self.current_layout = self.keylist[0]
        self.port = 'COM9'          # To not be hard coded later
        self.rotation = 90          # Degrees to rotate the image
        self.initUI()

    #Sets up the base window.
    def initUI(self):
        self.setWindowTitle('Dynamic Keyboard')

        button_grid = QGridLayout()

        # Defaults to first keyboard layout
        for key in self.current_layout[1]:
            self.names.append(key.get_letter())

        positions = [(i, j) for i in range(4) for j in range(3)]

        for position, name in zip(positions, self.names):
            button = QPushButton(name, self)
            self.buttons.append(button)
            button.setMinimumHeight(80)
            button_grid.addWidget(button, *position)

        # For various reasons can't use a nice for loop. Sorry :(
        self.buttons[0].clicked.connect(lambda: self.show_dialog(0))
        self.buttons[1].clicked.connect(lambda: self.show_dialog(1))
        self.buttons[2].clicked.connect(lambda: self.show_dialog(2))
        self.buttons[3].clicked.connect(lambda: self.show_dialog(3))
        self.buttons[4].clicked.connect(lambda: self.show_dialog(4))
        self.buttons[5].clicked.connect(lambda: self.show_dialog(5))
        self.buttons[6].clicked.connect(lambda: self.show_dialog(6))
        self.buttons[7].clicked.connect(lambda: self.show_dialog(7))
        self.buttons[8].clicked.connect(lambda: self.show_dialog(8))
        self.buttons[9].clicked.connect(lambda: self.show_dialog(9))
        self.buttons[10].clicked.connect(lambda: self.show_dialog(10))
        self.buttons[11].clicked.connect(lambda: self.show_dialog(11))

       # for button in self.buttons:
        #    button.clicked.connect(lambda: self.show_dialog(button))

        # Top menus
        menu_box = QHBoxLayout()
        for name, key in self.keylist:
            self.keyboard_list.addItem(name)
        self.keyboard_list.activated[str].connect(self.select_layout)
        self.keyboard_list.setEditable(True)
        menu_box.addWidget(self.keyboard_list)

        # Bottom pushbuttons
        save_layout = QPushButton("Save Layout Changes")
        save_layout.clicked.connect(lambda: self.save())
        delete_layout = QPushButton("Delete Layout")
        delete_layout.clicked.connect(lambda: self.delete())
        update_keyboard = QPushButton("Update Keyboard")
        update_keyboard.clicked.connect(lambda: self.upload())

        # Laying out bottom buttons
        hbox = QHBoxLayout()
        hbox.addWidget(save_layout)
        hbox.addWidget(delete_layout)
        hbox.addWidget(update_keyboard)

        # Putting all the boxes together
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(menu_box)
        vbox.addStretch(3)
        vbox.addLayout(button_grid)
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.show()

    def show_dialog(self, position):
        dialog = QInputDialog()
        letters = []
        for character in self.charlist:
            letters.append(character.get_letter())

        item, ok = dialog.getItem(dialog, 'Select Key', 'Select a new key:', letters)

        if ok:
            self.buttons[position].setText(item)
            self.names[position] = item


    def select_layout(self, text):
        index = 0
        # TODO: Implement special function for if 'Create New Layout' was selected
        # if text == 'Create New Layout':
        #     hello = 1
        #     # Pop up a dialog asking for text input
        #     # Save a new keylist with the dialog input name and current keys
        #     # Add the keyboard name to the middle of the list and make the widget jump to it?
        #
        # else:
        for name, key in self.keylist:
            if name == text:
                self.current_layout = self.keylist[index]
            index += 1
        self.names = []
        for key in self.current_layout[1]:
            self.names.append(key.get_letter())

        for index, button in enumerate(self.buttons):
            button.setText(self.names[index])

    def newlayout(self):
        hello = 1


    def upload(self):
        up.update_keyboard(self.current_layout[1], self.port, self.rotation)

    def save(self):
        #if self.keyboard_list.currentText() != self.current_layout[0]:
        # TODO: Save the current key list to the index
        # TODO: Write all the keylists to the JSON file

    def delete(self):
        hello = 1
        # TODO: Switch to the previous item
        # TODO: Delete the current row and the keylist in the file
        # TODO: Write all the keylists to the JSON file

    # #Returns list of all ports
    # #each port_list object has
    # # [0] = com port name
    # # [1] = name of connected object
    #
    # def ports():
    #     return list(serial.tools.list_ports.comports())
