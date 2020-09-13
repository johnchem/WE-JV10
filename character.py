#*-*coding:utf-8*-*

'''
	class personnage
'''

import pygame
import math
from element import *


class Character():
	'''

	'''
	def __init__(self, x, y , width, height, window):
		#position variable
		self.x, self.y = x, y
		self.dx, self.dy = 0, 0
		self.height, self.width = height, width
		#pygame variable
		self.window = window
		self.rect = pygame.Rect(x, y, width, height)
		#gameplay variable
		self.gravity = 2
		self.bravery = 10
		self.freeze = True
		self.freezeTime = 0
		self.tiredNess = 0
		self.jumps = 10
		#internal variable
		self.jumpHeight = 0
		self.currentJump = 0
		self.onGround = True
		self.color = (77,77,255)
		
	def draw(self):
		pygame.draw.rect(self.window, self.color, self.rect,0)
		pygame.draw.line(self.window, (0,0,0), (self.rect.left, self.rect.top), 
						(self.rect.right, self.rect.top), 2)

	def touchGround(self):
		self.onGround = True

	def move(self, **kwargs):
		up = kwargs.get('jump', 0)
		right = kwargs.get('right', 0)
		left = kwargs.get('left', 0)
		timer = kwargs.get('timer', None)

		#reset the position delta 
		self.dx, self.dy = 0, 0

		if self.freeze:
			if self.freezeTime > 1:
				self.freezeTime -= 1
			else:
				self.freeze = False
				self.color = (77,77,255)

		#set the position delta
		if self.onGround: 
			if up != 0 and self.jumps>0:
				self.jumps -= 1
				self.onGround = False
				self.jumpHeight = self.tired(up, timer)
				self.currentJump = self.jumpHeight
				if self.jumps == 0: print("no more jumps")
		else:
			if self.currentJump < 0: #speed to the top
				self.dy = -(self.currentJump)**2 + self.gravity
				self.currentJump -= self.jumpHeight*0.10
			else: #speed to the bottom
				self.dy = (self.currentJump)**2 + self.gravity
				self.currentJump -= self.jumpHeight*0.10
		self.dx = right + left

		#update the rect position
		self.rect.x += self.dx
		self.rect.y += int(self.dy)

	def tired(self, jumpHeight, timer):
		if timer != None:
			print(timer)
			if timer < 180: 
				factor= timer/180
			else: 
				factor=1 
			jumpHeight*=factor
		return jumpHeight

	def fear(self, distance):
		if distance < self.width:
			if not self.freeze:
				self.freeze = True
				self.color = (25, 25, 255)
				self.freezeTime = 59*(11-self.bravery)+10


def collisionDetection(char, listObj):
	for obj in listObj:
		if char.rect.colliderect(obj.rect):
			print(f" {char.rect.x}, {char.rect.y}")
			#hit from the object point of view
			hitLeft = char.rect.right > obj.rect.left # Moving right
			hitRight = char.rect.left < obj.rect.right # Moving left
			hitTop = char.rect.bottom > obj.rect.top # Moving down
			hitBottom = char.rect.top < obj.rect.bottom # Moving up

			print(f"{hitLeft} {hitRight} {hitTop} {hitBottom}")
			#from the object point of view
			if hitRight and (hitTop or hitBottom): # hit by the right side
				print("hit left")
				char.rect.right = obj.rect.left

			if hitLeft and (hitTop or hitBottom): # hit by the left side
				print("hit right")
				char.rect.left = obj.rect.right

			if hitTop and (hitRight, hitLeft): # land on the top side
				print("hit top")
				char.touchGround()
				char.rect.bottom = obj.rect.top

			if hitBottom and (hitRight or hitLeft): # Moving up; Hit the bottom side
				print("hit bottom")
				char.rect.top = obj.rect.bottom

			print(f" {char.rect.x}, {char.rect.y}")


def collisionBorder(char, border):
	rectBorder = border.get_rect()
	if not rectBorder.contains(char.rect):
			if char.rect.right > rectBorder.right: # Moving right; Hit the left side
				char.rect.right = rectBorder.right
			
			if char.rect.left < rectBorder.left: # Moving left; Hit the right side
				char.rect.left = rectBorder.left
			
			if char.rect.bottom > rectBorder.bottom: # Moving down; Hit the top side
				char.touchGround()
				char.rect.bottom = rectBorder.bottom
			
			if char.rect.top < rectBorder.top: # Moving up; Hit the bottom side
				char.rect.top = rectBorder.top

def proximityDetection(char, listHurdles):
	if char.onGround:
		for hurdle in listHurdles:
			distance = math.sqrt((char.rect.centerx - hurdle.rect.centerx)**2 + 
								(char.rect.centery - hurdle.rect.centery)**2)
			pygame.draw.line(win, (255,0,0), (char.rect.centerx, char.rect.centery) 
							,(hurdle.rect.centerx, hurdle.rect.centery),2)
			char.fear(distance)


if __name__ == '__main__':
	pygame.init()
	win = pygame.display.set_mode((1350,700))
	pygame.display.set_caption("test character")
	clock = pygame.time.Clock()
	font = pygame.font.SysFont("Comic Sans Ms", 20)

	char = Character(200,200,25,50,win)
	bloc = pad(100, 300, 300, 30, win)
	spike = hurdle(370, 270, 30, 30, (255,0,0), win)
	ListDisplay = [spike, bloc, char]

	run = True
	nbCycle = 0
	while run:
		clock.tick(60)

		key = pygame.key.get_pressed()
		keyPressed = False
		nbCycle += 1

		if key[pygame.K_UP]:
			if nbCycle > 5: #debounce the jump key
				char.move(jump=-(char.height/10), timer=nbCycle)
				keyPressed = True
				nbCycle=0 

		if key[pygame.K_RIGHT]:
			char.move(right=10)
			keyPressed = True

		if key[pygame.K_LEFT]:
			char.move(left=-10)
			keyPressed = True

		if not keyPressed:
			char.move()

		win.fill((255,255,255))

		collisionBorder(char, win)
		collisionDetection(char, [bloc, spike])
		proximityDetection(char, [spike])


		#draw element
		for x in ListDisplay:
			x.draw()
		
		#update screen
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
