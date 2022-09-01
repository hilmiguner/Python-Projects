import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate
from design import Ui_MainWindow

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.mywindow = Ui_MainWindow()
        self.mywindow.setupUi(self)
        self.init_actions()
        self.setWindowIcon(QIcon("Modules/Module PyQt5/Resources/tile.png"))
        self.setWindowTitle("Date & Time")

    def init_actions(self):
        self.mywindow.btn_calculate.clicked.connect(self.action_btn_calculate)
        self.mywindow.btn_calculate2.clicked.connect(self.action_btn_calculate2)

    # ACTIONS
    def action_btn_calculate(self):
        start = self.mywindow.date1.date()
        end = self.mywindow.date2.date()
        delta = start.daysTo(end)
        self.mywindow.lbl_result.setText(f"From {start.toPyDate()} to {end.toPyDate()} there are {delta} days.")

    def action_btn_calculate2(self):
        start = self.mywindow.date3.date()
        now = QDate.currentDate()
        delta = start.daysTo(now)
        self.mywindow.lbl_result.setText(f"From {start.toPyDate()} to {now.toPyDate()} there are {delta} days.")
        
def App():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()

App()