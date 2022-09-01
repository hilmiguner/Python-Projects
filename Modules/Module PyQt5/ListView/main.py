import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from design import Ui_MainWindow

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.mywindow = Ui_MainWindow()
        self.mywindow.setupUi(self)
        self.init_actions()
        self.setWindowIcon(QIcon("Modules/Module PyQt5/Resources/tile.png"))
        self.setWindowTitle("List View")
    
    def init_actions(self):
        pass

def App():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()

App()