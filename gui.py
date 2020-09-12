#*-*coding:utf-8*-*

'''
	creation and handling of the gui for the game

'''

import pygame
import sys
import os
import random
from pygame.locals import *

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
		self.Character = None
		self.elements = []
		
	def drawChar(self, color, x, y, width, height):
		Char = pygame.draw.rect(win, color, 
								(x,y,width,height),0)
		
	def _refresh(self):
		''' refresh the screen by drawing all the items'''
		self.window.fill(self.background)
		self.drawChar(LIGHTBLUE, 200, 200, 200, 200)
		#for key, obj in self.displayHud.item()
		#	obj.draw(self.window):
		pygame.display.update()

	def run(self):
		''' main loop who handle user event'''
		run = True
		clock = pygame.time.Clock()
		while run:
			clock.tick(500)
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