## @file collectable.py
#  @author Albert
#  @brief Contain the specific Collectable type
#  @date 04/11/2021

from .entity import Entity

## @brief Collectable is an object of type Entity
#  @details Extends from entity.py and implements the secrets of M4.2
class Collectable(Entity):
	## @brief Constructor method for Collectable
    #  @details Create the collectable using super(). Set the value.
	#  @param x int representing the x position of the collectable
	#  @param y int representing the y position of the collectable
	#  @param hp int representing the health points of the collectable 
	#  @param mat image representing the collectable on the game screen
	#  @param name string representing the name of the image of the object
	#  @param width int representing the width of the collectable
	#  @param height int representing the height of the collectable
	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
		super().__init__(x, y, name, height, width, hp, mat)
		self.val = collectableschema[name]['val']

	## @brief Determine if a collectable is useable
	#  @return True
	def useable(self):
		return True

	## @brief Use the collectable
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def use(self, gameinfo=None, player=None):
		gameinfo.rem(self)

collectableschema = {"gold":{"val":500},
		  			"emerald":{"val":800},
		  			"sapphire":{"val":1200},
		  			"ruby":{"val":1600},
		  			"diamond":{"val":5000},
		  			"bombPile":{"val":3},
		  			"ropePile":{"val":3}}