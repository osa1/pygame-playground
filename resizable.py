import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREENSIZE = (640, 480)

background_image = '/home/osa1/Pictures/cowboy-bebop.jpg'
font = pygame.font.SysFont('arial', 16)
screen = pygame.display.set_mode(SCREENSIZE, NOFRAME|RESIZABLE, 32)

background = pygame.image.load(background_image).convert()
text = font.render(background_image, True, (0,0,0), (255,255,255))

while True:
    event = pygame.event.wait()
    if event.type == QUIT: exit()
    if event.type == VIDEORESIZE:
        SCREENSIZE = event.size
        screen = pygame.display.set_mode(SCREENSIZE, NOFRAME|RESIZABLE, 32)
        pygame.display.set_caption("Window sresized to " + str(event.size))

    screen_width, screen_height = SCREENSIZE
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))

    screen.blit(text, (screen.get_width()-text.get_width()-20,
                       screen.get_height()-text.get_height()-20))

    pygame.display.update()
