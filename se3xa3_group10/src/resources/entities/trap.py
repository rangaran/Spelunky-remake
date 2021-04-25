## @file trap.py
#  @author Abeer
#  @brief Contain the specific Trap type represented by an entity
#  @date 04/11/2021

from .entity import Entity

## @brief Trap is an object of type Entity
#  @details Extends from entities.py and implements the secrets of M4.13
class Trap(Entity):
	def damage(self, d=0, gameinfo=None):
		super().damage(d, gameinfo)
		if self.hp <= 0:
			gameinfo.rem(self)