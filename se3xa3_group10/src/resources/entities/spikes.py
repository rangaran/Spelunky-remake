## @file spike.py
#  @author Abeer
#  @brief Contain the specific Spike type represented by an Trap(Entity)
#  @date 04/11/2021

from .trap import Trap

## @brief Spike is an object of type Trap
#  @details extends from trap.py and implements the secrets of M4.16
class Spikes(Trap):
	
	## @brief Constructor method for Spike
	#  @param x an integer element indicating the x position of the Spike trap object
	#  @param y an integer element indicating the y position of the Spike trap object
	#  @param hp an integer element indicating the health points of the spike trap object 
	#  @param mat an image representing the spike trap object on the game screen
	#  @param name a string representing the name of the image of the object
	#  @param width an integer element indicating the width of the spike object
	#  @param height an integer element indicating the height of the spike object
	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
		super().__init__(x, y, name, height, width, hp, mat)
		self.spikeDmg = 4
	
	## @brief Inflicts the spike trap damage on the player's health 
	#  @param gameinfo a ReadMap object element indicating the map where the spike object is on
	#  @param player a Mover object element representing the player of the game that is on the spike object
	def tick(self, gameinfo=None, player=None):
		if self.overlap(player) and player.ys > 0:
			player.damage(self.spikeDmg)