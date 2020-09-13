

from random import randrange, randint, choices
'''
pads = ((1100, 405, 161, 30), 
		(1192, 161, 138, 30), 
		(370, 372, 175, 30), 
		(776, 239, 171, 30), 
		(181, 207, 142, 30), 
		(978, 366, 144, 30), 
		(570, 466, 169, 30), 
		(826, 664, 115, 30), 
		(802, 648, 174, 30), 
		(256, 177, 149, 30))
'''

pads = ((818, 578, 292, 16), 
		(1106, 482, 148, 16), 
		(386, 562, 244, 16), 
		(754, 578, 148, 16), 
		(466, 226, 244, 16), 
		(738, 50, 228, 16), 
		(578, 674, 260, 16), 
		(322, 178, 212, 16), 
		(434, 578, 100, 16), 
		(882, 498, 196, 16))

hurdles = ((1106, 482-32),(466, 226-32),(322, 178-32),(882, 498-32),(818, 578-32))

def autoGenPads(nb, screenSize):
	listPad = []

	for i in range(0,nb):
		p = genPad(screenSize)
		for ax,ay,aw,ah in listPad:
			px,py,pw,ph = p
			#test if rect are overlapping
			if abs(ax-px) < (ah + ph):
				print("  ")
			#if overlap gen a new pad and reject previous
			#stop when all pad are generated
	return listPad

def genHurdles(nb, listPad):
	nbPad = len(listPad)
	for i in range(0,nb):
		pad = listPad[randint(0,nbPad)]


def genPad(screenSize):
	maxWidth = screenSize[0]
	maxHeight = screenSize[1]

	x = randrange(50,maxWidth-100,10)
	y = randrange(50,maxHeight-100,10)
	w = randrange(100,300,10)
	return (x, y, w, 30)


if __name__ == '__main__':
	screenSize = (1350,700)
	padPosX = choices(range(50,1350,16), k=10)
	padPosY = choices(range(50,700,16), k=10)
	padWidth = choices(range(100,300,16), k=10)
	padHeight = [16 for x in range(0,10)]
	print(f"{padPosX}, {padPosY}, {padWidth}, {padHeight}")
	pad = zip(padPosX, padPosY, padWidth, padHeight)
	print(tuple(pad))

