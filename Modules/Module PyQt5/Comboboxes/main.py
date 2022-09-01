import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from design import Ui_MainWindow

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.mywindow = Ui_MainWindow()
        self.mywindow.setupUi(self)
        self.setWindowTitle("Şehir Seçimi")
        self.setWindowIcon(QIcon("Modules/Module PyQt5/Resources/tile.png"))
        self.init_actions()

    def init_actions(self):
        self.mywindow.btn_get.clicked.connect(self.action_btn_get)
        self.mywindow.btn_load.clicked.connect(self.action_btn_load)
        self.mywindow.btn_delete.clicked.connect(self.action_btn_delete)
        self.mywindow.btn_delete_all.clicked.connect(self.action_btn_delete_all)

    # ACTIONS
    def action_btn_get(self):
        name = self.mywindow.combo_cities.currentText()
        if self.mywindow.combo_cities.currentIndex() != -1:
            self.mywindow.lbl_result.setText(f"{name} adlı şehir seçildi !")
        else:
            self.mywindow.lbl_result.setText("Liste boş olduğu için bir seçim yapılamadı.")

    def action_btn_load(self):
        name = self.mywindow.txt_load.text()
        self.mywindow.combo_cities.addItem(name)
        self.mywindow.lbl_result.setText(f"{name} adlı şehir, listeye başarılı bir şekilde eklendi.")
    
    def action_btn_delete(self):
        name = self.mywindow.txt_load.text()
        self.mywindow.combo_cities.removeItem(self.mywindow.combo_cities.findText(name))
        self.mywindow.lbl_result.setText(f"{name} ADLI GİRDİ TEMİZLENDİ !!!")

    def action_btn_delete_all(self):
        self.mywindow.combo_cities.clear()
        self.mywindow.lbl_result.setText("TÜM GİRDİLER TEMİZLENDİ !!!")

def app():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()

app()