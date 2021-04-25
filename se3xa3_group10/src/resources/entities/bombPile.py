## @file bombPile.py
#  @author Albert
#  @brief Contain the specific BombPile type
#  @date 04/11/2021

from .collectable import Collectable

## @brief BombPile is an object of type Collectable
#  @details Extends from collectable.py and implements the secrets of M4.9
class BombPile(Collectable):
	## @brief Use the bombPile
    #  @details Give the player bombs equal to the bombPile's value.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def use(self, gameinfo=None, player=None):
		super().use(gameinfo, player)
		player.bombs += self.val