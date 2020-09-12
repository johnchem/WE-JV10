
import pygame

class element():
	'''
		mother class for the display element
	'''
	def __init__(self, x, y ,height, width, color, window):
		#position variable
		self.x, self.y = x, y
		self.height, self.width = height, width
		self.window = window
		self.rect = pygame.Rect(x, y, width, height)
		self.color = color

	def draw(self):
		pygame.draw.rect(self.window, self.color, self.rect,0)


class hurdle(element):
	'''
		object which are frightful to the character
	'''
	def __init__(self, x, y ,height, width, color, window):
		super().__init__(x, y ,height, width, color, window)


class pad(element):
	'''
		plateform class
	'''
	def __init__(self, x, y ,height, width, window):
		self.color = (77, 255, 77)
		super().__init__(x, y ,height, width, self.color, window)
		

if __name__ == "__main__":
	pass