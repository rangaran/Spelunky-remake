## @file readmap.py
#  @author Albert
#  @brief M6 Contains level creation
#  @date 04/12/2021

#!/usr/bin/env python
from resources.blocks.blocks import *
from resources.blocks.bits import *
from resources.entities import *
import pygame
from pygame.locals import *
import os
import random

from resources.entities.enemy import Enemy

## @brief Details of map blocks
class MapCell():
	def __init__(self, posx=None, posy=None, mat=None, trans=None, soli=None, bittype=None, name=None):
		self.mat = mat
		self.posx = posx
		self.posy = posy
		self.trans = trans
		self.soli = soli
		self.bittype = bittype
		self.name = name

## @brief Map of all blocks
#  @details Implements the secrets of M5
class MapObj():
	## @brief Create the map
	#  @details Create the block map from the map data
	#  @param add File containing map data
	def __init__(self, add):
		base = []
		splitmap = add.split('\n')
		splitmap = self.filter(splitmap)
		for y in range(0,len(splitmap)):
			newbit = []
			splitmap[y] = splitmap[y].replace("\t", "")
			for x in range(0,len(splitmap[y])):
				attri = blocks[splitmap[y][x]]
				mat = pygame.image.load('resources%sblocks%s%s'% (os.sep, os.sep, attri['mat']))
				soli = attri['soli']
				trans = attri['trans']
				bittype = attri['bits']
				if splitmap[y][x] == "&":
					self.start = (x,y)
				elif splitmap[y][x] == "N":
					self.end = (x,y)
				newbit.append(MapCell(x,y,mat,trans,soli,bittype,splitmap[y][x]))
			base.append(newbit)
		self.mapinfo = base

		for row in self.mapinfo:
			for item in row:
				bitpass = bits.Bitloader()
				bitdict = bitpass.images
				bitpass.setoverlay(item, self, bitdict, item.bittype)

	## @brief Filter the map
	#  @details Remove white space from the map data
	#  @param splitmap File containing map data
	#  @return File containing filtered map data
	def filter(self, splitmap):
		f = []
		for y in range(0,len(splitmap)):
			if splitmap[y] == "":
				continue
			elif splitmap[y] != "E":
				f.append(splitmap[y].replace("\t", ""))
			elif splitmap[y] == "E":
				break
		return f

	## @brief Change a block
	#  @param x int representing block x coordinate
	#  @param y int representing block y coordinate
	#  @param type string representing block type
	def changeBlock(self, x, y, type):
		if x < 0 or x >= self.width() or y < 0 or y >= self.height():
			return
		elif self.mapinfo[y][x].name == "&" or self.mapinfo[y][x].name == "N":
			return

		attri = blocks[type]
		mat = pygame.image.load('resources%sblocks%s%s'% (os.sep, os.sep, attri['mat']))
		soli = attri['soli']
		trans = attri['trans']
		bittype = attri['bits']

		self.mapinfo[y][x] = MapCell(x,y,mat,trans,soli,bittype,type)

	## @brief Get a block
	#  @param x int representing block x coordinate
	#  @param y int representing block y coordinate
	#  @param MapCell object representing the block
	def tile(self, x, y):
		if x < 0 or x >= self.width() or y < 0 or y >= self.height():
			return MapCell(soli=True)
		else:
			return self.mapinfo[int(y)][int(x)]

	## @brief Get block map
	#  @return 2D array of blocks representing block map
	def map(self):
		return self.mapinfo

	## @brief Get block map height
	#  @return int representing block map height
	def height(self):
		return len(self.mapinfo)

	## @brief Get block map width
	#  @return int representing block map width
	def width(self):
		return len(self.mapinfo[0])

## @brief Map of all entities
#  @details Implements the secrets of M5
class EntMap():
	## @brief Create the entities
	#  @details Create the entities from the map data
	#  @param text File containing map data
	def __init__(self, text=None):
		rawentlist = text.split('\n')
		self.entlist = []
		self.enemylist = []

		del rawentlist[-1]

		for ent in rawentlist:
			entinfo = ent.split(' ')
			entattri = entities.entschema[entinfo[0]]

			mat = pygame.image.load('resources%sentities%simages%s%s' % (os.sep, os.sep, os.sep, entattri['mat']))
			hp = entattri['hp']
			height = entattri['height']
			width = entattri['width']
			x = int(entinfo[1])*32 + (32 - width)/2
			y = int(entinfo[2])*32 + 32 - height
			if len(entinfo) > 3:
				text = entinfo[3].replace(';',' ')
				print (text, x, y)
				text = text.replace('^',"\n")
			else:
				text = ''
			ent = entities.Entities.makeEnt(entinfo[0], x, y)
			if isinstance(ent, Sign):
				ent.setText(text)
			elif isinstance(ent, ArrowTrap):
				ent.setDirection(int(text))

			self.entlist.append(ent)
			if isinstance(ent, Enemy):
				self.enemylist.append(ent)

	## @brief Get number of entities
	#  @return int representing the number of entities
	def count(self):
		return len(self.entlist)

	## @brief Add an entity
	#  @param entry Entity object representing the entity to add
	def add(self, entry=None):
		self.entlist.append(entry)

	## @brief Remove an entity
	#  @param entry Entity object representing the entity to remove	
	def rem(self, entry=None):
		self.entlist.remove(entry)

## @brief Map of all blocks and entities
#  @details Implements the secrets of M5
class ReadMap():
	## @brief Create the map
	#  @details Create the block map and entities from the map data
	#  @param file File containing map data
	def __init__(self, file=None):
		f = open(file,'r')
		mapfile = f.read()
		f.close()
		
		self.gamemap = MapObj(mapfile.split('MAP\n')[1])
		self.entlist = EntMap(mapfile.split('ENT\n')[1].split('MAP\n')[0])

	## @brief Get the entities
	#  @return Array of Entity objects representing the entities
	def entities(self):
		return self.entlist.entlist

	## @brief Get the enemies
	#  @return Array of Enemy objects representing the enemies
	def enemies(self):
		return self.entlist.enemylist

	## @brief Add an entity
	#  @param ent Entity object representing the entity to add
	def add(self, ent):
		self.entlist.entlist.append(ent)
		if isinstance(ent, Enemy):
			self.entlist.enemylist.append(ent)

	## @brief Remove an entity
	#  @param ent Entity object representing the entity to remove
	def rem(self, ent):
		self.entlist.entlist.remove(ent)
		if isinstance(ent, Enemy):
			self.entlist.enemylist.remove(ent)

	## @brief Determine if a block is solid
	#  @param x int representing block x coordinate
	#  @param y int representing block y coordinate
	#  @return Whether or not the block is solid
	def solid(self, x, y):
		return self.gamemap.tile(x, y).soli

	## @brief Destroy a block
	#  @param x int representing block x coordinate
	#  @param y int representing block y coordinate
	def destroyBlock(self, x, y):
		self.gamemap.changeBlock(x, y, "0")

