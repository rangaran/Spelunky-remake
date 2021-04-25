## @file weapon.py
#  @author Albert
#  @brief Contain the specific Weapon type
#  @date 04/11/2021

from .entity import Entity

## @brief Weapon is an object of type Entity
#  @details Extends from entity.py and implements the secrets of M4.25
class Weapon(Entity):
	## @brief Constructor method for Weapon
    #  @details Create the weapon using super(). Set time and speed to 0.
	#  @param x int representing the x position of the weapon
	#  @param y int representing the y position of the weapon
	#  @param hp int representing the health points of the weapon 
	#  @param mat image representing the weapon on the game screen
	#  @param name string representing the name of the image of the object
	#  @param width int representing the width of the weapon
	#  @param height int representing the height of the weapon
	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
		super().__init__(x, y, name, height, width, hp, mat)
		self.damage = 0
		self.speed = 0
		self.activeFrames = 0
		self.time = 0
		self.active = 0
		self.direction = 1

	## @brief Swing the weapon
    #  @details If there is no time remaining, set time to SPEED, active to ACTIVEFRAMES, and add the
    #           weapon to the game.
	#  @param gameinfo ReadMap object representing the level environment
	def swing(self, gameinfo=None):
		if self.time > 0:
			return

		print("weapon swing")

		self.time = self.speed
		self.active = self.activeFrames
		gameinfo.add(self)

	## @brief Update the weapon with 1 unit of time
    #  @details If there is time remaining, reduce it. If the weapon is active, damage any overlapping
    #           entities. Else, remove it from the player's hand.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def tick(self, gameinfo=None, player=None):
		if self.time > 0:
			self.time -= 1

		#print("weapon tick")
	
		if self.active > 0:
			for ent in gameinfo.enemies():
				if ent.overlap(self):
					ent.damage(self.damage, gameinfo)
			self.active -= 1
		else:
			gameinfo.rem(self)
			player.emptyHand()
			#print("whip gone")

	## @brief Carry the weapon
    #  @details Carry the weapon while ignoring solid blocks.
	#  @param gameinfo ReadMap object representing the level environment
	#  @param player Mover object representing the player
	def carry(self, gameinfo=None, x=None, y=None):
		super().move(x, y)

	## @brief Reverse image and direction
	def flip(self):
		super().flipImage(True, False)
		self.direction = -self.direction