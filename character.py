#*-*coding:utf-8*-*

'''
	class personnage
'''

import pygame

class Character():
	'''

	'''
	def __init__(self, x, y ,height, width, window):
		self.x, self.y = x, y
		self.oldX, self.oldY  = x, y
		self.height, self.width = height, width
		self.window = window
		self.health = 10
		self.maxJumps = 10
		self.jumpsDone = 0
		self.hitBox = {"top":0, "bottom":0, "left":0,"right":0}
		self.tiredNess = 0
		self.onGround = True
		self.color = (77,77,255)

	def draw(self):
		self.gravity()
		pygame.draw.rect(self.window, self.color, 
						(self.x, self.y, self.width, self.height),0)

	def touchGround(self):
		self.onGround = True

	def gravity(self):
		self.oldPos()
		self.updateHitbox()
		if not self.onGround:
			self.y += 5

	def moveJump(self, value):
		'''
			excecute a jump and setting the character off ground
		'''
		self.oldPos()
		if self.onGround:
			self.jumpsDone += 1
			self.onGround = False
			self.y -= value
			self.updateHitbox()

	def moveFwd(self, value):
		self.oldPos()
		self.x += value
		self.updateHitbox()

	def moveBwd(self, value):
		self.oldPos()
		self.x -= value
		self.updateHitbox()

	def oldPos(self, restore = False):
		print(" ".join([str(value) for value in self.hitBox.values()]))
		if restore:
			self.x, self.y = self.oldX, self.oldY
			self.updateHitbox()
		self.oldX, self.oldY = self.x, self.y

	def updateHitbox(self):
		self.hitBox["top"] = self.y
		self.hitBox["bottom"] = self.y + self.height
		self.hitBox["right"] = self.x + self.width
		self.hitBox["left"] = self.x


if __name__ == '__main__':
	pygame.init()
	win = pygame.display.set_mode((1350,700))
	pygame.display.set_caption("test character")
	clock = pygame.time.Clock()
	font = pygame.font.SysFont("Comic Sans Ms", 20)

	char = Character(200,200,100,50,win)

	run = True
	while run:
		clock.tick(40)

		key = pygame.key.get_pressed()
		if key[pygame.K_UP]:
			char.moveJump(50)
		elif key[pygame.K_RIGHT]:
			char.moveFwd(10)
		elif key[pygame.K_LEFT]:
			char.moveBwd(10)

		if (char.hitBox["right"] < 10 or char.hitBox["left"] > 1350 or
			char.hitBox["top"] < 10):
			char.oldPos(restore = True)
		elif char.hitBox["bottom"] > 700:
			char.touchGround()
			char.oldPos(restore = True)
			

		#draw element
		win.fill((255,255,255))
		char.draw()
		
		#update screen
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
