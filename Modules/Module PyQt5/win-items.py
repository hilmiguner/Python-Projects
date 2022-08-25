import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon


def window():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    window.setGeometry(200, 200, 750, 750)
    window.setWindowTitle("Second Application")
    window.setWindowIcon(QIcon("Modules/Module PyQt5/Resources/tile.png"))
    window.setToolTip("My Tooltip")

    label_name = QtWidgets.QLabel(window)  # Creating a label and attaching to the parent widget.
    label_name.setText("Name:")  # Setting the text.
    label_name.move(100, 100)  # Setting the coordinate of the label.(100 from left and 100 from up.)

    label_surname = QtWidgets.QLabel(window)
    label_surname.setText("Surname:")
    label_surname.move(100, 150)

    txt_name = QtWidgets.QLineEdit(window)  # TEXT LINE
    txt_name.move(160, 100)

    txt_surname = QtWidgets.QLineEdit(window)
    txt_surname.move(160, 150)

    #------------------------------------------------
    # BUTTON FUNCTION WHEN IT IS CLICKED
    def when_clicked():
        print("Name: " + txt_name.text())
        print("Surname: " + txt_surname.text())
    #------------------------------------------------


    btn_save = QtWidgets.QPushButton(window)  # BUTTON
    btn_save.setText("Save")
    btn_save.move(160, 200)
    btn_save.clicked.connect(when_clicked)  # when_clicked is a function which is desinged by user to do wished commands when btn_save is clicked.

    window.show()
    app.exec_()


window()