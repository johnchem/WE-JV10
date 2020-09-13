
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
		if self.image:
			self.window.blit(self.image, self.rect)	
		else:
			pygame.draw.rect(self.window, self.color, self.rect,0)
		pygame.draw.line(self.window, (0,0,0), (self.rect.left, self.rect.top), 
						(self.rect.right, self.rect.top), 2)
		
class hurdle(element):
	'''
		object which are frightful to the character
	'''
	def __init__(self,x,y,width,height,color,image,window):
		super().__init__(x,y,width,height,color,image,window)


class pad(element):
	'''
		plateform class
	'''
	def __init__(self,x,y,width,height,right_side_image,left_side_image,middle_image,window):
		self.x, self.y = x, y
		self.height, self.width = height, width
		self.window = window
		self.rect = pygame.Rect(x, y, width, height)
		self.color = (77, 255, 77)
		self.r_Image = right_side_image
		self.l_Image = left_side_image
		self.m_image = middle_image

	def draw(self):
		nbBloc = int(self.width/16)
		for x in range(0, nbBloc):
			if x == 0 : 
				self.window.blit(self.l_Image, (self.x, self.y))
			elif x == nbBloc-1:
				self.window.blit(self.r_Image, (self.x+16*x, self.y))
			else:
				self.window.blit(self.m_image, (self.x+16*x, self.y))

class textBox():
	'''

	'''
	def __init__(self, font, label, color):
		self.font = font
		self.color = color
		self.label = label

	def update(self, text, color):
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