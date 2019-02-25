import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from mainWindow import Ui_MainWindow


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


app = QApplication(sys.argv)
window = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
