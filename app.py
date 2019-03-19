import sys
from functools import partial
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import QtGui
from pathlib import Path

# Importing UI files.
from mainWindow import Ui_MainWindow
from settings import Ui_Dialog

# Importing Player class.
from player import Player


# Class for creating the settings window imported from settings.py
class AppSettings(QDialog, Ui_Dialog):
    def __init__(self, player1, player2, *args):
        super().__init__()
        self.settings = Ui_Dialog()
        self.settings.setupUi(self)
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('imgs//mtg_icon.png'))

        # ToDo: Need to set the order of selection in the dialog window.
        #  So tabbing through the items gives you what you would expect.

        # Storing old names.
        self.player1_old_name = player1.name
        self.player2_old_name = player2.name

        # Setting the lineEdits to the current player names.
        self.playerOneName_lineEdit.setText(player1.name)
        self.playerTwoName_lineEdit.setText(player2.name)

        # Storing passed in player objects in local variables.
        self.player1 = player1
        self.player2 = player2

        # Initial player name values.
        self.playerOneName = self.player1.name
        self.playerTwoName = self.player2.name

        # Get changes from lineEdits when user types in them.
        self.playerOneName_lineEdit.textChanged.connect(self.sync_player01_line_edit)
        self.playerTwoName_lineEdit.textChanged.connect(self.sync_player02_line_edit)

        # A signal that runs the set_settings() function when set button is pressed.
        self.apply_pushButton.clicked.connect(self.set_settings)

        # If close is clicked, don't change any of the names, regardless of what is typed in lineEdits.
        self.buttonBox.rejected.connect(self.cancel_settings)


    def cancel_settings(self):
        """
        When the Cancel button in the settings dialog is pressed, the player names are set to their initial old names.
        """
        print("Cancelling settings...")
        self.player1.set_name(self.player1_old_name)
        self.player2.set_name(self.player2_old_name)

    def set_settings(self):
        """
        Changes the names of the Player objects.
        """
        print("Setting changes...")
        self.player1.set_name(self.playerOneName)
        self.player2.set_name(self.playerTwoName)

    # Call these functions when the lineEdit element has been changed.
    def sync_player01_line_edit(self, text):
        self.playerOneName = text

    def sync_player02_line_edit(self, text):
        self.playerTwoName = text


# Class for creating the app window imported from the Ui_MainWindow class in mainWindow.py.
class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("MtG: Life Counter")
        # ToDo: Use pathlib to set img paths so app will work regardless of operating system.
        self.setWindowIcon(QtGui.QIcon('imgs//mtg_icon.png'))

        self.home()

    # Functions concerning the home page.
    def home(self):
        # Create two default player objects.
        number_of_players = 1
        self.player_one = Player(number_of_players)
        self.ui.playerOne_label.setText(self.player_one.name)

        number_of_players += 1
        self.player_two = Player(number_of_players)
        self.ui.playerTwo_label.setText(self.player_two.name)

        # Add players to a list of players.
        self.players = [self.player_one, self.player_two]

        # Tracking the subtracting and adding of life points.
        self.ui.TakeLife01_pushButton.clicked.connect(partial(self.take_life, self.player_one))
        self.ui.TakeLife02_pushButton.clicked.connect(partial(self.take_life, self.player_two))

        self.ui.AddLife01_pushButton.clicked.connect(partial(self.add_life, self.player_one))
        self.ui.AddLife02_pushButton.clicked.connect(partial(self.add_life, self.player_two))

        # Tracking reset of life points.
        self.ui.reset_pushButton.clicked.connect(self.reset)

        # Open settings dialog.
        self.ui.settings_action.triggered.connect(partial(self.open_settings))

        # Exit menu item.
        self.ui.actionQuit.triggered.connect(self.close)

        self.show()

    # Function used for opening up the settings dialog box in the edit menu.
    def open_settings(self):
        """
        Opens the settings dialog box and passes Player objects to it.
        Also changes the player name labels to whatever new name may or may not have been given to players.
        """
        self.settingsWindow = AppSettings(self.player_one, self.player_two)
        self.settingsWindow.exec_()

        self.ui.playerOne_label.setText(str(self.player_one.name))
        self.ui.playerTwo_label.setText(str(self.player_two.name))

    # Functions that handles adding and subtracting life from players.
    def take_life(self, player):
        """
        Handles subtracting life from given players.
        :param player: Takes in a Player object to remove life from.
        """
        player.take_life()
        self.change_label(player)

        if player.life == 0:
            self.popup()


    def add_life(self, player):
        """
        Handles giving life to a given player.
        :param player: Takes in a Player object to give life to.
        """
        player.give_life()
        self.change_label(player)

    def popup(self):
        """
        Displayes a popup window declaring a winner when a player's life reaches 0.
        :return:
        """
        winner = ""

        #Find out who had the lowest health, and therefore find out the winner.
        if self.player_one.life == 0:
            winner = self.player_two.name
        else:
            winner = self.player_one.name

        msgBox = QMessageBox()
        msgBox.setWindowTitle('Winner!')
        msgBox.setText("Congratulations! %s is the winner!" % winner)
        msgBox.setWindowIcon(QtGui.QIcon('imgs//mtg_icon.png'))

        msgBox.show()
        msgBox.exec_()

        # Reset life points.
        self.reset()

    def reset(self):
        """
        Resets all player life points back to 20.
        """
        print("Resetting life points to base number")

        # Iterate through the list of players and reset their lives to 20.
        for player in self.players:
            print("Current player : %s " % player.name)
            player.reset_life()
            self.change_label(player)

    def change_label(self, player):
        """
        Decides which label to change based on the given players number (1 or 2).
        :param player: Takes in a Player pbject.
        :return:
        """
        if player.name_number == 1:
            self.ui.playerOneCounter_label.setText(str(player.life))
        elif player.name_number == 2:
            self.ui.PlayerTwoCounter_label.setText(str(player.life))


# Main.
def run():
    app = QApplication(sys.argv)
    window = AppWindow()

    sys.exit(app.exec_())


# Running Main.
run()

