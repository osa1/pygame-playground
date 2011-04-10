#!/usr/bin/env python

import pygame



screenx, screeny = 800, 800
screen = pygame.display.set_mode((screenx, screeny))
bluedir = 15
blueval = 0
running = 1
clock = pygame.time.Clock()


while running:
    bgcolor = 0, 50, blueval
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0

    screen.fill(bgcolor)

    blueval += bluedir
    print blueval
    if blueval == 255 or blueval == 0:
        bluedir *= -1

    pygame.display.flip()
    clock.tick(20)
    
    
