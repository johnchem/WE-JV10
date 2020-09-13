
import pygame

class element():
	'''
		mother class for the display element
	'''
	def __init__(self,x,y,width,height,color,image,window):
		#position variable
		self.x, self.y = x, y
		self.height, self.width = height, width
		self.window = window
		self.rect = pygame.Rect(x, y, width, height)
		self.color = color
		self.image = None

	def draw(self):
		#pygame.draw.rect(self.window, self.color, self.rect,0)
		self.window.blit(self.image, self.rect)	
		pygame.draw.line(self.window, (0,0,0), (self.rect.left, self.rect.top), 
						(self.rect.right, self.rect.top), 2)
		
class hurdle(element):
	'''
		object which are frightful to the character
	'''
	def __init__(self,x,y,width,height,color,image,window):
		super().__init__(x, y , width, height, color, window)


class pad(element):
	'''
		plateform class
	'''
	def __init__(self,x,y,width,height,image,window):
		self.color = (77, 255, 77)
		super().__init__(x, y ,width, height, self.color, window)

class textBox():
	'''

	'''
	def __init__(self, font, label, color):
		self.font = font
		self.color = color
		self.label = label

	def update(self, text, color=self.color):
		text = font.render('GeeksForGeeks', True, green, blue) 

	def draw(self):
		display_surface.blit(text, textRect)

class TextBox(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.initFont()
			self.initImage()
			self.initGroup()
			self.setText(['a','b'])

		def initFont(self):
			pygame.font.init()
			self.font = pygame.font.Font(None,3)

		def initImage(self):
			self.image = pygame.Surface((200,80))
			self.image.fill((255,255,255))
			self.rect = self.image.get_rect()
			self.rect.top = 0 ; self.rect.left = 0        

		def setText(self,text):
			tmp = pygame.display.get_surface()
			x_pos = self.rect.left+5
			y_pos = self.rect.top+5

			for t in text:
				x = self.font.render(t,False,(0,0,0))
				tmp.blit(x,(x_pos,y_pos))
				x_pos += 10

				if (x_pos > self.image.get_width()-5):
					x_pos = self.rect.left+5
					y_pos += 10

		def initGroup(self):
			self.group = pygame.sprite.GroupSingle()
			self.group.add(self)

		

if __name__ == "__main__":
	pass