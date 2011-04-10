import pygame
pygame.init()


SCREENX, SCREENY = 310, 310


running = True
screen = pygame.display.set_mode((SCREENX, SCREENY))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Consolas', 15)
text1 = font.render('(0, 0)', True, (0, 0, 0), (255, 255, 255))
text2 = font.render('(300, 300)', True, (0, 0, 0), (255, 255, 255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0


    screen.fill((0, 0, 0))
    
    pygame.draw.aaline(screen, (255, 255, 255), (5, 5), (305, 5))
    pygame.draw.aaline(screen, (255, 255, 255), (5, 5), (5, 305))
    pygame.draw.aaline(screen, (255, 255, 255), (305, 5), (305, 305))
    pygame.draw.aaline(screen, (255, 255, 255), (305, 305), (5, 305))

    screen.blit(text1, (5, 5))
    screen.blit(text2, (305-text2.get_width(), 305-text2.get_height()))

    clock.tick(50)
    pygame.display.flip()

