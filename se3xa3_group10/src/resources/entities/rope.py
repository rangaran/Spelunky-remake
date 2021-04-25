## @file rope.py
#  @author Albert
#  @brief Contain the specific Rope type
#  @date 04/11/2021

from .entity import Entity

## @brief Rope is an object of type Entity
#  @details Extends from entity.py and implements the secrets of M4.13
class Rope(Entity):
	## @brief Constructor method for Rope
    #  @details Create the rope using super(). Set the dist to LENGTH.
	#  @param x int representing the x position of the rope
	#  @param y int representing the y position of the rope
	#  @param hp int representing the health points of the rope 
	#  @param mat image representing the rope on the game screen
	#  @param name string representing the name of the image of the object
	#  @param width int representing the width of the rope
	#  @param height int representing the height of the rope
	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
		super().__init__(x, y, name, height, width, hp, mat)
		self.LENGTH = 4
		self.ys = 0
		self.dist = self.LENGTH *32

	## @brief Set the rope movement
	def throw(self):
		self.ys = -2

	## @brief Update the rope with 1 unit of time
    #  @details If the rope is moving, move it.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def tick(self, gameinfo=None, player=None):
		if self.ys != 0:
			self.move(gameinfo, self.ys)

	## @brief Move the rope
    #  @details If there is no block above and the rope can still travel, move it upwards. Else, stop
    #           moving and make the rope.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def move(self, gameinfo=None, y=None):
		tempy = self.y + y 
		if gameinfo.solid((self.x+1)/32, (tempy-1)/32) == False and \
			gameinfo.solid((self.x+(self.width-1))/32, (tempy-1)/32) == False and \
			self.dist > 0:
			self.y = tempy
			self.dist += self.ys
		else:
			self.ys = 0
			self.makeRope(gameinfo)

	## @brief Make the rope
    #  @details Create a rope with length dependent on how far it can extend downwards without reaching
    #           a block. Add it to the game
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def makeRope(self, gameinfo=None):
		dist = self.findDist(gameinfo)
		#print("block until ", dist)
		name = "rope" + str(dist)

		from .entities import Entities

		# self.mat = pygame.image.load('resources%sentities%s%s' % (os.sep, os.sep, entschema[name]['mat']))
		rope = Entities.makeEnt(self.name + str(dist), self.x, self.y)
		self.mat = rope.mat

		self.x = ((int)((self.x+1)/32)) * 32 + (32 - self.width) / 2 
		print("before ", self.y)
		self.y = int(self.y/32) * 32
		# self.height = entschema[name]["height"]
		self.height = rope.dimension()[0]
		print("Rope of length ", dist, "placed at ", self.x, self.y)

	## @brief Find the number of empty blocks downwards until the next solid block
	#  @param gameinfo ReadMap object representing the level environment
	#  @return int representing the number of empty blocks until the next solid block
	def findDist(self, gameinfo=None):
		dist = 1
		for dist in range(1, self.LENGTH + 1):
			#print("is block ok at ", (self.x+1)/32, (self.y+1)/32 + dist)
			if gameinfo.solid((self.x+1)/32, (self.y+1)/32 + dist) == True:
				break
		return dist

	# ## @brief Determine if a bomb is useable
	# #  @return False
	# def useable(self):
	# 	return False