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

	def __init__(self, window):
		self.background = WHITE
		self.window = window
		self.character = None
		self.elements = []
	
	def initElement(self):
		for x, y, w, h in levels.pads:
			self.elements.append(pad(x,y,w,h,self.window))

		for x ,y in levels.hurdles:
			self.elements.append(hurdle(x ,y, 30, 30, (255,0,0), self.window))

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

		self.character = Character(200,200,25,50,win)
		self.initElement()

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

			win.fill(self.background)

			collisionBorder(self.character, win)
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

	display = Display(win)
	display.run()