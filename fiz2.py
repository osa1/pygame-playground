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

def ara_birim_vektor(p1, p2):
    """
    p1'den p2'ye dogru birim vektor olusturur.
    """
    return Vector(p2[0]-p1[0], p2[1]-p1[1]).get_unit_vector()


SCREENX = 500
SCREENY = 500
UZUNLUK = 150
BEYAZ = (255, 255, 255) 

def _(v):
    """
    Normal kartezyen duzlemindeki koordinatlari
    pygame duzlemindekilere cevirir.
    ismi super dimi.
    """
    return v[0]+SCREENX/2, SCREENY/2-v[1]

def pyd(v):
    """
    Pygame duzleminden normal kartezyen duzeleme donustur."
    """
    return [v[0]-SCREENX/2, SCREENY/2-v[1]]

konumlar = [[200, 200]]
hizlar = [[1, 1]]


screen = pygame.display.set_mode((SCREENX, SCREENY), 0, 32)
clock = pygame.time.Clock()

pos = SCREENX/2
running = 1
vektorler = [[0, 0], [0, 0]]
r = [SCREENX/2-pos, -SCREENY/2-10+pos]
r = birim_vektorlestir(r)
vektorler = dik_vektor(r)  # [[x1, y1], [x2, y2]]



font = pygame.font.SysFont('Consolas', 15)
p1t = font.render('p1', True, (0, 0, 0), (255, 255, 255))
p2t = font.render('p2', True, (0, 0, 0), (255, 255, 255))
p3t = font.render('p3', True, (0, 0, 0), (255, 255, 255))
p4t = font.render('p4', True, (0, 0, 0), (255, 255, 255))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            r = [event.pos[0]-pos, -event.pos[1]+pos]
            #print r
            r = birim_vektorlestir(r)
            vektorler = dik_vektor(r)  # [[x1, y1], [x2, y2]]
            #print  ">>",  r, "<<"  # [x, y]

    screen.fill((0, 0, 0))

    # yuzeylerin orta noktalari
    m1 = vektorler[0][0]*UZUNLUK, vektorler[0][1]*UZUNLUK
    m2 = vektorler[1][0]*UZUNLUK, vektorler[1][1]*UZUNLUK
    m3 = -r[0]*UZUNLUK, -r[1]*UZUNLUK
    m4 = r[0]*UZUNLUK, r[1]*UZUNLUK

    # kenarlarin ortalarindan merkeze birim vektorler
    m1b = ara_birim_vektor(m1, (0, 0))
    m2b = ara_birim_vektor(m2, (0, 0))
    m3b = ara_birim_vektor(m3, (0, 0))
    m4b = ara_birim_vektor(m4, (0, 0))

    m1d = _(m1)
    m2d = _(m2)
    m3d = _(m3)
    m4d = _(m4)

    # yuzeylerin koseleri
    p1 = _((m1[0]+m3[0], m1[1]+m3[1]))
    p2 = _((m1[0]+m4[0], m1[1]+m4[1]))
    p3 = _((m2[0]+m4[0], m2[1]+m4[1]))
    p4 = _((m2[0]+m3[0], m2[1]+m3[1]))

    screen.blit(p1t, m1d)
    screen.blit(p2t, m2d)
    screen.blit(p3t, m3d)
    screen.blit(p4t, m4d)

    # yuzeylerin normal birim vektorleri
    p1n = ara_birim_vektor(m1, (0, 0))
    p2n = -p1n[0], -p1n[1]
    p3n = p1n[1], -p1n[0]
    p4n = -p1n[1], p1n[0]
    p1n = Vector(p1n)
    p2n = Vector(p2n)
    p3n = Vector(p3n)
    p4n = Vector(p4n)

    #screen.blit(p1t, p1)
    #screen.blit(p2t, p2)
    #screen.blit(p3t, p3)
    #screen.blit(p4t, p4)

    pygame.draw.aaline(screen, BEYAZ,
            p1, p2)
    pygame.draw.aaline(screen, BEYAZ,
            p2, p3)
    pygame.draw.aaline(screen, BEYAZ,
            p3, p4)
    pygame.draw.aaline(screen, BEYAZ,
            p4, p1)

    # toplar
    for konum, hiz in zip(konumlar, hizlar):
        vm1 = Vector(pyd(konum)) - Vector(m1)
        #print (vm1*vm1.dot_product(m1b)).length
        #print vm1
        if (vm1*vm1.dot_product(m1b)).length < 5:
            print "carpisma1",
            print pyd(konum)
        konum[0] += hiz[0]
        konum[1] += hiz[1]
        pygame.draw.circle(screen, BEYAZ, konum, 5)


    clock.tick(50)
    pygame.display.flip()
