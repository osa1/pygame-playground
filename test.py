import pygame
import pygame.locals as pyl
import sys

pygame.init()

running = True
screenx, screeny = 800, 800
screen = pygame.display.set_mode((screenx, screeny))
clock = pygame.time.Clock()
yer = [0, 0]

class Eksen:

    def __init__(self, eksen):
        self.eksen = eksen

        if self.eksen == 'x':
            self.baslangic = [0, screeny/2]
            self.bitis = [screenx, screeny/2]
        elif self.eksen == 'y':
            self.baslangic = [screenx/2, 0]
            self.bitis = [screenx/2, screeny]

    def yurut(self, x, y):
        if x and self.eksen == 'y':
            self.baslangic[0] += x
            self.bitis[0] += x
        if y and self.eksen == 'x':
            self.baslangic[1] += y
            self.bitis[1] += y
            
    def ciz(self):
        pygame.draw.aaline(screen, (255, 255, 255), self.baslangic, self.bitis)

Eksenler = [Eksen('x'), Eksen('y')]
font = pygame.font.SysFont('arial', 16)
pay = 100
hiz = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    
    for eksen in Eksenler:
        eksen.ciz()
        mousePos = pygame.mouse.get_pos()
        degisim = [0, 0]
        if mousePos[0] > screenx-pay:
            degisim[0] = -hiz
        if mousePos[0] < pay:
            degisim[0] = hiz
        if mousePos[1] > screeny-pay:
            degisim[1] = -hiz
        if mousePos[1] < pay:
            degisim[1] = hiz
        eksen.yurut(*degisim)

    yer[0] -= degisim[0]
    yer[1] += degisim[1]

    text = font.render('1', True, (0, 0, 0), (255, 255, 255))
    screen.blit(text, (screenx-50-text.get_width(), 50))

    pygame.display.flip()
    clock.tick(24)
