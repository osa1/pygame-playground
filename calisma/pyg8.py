import pygame, random

class Worm:
    def __init__(self, surface):
        self.surface = surface
        self.x = surface.get_width()/2
        self.y = surface.get_height()/2
        self.length = 1
        self.grow_to = 50
        self.vx = 0
        self.vy = -1
        self.body = []
        self.crashed = False
        self.color = 255, 255, 0

    def eat(self):
        self.grow_to += 25

    def event(self, event):
        if event.key == pygame.K_UP and self.dir_y != 1:
            self.vx, self.vy = (0, -1)
        elif event.key == pygame.K_DOWN and self.dir_y != -1:
            self.vx, self.vy = (0, 1)
        elif event.key == pygame.K_LEFT and self.dir_x != 1:
            self.vx, self.vy = (-1, 0)
        elif event.key == pygame.K_RIGHT and self.dir_x != -1:
            self.vx, self.vy = (1, 0)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if (self.x, self.y) in self.body:
            self.crashed = True

        self.body.insert(0, (self.x, self.y))

        if self.grow_to > self.length:
            self.length += 1

        if len(self.body) > self.length:
            self.body.pop()


    def draw(self):
        for x, y in self.body:
            self.surface.set_at((x, y), self.color)

    def position(self):
        return self.x, self.y

class Food:
    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(0, surface.get_width())
        self.y = random.randint(0, surface.get_height())
        self.color = 255, 255, 255

    def draw(self):
        self.surface.set_at((self.x, self.y), self.color)

    def position(self):
        return self.x, self.y

w = 500
h = 500

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

score = 0
worm = Worm(screen)
food = Food(screen)
running = True

while running:
    screen.fill((0, 0, 0))
    worm.move()
    worm.draw()
    food.draw()

    if worm.crashed:
        running = False
    elif worm.x <= 0 or worm.x >= w-1 or worm.y <= 0 or worm.y >= h-1:
        running = False
    elif worm.position() == food.position():
        score += 1
        worm.eat()
        print "score: %d" % score
        food = Food(screen)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        worm.event(event)

    pygame.display.flip()
    clock.tick(240)
