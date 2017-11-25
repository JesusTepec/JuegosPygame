import pygame, time, random
from pygame.locals import *

NEGRO = (204, 192, 20)
ANCHOVENTANA = 800
ALTOVENTANA = 800
NUEVACOMIDA = 40

def cargarRecursos():
    recursos = []
    recursos.append(pygame.image.load('images/panda.png'))
    recursos.append(pygame.image.load('images/strawberry.png'))
    recursos.append(pygame.mixer.Sound('sound/comer.wav'))
    recursos.append(pygame.image.load('images/3317-fondo.jpg'))
    return recursos

def reproducirMusicaFondo():
    pygame.mixer.music.load('sound/Music/8BitMetal.wav')
    pygame.mixer.music.play(-1, 0.0)

pygame.init()
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))
pygame.display.set_caption('Sprites y Sonido')

relojPrincipal = pygame.time.Clock()
jugador = pygame.Rect(300, 100, 40, 40)
recursos = cargarRecursos()
imagenEstiradaJugador = pygame.transform.scale(recursos[0], (40, 40))

comidas = []
for i in range(20):
    comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - 20), random.randint(0, ALTOVENTANA - 20), 20, 20))

contadorComida = 0

moverseIzquierda = False
moverseDerecha = False
moverseArriba = False
moverseAbajo = False

VELOCIDADMOVIMIENTO = 6

reproducirMusicaFondo()
músicaSonando = True

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == KEYDOWN:
            if evento.key == K_LEFT or evento.key == ord('a'):
                moverseDerecha = False
                moverseIzquierda = True
            if evento.key == K_RIGHT or evento.key == ord('d'):
                moverseIzquierda = False
                moverseDerecha = True
            if evento.key == K_UP or evento.key == ord('w'):
                moverseAbajo = False
                moverseArriba = True
            if evento.key == K_DOWN or evento.key == ord('s'):
                moverseArriba = False
                moverseAbajo = True
        if evento.type == KEYUP:
            if evento.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if evento.key == K_LEFT or evento.key == ord('a'):
                moverseIzquierda = False
            if evento.key == K_RIGHT or evento.key == ord('d'):
                moverseDerecha = False
            if evento.key == K_UP or evento.key == ord('w'):
                moverseArriba = False
            if evento.key == K_DOWN or evento.key == ord('s'):
                moverseAbajo = False
            if evento.key == ord('x'):
                jugador.top = random.randint(0, ALTOVENTANA - jugador.height)
                jugador.left = random.randint(0, ANCHOVENTANA - jugador.width)
            if evento.key == ord('m'):
                if músicaSonando:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                músicaSonando = not músicaSonando

        if evento.type == MOUSEBUTTONUP:
            comidas.append(pygame.Rect(evento.pos[0] - 10, evento.pos[1] - 10, 20, 20))

    contadorComida += 1
    if contadorComida >= NUEVACOMIDA:
        # agregar nueva comida
        contadorComida = 0
        comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - 20), random.randint(0, ALTOVENTANA - 20), 20, 20))

    superficieVentana.fill(NEGRO)
    superficieVentana.blit(recursos[3], [10, 100])

    if moverseAbajo and jugador.bottom < ALTOVENTANA:
        jugador.top += VELOCIDADMOVIMIENTO
    if moverseArriba and jugador.top > 0:
        jugador.top -= VELOCIDADMOVIMIENTO
    if moverseIzquierda and jugador.left > 0:
        jugador.left -= VELOCIDADMOVIMIENTO
    if moverseDerecha and jugador.right < ANCHOVENTANA:
        jugador.right += VELOCIDADMOVIMIENTO

    superficieVentana.blit(imagenEstiradaJugador, jugador)
    for comida in comidas[:]:
        if jugador.colliderect(comida):
            comidas.remove(comida)
            jugador = pygame.Rect(jugador.left, jugador.top, jugador.width + 2, jugador.height + 2)
            imagenEstiradaJugador = pygame.transform.scale(recursos[0], (jugador.width, jugador.height))
            if músicaSonando:
                recursos[2].play()

    for comida in comidas:
        superficieVentana.blit(recursos[1], comida)

    pygame.display.update()
    relojPrincipal.tick(40)
