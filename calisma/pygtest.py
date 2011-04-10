import pygame

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        else:
            print event.type
            
    clock.tick(20)
