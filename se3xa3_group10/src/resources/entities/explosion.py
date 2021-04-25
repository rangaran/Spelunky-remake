## @file explosion.py
#  @author Albert
#  @brief Contain the specific Explosion type
#  @date 04/11/2021

from .entity import Entity

## @brief Explosion is an object of type Entity
#  @details Extends from entity.py and implements the secrets of M4.12
class Explosion(Entity):
	## @brief Constructor method for Explosion
    #  @details Create the explosion using super(). Set the time to DURATION.
	#  @param x int representing the x position of the explosion
	#  @param y int representing the y position of the explosion
	#  @param hp int representing the health points of the explosion 
	#  @param mat image representing the explosion on the game screen
	#  @param name string representing the name of the image of the object
	#  @param width int representing the width of the explosion
	#  @param height int representing the height of the explosion
	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
		super().__init__(x, y, name, height, width, hp, mat)
		self.DURATION = 45
		self.time = self.DURATION
		self.DAMAGE = 10

	## @brief Update the explosion with 1 unit of time
    #  @details Reduce the time. If time reaches 0, remove the explosion from the game.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def tick(self, gameinfo=None, player=None):
		self.time -= 1

		if self.time == 0:
			gameinfo.rem(self)

	## @brief Destroy blocks, player, and entities
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def explode(self, gameinfo=None, player=None):
		self.destroyBlock(gameinfo)
		self.destroyEnt(gameinfo)
		self.destroyPlayer(player)

	## @brief Destroy nearby blocks
	#  @param gameinfo ReadMap object representing the level environment
	def destroyBlock(self, gameinfo=None):
		destroyed = []
		w = (self.x, self.x + self.width)
		h = (self.y, self.y + self.height)

		for i in range(int(w[0]/32), int(w[1]/32) + 1):
			for j in range(int(h[0]/32), int(h[1]/32) + 1):
				destroyed.append((i, j))

		for b in destroyed:
			gameinfo.destroyBlock(b[0],b[1])

	## @brief Damage nearby entities
	#  @param gameinfo ReadMap object representing the level environment
	def destroyEnt(self, gameinfo=None):
		destroyed = []
		for ent in gameinfo.entities():
			if self.overlap(ent):
				print("Explosion affected ",ent.name, ent.x//32, " ", ent.y//32)
				destroyed.append(ent)

		for ent in destroyed:
			ent.damage(self.DAMAGE, gameinfo)

	## @brief Damage the nearby player
	#  @param player Mover object representing the player
	def destroyPlayer(self, player=None):
		if self.overlap(player):
			player.damage(self.DAMAGE)