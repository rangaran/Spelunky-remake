## @file treasure.py
#  @author Albert
#  @brief Contain the specific Treasure type
#  @date 04/11/2021

from .collectable import Collectable

## @brief Treasure is an object of type Collectable
#  @details Extends from collectable.py and implements the secrets of M4.3
class Treasure(Collectable):
	## @brief Use the treasure
    #  @details Give the player gold equal to the treasure's value.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def use(self, gameinfo=None, player=None):
		super().use(gameinfo, player)
		player.gold += self.val
		print ("player gold: ", player.gold)