SCREENSIZE = (640, 480)
message = "   This is a demonstration of the scrolly message script.   "

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)

font = pygame.font.SysFont('arial', 80)
text_surface = font.render(message, True, (0,0,255))

x = 0
y = (SCREENSIZE[1] - text_surface.get_height()) / 2

background_image = 'cowboy-bebop.jpg'
background = pygame.image.load(background_image).convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT: exit()
 
    screen.blit(background, (0, 0))

    x -= 2
    if x < -text_surface.get_width():
        x = 0

    screen.blit(text_surface, (x, y))
    screen.blit(text_surface, (x+text_surface.get_width(), y))
    pygame.display.update()
