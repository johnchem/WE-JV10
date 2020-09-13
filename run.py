#*-*coding:utf-8*-*

import pygame

if __name__ == "__main__":
	pygame.init()
	win = pygame.display.set_mode((1350,700))
	pygame.display.set_caption("10Jumps")
	filename = 'game_assets/monsterboy_assets.png'
	#clock = pygame.time.Clock()
	#font = pygame.font.SysFont("Comic Sans Ms", 20)

	from gui import Display
	display = Display(win, filename)
	display.run()