import pygame, random, math

screenx, screeny = 500, 500 #ekran buyuklugu

class Ball:
    def __init__(self, surface):
        self.surface = surface
        self.radius = 10
        self.color = (255, 255, 255)
        self.x = random.randint(0+self.radius, screenx-self.radius)
        self.y = random.randint(0+self.radius, screeny-self.radius)
        self.vx = random.randint(1, 10)
        self.vy = random.randint(1, 10)
        
    def move(self, time_passed):
        if self.x >= screenx-self.radius or self.x <= self.radius:
            self.vx *= -1
        if self.y >= screeny-self.radius or self.y <= self.radius:
            self.vy *= -1
        self.x += self.vx * time_passed / 50
        self.y += self.vy * time_passed / 50
        
    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y),
                           self.radius)
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screenx, screeny), 0, 32)
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
        CollisionDetect(b)
        b.move(time_passed)
    
    pygame.display.flip()
