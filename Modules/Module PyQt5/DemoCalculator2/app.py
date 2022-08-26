import sys
from main_window import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("Modules/Module PyQt5/Resources/tile.png"))
        self.init_actions()

    def init_actions(self):
        self.ui.btn_sum.clicked.connect(self.calculate)
        self.ui.btn_diff.clicked.connect(self.calculate)
        self.ui.btn_multi.clicked.connect(self.calculate)
        self.ui.btn_div.clicked.connect(self.calculate)

    def calculate(self):
        sender = self.sender()  # Returns to clicked button.
        if sender is self.ui.btn_sum:
            try:
                result = float(self.ui.txtLine_num1.text()) + float(self.ui.txtLine_num2.text())
                self.ui.lbl_result.setText(f"Result of the summation -> {result}")
            except ValueError as err:
                result = "Please write numerical values on the blanks !"
                self.ui.lbl_result.setText(result)
        elif sender is self.ui.btn_diff:
            try:
                result = float(self.ui.txtLine_num1.text()) - float(self.ui.txtLine_num2.text())
                self.ui.lbl_result.setText(f"Result of the difference -> {result}")
            except ValueError as err:
                result = "Please write numerical values on the blanks !"
                self.ui.lbl_result.setText(result)
        elif sender is self.ui.btn_multi:
            try:
                result = float(self.ui.txtLine_num1.text()) * float(self.ui.txtLine_num2.text())
                self.ui.lbl_result.setText(f"Result of the multiplication -> {result}")
            except ValueError as err:
                result = "Please write numerical values on the blanks !"
                self.ui.lbl_result.setText(result)
        elif sender is self.ui.btn_div:
            try:
                result = float(self.ui.txtLine_num1.text()) / float(self.ui.txtLine_num2.text())
                self.ui.lbl_result.setText(f"Result of the division -> {result}")
            except ValueError as err:
                result = "Please write numerical values on the blanks !"
                self.ui.lbl_result.setText(result)
        else:
            self.ui.lbl_result.setText("Unexpected action !")

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec()

app = app()