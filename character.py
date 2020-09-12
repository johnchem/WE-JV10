#*-*coding:utf-8*-*

'''
	class personnage
'''

import pygame

class Character():
	'''

	'''
	def __init__(self, x, y ,height, width, window):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.window = window
		self.health = 10
		self.maxJumps = 10
		self.jumpsDone = 0
		self.hitBox = (0,0,0,0)
		self.tiredNess = 0
		self.onGround = True
		self.color = (77,77,255)

	def draw(self):
		pygame.draw.rect(self.window, self.color, 
						(self.x, self.y, self.width, self.height),0)

	def gravity(self):
		if not onGround:
			self.x -= 10

	def moveUp(self, value):
		self.x += value

	def moveFwd(self, value):
		self.y += value

	def moveBwd(self, value):
		self.y -= value

if __name__ == '__main__':
	pygame.init()
	win = pygame.display.set_mode((1350,700))
	pygame.display.set_caption("test character")
	clock = pygame.time.Clock()
	font = pygame.font.SysFont("Comic Sans Ms", 20)

	char = Character(200,200,100,50,win)

	run = True
	while run:
		clock.tick(500)

		#draw element
		win.fill((255,255,255))
		char.draw()
		
		#update screen
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
