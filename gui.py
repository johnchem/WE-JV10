#*-*coding:utf-8*-*

'''
	creation and handling of the gui for the game

'''

import pygame
import sys
import os
import random
from pygame.locals import *
from element import *
from character import *
from assets import *
import levels

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHTRED = (255,77,77)
LIGHTGREEN = (77,255,77)
LIGHTBLUE = (77,77,255)

	
class Display():
	''' 
		initialize of the display
		initialize all the elements
		handle the user events and refresh the screen
	'''

	def __init__(self, window, spriteFileName):
		self.background = WHITE
		self.window = window
		self.character = None
		self.elements = []
		self.hud = []

		#graphical element
		self.spriteSheet = None
		self.char_images = []
		self.pad_images = []
		self.hurdles_images = []
		self._initImage(spriteFileName)

	def _initImage(self, spriteFileName):
		char = {}
		pad = {"left_side":((41,64),(1,1)),
			"middle_side":((42,64),(1,1)),
			"right_side":((44,64),(1,1))}
		hurdles = {}

		self.spriteSheet = SpriteSheet(spriteFileName)
		for key, value in pad.items():
			self.pad_images.append(self.spriteSheet.get_image(value[0], value[1]))
	
	def _initCharacter(self,x,y,width,height):
		self.character = Character(x,y,width,height,self.window)

	def _initElement(self):
		for x, y, w, h in levels.pads:
			self.elements.append(pad(x,y,w,h,
								 self.pad_images[2],
								 self.pad_images[0],
								 self.pad_images[1], 
								 self.window))

		for x ,y in levels.hurdles:
			self.elements.append(hurdle(x ,y, 30, 30, (255,0,0), None, self.window))

	def _initHud(self):
		faceDisplay = pygame.rect()
		gaugeTiredNess = pygame.rect()
		gaugeBravery = pygame.rect()
		textJump = pygame.rect()
		textScore = pygame.rect()
		testTimer = pygame.rect()

	def _refresh(self):
		''' refresh the screen by drawing all the items'''
		#self.window.fill(self.background)
		#draw element
		for x in self.elements:
			x.draw()
		
		self.character.draw()
		pygame.display.update()


	def run(self):
		''' main loop who handle user event'''
		clock = pygame.time.Clock()
		font = pygame.font.SysFont("Comic Sans Ms", 20)

		self._initCharacter(200,200,16,36)
		self._initElement()

		run = True
		nbCycle = 0
		while run:
			clock.tick(60)

			key = pygame.key.get_pressed()
			keyPressed = False
			nbCycle += 1

			if key[pygame.K_UP]:
				if nbCycle > 5: #debounce the jump key
					self.character.move(jump=-(self.character.height/10), timer=nbCycle)
					keyPressed = True
					nbCycle=0 

			if key[pygame.K_RIGHT]:
				self.character.move(right=10)
				keyPressed = True

			if key[pygame.K_LEFT]:
				self.character.move(left=-10)
				keyPressed = True

			if not keyPressed:
				self.character.move()

			self.window.fill(self.background)

			collisionBorder(self.character, self.window)
			collisionDetection(self.character, self.elements)
			#proximityDetection(self.character, [spike])
			
			self._refresh()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					pygame.quit()


if __name__ == "__main__":
	pygame.init()
	win = pygame.display.set_mode((1350,700))
	pygame.display.set_caption("test display")
	clock = pygame.time.Clock()
	font = pygame.font.SysFont("Comic Sans Ms", 20)
	filename = 'game_assets/monsterboy_assets.png'

	display = Display(win, filename)
	display.run()