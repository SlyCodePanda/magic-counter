"""
This file holds the class for building player objects.
It allows you to:
    * Create a player with a default name and default initial life points.
    * Change the name of a player.
    * Give and take points from their life points.
"""


class Player(object):
    def __init__(self, name_number):
        self.name = "Player %s" % name_number
        self.life = 20
        self.name_number = name_number

    def set_name(self, new_name):
        """
        Change the name of the player.
        :param new_name: The new name of the player.
        """

        self.name = new_name
        print("The Players new name is %s " % self.name)

    def give_life(self):
        """
        Give a point of life to player.
        """
        self.life += 1

    def take_life(self):
        """
        Take away a point of life from player.
        :return:
        """
        self.life -= 1
        print("Life total = %i" % self.life)

    def reset_life(self):
        self.life = 20
