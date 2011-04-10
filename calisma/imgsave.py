import pygame
pygame.init()

text = "Omer Sinan Agacan"
font = pygame.font.SysFont("arial", 64)
surface = font.render(text, True, (0,0,0), (255,255,255))
pygame.image.save(surface, "name.png")
