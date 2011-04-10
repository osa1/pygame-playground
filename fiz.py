import pygame
import random
import math
pygame.init()

SCREENX, SCREENY = 500, 500
X = SCREENX/2
Y = SCREENY/2

Planes = [[X, 0, 250],
          [0, -Y, 250],
          [-X, 0, 250],
          [0, Y, 250]]

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREENX, SCREENY), 0, 32)
running = True


def dotProduct(v1, v2):
    r = []
    l = min(len(v1), len(v2))
    for i in range(l):
        r.append(v1[i] * v2[i])
    return r


def v_topla(v1, v2):
    r = []
    for i in range(len(v1)):
        r.append(v1[i] + v2[i])
    return r


def v_carp(i, v):
    r = []
    for k in v:
        r.append(i * k)
    return r

class Ball:
    def __init__(self, surface):
        self.surface = surface
        self.radius = 10
        self.color = (255, 255, 255)
        self.x = random.randint(-X+self.radius, X-self.radius)
        self.y = random.randint(-Y+self.radius, Y-self.radius)
        self.vx = random.randint(-10, 10)
        self.vy = random.randint(-10, 10)
        
    def move(self, time_passed):
        #if self.x >= X-self.radius or self.x <= -X+self.radius:
            #self.vx *= -1
        #if self.y >= Y-self.radius or self.y <= -Y+self.radius:
            #self.vy *= -1

       if (self.x < -X and dotProduct((self.vx, self.vy), Planes[2]) < 0):
           pass


       self.x += self.vx * time_passed / 50
       self.y += self.vy * time_passed / 50
        
    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x+250, self.y+250),
                           self.radius)
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREENX, SCREENY), 0, 32)
running = True

balls = []
for i in range(1, 11): #top sayisi
    balls.append(Ball(screen))

def CollisionDetect(b1):
    for b2 in balls:
        if b1 is not b2:
            range = math.sqrt((b1.x - b2.x)**2 + (b1.y - b2.y)**2)
            if range < (b1.radius + b2.radius):
                b1.vx, b2.vx = b2.vx, b1.vx
                b1.vy, b2.vy = b2.vy, b1.vy
                #b1.move(); b2.move()

while running:
    for event in pygame.event.get():
        #print event
        if event.type == pygame.QUIT:
            running = False
    
    time_passed = clock.tick(50)
    screen.fill((0, 0, 0))

    for b in balls:
        b.draw()
        b.move(time_passed)
    
    pygame.display.flip()
