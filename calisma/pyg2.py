import pygame
import time


x, y = 0, 0
dir = 1
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
running = 1
linecolor = 255, 0, 0
bgcolor = 0, 0, 0

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    screen.fill(bgcolor)
    pygame.draw.aaline(screen, linecolor, (0, y), (width-1, y))
    pygame.draw.aaline(screen, linecolor, (x, 0), (x, height-1))

    y += dir
    x += dir
    if y == 0 or y == height-1 or x == 0 or x == width-1: dir *= -1

    

    pygame.display.flip()
    
