## @file arrowtrap.py
#  @author Abeer
#  @brief Contain the specific ArrowTrap type represented by an Trap(Entity)
#  @date 04/11/2021

from .trap import Trap

## @brief ArrowTrap is an object of type Trap
#  @details Extends from trap.py and implements the secrets of M4.14
class ArrowTrap(Trap):
	
	## @brief Constructor method for ArrowTrap
	#  @param x an integer element indicating the x position of the arrow trap object
	#  @param y an integer element indicating the y position of the arrow trap object
	#  @param hp an integer element indicating the health points of the arrow trap object 
	#  @param mat an image representing the arrow trap object on the game screen
	#  @param name a string representing the name of the image of the object
	#  @param width an integer element indicating the width of the arrow trap object
	#  @param height an integer element indicating the height of the arrow trap object
	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
		super().__init__(x, y, name, height, width, hp, mat)
		self.arrowSense = 4 
		self.direction = -1
		#self.arrowMade = False
		# height = entschema["arrowL"]["height"]
		# width = entschema["arrowL"]["width"]
		
		# posx = int(self.x - width/2 + self.width/2)
		# posy = int(self.y - height + self.height)
		
		# self.arrow = makeEnt("arrowL", posx, posy)
		
		#time.sleep(2)
		self.arrowMade = True

	def setDirection(self, d):
		self.direction = d
		if self.direction == 1:
			self.flipImage(True, False)
	
	## @brief check if the player is within the sensing range of the arrow trap object
	#  @param gameinfo a ReadMap object element indicating the map where the arrow trap object is on
	#  @param player a Mover object element representing the player of the game that is within range
	#  @return a Boolean value indicating if the player was sensed or not, True is returned if the player is within range of the trap
	def sense(self,gameinfo=None, player=None):
		#check y level
		if self.y < player.y+player.height and player.y < self.y+self.height:
			#print("y-level")#check the x distance
			diff = player.x - self.x
			if diff != 0 and diff//abs(diff) == self.direction and abs(diff) <= 4*32:
				#print("x-level")
				return True
		#if player.y == self.y: #player.y < self.y+self.height or self.y < player.y+player.height:
		#	if player.x-self.x <= 4 or player.x-self.x >= -4:
		# if self.overlap(player):
			#print("trap detected player")
			# return True
		return False
	
	## @brief  animation movement of the arrow trap object attack mechanism to shoot an arrow 
	#  @param gameinfo a ReadMap object element indicating the map where the arrow trap object is on
	#  @param player a Mover object element representing the player of the game that is within range of arrow trap attack 
	#  @return a Boolean value indicating that animation for the frame update is done
	def tick(self, gameinfo=None, player=None):
		if self.arrowMade and self.sense(gameinfo, player):
			from .entities import Entities

			arrow = Entities.makeEnt("arrow", self.x, self.y)
			height = arrow.dimension()[0]
			width = arrow.dimension()[1]

			posx = int(self.x - width/2 + self.width/2)
			#posy = int(self.y - height + self.height)
			posy = int(self.y - height/2 + self.height/2)

			arrow = Entities.makeEnt("arrow", posx, posy)
			if self.direction == 1:
				arrow.flipImage(True, False)
			print("Trap will shoot arrow")
			gameinfo.add(arrow)
			arrow.throw(self.direction, 0)
			self.arrowMade = False
			#print("move")
			#self.arrow.arrowMove(gameinfo, player.x)
		#return True

	# def shoot(self, gameinfo=None, player=None):
		# places an arrow and shoots it
		# if self.arrowMade == False:
		# height = entschema["arrowL"]["height"]
		# width = entschema["arrowL"]["width"]
		
		# posx = int(self.x - width/2 + self.width/2)
		# posy = int(self.y - height + self.height)
		
		# arrow = makeEnt("arrowL", posx, posy)
		# gameinfo.add(arrow)
		# time.sleep(2)
		# self.arrowMade = True
		# arrow.arrowMove(gameinfo, player)