## @file entity.py
#  @author Albert
#  @brief Contain the specific Entity type
#  @date 04/11/2021
import pygame

## @brief Entity is an object
#  @details Implements the secrets of M4.1
class Entity():
	## @brief Constructor method for Entity
    #  @details Set the state.
	#  @param x int representing the x position of the entity
	#  @param y int representing the y position of the entity
	#  @param hp int representing the health points of the entity 
	#  @param mat image representing the entity on the game screen
	#  @param name string representing the name of the image of the object
	#  @param width int representing the width of the entity
	#  @param height int representing the height of the entity
	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.hp = hp
		self.mat = mat
		self.name = name

	## @brief Change the position
	#  @param x int representing the change in the x axis
	#  @param y int representing the change in the y axis
	def move(self, x=None, y=None):
		self.x += x
		self.y += y

	## @brief Set the position
	#  @param x int representing the position in the x axis
	#  @param y int representing the position in the y axis
	def set(self, x=None, y=None):
		self.x = x
		self.y = y	

	## @brief Get the position
	#  @return int, int representing the position in the x and y axis
	def position(self):
		return (self.x,self.y)

	## @brief Get the dimensions
	#  @return int, int representing the height and width
	def dimension(self):
		return (self.height,self.width)

	## @brief Take damage
    #  @details Take damage
	#  @param d int representing the damage taken
	#  @param gameinfo ReadMap object representing the level environment
	def damage(self, d=0, gameinfo=None):
		self.hp -= d

	## @brief Determine if an entity overlaps with self
    #  @details Check corners
	#  @param ent Entity object representing another Entity
	def overlap(self, ent=None):
		l1 = (self.position()[0], self.position()[1])
		r1 = (self.position()[0] + self.width, self.position()[1] + self.height)

		l2 = (ent.position()[0], ent.position()[1])
		r2 = (ent.position()[0] + ent.width, ent.position()[1] + ent.height)

		if(l1[0] >= r2[0] or l2[0] >= r1[0]): 
			return False
	
		if(l1[1] >= r2[1] or l2[1] >= r1[1]): 
			return False
	
		return True

	## @brief Update the Entity with 1 unit of time
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def tick(self, gameinfo=None, player=None):
		pass

	## @brief Determine if an entity is useable
	#  @return False
	def useable(self):
		return False

	## @brief Use the entity
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def use(self, gameinfo=None, player=None):
		pass

	## @brief Flip mat
	#  @param x boolean representing vertical mirroring
	#  @param y boolean representing horizontal mirroring
	def flipImage(self, x=None, y=None):
		self.mat = pygame.transform.flip(self.mat, x, y)