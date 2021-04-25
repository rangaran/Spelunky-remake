## @file mover.py
#  @author Albert, Abeer, Niyatha
#  @brief Contain the specific Mover type 
#  @date 04/11/2021

import pygame
import os
import random
import time
import math
import sys

from enum import Enum

from resources.entities import *
from resources.entities.weapon import Weapon
from resources.entities.enemy import Enemy

## @brief State contains an enumeration for the player sprite in the game and implements the secrets of M3
class State(Enum):
	standing = 0
	walking = 1
	falling = 2
	climbing = 3
	crouching = 4

## @brief Mover is a class that implements the player of the game and implements the secrets of M3 and M8 and M2
#  @details Implements the secrets of M2, M3, M8. The class contains the different player controls and the movement animation of the player on the screen
class Mover():
	## @brief constructor method for class Mover, intializes a Mover from a given player characteristics
    #  @param x is an integer element indicating the x position of the player Mover object
	#  @param y is an integer element indicating the y position of the player Mover object
	#  @param direction is an integer element indicating the direction of movement of the player Mover object
	#  @param speed is an integer element indicating the speed of movement of the player Mover object
	def __init__(self, x=None, y=None, direction=None, speed=None):
		self.state = State.standing
		self.xs = 0
		self.ys = 0
		self.invincibility = 0
		self.INVINCIBILITYTIME = 270
		self.STOMPDAMAGE = 1
		self.jumpDist = 0
		self.GRAVITY = 3
		self.MAXJUMP = 24
		self.bombs = 5
		self.ropes = 5
		self.adjustCamera = 0

		self.x = x
		self.y = y
		
		self.hp = 10
		self.direction = -1
		self.gold = 0
		imageroot = "resources%splayer%s" % (os.sep,os.sep)
		self.media = {'idle':pygame.image.load(imageroot+"guy_idle.png"),
						'heart':pygame.image.load(imageroot+"heart.png"),
						'falling':pygame.image.load(imageroot+'guy_falling.png'),
						'climbing':pygame.image.load(imageroot+"guy_climbing.png"),
						'crouching':pygame.image.load(imageroot+'guy_crouching.png'),
						'bomb':pygame.image.load(imageroot+'bombIcon.png'),
						'rope':pygame.image.load(imageroot+'ropeIcon.png')}
		self.sizes = {'idle':(12, 16),
						'falling':(14, 16),
						'climbing':(14, 15),
						'crouching':(15, 9)}
		self.hand = entities.Entities.makeEnt("emptyHand", self.x, self.y)
		self.image = self.media['idle']
		self.width = self.sizes['idle'][0]
		self.height = self.sizes['idle'][1]

		self.leave = False
	
	## @brief get the position of the player Mover object
    #  @return tuple of integers indicating the x and y position of the player Mover object
	def position(self):
		return (self.x,self.y)

	## @brief decrease the player Mover object health points when it is under attack
	#  @param d is an integer element indicating the damage on the player Mover object health points 
	#  @return nothing if the player is not damaged
	def damage(self, d=0):
		if self.invincibility > 0:
			return 
		self.hp -= d
		self.invincibility = self.INVINCIBILITYTIME 

	## @brief manages the player Mover object change of movement in the game run
	#  @param gameinfo a ReadMap object element indicating the map where the Mover object is on 
	def loop(self, gameinfo=None):
		self.gravity(gameinfo)
		self.controls(gameinfo)
		if self.state == State.climbing:
			self.climb(gameinfo, self.ys)
		else:
			self.move(gameinfo, self.xs, self.ys)
		if self.invincibility > 0:
			self.invincibility -= 1
		if self.adjustCamera > 0:
			self.adjustCamera += 1
		elif self.adjustCamera < 0:
			self.adjustCamera -= 1


	## @brief manages the player Mover object change of y direction movement in the game run
	#  @param gameinfo a ReadMap object element indicating the map where the Mover object is on 
	#  @return nothing if the player state is climb
	def gravity(self, gameinfo=None):
		if self.state == State.climbing:
			return

		if self.ys < 0 and self.jumpDist < self.MAXJUMP:
			self.ys = -self.GRAVITY
			self.jumpDist += 1
		else:
			#print("falling down")
			self.jumpDist = 0
			if self.ys <= 0:
				#print("under gravity")
				self.ys = self.GRAVITY
	
	## @brief manages the player Mover object jump movement in the game run
	#  @param gameinfo a ReadMap object indicating the map where the Mover object is on 
	#  @param maxjump an integer representing the max height of the Mover jump in the y direction
	def jump(self, gameinfo=None, maxjump=None):
		#self.jump = 1
		self.jumpDist = 0
		self.ys = -self.GRAVITY
		if self.state != State.climbing:
			self.ys = -self.GRAVITY
		else:
			self.jumpDist += self.MAXJUMP // 2

			print("yep")
		self.changeState(State.falling, self.direction)

	## @brief manages the player Mover object change of x and y direction movement in the game run
	#  @param gameinfo a ReadMap object indicating the map where the Mover object is on 
	#  @param x an integer indicating the change in the x direction move of the Mover object
	#  @param y an integer indicating the change in the y direction move of the Mover object
	def move(self, gameinfo=None, x=None, y=None):
		if x>0:
			tempx = self.x + x 
			if gameinfo.solid((tempx+(self.width-1))/32, (self.y+1)/32) == False and gameinfo.solid((tempx+(self.width-1))/32, (self.y+(self.height-1))/32) == False:
				self.x = self.x + x
				self.hand.carry(gameinfo, x, 0)
		
		if x<0:
			tempx = self.x + x 
			if gameinfo.solid((tempx+1)/32, (self.y+1)/32) == False and gameinfo.solid((tempx+1)/32, (self.y+(self.height-1))/32) == False:
				self.x = self.x + x
				self.hand.carry(gameinfo, x, 0)	
			
		if y>0:
			tempy = self.y + y 
			if gameinfo.solid((self.x+1)/32, (tempy+(self.height-1))/32) == False and gameinfo.solid((self.x+(self.width-1))/32, (tempy+(self.height-1))/32) == False:
				#Falling
				self.y = tempy
				self.changeState(State.falling, self.direction)
				self.hand.carry(gameinfo, 0, y)	
				if self.ys < 5:
					self.ys += 0.1
				for ent in gameinfo.enemies():
					if ent.overlap(self):
						ent.damage(self.STOMPDAMAGE, gameinfo)
						self.ys = -3
						print("stomped on", ent.name)
						break;
			elif self.state == State.falling: # do gravity for falling only
				#Falling but stopped
				if self.ys >= 5:
					self.hp -= 1
					print ("Ouch! HP currently at %s" % self.hp)
				self.ys = 0
				self.jumpDist = 0
				if x != 0:
					self.changeState(State.walking, self.direction)
				else:
					self.changeState(State.standing, self.direction)
			else:
				self.ys = 0

			
		if y<0:
			#Jumping?
			tempy = self.y + y 
			if gameinfo.solid((self.x+1)/32, (tempy+1)/32) == False and gameinfo.solid((self.x+(self.width-1))/32, (tempy+1)/32) == False:
				self.y = tempy
				self.hand.carry(gameinfo, 0, y)
			else:
				self.jumpDist = 0
				self.ys = 0
	
	## @brief manages the player Mover object change of movement when climbing in the game run
	#  @param gameinfo a ReadMap object indicating the map where the Mover object is on 
	#  @param y an integer indicating the change in the y direction move of the Mover object
	def climb(self, gameinfo=None, y=None):
		tempy = self.y + y 

		# check for solid block below
		if y > 0:
			if gameinfo.solid((self.x+1)/32, (tempy+(self.height-1))/32) == False and gameinfo.solid((self.x+(self.width-1))/32, (tempy+(self.height-1))/32) == False:
				self.y = tempy
			else:
				return

		# check for solid block above
		if y < 0:
			if gameinfo.solid((self.x+1)/32, (tempy+1)/32) == False and gameinfo.solid((self.x+(self.width-1))/32, (tempy+1)/32) == False:
				self.y = tempy
			else:
				return

		# check if still holding a rope
		restricted = True
		for ent in gameinfo.entities():
			if ent.name == "rope" and ent.overlap(self):
				restricted = False
				break;

		if restricted:
			self.y -= y
		else:
			self.hand.carry(gameinfo, 0, y)	

	## @brief manages the player Mover object hand state in the game run
	def emptyHand(self):
		self.hand = entities.Entities.makeEnt("emptyHand", self.x, self.y)

	## @brief manages the player Mover object change of sprite in the game run
	#  @param state a State type input indicating the change in the Mover object sprite
	#  @param dir an integer indicating the change in direction of the Mover object
	def changeState(self, state, dir):
		self.state = state
		oldDir = self.direction
		self.direction = dir

		if self.state == State.standing:
			img = self.media['idle']
			w = self.sizes['idle'][0]
			h = self.sizes['idle'][1]
		elif self.state == State.falling:
			img = self.media['falling']
			w = self.sizes['falling'][0]
			h = self.sizes['falling'][1]
		elif self.state == State.climbing:
			img = self.media['climbing']
			w = self.sizes['climbing'][0]
			h = self.sizes['climbing'][1]
		elif self.state == State.crouching:
			img = self.media['crouching']
			w = self.sizes['crouching'][0]
			h = self.sizes['crouching'][1]
		else:
			img = self.media['idle']
			w = self.sizes['idle'][0]
			h = self.sizes['idle'][1]

		if self.direction == 1:
			img = pygame.transform.flip(img, True, False)
		if self.direction != self.hand.direction:
			self.hand.flip()

		self.y += self.height - h # Adjust y due to change in height
		if self.direction == 1:
			self.x += self.width - w # Adjust y due to change in height

		self.image = img
		self.width = w
		self.height = h

	## @brief manages the player Mover object input controls and updates the game and player state accordingly
	#  @param key a keyboard input press by the player
	#  @param gameinfo a ReadMap object indicating the map where the Mover object is on 
	def controls(self, gameinfo):
		event = pygame.event.poll()

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			key = event.key
		
			if key == pygame.K_F12:
				pygame.display.toggle_fullscreen()

			if key == pygame.K_TAB:
				if self.hand.name == "emptyHand":
					# change for new coordinate
					for ent in gameinfo.entities():
						if ent.overlap(self) and ent.useable():
							ent.use(gameinfo,self)
							break
				else:
					self.hand.use(gameinfo, self)

			if key == pygame.K_LSHIFT:
				if self.state == State.crouching:
					if self.hand.name == "emptyHand":
						for ent in gameinfo.entities():
							if isinstance(ent, Throwable) and ent.overlap(self):
								print("picked up ", ent.name)
								self.hand = ent
								if self.direction == 1:
									x = self.x + (self.width - self.hand.width/2)
								else:
									x = self.x - self.hand.width/2
								y = self.y - self.hand.width/2
								self.hand.set(x, y)
								self.hand.pickup()
								break
					else:
						self.hand.putDown()
						self.emptyHand()
				else:
					if self.hand.name == "emptyHand":
						w = entities.entschema["whip"]["width"]
						if self.direction == 1:
							x = self.x + self.width
						else:
							x = self.x - w
						y = self.y + self.height/2
						whip = entities.Entities.makeEnt("whip", x, y)
						self.hand = whip
						self.hand.swing(gameinfo)
					elif not(isinstance(self.hand, Weapon)):
						self.hand.throw(self.direction * 1, 0)
						self.emptyHand()

			if key == pygame.K_LEFT:
				if self.state != State.climbing and self.state != State.falling: 
					self.changeState(State.walking, self.direction)
				self.changeState(self.state, -1)
				self.xs = -1
				if not(isinstance(self.hand, Weapon)):
					self.hand.set(self.x - self.hand.width/2, self.hand.position()[1])
				else:
					self.hand.set(self.x - self.hand.width, self.hand.position()[1])


			elif key == pygame.K_RIGHT:
				if self.state != State.climbing and self.state != State.falling: 
					self.changeState(State.walking, self.direction)
				self.changeState(self.state, 1)
				self.xs = 1
				if not(isinstance(self.hand, Weapon)):
					self.hand.set(self.x + (self.width - self.hand.width/2), self.hand.position()[1])
				else:
					self.hand.set(self.x + self.width, self.hand.position()[1])

		
			elif key == pygame.K_UP: 
				if self.state == State.standing:
					self.adjustCamera += 1

				for ent in gameinfo.entities():
					if ent.name == "rope" and ent.overlap(self):
						self.xs = 0
						self.ys = -1
						self.changeState(State.climbing, self.direction)
						self.x = ((int)((self.x+1)/32)) * 32 + (32 - self.width) / 2 

			elif key == pygame.K_DOWN:
				if self.state == State.climbing:
					self.ys = 1
				elif self.state == State.standing or self.state == State.walking:
					self.changeState(State.crouching, self.direction)
					self.adjustCamera -= 1

			if key == pygame.K_SPACE:
				if self.state != State.falling:
					self.jump(gameinfo)

			if key == pygame.K_ESCAPE: 
				pygame.quit()
				sys.exit()

			if key == pygame.K_b:
				if self.bombs <= 0:
					return
				self.bombs -= 1

				height = entschema["bomb"]['height']

				x = int(self.x)
				y = int(self.y + self.height - height)
				print ("Bomb placed at ", x, y)

				gameinfo.add(entities.Entities.makeEnt("bomb", x, y))

			if key == pygame.K_v:
				if self.ropes <= 0:
					return
				self.ropes -= 1

				height = entschema["rope"]['height']
				y = self.y
				x = int(self.x)


				if self.state != State.crouching:
					print ("rope placed at ", x, y)
					rope = entities.Entities.makeEnt("rope", x, y)
					rope.throw()
					gameinfo.add(rope)
				else:
					x = x + 32 * self.direction
					# prevent rope in wall
					if gameinfo.solid(x/32, y/32) == True:
						x = x - 32 * self.direction					
					rope = entities.Entities.makeEnt("rope", x, y)
					rope.makeRope(gameinfo)
					gameinfo.add(rope)

		elif event.type == pygame.KEYUP:
			key = event.key
			if key == pygame.K_LEFT: 
				if self.state == State.walking: 
					self.changeState(State.standing, self.direction)
				if self.xs == -1:
					self.xs = 0

			elif key == pygame.K_RIGHT: 
				if self.state == State.walking: 
					self.changeState(State.standing, self.direction)
				if self.xs == 1:
					self.xs = 0

			elif key == pygame.K_UP: 
				if self.state == State.climbing and self.ys == -1:
					self.ys = 0
				self.adjustCamera = 0

			if key == pygame.K_DOWN: 
				self.adjustCamera = 0
				print("stop cam ", self.adjustCamera)

				if self.state == State.climbing and self.ys == 1:
					self.ys = 0
				elif self.state == State.crouching or self.state == State.walking:
					if self.xs != 0:
						self.changeState(State.walking, self.direction)
					else:
						self.changeState(State.standing, self.direction)