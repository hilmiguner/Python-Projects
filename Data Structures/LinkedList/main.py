import sys
from design import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import presets

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Linked List")
        self.setWindowIcon(QIcon("C:/Users/Casper/Desktop/Programlama/Python/Python-Projects/Modules/Module PyQt5/Resources/tile.png"))
        self.loadLinkedList()
        self.initActions()

    def initActions(self):
        self.ui.btnAddNewNode.clicked.connect(self.actionBtnAddNewNode)

    def loadLinkedList(self):
        rowCount = presets.head1.size
        columnCount = 2

        self.ui.tableNodes.setRowCount(rowCount)
        self.ui.tableNodes.setColumnCount(columnCount)

        self.ui.tableNodes.setColumnWidth(0, 75)
        self.ui.tableNodes.setColumnWidth(1, 75)

        nodeValues = []
        tempNode = presets.head1
        while True:
            if tempNode.nextNode is None:
                nodeValues.append(tempNode.value)
                break
            nodeValues.append(tempNode.value)
            tempNode = tempNode.nextNode

        for row in range(rowCount):
            txt = f"{row+1}. node"
            for column in range(columnCount):
                if column == 0:
                    self.ui.tableNodes.setItem(row, column, QtWidgets.QTableWidgetItem(txt))
                elif column == 1:
                    self.ui.tableNodes.setItem(row, column, QtWidgets.QTableWidgetItem(str(nodeValues[row])))

    def actionBtnAddNewNode(self):
        newRowCount = self.ui.tableNodes.rowCount() + 1
        self.ui.tableNodes.setRowCount(newRowCount)
        self.ui.tableNodes.setItem(newRowCount-1, 0, QtWidgets.QTableWidgetItem(f"{newRowCount}. node"))
        self.ui.tableNodes.setItem(newRowCount-1, 1, QtWidgets.QTableWidgetItem(self.ui.txtNewNode.text()))


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()