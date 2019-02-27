import sys
from functools import partial
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from mainWindow import Ui_MainWindow


# Class for creating the app window imported from the Ui_MainWindow class in mainWindow.py.
class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.home()

    # Functions concerning the home page.
    def home(self):
        self.ui.TakeLife02_pushButton.clicked.connect(partial(self.takeLife, "player02"))
        self.ui.TakeLife01_pushButton.clicked.connect(partial(self.takeLife, "player01"))
        self.show()

    # Functions that handles adding and subtracting life from players.
    def takeLife(self, player):
        if player == "player02":
            print("Taking life from player 2!")
            # Getting the current life value of player 2.
            player02Counter = int(self.ui.PlayerTwoCounter_label.text())
            player02Counter = player02Counter - 1
            print("Current life = %s" % player02Counter)
            self.ui.PlayerTwoCounter_label.setText(player02Counter) # Line errors out the window for some reason...
            return
        elif player == "player01":
            print("Taking life from player 1!")

    def addLife(self):
        return "Adding life!"


# Main.
def run():
    app = QApplication(sys.argv)
    window = AppWindow()

    sys.exit(app.exec_())


# Running Main.
run()

