import sys
from db import db
from designTV import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.mywindow = Ui_MainWindow()
        self.mywindow.setupUi(self)
        self.initActions()
        self.setWindowIcon(QIcon("Modules/Module PyQt5/Resources/tile.png"))
        self.setWindowTitle("Table View")

        self.loadItems()

    def initActions(self):
        self.mywindow.btnSave.clicked.connect(self.action_btnSave)
        self.mywindow.tableProducts.doubleClicked.connect(self.action_doubleClicked)

    def loadItems(self):
        database = db()
        sql = "SELECT * FROM persons"
        database.cursor.execute(sql)
        items = database.cursor.fetchall()

        rowCount = len(items)
        columnCount = len(items[0])

        self.mywindow.tableProducts.setRowCount(rowCount)
        self.mywindow.tableProducts.setColumnCount(columnCount)

        self.mywindow.tableProducts.setColumnWidth(0, 100)
        self.mywindow.tableProducts.setColumnWidth(1, 50)

        for row in range(rowCount):
            for column in range(columnCount):
                self.mywindow.tableProducts.setItem(row, column, QtWidgets.QTableWidgetItem(items[row][column]))

    def action_btnSave(self):
        name = self.mywindow.txt_lineName.text()
        gender = self.mywindow.txt_lineGender.text().upper()

        database = db()
        sql = "INSERT INTO persons(Name, Gender) VALUES ('{}', '{}')".format(name, gender)
        try:
            database.cursor.execute(sql)
            database.connection.commit()
            newRowCount = self.mywindow.tableProducts.rowCount() + 1
            self.mywindow.tableProducts.setRowCount(newRowCount)
            self.mywindow.tableProducts.setItem(newRowCount-1, 0, QtWidgets.QTableWidgetItem(name))
            self.mywindow.tableProducts.setItem(newRowCount-1, 1, QtWidgets.QTableWidgetItem(gender))
        except Exception as err:
            QtWidgets.QMessageBox.critical(self, "ERROR!", f"An error occured while registring new entry.\n'{err}'", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
    
    def action_doubleClicked(self):
        items = self.mywindow.tableProducts.selectedItems()
        for item in items:
            print(item.text())

        

def App():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()

App()