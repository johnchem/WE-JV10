

from random import randrange, randint

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

hurdles = ((1110, 375),(590, 436),(300, 147),(200, 177),(410,342))

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
	padPosX = choices(range(0,1350,1), k=10)
	padPosY = choices(range(0,700,1), k=10)
	padWidth = choices(range(0,300,1), k=10)
	padHeight = [30 for x in range(0,10)]
	print(f"{padPosX}, {padPosY}, {padWidth}, {padHeight}")
	pad = zip(padPosX, padPosY, padWidth, padHeight)
	print(tuple(pad))

