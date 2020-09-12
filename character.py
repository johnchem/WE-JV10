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
		self.dx, self.dy = 0, 0
		self.jumpHeight = 0
		self.currentJump = 0
		self.height, self.width = height, width
		self.window = window
		self.rect = pygame.Rect(x, y, width, height)
		self.gravity = 2
		self.health = 10
		self.maxJumps = 10
		self.jumpsDone = 0
		self.tiredNess = 0
		self.onGround = True
		self.color = (77,77,255)

	def draw(self):
		pygame.draw.rect(self.window, self.color, self.rect,0)

	def touchGround(self):
		self.onGround = True

	def move(self, **kwargs):
		up = kwargs.get('jump', 0)
		right = kwargs.get('right', 0)
		left = kwargs.get('left', 0)

		#reset the position delta 
		self.dx, self.dy = 0, 0

		#set the position delta
		if self.onGround: 
			if up != 0:
				self.jumpsDone += 1
				self.onGround = False
				self.jumpHeight = up
				self.currentJump = up
		else:
			if self.currentJump < 0: #speed to the top
				self.dy = -self.currentJump**2 + self.gravity
				self.currentJump -= self.jumpHeight*0.10
			else: #speed to the bottom
				self.dy = self.currentJump**2 + self.gravity
				self.currentJump -= self.jumpHeight*0.10
		self.dx = right + left

		#update the rect position
		self.rect.x += self.dx
		self.rect.y += self.dy


def collisionDetection(char, listObj):
	for obj in listObj:
		if char.rect.colliderect(obj.rect):
			if char.dx > 0: # Moving right; Hit the left side of the obj
				char.rect.right = obj.rect.left
			if char.dx < 0: # Moving left; Hit the right side of the obj
				char.rect.left = obj.rect.right
			if char.dy > 0: # Moving down; Hit the top side of the obj
				char.rect.bottom = obj.rect.top
			if char.dy < 0: # Moving up; Hit the bottom side of the obj
				char.touchGround()
				char.rect.top = obj.rect.bottom

def collisionBorder(char, border):
	rectBorder = border.get_rect()
	#print(f"{rectBorder.x} {rectBorder.y} {char.rect.x} {char.rect.y}")
	print(f"{char.rect.left} {char.rect.right} {char.rect.top} {char.rect.bottom}")
	if not rectBorder.contains(char.rect):
			if char.dx > 0: # Moving right; Hit the left side
				char.rect.right = rectBorder.left
			if char.dx < 0: # Moving left; Hit the right side
				char.rect.left = rectBorder.right
			if char.dy > 0: # Moving down; Hit the top side
				char.touchGround()
				char.rect.bottom = rectBorder.bottom
			if char.dy < 0: # Moving up; Hit the bottom side
				char.rect.top = rectBorder.top

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
		keyPressed = False

		if key[pygame.K_UP]:
			char.move(jump=-5)
			keyPressed = True

		if key[pygame.K_RIGHT]:
			char.move(right=10)
			keyPressed = True

		if key[pygame.K_LEFT]:
			char.move(left=-10)
			keyPressed = True

		if not keyPressed:
			char.move()

		collisionBorder(char, win)

		#draw element
		win.fill((255,255,255))
		char.draw()
		
		#update screen
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
