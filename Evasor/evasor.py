
import pygame
import random
from pygame.locals import *

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


def colision(rectanguloJugador, villanos):
    for v in villanos:
        if rectanguloJugador.colliderect(v['rect']):
            return True
    return False


def detecta_direccion(evento):
    direccion = "FALSE"
    if evento.key == K_LEFT:
        direccion = "izquierda"
    if evento.key == K_RIGHT:
        direccion = "derecha"
    if evento.key == K_UP:
        direccion = "arriba"
    if evento.key == K_DOWN:
        direccion = "abajo"
    return direccion

def main():
    pygame.mixer.music.load('acrostics.wav')
    sonidoJuegoTerminado = pygame.mixer.Sound('juegoterminado.wav')
    imagenEnemigo = pygame.image.load('snake.png')
    imagenJugador = pygame.image.load('parrot.png')

    rectanguloJugador = imagenJugador.get_rect()
    rectanguloJugador.topleft = (ventana['ancho'] / 2, ventana['alto'] - rectanguloJugador[3] - 6)

    trucoReversa = trucoLento = False
    contador_agregar_enemigo = 0
    mover = {'arriba': [0, -5], 'abajo':[0, 5], 'izquierda': [-5, 0], 'derecha': [5, 0]}
    direccion_movimeinto = "FALSE"
    enemigos = []
    file = open("puntuacion.txt", "+r")
    puntaje = 0
    puntaje_maximo = file.read()
    del file
    game_over = False
    juego_inicia = False
    salir = False

    reloj = pygame.time.Clock()
    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
                salir = True
            if evento.type == KEYDOWN:
                if not juego_inicia:
                    juego_inicia = True
                    pygame.mixer.music.play()
                direccion_movimeinto = detecta_direccion(evento)
            if evento.type == KEYUP:
                direccion_movimeinto = "FALSE"
        if not juego_inicia:
            pantallaInicial(superficie)
        else:
            # ---------------- PINCIPAL -------------------
            if not trucoReversa and not trucoLento:
                contador_agregar_enemigo += 1
            if contador_agregar_enemigo == TASANUEVOENEMIGO:
                contador_agregar_enemigo = 0
                enemigos.append(nuevoEnemigo(imagenEnemigo))

            if direccion_movimeinto == "izquierda" and rectanguloJugador.left > 0:
                rectanguloJugador.move_ip(mover[direccion_movimeinto][0], mover[direccion_movimeinto][1])
            if direccion_movimeinto == "derecha" and rectanguloJugador.right < ventana['ancho']:
                rectanguloJugador.move_ip(mover[direccion_movimeinto][0], mover[direccion_movimeinto][1])
            if direccion_movimeinto == "arriba" and rectanguloJugador.top > 0:
                rectanguloJugador.move_ip(mover[direccion_movimeinto][0], mover[direccion_movimeinto][1])
            if direccion_movimeinto == "abajo" and rectanguloJugador.bottom < ventana['alto']:
                rectanguloJugador.move_ip(mover[direccion_movimeinto][0], mover[direccion_movimeinto][1])

            for e in enemigos:
                if not trucoReversa and not trucoLento:
                    e['rect'].move_ip(0, e['velocidad'])
                elif trucoReversa:
                    e['rect'].move_ip(0, -5)
                elif trucoLento:
                    e['rect'].move_ip(0, 1)

            if colision(rectanguloJugador, enemigos):
                if puntaje > int(puntaje_maximo):
                    file = open('puntuacion.txt', "w")
                    puntaje_maximo = puntaje
                    file.write(str(puntaje_maximo))
                    del file
                game_over = True
                sonidoJuegoTerminado.play()
                pygame.mixer.music.stop()

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
    return salir

if __name__ == "__main__":
    pygame.init()
    superficie = pygame.display.set_mode((ventana['ancho'], ventana['alto']))
    pygame.display.set_caption('Evasor')
    fuente_puntos = pygame.font.SysFont('Impact', 20)
    game_loop = False
    salir = main()
    if not salir:
        superficie.fill(COLOR_FONDO)
        pygame.draw.rect(superficie, [8, 5, 30], [0, ventana['ancho'] / 2 - 90, ventana['ancho'], 190])
        fuente = pygame.font.SysFont('Dimitri Swank', 48)
        dibujarTexto('Evasor', fuente, superficie, (ventana['ancho'] / 2) - 80, (ventana['alto'] / 3))
        fuente = pygame.font.SysFont('Quesha', 46)
        dibujarTexto('GAME OVER', fuente, superficie, superficie.get_rect().centerx - 92, (ventana['alto'] / 3) + 90)
        pygame.display.flip()
        while not game_loop:
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    game_loop = True
    pygame.quit()

'''
https://www.gamedeveloperstudio.com/ - Game Developer Studio
https://freesound.org -level failed
https://opengameart.org/content/copycat syncopika
'''
