## @file sign.py
#  @author Albert
#  @brief Contain the specific Sign type
#  @date 04/11/2021

from .entity import Entity

## @brief Sign is an object of type Entity
#  @details Extends from entity.py and implements the secrets of M4.11
class Sign(Entity):
	## @brief Constructor method for Sign
    #  @details Create the sign using super(). Set the text.
	#  @param x int representing the x position of the sign
	#  @param y int representing the y position of the sign
	#  @param hp int representing the health points of the sign 
	#  @param mat image representing the sign on the game screen
	#  @param name string representing the name of the image of the object
	#  @param width int representing the width of the sign
	#  @param height int representing the height of the sign
	def __init__(self, x=None, y=None, name=None, height=None, width=None, hp=None, mat=None):
		super().__init__(x, y, name, height, width, hp, mat)
		self.text= ""

	## @brief Set the test
	#  @param s string representing the text
	def setText(self, s):
		self.text = s

	## @brief Get the text
	#  @return string representing the text
	def getText(self):
		return self.text