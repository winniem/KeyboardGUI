# Keyboard GUI

import sys
from PyQt5.QtWidgets import *
from GUI import *

if __name__ == '__main__':

    app = QApplication(sys.argv)
    GUI = GUI()
    sys.exit(app.exec_())
