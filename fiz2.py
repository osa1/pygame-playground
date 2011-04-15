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

def prep_v(v):
    """
    v vektorune dik 2 vektoru doner
    [[x1, y1], [x2, y2]] seklinde
    """
    return [[v[1], -v[0]], [-v[1], v[0]]]

def norm_v(p1, p2):
    """
    p1'den p2'ye dogru birim vektor olusturur.
    normalized vector from p1 to p2
    """
    return Vector(p2[0]-p1[0], p2[1]-p1[1]).get_unit_vector()


SCREENX = 500
SCREENY = 500
LEN = 150
WHITE = (255, 255, 255) 
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

places = [[200, 200], [300, 300], [300, 300],[350, 350]]
vels = [[3, 3], [2, 0], [1, 0], [0, 1]]
time_passed = 0


screen = pygame.display.set_mode((SCREENX, SCREENY), 0, 32)
clock = pygame.time.Clock()

pos = SCREENX/2
running = 1
vectors = [[0, 0], [0, 0]]
r = [SCREENX/2-pos, -SCREENY/2-10+pos]
r = birim_vektorlestir(r)
vectors = prep_v(r)  # [[x1, y1], [x2, y2]]



font = pygame.font.SysFont('Consolas', 15)
p1t = font.render('m1', True, (0, 0, 0), WHITE)
p2t = font.render('m2', True, (0, 0, 0), WHITE)
p3t = font.render('m3', True, (0, 0, 0), WHITE)
p4t = font.render('m4', True, (0, 0, 0), WHITE)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
            running = False
        if event.type == pygame.MOUSEMOTION:
            r = [event.pos[0]-pos, -event.pos[1]+pos]
            #print r
            r = birim_vektorlestir(r)
            vectors = prep_v(r)  # [[x1, y1], [x2, y2]]
            #print  ">>",  r, "<<"  # [x, y]

    screen.fill((0, 0, 0))

    # yuzeylerin orta noktalari
    m1 = vectors[0][0]*LEN, vectors[0][1]*LEN
    m2 = vectors[1][0]*LEN, vectors[1][1]*LEN
    m3 = -r[0]*LEN, -r[1]*LEN
    m4 = r[0]*LEN, r[1]*LEN

    # kenarlarin ortalarindan merkeze birim vectors
    m1b = norm_v(m1, (0, 0))
    m2b = norm_v(m2, (0, 0))
    m3b = norm_v(m3, (0, 0))
    m4b = norm_v(m4, (0, 0))

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

    pygame.draw.aaline(screen, WHITE,
            p1, p2)
    pygame.draw.aaline(screen, WHITE,
            p2, p3)
    pygame.draw.aaline(screen, WHITE,
            p3, p4)
    pygame.draw.aaline(screen, WHITE,
            p4, p1)

    # toplar
    for p, vel in zip(places, vels):

        # uncomment this for gravity
        #vel[1] += time_passed*0.02

        if p[0] < 0:
            p[0] += SCREENX
        elif p[0] > SCREENX:
            p[0] -= SCREENX
        if p[1] < 0:
            p[1] += SCREENY
        elif p[1] > SCREENY:
            p[1] -= SCREENY
               
        # top pundan duvarin ortasina kadar olan vectors
        p_vektor = Vector(pyd(p))
        vm1 = p_vektor - Vector(m1)
        vm2 = p_vektor - Vector(m2)
        vm3 = p_vektor - Vector(m3)
        vm4 = p_vektor - Vector(m4)
        #print (vm1*vm1.dot_product(m1b)).length
        #print vm1
        if abs((m1b*vm1.dot_product(m1b)).length) < 5:
            v_vel = Vector((vel[0], -vel[1]))
            ref_v = v_vel - m1b*2*(v_vel.dot_product(m1b))
            vel[0] = ref_v[0]
            vel[1] = -ref_v[1]
        if abs((m2b*vm2.dot_product(m2b)).length) < 5:
            v_vel = Vector((vel[0], -vel[1]))
            ref_v = v_vel - m2b*2*(v_vel.dot_product(m2b))
            vel[0] = ref_v[0]
            vel[1] = -ref_v[1]
        if abs((m3b*vm3.dot_product(m3b)).length) < 5:
            v_vel = Vector((vel[0], -vel[1]))
            ref_v = v_vel - m3b*2*(v_vel.dot_product(m3b))
            vel[0] = ref_v[0]
            vel[1] = -ref_v[1]
        if abs((m4b*vm4.dot_product(m4b)).length) < 5:
            v_vel = Vector((vel[0], -vel[1]))
            ref_v = v_vel - m4b*2*(v_vel.dot_product(m4b))
            vel[0] = ref_v[0]
            vel[1] = -ref_v[1]
        p[0] += vel[0]
        p[1] += vel[1]
        #pygame.draw.circle(screen, WHITE, p, YARICAP)
        pygame.draw.circle(screen, WHITE, (int(p[0]), int(p[1])), YARICAP)


    time_passed = clock.tick(60)
    pygame.display.flip()
