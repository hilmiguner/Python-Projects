import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

class MainForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        
        self.setWindowTitle("Calculator")
        self.setGeometry(200, 200, 510, 200)
        self.setWindowIcon(QIcon("Modules/Module PyQt5/Resources/tile.png"))
        self.initUI()

        self.show()

    def initUI(self):
        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText("First number: ")
        self.lbl_num1.move(50, 30)

        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText("Second number: ")
        self.lbl_num2.move(50, 80)

        self.txt_num1 = QtWidgets.QLineEdit(self)
        self.txt_num1.move(150, 37)
        self.txt_num1.resize(300, 20)

        self.txt_num2 = QtWidgets.QLineEdit(self)
        self.txt_num2.move(150, 87)
        self.txt_num2.resize(300, 20)

        self.btn_sum = QtWidgets.QPushButton(self)
        self.btn_sum.setText("Sum")
        self.btn_sum.move(150, 120)
        self.btn_sum.resize(75, 35)
        self.btn_sum.clicked.connect(self.calculate)

        self.btn_diff = QtWidgets.QPushButton(self)
        self.btn_diff.setText("Difference")
        self.btn_diff.move(225, 120)
        self.btn_diff.resize(75, 35)
        self.btn_diff.clicked.connect(self.calculate)

        self.btn_multi = QtWidgets.QPushButton(self)
        self.btn_multi.setText("Multiplication")
        self.btn_multi.move(300, 120)
        self.btn_multi.resize(75, 35)
        self.btn_multi.clicked.connect(self.calculate)

        self.btn_div = QtWidgets.QPushButton(self)
        self.btn_div.setText("Division")
        self.btn_div.move(375, 120)
        self.btn_div.resize(75, 35)
        self.btn_div.clicked.connect(self.calculate)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.move(50, 160)
        self.lbl_result.resize(400, 35)

    def calculate(self):
        sender = self.sender()  # Returns to clicked button.
        if sender is self.btn_sum:
            try:
                result = float(self.txt_num1.text()) + float(self.txt_num2.text())
                self.lbl_result.setText(f"Result of the summation -> {result}")
            except ValueError as err:
                result = "Please write numerical values on the blanks !"
                self.lbl_result.setText(result)
        elif sender is self.btn_diff:
            try:
                result = float(self.txt_num1.text()) - float(self.txt_num2.text())
                self.lbl_result.setText(f"Result of the difference -> {result}")
            except ValueError as err:
                result = "Please write numerical values on the blanks !"
                self.lbl_result.setText(result)
        elif sender is self.btn_multi:
            try:
                result = float(self.txt_num1.text()) * float(self.txt_num2.text())
                self.lbl_result.setText(f"Result of the multiplication -> {result}")
            except ValueError as err:
                result = "Please write numerical values on the blanks !"
                self.lbl_result.setText(result)
        elif sender is self.btn_div:
            try:
                result = float(self.txt_num1.text()) / float(self.txt_num2.text())
                self.lbl_result.setText(f"Result of the division -> {result}")
            except ValueError as err:
                result = "Please write numerical values on the blanks !"
                self.lbl_result.setText(result)
        else:
            self.lbl_result.setText("Unexpected action !")

def App():
    app = QtWidgets.QApplication(sys.argv)
    window = MainForm()
    app.exec()

App()