## @file main.py
#  @author Niyatha
#  @brief Contains the main program to drive the game
#  @date 04/12/2021

import pygame
#Standard lib
import os
import sys
import time
import random
import math
#Own Files
import readmap
import mover
import camera
import display

pygame.init()
height = 320
width = 320
window = pygame.display.set_mode((height,width),pygame.RESIZABLE)
pygame.display.set_caption('MacLunky!')
screen = pygame.display.get_surface()
screen.convert_alpha()
clock = pygame.time.Clock()

## @brief Main function to create an instance of the playable game
#  @details M5 creates the map objects and places the player on the map whose
#			positions are controlled by the user's key strokes.
def main():
	
	global gameinfo
	gameinfo = readmap.ReadMap('final.map')
	newmover = mover.Mover(x=gameinfo.gamemap.start[0]*32,y=gameinfo.gamemap.start[1]*32, direction=0, speed=0)

	cam = camera.cam(newmover.x, newmover.y, width, height, gameinfo.gamemap.width()*32, gameinfo.gamemap.height()*32)
	
	ui = display.display()
	
	while True:
		pygame.event.pump()

		newmover.loop(gameinfo)

		if newmover.position()[0] // 32 == gameinfo.gamemap.end[0] and \
			newmover.position()[1] // 32 == gameinfo.gamemap.end[1]:
			newmover.leave = 1

		#Gamemap display
		for k in gameinfo.gamemap.map():
			for i in k:						
				screen.blit(i.mat, (i.posx*32-cam.x,i.posy*32-cam.y))

		#Entity display
		for ent in gameinfo.entities():
			screen.blit(ent.mat, (ent.position()[0]-cam.x,ent.position()[1]-cam.y))

		#Entity tick
		for ent in gameinfo.entities():
			ent.tick(gameinfo, newmover)
		
		#Player display
		screen.blit(newmover.image, (newmover.x-cam.x,newmover.y-cam.y))

		#UI elements
		ui.ui(screen, cam, newmover, gameinfo)

		#Camera update
		cam.move(newmover.x, newmover.y, newmover.adjustCamera)

		pygame.display.flip()
		clock.tick(90)

main()
