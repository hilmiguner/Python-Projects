from mimetypes import init
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application")
        self.setGeometry(200, 200, 700, 700)
        self.setWindowIcon(QIcon("Modules/Module PyQt5/Resources/tile.png"))
        self.setToolTip("My ToolTip")

        self.initUI()

        self.show()
    
    def initUI(self):
        self.label_name = QtWidgets.QLabel(self)
        self.label_name.setText("Name:")
        self.label_name.move(100, 100)

        self.label_surname = QtWidgets.QLabel(self)
        self.label_surname.setText("Surname:")
        self.label_surname.move(100, 150)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(160, 100)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(160, 150)

        self.btn_save = QtWidgets.QPushButton(self)  # BUTTON
        self.btn_save.setText("Save")
        self.btn_save.move(160, 200)
        self.btn_save.clicked.connect(self.event_clicked_on_btn_save)

        self.label_result1 = QtWidgets.QLabel(self)
        self.label_result1.move(300, 100)
        self.label_result1.setText("Your name: ")

        self.label_result2 = QtWidgets.QLabel(self)
        self.label_result2.move(300, 150)
        self.label_result2.setText("Your surname: ")
    
    def event_clicked_on_btn_save(self):
        self.label_result1.setText("Your name: " + self.txt_name.text())
        self.label_result2.setText("Your surname: " + self.txt_surname.text())
        print(f"Name: {self.txt_name.text()}")
        print(f"Surname: {self.txt_surname.text()}")

app = QtWidgets.QApplication(sys.argv)
obj = MyWindow()
app.exec()