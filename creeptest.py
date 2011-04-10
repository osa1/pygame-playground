#!/usr/bin/env python

import pygame
import pygame.locals as pyl
from vec2d import vec2d

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
BG_COLOR = 150, 150, 80
CREEP_FILENAMES = ['creeps_1/bluecreep.png',
				   'creeps_1/graycreep.png',
				   'creeps_1/pingcreep.png']
N_CREEPS = 20

pygame.init()


class Creep(pygame.sprite.Sprite):
	def __init__(self, screen, img_filename, init_position,
				 init_direction, speed):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		self.speed = speed
		self.base_image = pygame.image.load(img_filename).convert_alpha()
		self.image = self.base_image
		self.pos = vec2d(init_position)
		self.direction = vec2d(init_position).normalized()
		
	def update(self, time_passed):
		self._change_direction(time_passed)
		self.image = pygame.transform.rotate(
			self.base_image, -self.direction.angle)
		displacement = vec2d(
			self.direction.x * self.speed * time_passed,
			self.direction.y * self.speed * time_passed)

		self.pos += displacement
		self.image_w, self.image_h = self.image.get_size()
		bounds_rect = self.screen.get_rect().inflate(
			-self.image_w, -self.image_h)
		
	def blitme(self):
		draw_pos = self.image.get_rect().move(
			self.pos.x - self.image_w / 2,
			self.pos.y - self.image_h / 2)
		self.screen.blit(self.image, draw_pos)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.clock.Clock()

creeps = []
for i in range(N_CREEPS):
	creeps.append(Creep(screen,
						random.choice(CREEP_FILENAMES),
						(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)),
						random.choice([-1, -1]), random.choice([-1, 1]), 0.1))

while True:
	
	time_passed = clock.tick(50)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit_game()
			
	screen.fill(BG_COLOR)
	
	for creep in creeps:
		creep.update(time_passed)
		creep.blitme()
			
	pygame.display.flip()
