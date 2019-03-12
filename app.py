import sys
from functools import partial
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from mainWindow import Ui_MainWindow
from settings import Ui_Dialog


# Class for creating the settings window imported from settings.py
class AppSettings(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.settings = Ui_Dialog()
        self.settings.setupUi(self)
        self.setupUi(self)

        # Setting default player names.
        self.playerOneName = "Player One"
        self.playerTwoName = "Player Two"

        # ToDo : .textChanged (line 24) is not working. Not recognizing when lineEdit is changed.
        # Change the names of the players
        if self.settings.playerOneName_lineEdit.textChanged:
            print("TEXT CHANGED!")
        self.settings.playerOneName_lineEdit.textChanged.connect(self.syncLineEdit)
        print("string: %s " % self.playerOneName)
        # self.show()

    # Call this function when the lineEdit element has been changed.
    def syncLineEdit(self, text):
        self.playerOneName = text
        print("NEW TEXT : %s" % text)
        return text


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
        self.player02Counter = self.basePoints
        self.player01Counter = self.basePoints

        # Tracking the subtracting and adding of life points.
        self.ui.TakeLife02_pushButton.clicked.connect(partial(self.takeLife, "player02"))
        self.ui.TakeLife01_pushButton.clicked.connect(partial(self.takeLife, "player01"))

        self.ui.AddLife02_pushButton.clicked.connect(partial(self.addLife, "player02"))
        self.ui.AddLife01_pushButton.clicked.connect(partial(self.addLife, "player01"))

        # Tracking reset of life points.
        self.ui.reset_pushButton.clicked.connect(partial(self.reset))

        # Open settings dialog.
        self.ui.settings_action.triggered.connect(self.openSettings)

        # Exit menu item.
        self.ui.actionQuit.triggered.connect(self.close)

        self.show()

    # Function used for opening up the settings dialog box in the edit menu.
    def openSettings(self):
        self.settingsWindow = AppSettings()
        self.settingsWindow.exec_()

        print("New name recieved: %s" % self.settingsWindow.playerOneName)

    # Functions that handles adding and subtracting life from players.
    def takeLife(self, player):
        # TODO:
        #  Come up with a better way of deducting points so it is easier to add more than just two players to games.

        # Reducing Player 02 life points.
        if player == "player02":
            print("Taking life from player 2!")
            # Getting the current life value of player 2.
            self.player02Counter = int(self.ui.PlayerTwoCounter_label.text())
            self.player02Counter = self.player02Counter - 1
            print("Current life = %s" % self.player02Counter)
            self.ui.PlayerTwoCounter_label.setText(str(self.player02Counter))

            # Check if player 2 counter = 0.
            if self.ui.PlayerTwoCounter_label.text() == '0':
                print("Player 2 life = %s" % self.player02Counter)
                # Present pop-up window.
                self.popup()

        # Reducing Player 01 life points
        elif player == "player01":
            print("Taking life from player 1!")
            # Getting the current life value of player 2.
            self.player01Counter = int(self.ui.playerOneCounter_label.text())
            self.player01Counter = self.player01Counter - 1
            print("Current life = %s" % self.player01Counter)
            self.ui.playerOneCounter_label.setText(str(self.player01Counter))

            # Check if player 1 counter = 0.
            if self.ui.playerOneCounter_label.text() == '0':
                # Present pop-up window.
                self.popup()

        return

    def addLife(self, player):
        # Reducing Player 02 life points.
        if player == "player02":
            print("Adding life to player 2!")
            # Getting the current life value of player 2.
            self.player02Counter = int(self.ui.PlayerTwoCounter_label.text())
            self.player02Counter = self.player02Counter + 1
            print("Current life = %s" % self.player02Counter)
            self.ui.PlayerTwoCounter_label.setText(str(self.player02Counter))

        # Reducing Player 01 life points
        elif player == "player01":
            print("Adding life to player 1!")
            # Getting the current life value of player 2.
            self.player01Counter = int(self.ui.playerOneCounter_label.text())
            self.player01Counter = self.player01Counter + 1
            print("Current life = %s" % self.player01Counter)
            self.ui.playerOneCounter_label.setText(str(self.player01Counter))

        return

    # Shows popup declaring who is the winner and who is the loser.
    def popup(self):
        winner = ""

        #Find out who had the lowest health, and therefore find out the winner.
        if int(self.player01Counter) > int(self.player02Counter):
            winner = "Player One"
        else:
            winner = "Player Two"

        msgBox = QMessageBox()
        msgBox.setText("Congratulations! %s is the winner!" % winner)

        msgBox.show()
        msgBox.exec_()

        # Reset life points.
        self.reset()

    # Reset all player health to base value.
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

