
import pygame
import random

ventana = {'ancho': 500, 'alto': 600}
COLOR_FUENTE = (250, 240, 40)
COLOR_FONDO = (13, 140, 255)
FPS = 40
enemigo = {'sizeMin': 10, 'sizeMax': 40, 'velocidadMin': 1, 'velocidadMax': 8}

TASANUEVOENEMIGO = 12
TASAMOVIMIENTOJUGADOR = 5
puntaje_maximo = 0


def jugadorGolpeaEnemigo(rectanguloJugador, enemigos):
    for v in enemigos:
        if rectanguloJugador.colliderect(v['rect']):
            return True
    return False


def dibujarTexto(texto, fuente, superficie, x, y):
    objetotexto = fuente.render(texto, 1, COLOR_FUENTE)
    rectangulotexto = objetotexto.get_rect()
    rectangulotexto.topleft = (x, y)
    superficie.blit(objetotexto, rectangulotexto)


def pantallaInicial(superficie):
    superficie.fill(COLOR_FONDO)
    pygame.draw.rect(superficie, [8, 5, 30], [0, ventana['ancho'] / 2 - 90, ventana['ancho'], 190])
    fuente = pygame.font.SysFont('Dimitri Swank', 48)
    dibujarTexto('Evasor', fuente, superficie, (ventana['ancho'] / 2) - 80, (ventana['alto'] / 3))
    fuente = pygame.font.SysFont('Quesha', 46)
    dibujarTexto('Presione una tecla para comenzar.', fuente, superficie, (ventana['ancho'] / 2) - 220, (ventana['alto'] / 3) + 100)

def dibujar_tablero(puntaje, puntaje_maximo, fuente_puntos):
    pygame.draw.rect(superficie, [8, 5, 30], [0, 0, ventana['ancho'], 60])
    dibujarTexto('Puntaje: %s' % (puntaje), fuente_puntos, superficie, 10, 2)
    dibujarTexto('Puntaje Máximo: %s' % (puntaje_maximo), fuente_puntos, superficie, 10, 30)


def nuevoEnemigo(imagen_enemigo):
    size_enemigo = random.randint(enemigo['sizeMin'], enemigo['sizeMax'])
    x_rect = random.randint(0, ventana['ancho'] - size_enemigo)
    nuevo_enemigo = {
        'rect': pygame.Rect(x_rect, 0 - size_enemigo, size_enemigo, size_enemigo),
        'velocidad': random.randint(enemigo['velocidadMin'], enemigo['velocidadMax']),
        'superficie': pygame.transform.scale(imagen_enemigo, (size_enemigo, size_enemigo))}
    return nuevo_enemigo


def main():
    pygame.mixer.music.load('copycat.wav')
    imagenEnemigo = pygame.image.load('snake.png')
    imagenJugador = pygame.image.load('parrot.png')
    rectanguloJugador = imagenJugador.get_rect()
    rectanguloJugador.topleft = (ventana['ancho'] / 2, ventana['alto'] - rectanguloJugador[3])
    trucoReversa = trucoLento = False
    contadorAgregarEnemigo = 0
    reloj = pygame.time.Clock()
    game_over = False
    juego_inicia = False
    pantallaInicial(superficie)
    enemigos = []
    puntaje = 0
    fuente_puntos = pygame.font.SysFont('Impact', 20)

    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN and juego_inicia == False:
                juego_inicia = True
            #    pygame.mixer.music.play()
        if not juego_inicia:
            pantallaInicial(superficie)
        else:
            # ---------------- PINCIPAL -------------------
            if not trucoReversa and not trucoLento:
                contadorAgregarEnemigo += 1
            if contadorAgregarEnemigo == TASANUEVOENEMIGO:
                contadorAgregarEnemigo = 0
                enemigos.append(nuevoEnemigo(imagenEnemigo))
            for e in enemigos:
                if not trucoReversa and not trucoLento:
                    e['rect'].move_ip(0, e['velocidad'])
                elif trucoReversa:
                    e['rect'].move_ip(0, -5)
                elif trucoLento:
                    e['rect'].move_ip(0, 1)
            superficie.fill(COLOR_FONDO)

            dibujar_tablero(puntaje, puntaje_maximo, fuente_puntos)
            superficie.blit(imagenJugador, rectanguloJugador)

            for e in enemigos[:]:
                if e['rect'].top > ventana['alto']:
                    enemigos.remove(e)
                    puntaje += 1
            for e in enemigos:
                superficie.blit(e['superficie'], e['rect'])

        pygame.display.flip()
        reloj.tick(60)
        #end while gameloop
    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    superficie = pygame.display.set_mode((ventana['ancho'], ventana['alto']))
    pygame.display.set_caption('Evasor')
    main()

'''
https://www.gamedeveloperstudio.com/ - Game Developer Studio
https://freesound.org -level failed
https://opengameart.org/content/copycat syncopika
'''
