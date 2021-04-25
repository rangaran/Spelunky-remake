## @file entities.py
#  @author Albert
#  @brief M4 Contains entity creation
#  @date 04/11/2021
import pygame
import os

from .whip import Whip
from .spikes import Spikes
from .arrowTrap import ArrowTrap
from .arrow import Arrow
from .throwable import Throwable
from .emptyHand import EmptyHand
from .chest import Chest
from .bomb import Bomb
from .explosion import Explosion
from .rope import Rope
from .snake import Snake
from .spider import Spider
from .gold import Gold
from .sapphire import Sapphire
from .emerald import Emerald
from .ruby import Ruby
from .diamond import Diamond 
from .bombPile import BombPile
from .ropePile import RopePile
from .sign import Sign

entschema = {"chest":{"hp":0,"mat":"chest.png","width":12,"height":12,'obj':Chest},
			"gold":{"hp":0,"mat":"gold.png","width":24,"height":7,'obj':Gold},
			"emerald":{"hp":0,"mat":"emerald.png","width":20,"height":17,'obj':Emerald},
			"sapphire":{"hp":0,"mat":"sapphire.png","width":17,"height":18,'obj':Sapphire},
			"ruby":{"hp":0,"mat":"ruby.png","width":19,"height":19,'obj':Ruby},
			"diamond":{"hp":0,"mat":"diamond.png","width":23,"height":17,'obj':Diamond},
			"bombPile":{"hp":0,"mat":"bombPile.png","width":12,"height":12,'obj':BombPile},
			"ropePile":{"hp":0,"mat":"ropePile.png","width":12,"height":13,'obj':RopePile},
			"snake":{"hp":0,"mat":"snake.png","width":20,"height":19,'obj':Snake},
			"spider":{"hp":0,"mat":"spider.png","width":12,"height":12,'obj':Spider},
			"sign":{"hp":0,"mat":"sign.png","width":22,"height":23,'obj':Sign},
			"bomb":{"hp":1,"mat":"bomb.png","width":12,"height":12,'obj':Bomb},
			"explosion":{"hp":0,"mat":"explosion.png","width":48,"height":48,'obj':Explosion},
			"rope":{"hp":0,"mat":"rope.png","width":10,"height":10,'obj':Rope},
			"rope1":{"hp":0,"mat":"rope1.png","width":4,"height":32,'obj':Rope},
			"rope2":{"hp":0,"mat":"rope2.png","width":4,"height":64,'obj':Rope},
			"rope3":{"hp":0,"mat":"rope3.png","width":4,"height":96,'obj':Rope},
			"rope4":{"hp":0,"mat":"rope4.png","width":4,"height":128,'obj':Rope},
			"arrow":{"hp":0,"mat":"sArrowLeft_0.png","width":8,"height":8,'obj':Arrow},
			"arrowTrap":{"hp":0,"mat":"sArrowTrapLeft_0.png","width":16,"height":16,'obj':ArrowTrap},
			"spikes":{"hp":0,"mat":"spikes.png","width":32,"height":20,'obj':Spikes},
			"emptyHand":{"hp":0,"mat":"emptyHand.png","width":1,"height":1,'obj':EmptyHand},
			"whip":{"hp":0,"mat":"whip.png","width":16,"height":4,'obj':Whip}}	
			
## @brief Entities is a class that makes entities
#  @details Implements the secrets of M4
class Entities():
	## @brief Create an entity
	#  @param x an integer element indicating the x position of the entity object
	#  @param y an integer element indicating the y position of the entity object
	#  @param name a string representing the name of the entity
	#  @return Entity object representing the created entity
	def makeEnt(name, x, y):
			entattri = entschema[name]

			mat = pygame.image.load('resources%sentities%simages%s%s' % (os.sep, os.sep, os.sep, entattri['mat']))
			hp = entattri['hp']

			height = entattri['height']
			width = entattri['width']
			#text = ""
			newent = entschema[name]

			#print("placed at ",self.x, self.y)

			#print(x,y,hp,mat,name,text,width,height)

			entobj = newent['obj'](x,y,name,height,width,hp,mat)

			return entobj


# class Throwable(Entity):
# 	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
# 		super().__init__(x, y, name, height, width, hp, mat)
# 		self.xs = 0
# 		self.ys = 0
# 		self.held = False
# 		self.thrown = False
# 		self.direction = 1
# 		self.GRAVITY = 3
# 		self.TOOFASTFORGRAVITY = 1

# 	def pickup(self):
# 		self.held = True

# 	def putDown(self):
# 		self.held = False

# 	def throw(self, xs=None, ys=None):
# 		self.xs = xs
# 		self.ys = ys
# 		self.direction = xs//abs(xs) if xs != 0 else self.direction

# 		self.held = False
# 		self.thrown = True
# 		print("started throw ", self.xs, self.ys)

# 	def flip(self):
# 		super().flipImage(True, False)
# 		self.direction = -self.direction

# 	def rem(self, gameinfo=None, player=None):
# 		print("used")
# 		#super().use(gameinfo, player)
# 		gameinfo.rem(self)
# 		self.putDown()
# 		if player.hand == self:
# 			player.hand = Entities.makeEnt("emptyHand", player.x, player.y)

# 	def tick(self, gameinfo=None, player=None):
# 		if not(self.held):
# 			self.gravity(gameinfo)
# 			self.move(gameinfo, self.xs, self.ys)


# 	def gravity(self, gameinfo=None):
# 		self.ys = self.GRAVITY# + self.ys
# 		if abs(self.xs) >= self.TOOFASTFORGRAVITY:
# 			self.ys = 0
# 		#self.move(gameinfo, self.xs, ys)

# 	def move(self, gameinfo=None, x=None, y=None):
# 		if x>0:
# 			tempx = self.x + x 
# 			if gameinfo.solid((tempx+(self.width-1))/32, (self.y+1)/32) == False and gameinfo.solid((tempx+(self.width-1))/32, (self.y+(self.height-1))/32) == False:
# 				self.x = self.x + x
# 			else:
# 				self.xs = 0
		
# 		if x<0:
# 			tempx = self.x + x 
# 			if gameinfo.solid((tempx+1)/32, (self.y+1)/32) == False and gameinfo.solid((tempx+1)/32, (self.y+(self.height-1))/32) == False:
# 				self.x = self.x + x
# 			else:
# 				self.xs = 0
			
# 		if y>0:
# 			tempy = self.y + y 
# 			if gameinfo.solid((self.x+1)/32, (tempy+(self.height-1))/32) == False and gameinfo.solid((self.x+(self.width-1))/32, (tempy+(self.height-1))/32) == False:
# 				self.y = tempy
# 				if self.ys <= 1:
# 					self.ys += 0.1
# 				#print("gravity ", self.ys)
# 			else:
# 				self.ys = 0
			
# 		if y<0:
# 			tempy = self.y + y 
# 			if gameinfo.solid((self.x+1)/32, (tempy+1)/32) == False and gameinfo.solid((self.x+(self.width-1))/32, (tempy+1)/32) == False:
# 				self.y = tempy

# 	def carry(self, gameinfo=None, x=None, y=None):
# 		super().move(x, y)

# class Collectable(Entity):
# 	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
# 		super().__init__(x, y, name, height, width, hp, mat)
# 		self.val = collectableschema[name]['val']

# 	def useable(self):
# 		return True

# 	def use(self, gameinfo=None, player=None):
# 		gameinfo.rem(self)

# class Treasure(Collectable):
# 	def use(self, gameinfo=None, player=None):
# 		super().use(gameinfo, player)
# 		player.gold += self.val
# 		print ("player gold: ", player.gold)


# class Gold(Treasure):
# 	pass

# class Sapphire(Treasure):
# 	pass

# class Emerald(Treasure):
# 	pass

# class Ruby(Treasure):
# 	pass

# class Diamond(Treasure):
# 	pass

# class BombPile(Collectable):
# 	def use(self, gameinfo=None, player=None):
# 		super().use(gameinfo, player)
# 		player.bombs += self.val

# class RopePile(Collectable):
# 	def use(self, gameinfo=None, player=None):
# 		super().use(gameinfo, player)
# 		player.ropes += self.val

# class Chest(Throwable):
# 	# def __init__(self, x=None, y=None, name=None, height=None,
# 	# 			 width=None, hp=None, mat=None):
# 	# 	super().__init__(x, y, name, height, width, hp, mat)
# 		# self.open = False

# 	def useable(self):
# 		return True

# 	def use(self, gameinfo=None, player=None):
# 		super().rem(gameinfo, player)
# 		# if (self.open):
# 		# 	return
# 		# self.open = True

# 		namelist = ['gold','emerald', 'sapphire', 'ruby', 'diamond', 'bombPile', 'ropePile']
# 		name = random.choice(namelist)

# 		height = entschema[name]['height']
# 		width = entschema[name]['width']
# 		x = int(self.x + (self.width/2 - width/2))
# 		y = int(self.y + self.height - height )

# 		gameinfo.add(Entities.makeEnt(name, x, y))
# 		#gameinfo.rem(self)

# class Sign(Entity):
# 	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
# 		super().__init__(x, y, name, height, width, hp, mat)
# 		self.text= ""
# 	def setText(self, s):
# 		self.text = s
	
# 	def getText(self):
# 		return self.text


#-------------------ENEMY-------------------------
# class Enemy(Entity):
# 	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
# 		super().__init__(x, y, name, height, width, hp, mat)
# 		self.xs = 0
# 		self.ys = 0
# 		self.GRAVITY = 3
# 		self.attack = 0

# 	def tick(self, gameinfo=None, player=None):
# 		self.gravity()
# 		self.move(gameinfo, self.xs, self.ys)

# 		if self.overlap(player):
# 			player.damage(self.attack)

# 	def damage(self, d=0, gameinfo=None):
# 		super().damage(d, gameinfo)
# 		if self.hp <= 0:
# 			gameinfo.rem(self)

# 	def gravity(self):
# 		self.ys = self.GRAVITY

# 	def move(self, gameinfo=None, x=None,y=None):
# 		pass

# class Spider(Enemy):
# 	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
# 		super().__init__(x, y, name, height, width, hp, mat)
# 		self.MAXJUMP = 24
# 		self.time = 0
# 		self.CD = 2*90
# 		self.jumpDist = 0
# 		self.senseRange = 4
# 		self.SPIDERATTACK = 1
# 		self.attack = self.SPIDERATTACK

# 	def gravity(self):
# 		if self.ys < 0 and self.jumpDist < self.MAXJUMP:
# 			self.ys = -self.GRAVITY
# 			self.jumpDist += 1
# 		else:
# 			#print("falling down")
# 			self.jumpDist = 0
# 			self.ys = self.GRAVITY

# 	def move(self, gameinfo=None, x=None, y=None):
# 		if x>0:
# 			tempx = self.x + x 
# 			if gameinfo.solid((tempx+(self.width-1))/32, (self.y+1)/32) == False and gameinfo.solid((tempx+(self.width-1))/32, (self.y+(self.height-1))/32) == False:
# 				self.x = self.x + x
		
# 		if x<0:
# 			tempx = self.x + x 
# 			if gameinfo.solid((tempx+1)/32, (self.y+1)/32) == False and gameinfo.solid((tempx+1)/32, (self.y+(self.height-1))/32) == False:
# 				self.x = self.x + x
			
# 		if y>0:
# 			tempy = self.y + y 
# 			if gameinfo.solid((self.x+1)/32, (tempy+(self.height-1))/32) == False and gameinfo.solid((self.x+(self.width-1))/32, (tempy+(self.height-1))/32) == False:
# 				#Falling
# 				self.y = tempy
# 				self.ys += 0.1
# 			else:
# 				#landing
# 				self.xs = 0

# 		if y<0:
# 			tempy = self.y + y 
# 			if gameinfo.solid((self.x+1)/32, (tempy+1)/32) == False and gameinfo.solid((self.x+(self.width-1))/32, (tempy+1)/32) == False:
# 				self.y = tempy
# 			else:
# 				self.jumpDist = 0
# 				self.ys = 0

# 	def tick(self, gameinfo=None, player=None):
# 		self.sense(player)
# 		self.gravity()

# 		if self.time > 0:
# 			self.time -= 1

# 		self.move(gameinfo, self.xs, self.ys)

# 		if self.overlap(player):
# 			player.damage(self.attack)

# 	def sense(self, player=None):
# 		#check y level
# 		if self.y < player.y+player.height and player.y < self.y+self.height:
# 			#print("y-level")#check the x distance
# 			if abs(self.x - player.x) <= self.senseRange*32 and self.time == 0:
# 				if self.x < player.x:
# 					self.xs = 1
# 				else:
# 					self.xs = -1
# 				self.time = self.CD
# 				self.ys = -1

# class Snake(Enemy):
# 	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
# 		super().__init__(x, y, name, height, width, hp, mat)
# 		self.xs = 0.5
# 		self.SNAKEATTACK = 1
# 		self.attack = self.SNAKEATTACK
			
# 	def move(self, gameinfo=None, x=None,y=None):
# 		tempx = self.x + x

# 		# turn if block in front is solid or if going forward would lead to falling off edge
# 		if x>0:
# 			if (gameinfo.solid((tempx+(self.width-1))/32, (self.y+1)/32) == True and \
# 				gameinfo.solid((tempx+(self.width-1))/32, (self.y+(self.height-1))/32) == True) or \
# 				(gameinfo.solid((tempx+(self.width-1))/32, (self.y+1)/32 + 1) == False and \
# 				gameinfo.solid((tempx+(self.width-1))/32, (self.y+(self.height-1))/32 + 1) == False):
# 				self.xs = -self.xs
# 				self.flipImage(True, False)
# 			else:
# 				self.x = tempx

		
# 		if x<0:
# 			if (gameinfo.solid((tempx+1)/32, (self.y+1)/32) == True and \
# 			gameinfo.solid((tempx+1)/32, (self.y+(self.height-1))/32) == True) or \
# 			(gameinfo.solid((tempx+1)/32, (self.y+1)/32 + 1) == False and \
# 			gameinfo.solid((tempx+1)/32, (self.y+(self.height-1))/32 + 1) == False):
# 				self.xs = -self.xs
# 				self.flipImage(True, False)
# 			else:
# 				self.x = tempx

# 		if y>0:
# 			tempy = self.y + y 
# 			if gameinfo.solid((self.x+1)/32, (tempy+(self.height-1))/32) == False and gameinfo.solid((self.x+(self.width-1))/32, (tempy+(self.height-1))/32) == False:
# 				self.y = tempy
# 				self.ys += 0.1

		#if gameinfo.solid((tempx+1)/32,(self.y)/32) == False and \
		#	gameinfo.solid((tempx)/32,(self.y+(self.height))/32) == False:
		#	self.x = tempx
		#	self.dist += self.moving
		#else:
		#	self.moving = - self.moving
		#	self.dist -= self.moving

		#print("snake moving ", gameinfo.solid((tempx+1)/32,(self.y)/32) == False and \
		#	gameinfo.solid((tempx)/32,(self.y+(self.height))/32) == False)

	# def makeSnake(self, gameinfo=None):
	# 	dist = self.findDist(gameinfo)
	# 	print("block until ", dist)
	# 	name = "snake" 
	# 	newent = entschema[name]
	# 	self.mat = pygame.image.load('resources%sentities%s%s' % (os.sep, os.sep, newent['mat']))
	# 	self.x = ((int)((self.x+1)/32)) * 32 + (32 - self.width) / 2 
	# 	self.height = entschema[name]["height"]
	# 	print("snake moved to ", self.x)
		
	# def tick(self, gameinfo=None, player=None):
	# 	self.move(gameinfo, self.moving, 0)
	# 	#print("snake move")
	# 	if self.overlap(player):
	# 		player.damage(self.SNAKEDAMAGE)

	# def damage(self, d=0, gameinfo=None):
	# 	super().damage(d, gameinfo)
	# 	if self.hp <= 0:
	# 		gameinfo.rem(self)
#-------------------ENEMY-------------------------

# class Bomb(Throwable):
# 	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
# 		super().__init__(x, y, name, height, width, hp, mat)
# 		self.BOMBTIME = 180
# 		#self.BOMBSIZE = 2
# 		self.time = self.BOMBTIME
		
# 	def tick(self, gameinfo=None, player=None):
# 		self.time -= 1

# 		super().tick(gameinfo, player)

# 		if self.time == 0 or (self.thrown and self.xs == 0) or self.hp <= 0:
# 			self.explode(gameinfo, player)

# 		# return self.time == 0

# 	def explode(self, gameinfo=None, player=None):
# 		#print ("explosion")

# 		height = entschema["explosion"]['height']
# 		width = entschema["explosion"]['width']
# 		x = int(self.x - width/2 + self.width)
# 		y = int(self.y - height/2 + self.height)

# 		print("Explosion at ",x, y)

# 		#print(x,y,hp,mat,name,text,width,height)

# 		explosion = Entities.makeEnt("explosion", x, y)
# 		gameinfo.add(explosion)
# 		self.rem(gameinfo, player)
# 		explosion.explode(gameinfo, player)

	# def useable(self):
	# 	return False

# class Explosion(Entity):
# 	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
# 		super().__init__(x, y, name, height, width, hp, mat)
# 		self.DURATION = 45
# 		self.time = self.DURATION
# 		self.DAMAGE = 10

# 	def tick(self, gameinfo=None, player=None):
# 		self.time -= 1

# 		if self.time == 0:
# 			gameinfo.rem(self)

# 	def explode(self, gameinfo=None, player=None):
# 		self.destroyBlock(gameinfo)
# 		self.destroyEnt(gameinfo)
# 		self.destroyPlayer(player)

# 	def destroyBlock(self, gameinfo=None):
# 		destroyed = []
# 		w = (self.x, self.x + self.width)
# 		h = (self.y, self.y + self.height)

# 		for i in range(int(w[0]/32), int(w[1]/32) + 1):
# 			for j in range(int(h[0]/32), int(h[1]/32) + 1):
# 				destroyed.append((i, j))

# 		for b in destroyed:
# 			gameinfo.destroyBlock(b[0],b[1])


# 	def destroyEnt(self, gameinfo=None):
# 		destroyed = []
# 		for ent in gameinfo.entities():
# 			if self.overlap(ent):
# 				print("Explosion affected ",ent.name, ent.x//32, " ", ent.y//32)
# 				destroyed.append(ent)

# 		for ent in destroyed:
# 			ent.damage(self.DAMAGE, gameinfo)

# 	def destroyPlayer(self, player=None):
# 		if self.overlap(player):
# 			player.damage(self.DAMAGE)

# 	def damage(self, d=0, gameinfo=None):
# 		pass

# class Rope(Entity):
# 	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
# 		super().__init__(x, y, name, height, width, hp, mat)
# 		self.LENGTH = 4
# 		self.ys = 0
# 		self.dist = self.LENGTH *32

# 	def throw(self):
# 		self.ys = -2

# 	def tick(self, gameinfo=None, player=None):
# 		if self.ys != 0:
# 			self.move(gameinfo, self.ys)

# 	def move(self, gameinfo=None, y=None):
# 		tempy = self.y + y 
# 		if gameinfo.solid((self.x+1)/32, (tempy-1)/32) == False and \
# 			gameinfo.solid((self.x+(self.width-1))/32, (tempy-1)/32) == False and \
# 			self.dist > 0:
# 			self.y = tempy
# 			self.dist += self.ys
# 		else:
# 			self.ys = 0
# 			self.makeRope(gameinfo)

# 	def makeRope(self, gameinfo=None):
# 		dist = self.findDist(gameinfo)
# 		#print("block until ", dist)
# 		name = "rope" + str(dist)

# 		self.mat = pygame.image.load('resources%sentities%s%s' % (os.sep, os.sep, entschema[name]['mat']))
# 		self.x = ((int)((self.x+1)/32)) * 32 + (32 - self.width) / 2 
# 		print("before ", self.y)
# 		self.y = int(self.y/32) * 32
# 		self.height = entschema[name]["height"]
# 		print("Rope of length ", dist, "placed at ", self.x, self.y)

# 	def findDist(self, gameinfo=None):
# 		dist = 1
# 		for dist in range(1, self.LENGTH + 1):
# 			#print("is block ok at ", (self.x+1)/32, (self.y+1)/32 + dist)
# 			if gameinfo.solid((self.x+1)/32, (self.y+1)/32 + dist) == True:
# 				break
# 		return dist

# class EmptyHand(Throwable):
# 	pass
	# def __init__(self, x=None, y=None, hp=None, mat=None, name=None, text=None, width=None,
	# 			 height=None):
	# 	super().__init__(x, y, name, height, width, hp, mat)

# class Weapon(Entity):
# 	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
# 		super().__init__(x, y, name, height, width, hp, mat)
# 		self.damage = 0
# 		self.speed = 0
# 		self.activeFrames = 0
# 		self.time = 0
# 		self.active = 0
# 		self.direction = 1

# 	def swing(self, gameinfo=None):
# 		if self.time > 0:
# 			return

# 		print("weapon swing")

# 		self.time = self.speed
# 		self.active = self.activeFrames
# 		gameinfo.add(self)

# 	def tick(self, gameinfo=None, player=None):
# 		if self.time > 0:
# 			self.time -= 1

# 		#print("weapon tick")
	
# 		if self.active > 0:
# 			for ent in gameinfo.enemies():
# 				if ent.overlap(self):
# 					ent.damage(self.damage, gameinfo)
# 			self.active -= 1
# 		else:
# 			gameinfo.rem(self)
# 			player.emptyHand()
# 			#print("whip gone")

# 	def carry(self, gameinfo=None, x=None, y=None):
# 		super().move(x, y)

# 	def flip(self):
# 		super().flipImage(True, False)
# 		self.direction = -self.direction
		

	#def active(self):
	#	return self.active > 0
# class Whip(Weapon):
# 	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
# 		super().__init__(x, y, name, height, width, hp, mat)
# 		self.damage = 1
# 		self.speed = 45
# 		self.activeFrames = 45

#------------NEWTraps-----------
# class Trap(Entity):

# 	def damage(self, d=0, gameinfo=None):
# 		super().damage(d, gameinfo)
# 		if self.hp <= 0:
# 			gameinfo.rem(self)

# class ArrowTrap(Trap):
# 	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
# 		super().__init__(x, y, name, height, width, hp, mat)
# 		self.arrowSense = 4 
# 		self.direction = -1
# 		#self.arrowMade = False
# 		# height = entschema["arrowL"]["height"]
# 		# width = entschema["arrowL"]["width"]
		
# 		# posx = int(self.x - width/2 + self.width/2)
# 		# posy = int(self.y - height + self.height)
		
# 		# self.arrow = makeEnt("arrowL", posx, posy)
		
# 		#time.sleep(2)
# 		self.arrowMade = True

# 	def setDirection(self, d):
# 		self.direction = d
# 		if self.direction == 1:
# 			self.flipImage(True, False)
# 	def sense(self,gameinfo=None, player=None):
# 		#check y level
# 		if self.y < player.y+player.height and player.y < self.y+self.height:
# 			#print("y-level")#check the x distance
# 			diff = player.x - self.x
# 			if diff != 0 and diff//abs(diff) == self.direction and abs(diff) <= 4*32:
# 				#print("x-level")
# 				return True
# 		#if player.y == self.y: #player.y < self.y+self.height or self.y < player.y+player.height:
# 		#	if player.x-self.x <= 4 or player.x-self.x >= -4:
# 		# if self.overlap(player):
# 			#print("trap detected player")
# 			# return True
# 		return False
# 	def tick(self, gameinfo=None, player=None):
# 		if self.arrowMade and self.sense(gameinfo, player):
# 			height = entschema["arrow"]["height"]
# 			width = entschema["arrow"]["width"]

# 			posx = int(self.x - width/2 + self.width/2)
# 			#posy = int(self.y - height + self.height)
# 			posy = int(self.y - height/2 + self.height/2)

# 			arrow = Entities.makeEnt("arrow", posx, posy)
# 			if self.direction == 1:
# 				arrow.flipImage(True, False)
# 			print("Trap will shoot arrow")
# 			gameinfo.add(arrow)
# 			arrow.throw(self.direction, 0)
# 			self.arrowMade = False
# 			#print("move")
# 			#self.arrow.arrowMove(gameinfo, player.x)
# 		#return True
# 	# def shoot(self, gameinfo=None, player=None):
# 		# places an arrow and shoots it
# 		# if self.arrowMade == False:
# 		# height = entschema["arrowL"]["height"]
# 		# width = entschema["arrowL"]["width"]
		
# 		# posx = int(self.x - width/2 + self.width/2)
# 		# posy = int(self.y - height + self.height)
		
# 		# arrow = makeEnt("arrowL", posx, posy)
# 		# gameinfo.add(arrow)
# 		# time.sleep(2)
# 		# self.arrowMade = True
# 		# arrow.arrowMove(gameinfo, player)
		
# class Arrow(Throwable):
# 	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
# 		super().__init__(x, y, name, height, width, hp, mat)
# 		#self.arrowSpeed = 2
# 		self.ARROWDAMAGE = 2
# 		#self.arrowTime = -1
# 		#self.moveX = self.x
# 		self.playerOwned = False

# 	def pickup(self):
# 		super().pickup()
# 		self.playerOwned = True

# 	def putDown(self):
# 		super().putDown()
# 		self.playerOwned = False

# 	def tick(self, gameinfo=None, player=None):
# 		super().tick(gameinfo, player)
# 		# self.destroyArrow(gameinfo, player)
# 		# self.arrowTime -= 1
# 		#if self.arrowTime == 0:
# 		#	gameinfo.rem(self)
# 		#self.arrowMove(gameinfo, player.x)
# 		#self.move(gameinfo, self.xs, self.ys)
# 		if self.xs != 0:
# 			if not(self.playerOwned) and self.overlap(player):
# 				player.damage(self.ARROWDAMAGE)
# 				self.xs = 0
# 			else:
# 				for ent in gameinfo.enemies():
# 					if self.overlap(ent):
# 						ent.damage(self.ARROWDAMAGE, gameinfo)
# 						self.xs = 0
# 						break
# 		#self.destroyArrow(gameinfo, player)

# 	def arrowMove(self, gameinfo, playerPos):
# 		if playerPos > self.x: #shoot right
# 			tempx = self.x + self.arrowSpeed
# 			#print("check move right")
# 			if gameinfo.solid((tempx+(self.width-1))/32, (self.y+1)/32) == False and gameinfo.solid((tempx+(self.width-1))/32, (self.y+(self.height-1))/32) == False:
# 				#self.moveX = self.moveX + self.arrowSpeed
# 				self.x = tempx
# 				#print("move right")
# 				#rightDirection(gameinfo, player, moveX, self.y)
# 		else: 
# 			tempx = self.x - self.arrowSpeed 
# 			#print("check move left")
# 			if gameinfo.solid((tempx+1)/32, (self.y+1)/32) == False and gameinfo.solid((tempx+1)/32, (self.y+(self.height-1))/32) == False:
# 			#self.moveX = self.moveX - self.arrowSpeed
# 				self.x = tempx
# 				#print("move left")
# 			#leftDirection(gameinfo, player, moveX, self.y)
			
# 	#def rightDirection(gameinfo, player
# 	def destroyArrow(self, gameinfo=None, player=None):
# 		if self.overlap(player):
# 			#gameinfo.rem(self)
# 			player.damage(self.ARROWDAMAGE)
# 			#self.arrowSpeed = 0
# 			self.xs = 0
			

# class Spikes(Trap):
# 	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
# 		super().__init__(x, y, name, height, width, hp, mat)
# 		self.spikeDmg = 4
# 	def tick(self, gameinfo=None, player=None):
# 		if self.overlap(player) and player.ys > 0:
# 			player.damage(self.spikeDmg)
#####--------NEWTraps------------------------------------



# def makeEnt(name, x, y):
# 		entattri = entschema[name]

# 		mat = pygame.image.load('resources%sentities%s%s' % (os.sep, os.sep, entattri['mat']))
# 		hp = entattri['hp']

# 		height = entattri['height']
# 		width = entattri['width']
# 		#text = ""
# 		newent = entschema[name]

# 		#print("placed at ",self.x, self.y)

# 		#print(x,y,hp,mat,name,text,width,height)

# 		entobj = newent['obj'](x,y,name,height,width,hp,mat)

# 		return entobj

# collectableschema = {"gold":{"val":500},
# 		  			"emerald":{"val":800},
# 		  			"sapphire":{"val":1200},
# 		  			"ruby":{"val":1600},
# 		  			"diamond":{"val":5000},
# 		  			"bombPile":{"val":3},
# 		  			"ropePile":{"val":3}}