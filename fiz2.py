import pygame
from vector import *
pygame.init()

def birim_vektorlestir(v):
    """
    v; vektor [x, y]
    donus degeri; ayni yonlu birim vektor
    """
    uzunluk = sqrt(v[0]**2 + v[1]**2)
    return [v[0]/uzunluk, v[1]/uzunluk]

def dik_vektor(v):
    """
    v vektorune dik 2 vektoru doner
    [[x1, y1], [x2, y2]] seklinde
    """
    return [[v[1], -v[0]], [-v[1], v[0]]]


SCREENX = 300
SCREENY = 300
UZUNLUK = 100

def _(v):
    """
    Normal kartezyen duzlemindeki koordinatlari
    pygame duzlemindekilere cevirir.
    ismi super dimi.
    """
    return v[0]+SCREENX/2, SCREENY/2-v[1]


if __name__ == "__main__":

    screen = pygame.display.set_mode((SCREENX, SCREENY), 0, 32)
    clock = pygame.time.Clock()

    pos = SCREENX/2
    running = 1
    vektorler = [[0, 0], [0, 0]]
    r = [SCREENX/2-pos, -SCREENY/2-10+pos]
    r = birim_vektorlestir(r)
    vektorler = dik_vektor(r)  # [[x1, y1], [x2, y2]]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                r = [event.pos[0]-pos, -event.pos[1]+pos]
                print r
                r = birim_vektorlestir(r)
                vektorler = dik_vektor(r)  # [[x1, y1], [x2, y2]]
                #print  ">>",  r, "<<"  # [x, y]

        screen.fill((0, 0, 0))

        m1 = vektorler[0][0]*UZUNLUK, vektorler[0][1]*UZUNLUK
        m2 = vektorler[1][0]*UZUNLUK, vektorler[1][1]*UZUNLUK
        m3 = -r[0]*UZUNLUK, -r[1]*UZUNLUK
        m4 = r[0]*UZUNLUK, r[1]*UZUNLUK
        m1d = _(m1)
        m2d = _(m2)
        m3d = _(m3)
        m4d = _(m4)

        p1 = _((m1[0]+m3[0], m1[1]+m3[1]))
        p2 = _((m1[0]+m4[0], m1[1]+m4[1]))
        p3 = _((m2[0]+m4[0], m2[1]+m4[1]))
        p4 = _((m2[0]+m3[0], m2[1]+m3[1]))

        pygame.draw.aaline(screen, (255, 255, 255),
                p1, p2)
        pygame.draw.aaline(screen, (255, 255, 255),
                p2, p3)
        pygame.draw.aaline(screen, (255, 255, 255),
                p3, p4)
        pygame.draw.aaline(screen, (255, 255, 255),
                p4, p1)


        clock.tick(50)
        pygame.display.flip()
