import pygame, random

width, height = 640, 400

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

while running:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            screen.set_at((x, y), (red, green, blue))
    pygame.display.flip()
    clock.tick(240)
