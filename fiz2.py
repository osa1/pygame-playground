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
YARICAP = 5

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

konumlar = [[200, 200], [300, 300], [300, 300],[350, 350]]
hizlar = [[3, 3], [2, 0], [1, 0], [0, 1]]


screen = pygame.display.set_mode((SCREENX, SCREENY), 0, 32)
clock = pygame.time.Clock()

pos = SCREENX/2
running = 1
vektorler = [[0, 0], [0, 0]]
r = [SCREENX/2-pos, -SCREENY/2-10+pos]
r = birim_vektorlestir(r)
vektorler = dik_vektor(r)  # [[x1, y1], [x2, y2]]



font = pygame.font.SysFont('Consolas', 15)
p1t = font.render('p1', True, (0, 0, 0), BEYAZ)
p2t = font.render('p2', True, (0, 0, 0), BEYAZ)
p3t = font.render('p3', True, (0, 0, 0), BEYAZ)
p4t = font.render('p4', True, (0, 0, 0), BEYAZ)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
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

        if konum[0] < 0:
            konum[0] += SCREENX
        elif konum[0] > SCREENX:
            konum[0] -= SCREENX
        if konum[1] < 0:
            konum[1] += SCREENY
        elif konum[1] > SCREENY:
            konum[1] -= SCREENY
               
        # top konumundan duvarin ortasina kadar olan vektorler
        konum_vektor = Vector(pyd(konum))
        vm1 = konum_vektor - Vector(m1)
        vm2 = konum_vektor - Vector(m2)
        vm3 = konum_vektor - Vector(m3)
        vm4 = konum_vektor - Vector(m4)
        #print (vm1*vm1.dot_product(m1b)).length
        #print vm1
        if abs((m1b*vm1.dot_product(m1b)).length) < 5:
            v_hiz = Vector((hiz[0], -hiz[1]))
            ref_v = v_hiz - m1b*2*(v_hiz.dot_product(m1b))
            hiz[0] = ref_v[0]
            hiz[1] = -ref_v[1]
        if abs((m2b*vm2.dot_product(m2b)).length) < 5:
            v_hiz = Vector((hiz[0], -hiz[1]))
            ref_v = v_hiz - m2b*2*(v_hiz.dot_product(m2b))
            hiz[0] = ref_v[0]
            hiz[1] = -ref_v[1]
        if abs((m3b*vm3.dot_product(m3b)).length) < 5:
            v_hiz = Vector((hiz[0], -hiz[1]))
            ref_v = v_hiz - m3b*2*(v_hiz.dot_product(m3b))
            hiz[0] = ref_v[0]
            hiz[1] = -ref_v[1]
        if abs((m4b*vm4.dot_product(m4b)).length) < 5:
            v_hiz = Vector((hiz[0], -hiz[1]))
            ref_v = v_hiz - m4b*2*(v_hiz.dot_product(m4b))
            hiz[0] = ref_v[0]
            hiz[1] = -ref_v[1]
        konum[0] += hiz[0]
        konum[1] += hiz[1]
        pygame.draw.circle(screen, BEYAZ, konum, YARICAP)


    clock.tick(60)
    pygame.display.flip()
