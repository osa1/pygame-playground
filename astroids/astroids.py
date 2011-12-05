import math
import random
import pygame

SCREENX, SCREENY = 700, 700

# TODO: general Entity class

class Ship:
    def __init__(self, posx=SCREENX/2, posy=SCREENY/2):
        self.posx = posx
        self.posy = posy

        self.angle = 90
        self.rotation_speed = 200
        self.direction = 0

        self.vx = 0
        self.vy = 0

        self.angles = [90, 215, 0, 315]
        self.p_distances_from_origin = (10, 10, 0, 10)

    def update(self, ticks):
        secs = float(ticks) / 1000
        
        self.posx += self.vx*secs
        self.posy += self.vy*secs

        self.rotate(ticks, self.direction)

    def rotate(self, ticks, direction):
        secs = float(ticks) / 1000

        if direction:
            self.angle += direction*secs*self.rotation_speed
            self.angle %= 360
            for i in xrange(len(self.angles)):
                self.angles[i] += direction*secs*self.rotation_speed
                self.angles[i] %= 360

    def accelerate(self, ticks):
        rads = math.radians(self.angle)
        self.vx += ticks/2*math.cos(rads)
        self.vy += ticks/2*math.sin(rads)

        if self.vx > 250:
            self.vx = 250

        if self.vy > 250:
            self.vy = 250

    def point_list(self):
        return [(p*math.cos(math.radians(a))+self.posx,
            p*math.sin(math.radians(a))+self.posy) \
                    for p, a in zip(self.p_distances_from_origin, self.angles)]

    def draw(self, surface):
        pygame.draw.polygon(surface, (255, 100, 100), self.point_list(), 1)

class Astroid:
    def __init__(self, points=5, radius=50,
            radius_range=10, angle_range=20):
        self.points = points
        self.radius = radius

        self.radius_range = radius_range

        self.posx = 0
        self.posy = 0
        self.vx = 0
        self.vy = 0

        self.rotation = 0

        self.angles = [a * 360/points + random.randint(-angle_range, angle_range)
                for a in xrange(points)]

        self.p_distances_from_origin = \
                [random.randint(radius-radius_range, radius+radius_range)
                        for p in xrange(points)]

    def point_list(self, center=None):
        if not center:
            center = (self.posx, self.posy)

        return [(center[0]+p*math.cos(math.radians(d)),
                 center[1]+p*math.sin(math.radians(d)))
                 for (p, d) in zip(self.p_distances_from_origin, self.angles)]

    def rotate(self, angle):
        for i in xrange(len(self.angles)):
            self.angles[i] += angle
            self.angles[i] %= 360
            
    def draw(self, surface):
        pygame.draw.polygon(surface, (255, 255, 255), self.point_list(), 1)

    def update(self, ticks):
        secs = float(ticks) / 1000
        self.posx += float(self.vx) * secs
        self.posy += float(self.vy) * secs
        self.rotate(self.rotation * secs)

    def inside_polygon(self, p):
        """Raycasting method."""
        point_list = self.point_list()
        counter = 0

        for x, y in zip(point_list, point_list[1:] + [point_list[0]]):
            if p[1] > min(x[1], y[1]) and \
                    p[1] <= max(x[1], y[1]) and \
                    p[0] <= max(x[0], y[0]) and \
                    x[1] != y[1]:
                        xinters = (p[1]-x[1])*(y[0]-x[0])/(y[1]-x[1])+x[0]
                        if (x[0] == y[0]) or (p[0] <= xinters):
                                counter += 1

        if counter % 2 == 0:
            return False
        return True

def generate_random_astroid():
    radius_range = random.randint(1, 10)
    radius = random.randint(radius_range*2, radius_range*3)
    a = Astroid(points=random.randint(4, 10),
            radius_range=radius_range,
            radius=radius)

    # TODO
    a.posx = random.choice((-a.radius_range, SCREENX+a.radius_range))
    a.posy = random.choice((-a.radius_range, SCREENY+a.radius_range))

    a.vx = random.randint(10, 100)
    if a.posx > 0:
        a.vx = -a.vx

    a.vy = random.randint(10, 100)
    if a.posy > 0:
        a.vy = -a.vy

    a.rotation = random.randrange(10, 100)

    return a


if __name__ == "__main__":
    # TODO maintainable game loop
    pygame.font.init()
    font = pygame.font.SysFont("Consolas", 40)
    pause_text = font.render("Paused", 1, (255, 255, 255))
    crashed_text = font.render("Crashed", 1, (255, 255, 255))

    ticks = 0
    running = True  # any better ways to save game state?
    paused = False
    crashed = False

    screen = pygame.display.set_mode((700, 700), 0, 32)
    time = pygame.time.Clock()

    astroids = []
    ship = Ship()

    while running:
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                astroids.append(generate_random_astroid())
                #print "mousepos", pygame.mouse.get_pos()
                #for a in astroids[:]:
                    #if a.inside_polygon(pygame.mouse.get_pos()):
                        #astroids.remove(a)
            elif event.type == pygame.KEYDOWN:
                if pressed[pygame.K_ESCAPE]:
                    paused = not paused
                if pressed[pygame.K_UP]:
                    ship.accelerate(ticks)
            
            if event.type == pygame.KEYDOWN or \
                    event.type == pygame.KEYUP:
                if pressed[pygame.K_LEFT]:
                    ship.direction = -1
                elif pressed[pygame.K_RIGHT]:
                    ship.direction = 1
                else:
                    ship.direction = 0

        if pressed[pygame.K_UP]:
            ship.accelerate(ticks)

        screen.fill((0, 0, 0))
        ship.draw(screen)

        # draw astroids and check for collisions
        for a in astroids[:]:
            a.draw(screen)
            if not paused and not crashed:
                if a.posx - 2*a.radius_range > SCREENX or \
                        a.posx + 2*a.radius_range < 0 or \
                        a.posy - 2*a.radius_range > SCREENY or \
                        a.posy + 2*a.radius_range < 0:
                            astroids.remove(a)
                a.update(ticks)
        if paused:
            screen.blit(pause_text, (100, 100))
        elif not crashed:
            ship.update(ticks)

        for a in astroids:
            for p in ship.point_list():
                if a.inside_polygon(p):
                    crashed = True

        if crashed:
            screen.blit(crashed_text, (100, 100))

        pygame.display.flip()
        ticks = time.tick(40)
