import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from design_file import Ui_MainWindow

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.mywindow = Ui_MainWindow()
        self.mywindow.setupUi(self)
        self.init_actions()
        self.setWindowIcon(QIcon("Modules/Module PyQt5/Resources/tile.png"))

    def init_actions(self):
        self.mywindow.btn_get.clicked.connect(self.action_btn_get)
        self.mywindow.btn_clear.clicked.connect(self.action_btn_clear)

    # ACTIONS
    def action_btn_get(self):
        radio_buttons = self.mywindow.widget_country.findChildren(QtWidgets.QRadioButton)
        for btn in radio_buttons:
            if btn.isChecked():
                self.mywindow.lbl_result.setText(f"Ülkeniz: {btn.text()}")
                break

    def action_btn_clear(self):
        radio_buttons = self.mywindow.widget_country.findChildren(QtWidgets.QRadioButton)
        for btn in radio_buttons:
            if btn.isChecked():
                btn.setAutoExclusive(False)
                btn.setChecked(False)
                btn.setAutoExclusive(True)
                break


def app():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()
    

app()