#*-*coding:utf-8*-*

import pygame

if name == "__main__":
	pygame.init()
	win = pygame.display.set_mode((1350,700))
	pygame.display.set_caption("10Jumps")
	clock = pygame.time.Clock()
	font = pygame.font.SysFont("Comic Sans Ms", 20)

	from gui import Display
	display = Display(win)
	display.run()