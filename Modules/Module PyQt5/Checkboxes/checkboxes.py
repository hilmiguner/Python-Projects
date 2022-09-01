import sys
from PyQt5 import QtWidgets
from checkboxesdesign import Ui_MainWindow

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.mywindow = Ui_MainWindow()
        self.mywindow.setupUi(self)
        self.init_actions()

    def init_actions(self):
        self.mywindow.btn_get.clicked.connect(self.action_btn_get)

    # ACTIONS
    def action_btn_get(self):
        temp_list = []
        temp_str = ""

        if self.mywindow.cb_cinema.isChecked():
            temp_list.append("sinemaya gitmeyi")
        if self.mywindow.cb_book.isChecked():
            temp_list.append("kitap okumayı")
        if self.mywindow.cb_sport.isChecked():
            temp_list.append("spor yapmayı")
        
        if len(temp_list) > 1:
            temp_str = ", ".join(temp_list[:-1])
            temp_str += " ve " + temp_list[-1] + " sever."
        elif len(temp_list) == 0:
            temp_str = "Lütfen en az bir seçim yapınız!"
        else:
            temp_str = temp_list[0] + " sever."

        self.mywindow.lbl_result.setText(temp_str.capitalize())

def app():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()

app()

