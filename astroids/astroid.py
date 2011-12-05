import math
import random
import pygame
import game_state

# TODO: general Entity class

class Ship:
    def __init__(self, posx=game_state.screen.get_width()/2,
            posy=game_state.screen.get_height()/2):
        self.posx = posx
        self.posy = posy

        self.angle = 90
        self.rotation_speed = 200
        self.direction = 0

        self.vx = 0
        self.vy = 0

        self.angles = [90, 215, 0, 315]
        self.p_distances_from_origin = (10, 10, 0, 10)

    def update(self):
        secs = float(game_state.ticks) / 1000
        
        self.posx += self.vx*secs
        self.posy += self.vy*secs

        self.rotate(self.direction)

    def rotate(self, direction):
        secs = float(game_state.ticks) / 1000

        if direction:
            self.angle += direction*secs*self.rotation_speed
            self.angle %= 360
            for i in xrange(len(self.angles)):
                self.angles[i] += direction*secs*self.rotation_speed
                self.angles[i] %= 360

    def accelerate(self):
        rads = math.radians(self.angle)
        self.vx += game_state.ticks/2*math.cos(rads)
        self.vy += game_state.ticks/2*math.sin(rads)

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

    def key_pressed(self, pressed):
        if pressed[pygame.K_UP]:
            self.accelerate()
        if pressed[pygame.K_LEFT]:
            self.rotate(-1)
        elif pressed[pygame.K_RIGHT]:
            self.rotate(1)

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

    def update(self):
        secs = float(game_state.ticks) / 1000
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
    a.posx = random.choice((-a.radius_range, game_state.screen.get_width()+a.radius_range))
    a.posy = random.choice((-a.radius_range, game_state.screen.get_height()+a.radius_range))

    a.vx = random.randint(10, 100)
    if a.posx > 0:
        a.vx = -a.vx

    a.vy = random.randint(10, 100)
    if a.posy > 0:
        a.vy = -a.vy

    a.rotation = random.randrange(10, 100)

    return a
