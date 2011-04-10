import pygame

x = y = 0
running = 1
clock = pygame.time.Clock()
screenx, screeny = 800, 800
screen = pygame.display.set_mode((screenx, screeny))

bgcolor = 0, 0, 0
blueval = 0
bluedir = 15
linecolor = 255, 255, 255

class Bolge:
	def __init__(self, baslangicx, baslangicy, bitisx, bitisy):
		self.baslangicx = baslangicx
		self.baslangicy = baslangicy
		self.bitisx = bitisx
		self.bitisy = bitisy
	def __contains__(self, item):
		x, y = item
		return x > self.baslangicx and \
		       y > self.baslangicy and \
		       x < self.bitisx and \
		       y < self.bitisy

while running:
    for event in pygame.event.get():
        print event
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
        #elif event.type == pygame.MOUSEBUTTONUP:
        #    x, y = event.pos
        #    screen.set_at((x, y), (255, 255, 255))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 1
            elif event.key == pygame.K_DOWN:
                y += 1
            elif event.key == pygame.K_LEFT:
                x -= 1
            elif event.key == pygame.K_RIGHT:
                x += 1

    screen.fill(bgcolor)

    bolge1 = Bolge(0,0, screenx/2, screeny/2)
    bolge2 = Bolge(screenx/2, 0, screenx, screeny/2)
    bolge3 = Bolge(screenx/2, screeny/2, screenx, screeny)
    bolge4 = Bolge(0, screeny/2, screenx/2, screeny)

    mbolge = bolge1
    for bolge in bolge1, bolge2, bolge3, bolge4:
        if (x, y) in bolge:
            mbolge = bolge

    if mbolge == bolge1:
        renk = (0, 0, blueval)
    elif mbolge == bolge2:
        renk = (0, blueval, 0)
    elif mbolge == bolge3:
        renk = (blueval, 0, 0)
    elif mbolge == bolge4:
        renk = (blueval, blueval, blueval)

    pygame.draw.aaline(screen, renk, (x, y+20), (x, y-20))
    pygame.draw.aaline(screen, renk, (x+20, y), (x-20, y))

    pygame.draw.aaline(screen, renk, (0, 0), (x, y))
    pygame.draw.aaline(screen, renk, (screenx, screeny), (x, y))
    
    blueval += bluedir
    if blueval == 255 or blueval == 0: bluedir *= -1
    pygame.display.flip()

    clock.tick(20)
