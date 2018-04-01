# Keyboard GUI

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
import json_operations as js
import update_keyboard as up
from PyQt5.QtCore import Qt

charfile = 'bitmaps.json'
keyfile = 'keylists.json'

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
        self.buttons[0].clicked.connect(lambda: self.change_key(0))
        self.buttons[1].clicked.connect(lambda: self.change_key(1))
        self.buttons[2].clicked.connect(lambda: self.change_key(2))
        self.buttons[3].clicked.connect(lambda: self.change_key(3))
        self.buttons[4].clicked.connect(lambda: self.change_key(4))
        self.buttons[5].clicked.connect(lambda: self.change_key(5))
        self.buttons[6].clicked.connect(lambda: self.change_key(6))
        self.buttons[7].clicked.connect(lambda: self.change_key(7))
        self.buttons[8].clicked.connect(lambda: self.change_key(8))
        self.buttons[9].clicked.connect(lambda: self.change_key(9))
        self.buttons[10].clicked.connect(lambda: self.change_key(10))
        self.buttons[11].clicked.connect(lambda: self.change_key(11))

       # for button in self.buttons:
        #    button.clicked.connect(lambda: self.show_dialog(button))

        # Top menus
        menu_box = QHBoxLayout()
        for name, key in self.keylist:
            self.keyboard_list.addItem(name)
        # self.keyboard_list.activated[str].connect(self.select_layout)
        self.keyboard_list.setEditable(True)
        self.keyboard_list.editTextChanged.connect(lambda: self.select_layout())
        menu_box.addWidget(self.keyboard_list)
        enter = QShortcut(QKeySequence(Qt.Key_Return), self)
        enter.activated.connect(self.new_layout)

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

    def change_key(self, position):
        dialog = QInputDialog()
        letters = []
        for character in self.charlist:
            letters.append(character.get_letter())

        item, ok = dialog.getItem(dialog, 'Select Key', 'Select a new key:', letters)

        if ok:
            self.buttons[position].setText(item)
            self.names[position] = item


    def select_layout(self):
        index = 0
        for name, key in self.keylist:
            if name == self.keyboard_list.currentText():
                self.current_layout = self.keylist[index]
            index += 1
        self.names = []
        for key in self.current_layout[1]:
            self.names.append(key.get_letter())

        for index, button in enumerate(self.buttons):
            button.setText(self.names[index])

    def upload(self):
        up.update_keyboard(self.current_layout[1], self.port, self.rotation)

    def save(self):
        temp_layout = []
        list_index = 0
        counter = 0
        for name, key in self.keylist:
            if name == self.keyboard_list.currentText():
                temp_layout = key
                list_index = counter
                break
            counter += 1

        for index, name in enumerate(self.names):
            if name != temp_layout[index].get_letter():
                for char in self.charlist:
                    if char.get_letter() == name:
                        temp_layout[index] = char
                        break

        self.keylist[list_index] = (self.keyboard_list.currentText(), temp_layout)

        js.write_key_lists(self.keylist, keyfile)

    def delete(self):
        list_index = 0
        counter = 0

        # Finds the current list
        for name, key in self.keylist:
            if name == self.keyboard_list.currentText():
                list_index = counter
                break
            counter += 1
        del self.keylist[list_index]

        index = self.keyboard_list.currentIndex()
        self.keyboard_list.removeItem(index)

        js.write_key_lists(self.keylist, keyfile)

    def new_layout(self):
        if self.keyboard_list.currentText != self.current_layout[0]:
            temp_keylist = self.current_layout[1]
            temp_name = self.keyboard_list.currentText()
            self.keylist.append((temp_name, temp_keylist))
            self.current_layout = self.keylist[-1]      #Python for last element in a list
            self.keyboard_list.addItem(temp_name)

    # #Returns list of all ports
    # #each port_list object has
    # # [0] = com port name
    # # [1] = name of connected object
    #
    # def ports():
    #     return list(serial.tools.list_ports.comports())
