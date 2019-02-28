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
        # Setting base life points.
        self.basePoints = "20"

        # Tracking the subtracting and adding of life points.
        self.ui.TakeLife02_pushButton.clicked.connect(partial(self.takeLife, "player02"))
        self.ui.TakeLife01_pushButton.clicked.connect(partial(self.takeLife, "player01"))

        self.ui.AddLife02_pushButton.clicked.connect(partial(self.addLife, "player02"))
        self.ui.AddLife01_pushButton.clicked.connect(partial(self.addLife, "player01"))

        # Tracking reset of life points.
        self.ui.reset_pushButton.clicked.connect(partial(self.reset))

        self.show()

    # Functions that handles adding and subtracting life from players.
    def takeLife(self, player):
        # TODO:
        #  Come up with a better way of deducting points so it is easier to add more than just two players to games.

        # Reducing Player 02 life points.
        if player == "player02":
            print("Taking life from player 2!")
            # Getting the current life value of player 2.
            player02Counter = int(self.ui.PlayerTwoCounter_label.text())
            player02Counter = player02Counter - 1
            print("Current life = %s" % player02Counter)
            self.ui.PlayerTwoCounter_label.setText(str(player02Counter))

        # Reducing Player 01 life points
        elif player == "player01":
            print("Taking life from player 1!")
            # Getting the current life value of player 2.
            player01Counter = int(self.ui.playerOneCounter_label.text())
            player01Counter = player01Counter - 1
            print("Current life = %s" % player01Counter)
            self.ui.playerOneCounter_label.setText(str(player01Counter))

        return

    def addLife(self, player):
        # Reducing Player 02 life points.
        if player == "player02":
            print("Adding life to player 2!")
            # Getting the current life value of player 2.
            player02Counter = int(self.ui.PlayerTwoCounter_label.text())
            player02Counter = player02Counter + 1
            print("Current life = %s" % player02Counter)
            self.ui.PlayerTwoCounter_label.setText(str(player02Counter))

        # Reducing Player 01 life points
        elif player == "player01":
            print("Adding life to player 1!")
            # Getting the current life value of player 2.
            player01Counter = int(self.ui.playerOneCounter_label.text())
            player01Counter = player01Counter + 1
            print("Current life = %s" % player01Counter)
            self.ui.playerOneCounter_label.setText(str(player01Counter))

        return

    def reset(self):
        print("Resetting life points to base number")
        self.ui.playerOneCounter_label.setText(str(self.basePoints))
        self.ui.PlayerTwoCounter_label.setText(str(self.basePoints))


# Main.
def run():
    app = QApplication(sys.argv)
    window = AppWindow()

    sys.exit(app.exec_())


# Running Main.
run()

