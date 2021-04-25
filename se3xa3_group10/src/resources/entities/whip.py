## @file whio.py
#  @author Albert
#  @brief Contain the specific Whip type
#  @date 04/11/2021

from .weapon import Weapon

## @brief Whip is an object of type Weapon
#  @details Extends from weapon.py and implements the secrets of M4.26
class Whip(Weapon):
	## @brief Constructor method for Whip
    #  @details Create the whip using super().
	#  @param x int representing the x position of the whip
	#  @param y int representing the y position of the whip
	#  @param hp int representing the health points of the whip 
	#  @param mat image representing the whip on the game screen
	#  @param name string representing the name of the image of the object
	#  @param width int representing the width of the whip
	#  @param height int representing the height of the whip
	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
		super().__init__(x, y, name, height, width, hp, mat)
		self.damage = 1
		self.speed = 45
		self.activeFrames = 45