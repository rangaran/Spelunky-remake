## @file snake.py
#  @author Niyatha
#  @brief Contain the specific Snake type
#  @date 04/11/2021

from .enemy import Enemy

## @brief Snake is an object of type Enemy
#  @details Extends from enemy.py and implements the secrets of M4.19
class Snake(Enemy):
	## @brief Constructor method for snake
	#  @param x an integer element indicating the x position of the snake enemy object
	#  @param y an integer element indicating the y position of the snake enemy object
	#  @param hp an integer element indicating the health points of the snake enemy object 
	#  @param mat an image representing the  snake object on the game screen
	#  @param name a string representing the name of the image of the object
	#  @param text a string representing additional object information
	#  @param width an integer element indicating the width of the snake object
	#  @param height an integer element indicating the height of the snake object
	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
		super().__init__(x, y, name, height, width, hp, mat)
		self.xs = 0.5
		self.SNAKEATTACK = 1
		self.attack = self.SNAKEATTACK
        
	## @brief Move the snake
    #  @details If there is no solid block the snake continues movement. If solid block exists
	#			switch direction of straightline movement.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param x subsequent movement by x amount on x axis 
	#  @param y subsequent movement by y amount on y axis 
	def move(self, gameinfo=None, x=None,y=None):
		tempx = self.x + x

		# turn if block in front is solid or if going forward would lead to falling off edge
		if x>0:
			if (gameinfo.solid((tempx+(self.width-1))/32, (self.y+1)/32) == True and \
				gameinfo.solid((tempx+(self.width-1))/32, (self.y+(self.height-1))/32) == True) or \
				(gameinfo.solid((tempx+(self.width-1))/32, (self.y+1)/32 + 1) == False and \
				gameinfo.solid((tempx+(self.width-1))/32, (self.y+(self.height-1))/32 + 1) == False):
				self.xs = -self.xs
				self.flipImage(True, False)
			else:
				self.x = tempx

		
		if x<0:
			if (gameinfo.solid((tempx+1)/32, (self.y+1)/32) == True and \
			gameinfo.solid((tempx+1)/32, (self.y+(self.height-1))/32) == True) or \
			(gameinfo.solid((tempx+1)/32, (self.y+1)/32 + 1) == False and \
			gameinfo.solid((tempx+1)/32, (self.y+(self.height-1))/32 + 1) == False):
				self.xs = -self.xs
				self.flipImage(True, False)
			else:
				self.x = tempx

		if y>0:
			tempy = self.y + y 
			if gameinfo.solid((self.x+1)/32, (tempy+(self.height-1))/32) == False and gameinfo.solid((self.x+(self.width-1))/32, (tempy+(self.height-1))/32) == False:
				self.y = tempy
				self.ys += 0.1

		#if gameinfo.gamemap.tile((tempx+1)/32,(self.y)/32).soli == False and \
		#	gameinfo.gamemap.tile((tempx)/32,(self.y+(self.height))/32).soli == False:
		#	self.x = tempx
		#	self.dist += self.moving
		#else:
		#	self.moving = - self.moving
		#	self.dist -= self.moving

		#print("snake moving ", gameinfo.gamemap.tile((tempx+1)/32,(self.y)/32).soli == False and \
		#	gameinfo.gamemap.tile((tempx)/32,(self.y+(self.height))/32).soli == False)
			
			
	# ## @brief Make the snake
    # #  @details Create the snake on the map based on coordinates predefined in map file. Add it to the playable game
	# #  @param gameinfo ReadMap object representing the level environment
	# def makeSnake(self, gameinfo=None):
	# 	dist = self.findDist(gameinfo)
	# 	print("block until ", dist)
	# 	name = "snake" 
	# 	newent = entschema[name]
	# 	self.mat = pygame.image.load('resources%sentities%s%s' % (os.sep, os.sep, newent['mat']))
	# 	self.x = ((int)((self.x+1)/32)) * 32 + (32 - self.width) / 2 
	# 	self.height = entschema[name]["height"]
	# 	print("snake moved to ", self.x)

	# ## @brief Inflicts the snake object damage on the player's health and checks the range of attack per tick
	# #  @param gameinfo a ReadMap object element indicating the map where the snake object is on
	# #  @param player a Mover object element representing the player of the game that is on the snake object	
	# def tick(self, gameinfo=None, player=None):
	# 	self.move(gameinfo, self.moving, 0)
	# 	#print("snake move")
	# 	if self.overlap(player):
	# 		player.damage(self.SNAKEDAMAGE)

	# ## @brief Damage the player
	# #  @param gameinfo ReadMap object representing the level environment
	# #  @param d damage amount to hp
	# def damage(self, d=0, gameinfo=None):
	# 	super().damage(d, gameinfo)
	# 	if self.hp <= 0:
	# 		gameinfo.entlist.rem(self)