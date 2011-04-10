import pygame, random

class Worm:
    def __init__(self, surface, x, y, length):
        self.surface = surface
        self.x = x
        self.y = y
        self.length = length
        self.dir_x = 0
        self.dir_y = -1
        self.body = []
        self.crashed = False

    def key_event(self, event):
        if event.key == pygame.K_UP and self.dir_y != 1:
            self.dir_x, self.dir_y = (0, -1)
        elif event.key == pygame.K_DOWN and self.dir_y != -1:
            self.dir_x, self.dir_y = (0, 1)
        elif event.key == pygame.K_LEFT and self.dir_x != 1:
            self.dir_x, self.dir_y = (-1, 0)
        elif event.key == pygame.K_RIGHT and self.dir_x != -1:
            self.dir_x, self.dir_y = (1, 0)

    def move(self):
        self.x += self.dir_x
        self.y += self.dir_y

        r, g, b, a = self.surface.get_at((self.x, self.y))
        if (r, g, b) != (0, 0, 0):
            self.crashed = True
            print r, g, b

        self.body.insert(0, (self.x, self.y))

        if len(self.body) >= self.length:
            self.body.pop()

        self.last = self.body[-1]

    def draw(self):
        for x, y in self.body:
            self.surface.set_at((x, y), (255, 255, 255))
            self.surface.set_at(self.last, (0, 0, 0))

    def eat(self):
        print 'yummy!'
        self.length += 1

class Food:
    def __init__(self, surface, x, y, clr):
        self.surface = surface
        self.x = x
        self.y = y
        self.clr = clr
    def draw(self):
        self.surface.set_at((self.x, self.y), self.clr)
        if w.x == self.x and w.y == self.y:
            self.x = random.randint(0, width)
            self.y = random.randint(0, height)

width = 640
height = 400

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

w = Worm(screen, width/2, height/2, 200)
f = Food(screen,
         random.randint(0, width), random.randint(0, height),
         (100, 100, 100))

while running:
    w.draw()
    w.move()
    f.draw()


    if w.crashed or w.x <= 0 or w.x >= width-1 or w.y <= 0 or w.y >= height-1:
        print 'Crash!'
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            w.key_event(event)

    pygame.display.flip()
    clock.tick(240)

if not running: print w.body
