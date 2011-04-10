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
    donus degeri; birim vektor
    """
    uzunluk = sqrt(v[0]**2 + v[1]**2)
    return [v[0]/uzunluk, v[1]/uzunluk]

def dik_vektor(v):
    """
    v vektorune dik 2 vektoru doner
    [[x1, y1], [x2, y2]] seklinde
    """
    print "dik_vektor: " + str([[v[1], -v[0]], [-v[1], v[0]]])
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




def form1(normal, nokta):
    """
    normal; normal vektoru [x, y]
    nokta; nokta koordinatlari [x, y]
    cizginin baslangic ve bitis koordinatlari ((x0, y0), (x1, y1))
    """
    pass


if __name__ == "__main__":

    screen = pygame.display.set_mode((500, 500), 0, 32)
    clock = pygame.time.Clock()

    pos = 250
    running = 1
    vektorler = [[0, 0], [0, 0]]
    r = [0, 0]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                r = [event.pos[0]-pos, -event.pos[1]+pos]
                r = birim_vektorlestir(r)
                vektorler = dik_vektor(r)
                print  ">>",  r, "<<", 

        screen.fill((0, 0, 0))
        uzunluk = 100
        # dik
        pygame.draw.aaline(screen, (255, 255, 255),
                (0+pos, 0+pos),
                (vektorler[0][0]*uzunluk+pos, -vektorler[0][1]*uzunluk+pos))
        pygame.draw.aaline(screen, (255, 255, 255),
                (0+pos, 0+pos),
                (vektorler[1][0]*uzunluk+pos, -vektorler[1][1]*uzunluk+pos))

        # paralel
        pygame.draw.aaline(screen, (255, 255, 255),
                (0+pos, 0+pos),
                (r[0]*uzunluk+pos, -r[1]*uzunluk+pos))
        pygame.draw.aaline(screen, (255, 255, 255),
                (0+pos, 0+pos),
                (-r[0]*uzunluk+pos, r[1]*uzunluk+pos))

        clock.tick(50)
        pygame.display.flip()

    #n = [1, 0]
    #v1 = [-1, -1]
    #print yeni_vektor(v1, n)
    #raw_input()
