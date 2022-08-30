from pickle import TRUE
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPalette, QColor

class Color(QtWidgets.QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 500, 500)

        hlayout1 = QtWidgets.QHBoxLayout()  # HORIZONTAL

        hlayout1.addWidget(Color("red"))
        hlayout1.addWidget(Color("blue"))
        hlayout1.addWidget(Color("green"))
        # hlayout1.setContentsMargins(50, 20, 30, 70)
        hlayout1.setSpacing(50)

        hlayout2 = QtWidgets.QHBoxLayout()

        hlayout2.addWidget(Color("red"))
        hlayout2.addWidget(Color("green"))
        hlayout2.setSpacing(20)

        vlayout = QtWidgets.QVBoxLayout()   # VERTICAL

        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        # glayout = QtWidgets.QGridLayout()
        # glayout.addWidget(Color("red"), 0, 0)  # Numbers corresponds to indexes.
        # glayout.addWidget(Color("blue"), 1, 0)
        # glayout.addWidget(Color("green"), 0, 2)
        # glayout.addWidget(Color("yellow"), 3, 1)

        widget = QtWidgets.QWidget()
        widget.setLayout(vlayout)

        self.setCentralWidget(widget)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()

app()