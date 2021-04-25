## @file ropePile.py
#  @author Albert
#  @brief Contain the specific RopePile type
#  @date 04/11/2021

from .collectable import Collectable

## @brief RopePile is an object of type Collectable
#  @details Extends from collectable.py and implements the secrets of M4.10
class RopePile(Collectable):
	## @brief Use the ropePile
    #  @details Give the player ropes equal to the ropePile's value.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def use(self, gameinfo=None, player=None):
		super().use(gameinfo, player)
		player.ropes += self.val