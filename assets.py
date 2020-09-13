# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

# Additional notes
# - Further adaptations from https://www.pygame.org/wiki/Spritesheet
# - Cleaned up overall formatting.
# - Updated from Python 2 -> Python 3.

import pygame


class SpriteSheet:
	def __init__(self, filename):
		"""Load the sheet."""
		try:
			self.sheet = pygame.image.load(filename).convert()
		except pygame.error as e:
			print(f"Unable to load spritesheet image: {filename}")
			raise SystemExit(e)


	def image_at(self, rectangle, colorkey = None):
		"""Load a specific image from a specific rectangle."""
		# Loads image from x, y, x+offset, y+offset.
		rect = pygame.Rect(rectangle)
		image = pygame.Surface(rect.size).convert()
		image.blit(self.sheet, (0, 0), rect)
		if colorkey is not None:
			if colorkey == -1:
				colorkey = image.get_at((0,0))
			image.set_colorkey(colorkey, pygame.RLEACCEL)
		return image

	def images_at(self, rects, colorkey = None):
		"""Load a whole bunch of images and return them as a list."""
		return [self.image_at(rect, colorkey) for rect in rects]

	def load_strip(self, rect, image_count, colorkey = None):
		"""Load a whole strip of images, and return them as a list."""
		tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
				for x in range(image_count)]
		return self.images_at(tups, colorkey)

	def get_image(self, origine, size):
		'''
			origine : tuple (x,y) position of the origine of the picture
			size : tuple (x,y) number of square of 16px is width and height
		'''
		element = (origine[0]*16, origine[1]*16, size[0]*16, size[1]*16)
		return  self.image_at(element)


if __name__ == "__main__":
	pygame.init()
	win = pygame.display.set_mode((500,500))
	pygame.display.set_caption("test assets")
	clock = pygame.time.Clock()
	font = pygame.font.SysFont("Comic Sans Ms", 20)

	filename = 'game_assets/monsterboy_assets.png'
	element_ss = SpriteSheet(filename)


	run = True
	while run:
		clock.tick(60)
		win.fill((255,255,255))

		image = element_ss.get_image((61,24),(2,2))
		image = pygame.transform.scale(image, (120, 120))
		rect = image.get_rect()
		rect.topleft = 0, 0
		win.blit(image, rect)

		#update screen
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
