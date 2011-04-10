import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screensize = (1600, 900)
background_image = '/home/osa1/Pictures/cowboy-bebop.jpg'
screen = pygame.display.set_mode(screensize, 0, 32)
background = pygame.image.load(background_image).convert()

Fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode(screensize, FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode(screensize, 0, 32)

    screen.blit(background, (0,0))
    pygame.display.update()
