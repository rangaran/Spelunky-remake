## @file arrow.py
#  @author Abeer
#  @brief Contain the specific Arrow type represented by a Throwable
#  @date 04/11/2021

from .throwable import Throwable

## @brief Arrow is an object of type Throwable
#  @details Extends from throwable.py and implements the secrets of M4.15
class Arrow(Throwable):
	
	## @brief Constructor method for Arrow
	#  @param x an integer element indicating the x position of the arrow object
	#  @param y an integer element indicating the y position of the arrow object
	#  @param hp an integer element indicating the health points of the arrow object 
	#  @param mat an image representing the arrow object on the game screen
	#  @param name a string representing the name of the image of the object
	#  @param width an integer element indicating the width of the arrow object
	#  @param height an integer element indicating the height of the arrow object
	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
		super().__init__(x, y, name, height, width, hp, mat)
		#self.arrowSpeed = 2
		self.ARROWDAMAGE = 2
		#self.arrowTime = -1
		#self.moveX = self.x
		self.playerOwned = False
	
	## @brief Set held and playerOwned to True
	def pickup(self):
		super().pickup()
		self.playerOwned = True

	## @brief Set held and playerOwned to False
	def putDown(self):
		super().putDown()
		self.playerOwned = False

	## @brief animation movement of the arrow object that is in attack mode  
	#  @param gameinfo a ReadMap object element indicating the map where the arrow object is on
	#  @param player a Mover object element representing the player of the game that is within range of arrow attack 
	def tick(self, gameinfo=None, player=None):
		super().tick(gameinfo, player)
		# self.destroyArrow(gameinfo, player)
		# self.arrowTime -= 1
		#if self.arrowTime == 0:
		#	gameinfo.rem(self)
		#self.arrowMove(gameinfo, player.x)
		#self.move(gameinfo, self.xs, self.ys)
		if self.xs != 0:
			if not(self.playerOwned) and self.overlap(player):
				player.damage(self.ARROWDAMAGE)
				self.xs = 0
			else:
				for ent in gameinfo.enemies():
					if self.overlap(ent):
						ent.damage(self.ARROWDAMAGE, gameinfo)
						self.xs = 0
						break
		#self.destroyArrow(gameinfo, player)
	
	# ## @brief updates the movement of the arrow object that is in attack mode by updating the positions of the object  
	# #  @param gameinfo a ReadMap object element indicating the map where the arrow object is on
	# #  @param playerPos an integer element representing the player x position in the game to check for arrow surroundings
	# def arrowMove(self, gameinfo, playerPos):
	# 	if playerPos > self.x: #shoot right
	# 		tempx = self.x + self.arrowSpeed
	# 		#print("check move right")
	# 		if gameinfo.solid((tempx+(self.width-1))/32, (self.y+1)/32) == False and gameinfo.solid((tempx+(self.width-1))/32, (self.y+(self.height-1))/32) == False:
	# 			#self.moveX = self.moveX + self.arrowSpeed
	# 			self.x = tempx
	# 			#print("move right")
	# 			#rightDirection(gameinfo, player, moveX, self.y)
	# 	else: 
	# 		tempx = self.x - self.arrowSpeed 
	# 		#print("check move left")
	# 		if gameinfo.solid((tempx+1)/32, (self.y+1)/32) == False and gameinfo.solid((tempx+1)/32, (self.y+(self.height-1))/32) == False:
	# 		#self.moveX = self.moveX - self.arrowSpeed
	# 			self.x = tempx
	# 			#print("move left")
	# 		#leftDirection(gameinfo, player, moveX, self.y)
			
	# ## @brief inflicts the arrow object damage on the player that is near the arrow attack and destroys the arrow after the attack  
	# #  @param gameinfo a ReadMap object element indicating the map where the arrow object is on
	# #  @param player a Mover object element representing the player of the game that is within range of arrow attack
	# def destroyArrow(self, gameinfo=None, player=None):
	# 	if self.overlap(player):
	# 		#gameinfo.rem(self)
	# 		player.damage(self.ARROWDAMAGE)
	# 		#self.arrowSpeed = 0
	# 		self.xs = 0