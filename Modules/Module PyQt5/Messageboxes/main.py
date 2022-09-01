import sys
from tkinter import E
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from design import Ui_MainWindow

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.mywindow = Ui_MainWindow()
        self.mywindow.setupUi(self)
        self.setWindowIcon(QIcon("Modules/Module PyQt5/Resources/tile.png"))
        self.init_actions()

    def init_actions(self):
        self.mywindow.btn_exit.clicked.connect(self.action_btn_exit)

    # ACTIONS
    def action_btn_exit(self):
        # --------------------------------------------------------------------------------------
        # def popup_button(i):
        #         if i.text() == "OK":
        #             QtWidgets.qApp.quit()
        #         elif i.text() == "Cancel":
        #             pass
        #         elif i.text() == "Ignore":
        #             pass

        # msg = QMessageBox()
        # msg.setWindowTitle("Closing Application")
        # msg.setText("Are you sure ?")
        # msg.setIcon(QMessageBox.Warning)
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
        # msg.setDefaultButton(QMessageBox.Ok)
        # msg.setDetailedText("Details...")
        # msg.buttonClicked.connect(popup_button)

        # x = msg.exec()
        # --------------------------------------------------------------------------------------

        # OR

        respond = QMessageBox.warning(self, "Close Application", "Are you sure ?", QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore, QMessageBox.Ok)
        if respond == QMessageBox.Ok:
            QtWidgets.qApp.quit()
        
def app():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()

app()