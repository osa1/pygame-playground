import pygame
import time

screen = pygame.display.set_mode((400, 400))
running = 1

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    screen.fill((0, 0, 0))
    bas_x, bas_y = (0, 0)
    beyaz = (255, 255, 255)
    for i in range(410/10):
        pygame.draw.aaline(screen, beyaz, (bas_x, i*10),
                          (400-i*10, bas_y))
        pygame.draw.aaline(screen, beyaz, (i*10, 400-bas_y),
                           (400, 400-(i*10)))
    pygame.display.flip()
