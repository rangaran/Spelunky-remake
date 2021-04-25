## @file bomb.py
#  @author Albert
#  @brief Contain the specific Bomb type
#  @date 04/11/2021

from .throwable import Throwable

## @brief Bomb is an object of type Throwable
#  @details Extends from throwable.py and implements the secrets of M4.16
class Bomb(Throwable):
	## @brief Constructor method for Bomb
    #  @details Create the bomb using super(). Set the time to BOMBTIME.
	#  @param x int representing the x position of the bomb
	#  @param y int representing the y position of the bomb
	#  @param hp int representing the health points of the bomb 
	#  @param mat image representing the bomb on the game screen
	#  @param name string representing the name of the image of the object
	#  @param width int representing the width of the bomb
	#  @param height int representing the height of the bomb
	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
		super().__init__(x, y, name, height, width, hp, mat)
		self.BOMBTIME = 180
		self.time = self.BOMBTIME

	## @brief Update the bomb with 1 unit of time
    #  @details Reduce the time. Call super.tick(). Explode if time reaches 0, the bomb stops on a wall,
	#			or is destroyed.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def tick(self, gameinfo=None, player=None):
		self.time -= 1

		super().tick(gameinfo, player)

		if self.time == 0 or (self.thrown and self.xs == 0) or self.hp <= 0:
			self.explode(gameinfo, player)

	## @brief Explode the bomb
    #  @details Create an explosion concentric with the bomb. Add it to the game and remove the bomb.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def explode(self, gameinfo=None, player=None):
		from .entities import Entities

		explosion = Entities.makeEnt("explosion", self.x, self.y)
		height = explosion.dimension()[0]
		width = explosion.dimension()[1]

		x = int(self.x - width/2 + self.width)
		y = int(self.y - height/2 + self.height)

		print("Explosion at ",x, y)

		#print(x,y,hp,mat,name,text,width,height)

		explosion = Entities.makeEnt("explosion", x, y)
		gameinfo.add(explosion)
		self.rem(gameinfo, player)
		explosion.explode(gameinfo, player)