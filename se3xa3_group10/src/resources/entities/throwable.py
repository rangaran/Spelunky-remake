## @file throwable.py
#  @author Albert
#  @brief Contain the specific Throwable type
#  @date 04/11/2021

from .entity import Entity

## @brief Throwable is an object of type Entity
#  @details Extends from entity.py and implements the secrets of M4.14
class Throwable(Entity):
	## @brief Constructor method for Throwable
    #  @details Create the throwable using super(). Set the speeds to 0, possesions to False.
	#  @param x int representing the x position of the throwable
	#  @param y int representing the y position of the throwable
	#  @param hp int representing the health points of the throwable 
	#  @param mat image representing the throwable on the game screen
	#  @param name string representing the name of the image of the object
	#  @param width int representing the width of the throwable
	#  @param height int representing the height of the throwable
	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
		super().__init__(x, y, name, height, width, hp, mat)
		self.xs = 0
		self.ys = 0
		self.held = False
		self.thrown = False
		self.direction = 1
		self.GRAVITY = 3
		self.TOOFASTFORGRAVITY = 1

	## @brief Set held to True
	def pickup(self):
		self.held = True

	## @brief Set held to False
	def putDown(self):
		self.held = False

	## @brief Throw the throeable
    #  @details Set the speeds and possesion.
	#  @param xs int representing the x speed
	#  @param ys int representing the y speed
	def throw(self, xs=None, ys=None):
		self.xs = xs
		self.ys = ys
		self.direction = xs//abs(xs) if xs != 0 else self.direction

		self.held = False
		self.thrown = True
		print("started throw ", self.xs, self.ys)

	## @brief Reverse image and direction
	def flip(self):
		super().flipImage(True, False)
		self.direction = -self.direction

	## @brief Remove the throwable
    #  @details Remove the explosion from the game, and empty the player's hand.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def rem(self, gameinfo=None, player=None):
		print("used")
		#super().use(gameinfo, player)
		gameinfo.rem(self)
		self.putDown()
		if player.hand == self:
			player.hand = Entities.makeEnt("emptyHand", player.x, player.y)

	## @brief Update the throwable with 1 unit of time
    #  @details If not held, the throwable is affected by gravity.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def tick(self, gameinfo=None, player=None):
		if not(self.held):
			self.gravity(gameinfo)
			self.move(gameinfo, self.xs, self.ys)

	## @brief Adjust movement of the throwable
    #  @details If xs is not grater than TOOFASTFORGRAVITY, the throwable is affected by gravity.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def gravity(self, gameinfo=None):
		self.ys = self.GRAVITY# + self.ys
		if abs(self.xs) >= self.TOOFASTFORGRAVITY:
			self.ys = 0
		#self.move(gameinfo, self.xs, ys)

	## @brief Move the throwable
    #  @details Move the throwable, If it collides with a solid block, stop it.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player	def move(self, gameinfo=None, x=None, y=None):
	def move(self, gameinfo=None, x=None, y=None):
		if x>0:
			tempx = self.x + x 
			if gameinfo.solid((tempx+(self.width-1))/32, (self.y+1)/32) == False and gameinfo.solid((tempx+(self.width-1))/32, (self.y+(self.height-1))/32) == False:
				self.x = self.x + x
			else:
				self.xs = 0
		
		if x<0:
			tempx = self.x + x 
			if gameinfo.solid((tempx+1)/32, (self.y+1)/32) == False and gameinfo.solid((tempx+1)/32, (self.y+(self.height-1))/32) == False:
				self.x = self.x + x
			else:
				self.xs = 0
			
		if y>0:
			tempy = self.y + y 
			if gameinfo.solid((self.x+1)/32, (tempy+(self.height-1))/32) == False and gameinfo.solid((self.x+(self.width-1))/32, (tempy+(self.height-1))/32) == False:
				self.y = tempy
				if self.ys <= 1:
					self.ys += 0.1
				#print("gravity ", self.ys)
			else:
				self.ys = 0
			
		if y<0:
			tempy = self.y + y 
			if gameinfo.solid((self.x+1)/32, (tempy+1)/32) == False and gameinfo.solid((self.x+(self.width-1))/32, (tempy+1)/32) == False:
				self.y = tempy

	## @brief Carry the throwable
    #  @details Carry the throwable while ignoring solid blocks.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def carry(self, gameinfo=None, x=None, y=None):
		super().move(x, y)
