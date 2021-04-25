## @file display.py
#  @author Albert, Abeer, Niyatha
#  @brief Contain the specific display format content 
#  @date 03/29/2021

import pygame
import os
import random
import time
import font
import sys

## @brief Display is a class that implements the game user interface screen placements and changes and implements the secrets of M1
#  @details Implements the secrets of M1. The class contains screen changes information and the displayed content of the game
class display():
	## @brief constructor method for class display, intializes text font for game screen information to be displayed
	def __init__(self):
		self.textfont = pygame.image.load('resources%s%s' % (os.sep, 'font-12x16.png'))
		self.c = 1
	
	## @brief method for updating the game display on the screen
    #  @param screen is a pygame display surface representing the game screen 
	#  @param camera is a camera object indicating the player screen view
	#  @param player is a Mover element indicating the player playing the game and interacting with the screen
	#  @param gameinfo a ReadMap object element indicating the map where the Mover object is on 
	def ui(self, screen=None, camera=None, player=None, gameinfo=None):
		self.sign(screen,camera,gameinfo,player)
		#self.showent(screen,camera,gameinfo)
		self.resourceDisp(screen,player)
		self.goldDisp(screen,player)
		self.gameover(screen,player)
		#self.location(screen, player)

	## @brief method for updating the game display for showing entities objects on the scren
    #  @param screen is a pygame display surface representing the game screen 
	#  @param cam is a camera object indicating the player screen view
	#  @param gameinfo a ReadMap object element indicating the map where the Mover object is on 
	def showent(self, screen=None,cam=None,gameinfo=None):
		for ent in gameinfo.entities():
			fontsize = font.size(ent.name)
			offcount = (32-ent.width,32-ent.height-8)
			#offcount = (32-ent.width,32-ent.height)

			position = (ent.position()[0]-fontsize[0]/2+fontsize[0]-cam.x,
			ent.position()[1]+fontsize[1]/2-fontsize[1]-cam.y)

			result = pygame.Surface((fontsize[0]+4, fontsize[1]+4), pygame.SRCALPHA)
			result.fill((90,90,90,40))
			result.blit(font.render(self.textfont,ent.name,(90,90,180,255)),
			(2,2))
			screen.blit(result,position)

	## @brief method for updating the game display for showing the sign text information as a player passes the entity on the screen
    #  @param screen is a pygame display surface representing the game screen 
	#  @param cam is a camera object indicating the player screen view
	#  @param player is a Mover element indicating the player playing the game and interacting with the screen
	#  @param gameinfo a ReadMap object element indicating the map where the Mover object is on 
	def sign(self,screen=None,cam=None,gameinfo=None,player=None):
		for ent in gameinfo.entities():
			if ent.overlap(player) and ent.name == 'sign':
				fontsize = font.size(ent.text)

				result = pygame.Surface((fontsize[0]+4, fontsize[1]+4), pygame.SRCALPHA)
				result.fill((90,90,90,200))
				result.blit(font.render(self.textfont,ent.getText(),(140,140,180,255)),
				(2,2))
				w = 150-fontsize[0]/2
				screen.blit(result,(w,250))
	
	## @brief method for updating the game display for showing the player state information on the screen
	#  @details updates the information displayed about the player health and resources to be used to aid the player in the game
    #  @param screen is a pygame display surface representing the game screen 
	#  @param player is a Mover element indicating the player playing the game and interacting with the screen
	def resourceDisp(self, screen=None, player=None):
		count = 0
		jiggle = 12
		# for i in range(0,player.hp):
		# 	#if player.hp < 6: jiggle = random.randint(12,13)
		# 	screen.blit(player.media['heart'],(count+14,jiggle))
		# 	count += 12
		screen.blit(player.media['heart'],(count+14,jiggle))
		count += 14
		text = "%s" % player.hp
		fontsize = font.size(text)
		result = pygame.Surface((fontsize[0], fontsize[1]), pygame.SRCALPHA)
		result.blit(font.render(self.textfont,text,(255,194,0,255)),
		(2,2))
		screen.blit(result,(count+14,8))
		count += 12

		screen.blit(player.media['bomb'],(count+28,12))
		count += 28

		text = "%s" % player.bombs
		fontsize = font.size(text)
		result = pygame.Surface((fontsize[0], fontsize[1]), pygame.SRCALPHA)
		result.blit(font.render(self.textfont,text,(255,194,0,255)),
		(2,2))
		screen.blit(result,(count+14,8))
		count += 14


		screen.blit(player.media['rope'],(count+28,12))
		count += 28
		text = "%s" % player.ropes
		fontsize = font.size(text)
		result = pygame.Surface((fontsize[0], fontsize[1]), pygame.SRCALPHA)
		result.blit(font.render(self.textfont,text,(255,194,0,255)),
		(2,2))
		screen.blit(result,(count+14,8))

	## @brief method for updating the game display for showing the gold to be collected on the screen
    #  @param screen is a pygame display surface representing the game screen 
	#  @param player is a Mover element indicating the player playing the game and interacting with the screen
	def goldDisp(self, screen=None, player=None):
		text = "$%s" % player.gold
		fontsize = font.size(text)

		result = pygame.Surface((fontsize[0]+4, fontsize[1]+4), pygame.SRCALPHA)

		result.fill((90,90,90,150))
		result.blit(font.render(self.textfont,text,(255,194,0,255)),
		(2,2))

		screen.blit(result,(12,32))

	## @brief method for updating the game screen when the win condition is met or the lose condition is met or exit condition met
    #  @param screen is a pygame display surface representing the game screen 
	#  @param player is a Mover element indicating the player playing the game and interacting with the screen
	def gameover(self,screen=None,player=None):
		if player.hp <= 0:
			self.addScore(screen, player)
			screen.fill((0,0,0))
			text = "You have died"
			x=260-font.size(text)[0]
			screen.blit(font.render(self.textfont, text, (255,255,255)),(x,300))
			del player
			pygame.display.flip()
			time.sleep(3)
			pygame.quit()
			sys.exit()
		elif player.leave == True:
			self.addScore(screen, player)
			end = pygame.image.load("MacLunkyLogo.jpg")
			end = pygame.transform.scale(end,(320,320))
			screen.blit(end, (0,0))

			# pygame.font.init()
			# myfont = pygame.font.SysFont('Comic Sans MS', 30)
			# messageS = myfont.render('YOU SURVIVED!', False, (255,255,255))

			text = "YOU SURVIVED!"
			fontsize = font.size(text)

			result = pygame.Surface((fontsize[0]+4, fontsize[1]+4), pygame.SRCALPHA)

			result.fill((90,90,90,150))
			result.blit(font.render(self.textfont,text,(255,194,0,255)),
			(2,2))

			screen.blit(result,(160 - fontsize[0] // 2,160))


			#screen.blit(end, (0,0))
			#screen.blit(messageS, (27,150))
			pygame.display.flip()
			time.sleep(3)
			pygame.quit()
			sys.exit()
			
	## @brief method for saving the player is score in a highscore file that can be accessed by the player outside the game
    #  @param screen is a pygame display surface representing the game screen 
	#  @param player is a Mover element indicating the player playing the game and interacting with the screen
	def addScore(self,screen=None,player=None):
		scoreFile = open("userHighscore.txt","w+")
		highscore = scoreFile.read()
		if highscore == '':
			highscoreL = 0
		elif highscore != '':
			highscoreL = int((highscore))
		if player.gold > highscoreL:
			scoreFile.write(str(player.gold))
		scoreFile.close()

	def location(self, screen=None, player=None):
		text = "%s" % (int)(player.x // 32)
		textb = "%s" % (int)(player.y // 32)
		text = text + " " + textb
		fontsize = font.size(text)
		result = pygame.Surface((fontsize[0], fontsize[1]), pygame.SRCALPHA)
		result.blit(font.render(self.textfont,text,(255,194,0,255)),
		(2,2))
		screen.blit(result,(10,60))