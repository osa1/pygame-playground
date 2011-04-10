import pygame
from math import sqrt
pygame.init()

def cross_product(v1, v2):
    r = []
    l = min(len(v1), len(v2))
    for i in range(l):
        r.append(v1[i] * v2[i])
    return r

def dot_product(v1, v2):
    r = 0
    for i in range(len(v1)):
        r += v1[i] * v2[i]
    return r

def vektor_fark(v1, v2):
    """
    v1, v2; vektorler [x, y]
    donus degeri; v1-v2
    """
    return [v1[0] - v2[0], v1[1] - v2[1]]

def birim_vektor(n1, n2):
    """
    n1, n2 noktalar ([x, y])
    iki vektor nokta arasindaki birim vektoru verir.
    baslangic n1, bitis n2 seklinde
    """
    v = [n2[0]-n1[0], n2[1]-n1[1]]
    uzaklik = sqrt(v[0]**2 + v[1]**2)
    v[0] /= uzaklik
    v[1] /= uzaklik
    return v

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


def vektor_carpim(n, v):
    """
    n; sayi
    v, vektor [x, y]
    bir vektoru bir sayiyla carpmak
    """
    return [v[0]*n, v[1]*n]


def yeni_vektor(v, n):
    """
    v; vektor [x, y]
    n; yuzey normal vektoru(birim vektor) [x, y]
    donus degeri; carpmadan sonraki yeni vektor
    """
    n = birim_vektorlestir(n)
    r = vektor_fark(v, vektor_carpim(2*dot_product(n, v), n))
    return r;



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
    r = [0, 0]
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
        #print "-----------------------------------------------------------------"
        #print m1
        #print m2
        #print m3
        #print m4
        
        #pygame.draw.circle(screen, (255, 255, 255),
                #m1d, 5)
        #pygame.draw.circle(screen, (255, 255, 255),
                #m2d, 5)
        #pygame.draw.circle(screen, (255, 255, 255),
                #m3d, 5)
        #pygame.draw.circle(screen, (255, 255, 255),
                #m4d, 5)


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


        #pygame.draw.circle(screen, (255, 255, 255),
                #_((m1[0]+m3[0], m1[1]+m3[1])), 5)
        #pygame.draw.circle(screen, (255, 255, 255),
                #_((m1[0]+m4[0], m1[1]+m4[1])), 5)
        #pygame.draw.circle(screen, (255, 255, 255),
                #_((m2[0]+m4[0], m2[1]+m4[1])), 5)
        #pygame.draw.circle(screen, (255, 255, 255),
                #_((m2[0]+m3[0], m2[1]+m3[1])), 5)

        ## dik
        #pygame.draw.aaline(screen, (255, 255, 255),
                #(0+pos, 0+pos),
                #m1d)
        #pygame.draw.aaline(screen, (255, 255, 255),
                #(0+pos, 0+pos),
                #m2d)

        ## paralel
        #pygame.draw.aaline(screen, (255, 255, 255),
                #(0+pos, 0+pos),
                #m3d)
        #pygame.draw.aaline(screen, (255, 255, 255),
                #(0+pos, 0+pos),
                #m4d)

        clock.tick(50)
        pygame.display.flip()
