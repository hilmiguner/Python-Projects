import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

def window():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    window.setWindowTitle("First Application")  # Sets the title of the app.

    window.setGeometry(200, 200, 500, 500)  # First two parameters mean position of the application. Last two parameters mean width and height.
    # Left upper corner is (0,0) in coordinate system.

    window.setWindowIcon(QIcon("Modules/Module PyQt5/Resources/tile.png"))  # Sets the icon of the window.

    window.setToolTip("My ToolTip")  # Sets the text which appears when mouse cursor stops anywhere on the application's window.

    window.show()  # Sets the window visible.

    app.exec()  # app.exec() kills the terminal when we closed the app.

window()