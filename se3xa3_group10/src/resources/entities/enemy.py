## @file enemy.py
#  @author Niyatha
#  @brief Contain the specific Enemy type
#  @date 04/11/2021

from .entity import Entity

## @brief Enemy is an object of type Entity
#  @details Extends from entity.py and implements the secrets of M4.18
class Enemy(Entity):
	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
		super().__init__(x, y, name, height, width, hp, mat)
		self.xs = 0
		self.ys = 0
		self.GRAVITY = 3
		self.attack = 0

	## @brief Update the enemy with 1 unit of time
    #  @details Gravity effect, move, damage player.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def tick(self, gameinfo=None, player=None):
		self.gravity()
		self.move(gameinfo, self.xs, self.ys)

		if self.overlap(player):
			player.damage(self.attack)

	## @brief Take damage
    #  @details Take damage. Remove from game if dead.
	#  @param d int representing the damage taken
	#  @param gameinfo ReadMap object representing the level environment
	def damage(self, d=0, gameinfo=None):
		super().damage(d, gameinfo)
		if self.hp <= 0:
			gameinfo.rem(self)

	## @brief Gravity effect
	def gravity(self):
		self.ys = self.GRAVITY

	## @brief Move
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def move(self, gameinfo=None, x=None,y=None):
		pass