## @file chest.py
#  @author Albert
#  @brief Contain the specific Chest type
#  @date 04/11/2021

import random

from .throwable import Throwable

## @brief Chest is an object of type Throwable
#  @details Extends from throwable.py and implements the secrets of M4.15
class Chest(Throwable):
	## @brief Constructor method for Chest
    #  @details Create the chest using super(). Set open to False.
	#  @param x int representing the x position of the chest
	#  @param y int representing the y position of the chest
	#  @param hp int representing the health points of the chest 
	#  @param mat image representing the chest on the game screen
	#  @param name string representing the name of the image of the object
	#  @param text string representing addditional object information
	#  @param width int representing the width of the chest
	#  @param height int representing the height of the chest
	# def __init__(self, x=None, y=None, hp=None, mat=None, name=None, text=None, width=None,
	# 			 height=None):
	# 	super().__init__(x, y, hp, mat, name, text, width, height)
	# 	self.open = False

	## @brief Determine if a chest is useable
	#  @return True
	def useable(self):
		return True

	## @brief Use the throwable
    #  @details Call super(). If not open create a random Treasure, place it centred with the chest, and
    #           add it to the game.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def use(self, gameinfo=None, player=None):
		super().rem(gameinfo, player)

		namelist = ['gold','emerald', 'sapphire', 'ruby', 'diamond', 'bombPile', 'ropePile']
		name = random.choice(namelist)

		from .entities import Entities

		collectable = Entities.makeEnt(name, self.x, self.y)
		height = collectable.dimension()[0]
		width = collectable.dimension()[1]
		x = int(self.x + (self.width/2 - width/2))
		y = int(self.y + self.height - height )

		gameinfo.add(Entities.makeEnt(name, x, y))
		#gameinfo.rem(self)