## @file spider.py
#  @author Niyatha
#  @brief Contain the specific Spider type
#  @date 03/29/2021

from .enemy import Enemy

## @brief Spider is an object of type Enemy
#  @details Extends from enemy.py and implements the secrets of M4.20
class Spider(Enemy):
	## @brief Constructor method for spider
	#  @param x an integer element indicating the x position of the spider enemy object
	#  @param y an integer element indicating the y position of the spider enemy object
	#  @param hp an integer element indicating the health points of the spider enemy object 
	#  @param mat an image representing the  spider object on the game screen
	#  @param name a string representing the name of the image of the object
	#  @param width an integer element indicating the width of the spider object
	#  @param height an integer element indicating the height of the spider object
	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
		super().__init__(x, y, name, height, width, hp, mat)
		self.MAXJUMP = 24
		self.time = 0
		self.CD = 2*90
		self.jumpDist = 0
		self.senseRange = 4
		self.SPIDERATTACK = 1
		self.attack = self.SPIDERATTACK

	## @brief Controls jump that is gravity restrictions of spider
    #  @details If jumping, set ys to -gravity and increase jumpDist. Else, set ys to gravity
	#			and reset jumpDist
	def gravity(self):
		if self.ys < 0 and self.jumpDist < self.MAXJUMP:
			self.ys = -self.GRAVITY
			self.jumpDist += 1
		else:
			#print("falling down")
			self.jumpDist = 0
			self.ys = self.GRAVITY

	## @brief Move the spider
    #  @details If there is no solid block the spider can continue to jump based on the spider sense
	#			wrt the player's position
	#  @param gameinfo ReadMap object representing the level environment
	#  @param x subsequent movement by x amount on x axis 
	#  @param y subsequent movement by y amount on y axis
	def move(self, gameinfo=None, x=None, y=None):
		if x>0:
			tempx = self.x + x 
			if gameinfo.solid((tempx+(self.width-1))/32, (self.y+1)/32) == False and gameinfo.solid((tempx+(self.width-1))/32, (self.y+(self.height-1))/32) == False:
				self.x = self.x + x
		
		if x<0:
			tempx = self.x + x 
			if gameinfo.solid((tempx+1)/32, (self.y+1)/32) == False and gameinfo.solid((tempx+1)/32, (self.y+(self.height-1))/32) == False:
				self.x = self.x + x
			
		if y>0:
			tempy = self.y + y 
			if gameinfo.solid((self.x+1)/32, (tempy+(self.height-1))/32) == False and gameinfo.solid((self.x+(self.width-1))/32, (tempy+(self.height-1))/32) == False:
				#Falling
				self.y = tempy
				self.ys += 0.1
			else:
				#landing
				self.xs = 0

		if y<0:
			tempy = self.y + y 
			if gameinfo.solid((self.x+1)/32, (tempy+1)/32) == False and gameinfo.solid((self.x+(self.width-1))/32, (tempy+1)/32) == False:
				self.y = tempy
			else:
				self.jumpDist = 0
				self.ys = 0

	## @brief Inflicts the spider object damage on the player's health and checks the range of attack per tick
	#  @param gameinfo a ReadMap object element indicating the map where the spider object is on
	#  @param player a Mover object element representing the player of the game that is on the spider object
	def tick(self, gameinfo=None, player=None):
		self.sense(player)
		self.gravity()

		if self.time > 0:
			self.time -= 1

		self.move(gameinfo, self.xs, self.ys)

		if self.overlap(player):
			player.damage(self.attack)   
    
	## @brief Sense the player based on range from the spider
	#  @param player Mover object representing the player
	def sense(self, player=None):
		#check y level
		if self.y < player.y+player.height and player.y < self.y+self.height:
			#print("y-level")#check the x distance
			if abs(self.x - player.x) <= self.senseRange*32 and self.time == 0:
				if self.x < player.x:
					self.xs = 1
				else:
					self.xs = -1
				self.time = self.CD
				self.ys = -1

	# ## @brief Damage the player
	# #  @param gameinfo ReadMap object representing the level environment
	# #  @param d damage amount to hp
	# def damage(self, d=0, gameinfo=None):
	# 	super().damage(d, gameinfo)
	# 	if self.hp <= 0:
	# 		gameinfo.entlist.rem(self)

	# ## @brief Make the spider
    # #  @details Create the spider on the map based on coordinates predefined in map file. Add it to the playable game
	# #  @param gameinfo ReadMap object representing the level environment
	# def makeSpider(self, gameinfo=None):
	# 	dist = self.findDist(gameinfo)
	# 	print("block until ", dist)
	# 	name = "spider" 
	# 	newent = entschema[name]
	# 	self.mat = pygame.image.load('resources%sentities%s%s' % (os.sep, os.sep, newent['mat']))
	# 	self.x = ((int)((self.x+1)/32)) * 32 + (32 - self.width) / 2 
	# 	self.height = entschema[name]["height"]
	# 	print("spider moved to ", self.x)
