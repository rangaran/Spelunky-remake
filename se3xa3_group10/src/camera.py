## @file camera.py
#  @author Niyatha
#  @brief Contains the camera restrictions to add objects on the playable screen
#  @date 04/12/2021

## @brief Update the camera showing the game based on player movement
#  @details Implements the secrets of M1. Show only the portion of the map applicable to the player's motion by the user
class cam():

	## @brief Constructor to create the camera type
	#  @param x an integer element indicating the x position of the camera object
	#  @param y an integer element indicating the y position of the camera object
	#  @param height an integer element indicating the height of the camera object
	#  @param mapw an integer element indicating the width of the camera map
	#  @param maph an integer element indicating the height of the camera map
	def __init__(self, x=0, y=0, width=0, height=0, mapw = 0, maph = 0):
		if x - width//2 < 0:
			self.x = 0
		elif x - width//2 + width < mapw:
			self.x = x - width//2
		else:
			self.x = mapw - width

		if y - height//2 < 0:
			self.y = 0
		elif y - height//2 + height < maph:
			self.y = y - height//2
		else:
			self.y = maph - height

		self.width = width
		self.height = height
		self.mapw = mapw
		self.maph = maph
		print ("H: %s | W: %s" %  (self.height, self.width))
		self.adj = 0

	## @brief Move the camera
    #  @details Move the camera to where the player is, lock to the corners of the map
	#  @param x x axis coordinate position of the player wrt to the camera coordinates
	#  @param y y axis coordinate position of the player wrt to the camera coordinates
	#  @param adj int representing how much to move the camera
	def move(self, x, y, adj):
		if adj > 90 and abs(self.adj) < 2*32 and self.y - 1 >= 0:
			self.adj -= 1
			self.y -= 1
		elif adj < -90 and abs(self.adj) < 2*32 and self.y + self.height + 1 <= self.maph:
			self.adj += 1
			self.y += 1
		elif adj == 0:
			self.y -= self.adj
			self.adj = 0
			if y-self.height/2> 0 and y+self.height/2< self.maph:
				self.y = y-self.height/2

		"""Move the camera to where the player is, lock to the corners of the map"""
		if x-self.width/2 > 0 and x+self.width/2 < self.mapw:
			self.x = x-self.width/2
