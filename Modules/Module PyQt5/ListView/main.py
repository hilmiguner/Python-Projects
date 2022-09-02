import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from design import Ui_MainWindow
from db import db

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.mywindow = Ui_MainWindow()
        self.mywindow.setupUi(self)
        self.init_actions()
        self.setWindowIcon(QIcon("Modules/Module PyQt5/Resources/tile.png"))
        self.setWindowTitle("List View")

        #-------------------
        #LOADING STUDENTS
        self.loadStudents()
        #-------------------
    
    def init_actions(self):
        self.mywindow.btn_add.clicked.connect(self.action_btn_add)
        self.mywindow.btn_edit.clicked.connect(self.action_btn_edit)
        self.mywindow.btn_remove.clicked.connect(self.action_btn_remove)
        self.mywindow.btn_up.clicked.connect(self.action_btn_up)
        self.mywindow.btn_down.clicked.connect(self.action_btn_down)
        self.mywindow.btn_sort.clicked.connect(self.action_btn_sort)
        self.mywindow.btn_exit.clicked.connect(self.action_btn_exit)

    def loadStudents(self):
        database = db()
        sql = "SELECT * FROM names"
        database.cursor.execute(sql)
        names = database.cursor.fetchall()
        for name in names:
            self.mywindow.listWidget.addItem(name[0])
        self.mywindow.listWidget.setCurrentRow(0)

    #*******************************************************************************************************************
    # ACTIONS
    def action_btn_add(self):
        name, respond = QtWidgets.QInputDialog.getText(self, "Yeni Girdi", "İsim giriniz.")
        if respond:
            database = db()
            sql = "INSERT INTO names(name) VALUES ('{}')".format(name)    
            try:
                database.cursor.execute(sql)
                database.connection.commit()
                self.mywindow.listWidget.addItem(name)
                self.mywindow.listWidget.setCurrentRow(self.mywindow.listWidget.count()-1)
            except Exception as err:
                QtWidgets.QMessageBox.critical(self, "HATA", f"Girdi sunucuya aktarılırken bir hata ile karşılaşıldı.\n'{err}'", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def action_btn_edit(self):
        oldName = self.mywindow.listWidget.currentItem().text()
        name, respond = QtWidgets.QInputDialog.getText(self, "Düzenle", "Yeni ismi yazınız.", text=oldName)
        if respond:
            database = db()
            sql = "UPDATE names SET Name='{}' WHERE Name='{}'".format(name, oldName)
            try:
                database.cursor.execute(sql)
                database.connection.commit()
                self.mywindow.listWidget.currentItem().setText(name)
            except Exception as err:
                QtWidgets.QMessageBox.critical(self, "HATA", f"Girdi sunucuya aktarılırken bir hata ile karşılaşıldı\n{err}", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def action_btn_remove(self):
        if self.mywindow.listWidget.count() == 0:
                QtWidgets.QMessageBox.critical(self, "HATA!", "Listede girdi olmadığı için silme işlemi geçersiz!", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        else:
            name = self.mywindow.listWidget.currentItem().text()
            respond = QtWidgets.QMessageBox.warning(
                self,
                "Girdi Siliniyor",
                f"'{name}' adlı girdiyi silmek istediğinize emin misiniz ?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.Yes
                )
            if respond == QtWidgets.QMessageBox.Yes:
                name = self.mywindow.listWidget.currentItem().text()
                database = db()
                sql = "DELETE FROM names WHERE Name='{}'".format(name)
                try:
                    database.cursor.execute(sql)
                    database.connection.commit()
                    item = self.mywindow.listWidget.takeItem(self.mywindow.listWidget.currentRow())
                    del item
                except Exception as err:
                    QtWidgets.QMessageBox.critical(self, "HATA", f"Girdi sunucuya aktarılırken bir hata ile karşılaşıldı\n{err}", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)   

    def action_btn_up(self):
        oldIndex = self.mywindow.listWidget.currentRow()
        newIndex = oldIndex - 1
        if oldIndex > 0:
            item = self.mywindow.listWidget.takeItem(oldIndex)
            self.mywindow.listWidget.insertItem(newIndex, item)
            self.mywindow.listWidget.setCurrentRow(newIndex)

    def action_btn_down(self):
        oldIndex = self.mywindow.listWidget.currentRow()
        newIndex = oldIndex + 1
        if oldIndex < (self.mywindow.listWidget.count()-1):
            item = self.mywindow.listWidget.takeItem(oldIndex)
            self.mywindow.listWidget.insertItem(newIndex, item)
            self.mywindow.listWidget.setCurrentRow(newIndex)

    def action_btn_sort(self):
        self.mywindow.listWidget.sortItems()

    def action_btn_exit(self):
        msg = QtWidgets.QMessageBox.warning(self, "Warning!", "Are you sure ?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        if msg == QtWidgets.QMessageBox.Yes:
            QtWidgets.qApp.quit()
    #*******************************************************************************************************************

def App():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()

App()