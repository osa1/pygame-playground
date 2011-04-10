import pygame
 
w = h = 500
size = 250
step = 10
lines = []
pos = 0
maxlines = 60

for x in range(0, size+1, step):
    lines.append((0, size-x, x, 0))

for x in range(0, size+1, step):
    lines.append((w - (size-x), 0, w, x))

for x in range(0, size+1, step):
    lines.append((w, h - (size-x), w-x, h))

for x in range(0, size+1, step):
    lines.append((size-x, h, 0, h-x))

print lines

screen = pygame.display.set_mode((w+1, h+1))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    col = 0
    cur = pos

    for i in range(maxlines):
        x1, y1, x2, y2 = lines[cur]
        pygame.draw.line(screen, (col, col, col), (x1, y1), (x2, y2))

        cur += 1
        if cur >= len(lines): cur = 0
        col += 240 / maxlines
        
    pos += 1
    if pos >= len(lines): pos = 0

    pygame.display.flip()
    clock.tick(40)
