
import pygame
import random
from pygame.locals import *

ventana = {'ancho': 500, 'alto': 600}
COLOR_FUENTE = (250, 240, 40)
COLOR_FONDO = (13, 140, 255)
FPS = 40
enemigo = {'sizeMin': 10, 'sizeMax': 40, 'velocidadMin': 1, 'velocidadMax': 4}

TASAMOVIMIENTOJUGADOR = 5


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


def pantallaInicial(superficie, titulo, mensaje):
    superficie.fill(COLOR_FONDO)
    pygame.draw.rect(superficie, [8, 5, 30], [0, ventana['ancho'] / 2 - 90, ventana['ancho'], 190])
    fuente = pygame.font.SysFont('Dimitri Swank', 48)
    x = 24 * len(titulo)
    dibujarTexto(titulo, fuente, superficie, (ventana['ancho'] - x) / 2, (ventana['alto'] / 3))
    fuente = pygame.font.SysFont('Quesha', 46)
    dibujarTexto(mensaje, fuente, superficie, (ventana['ancho'] / 2) - 170, (ventana['alto'] / 3) + 100)
    pygame.display.flip()


def dibujar_tablero(puntaje, nivel, puntaje_maximo, fuente_puntos):
    pygame.draw.rect(superficie, [8, 5, 30], [0, 0, ventana['ancho'], 90])
    dibujarTexto('Nivel: %s' % (nivel), fuente_puntos, superficie, 10, 2)
    dibujarTexto('Puntaje: %s' % (puntaje), fuente_puntos, superficie, 10, 30)
    dibujarTexto('Puntaje Máximo: %s' % (puntaje_maximo), fuente_puntos, superficie, 10, 60)


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
    pygame.mixer.music.load('copycat.wav')
    sonido_juego_terminado = pygame.mixer.Sound('soundLose.ogg')
    imagen_enemigo = pygame.image.load('snake.png')
    imagen_jugador = pygame.image.load('parrot.png')

    rectangulo_jugador = imagen_jugador.get_rect()
    rectangulo_jugador.topleft = (ventana['ancho'] / 2, ventana['alto'] - rectangulo_jugador[3] - 6)

    contador_agregar_enemigo = 0
    mover = {'arriba': [0, -5], 'abajo':[0, 5], 'izquierda': [-5, 0], 'derecha': [5, 0]}
    direccion_movimeinto = "FALSE"
    enemigos = []
    file = open("puntuacion.txt", "+r")
    puntaje = 0
    nivel = 1
    puntaje_maximo = file.read()
    numero_enemigos = 40
    ultimo_puntaje = 0
    del file
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    game_over = False
    close = False

    reloj = pygame.time.Clock()
    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
                close = True
            if evento.type == KEYDOWN:
                direccion_movimeinto = detecta_direccion(evento)
            if evento.type == KEYUP:
                direccion_movimeinto = "FALSE"
        contador_agregar_enemigo += 1
        if contador_agregar_enemigo == numero_enemigos:
            contador_agregar_enemigo = 0
            enemigos.append(nuevoEnemigo(imagen_enemigo))

        if direccion_movimeinto == "izquierda" and rectangulo_jugador.left > 0:
            rectangulo_jugador.move_ip(mover[direccion_movimeinto][0], mover[direccion_movimeinto][1])
        if direccion_movimeinto == "derecha" and rectangulo_jugador.right < ventana['ancho']:
            rectangulo_jugador.move_ip(mover[direccion_movimeinto][0], mover[direccion_movimeinto][1])
        if direccion_movimeinto == "arriba" and rectangulo_jugador.top > 90:
            rectangulo_jugador.move_ip(mover[direccion_movimeinto][0], mover[direccion_movimeinto][1])
        if direccion_movimeinto == "abajo" and rectangulo_jugador.bottom < ventana['alto']:
            rectangulo_jugador.move_ip(mover[direccion_movimeinto][0], mover[direccion_movimeinto][1])

        for e in enemigos:
            e['rect'].move_ip(0, e['velocidad'])

        if colision(rectangulo_jugador, enemigos):
            if puntaje > int(puntaje_maximo):
                file = open('puntuacion.txt', "w")
                puntaje_maximo = puntaje
                file.write(str(puntaje_maximo))
                del file
            game_over = True
            sonido_juego_terminado.play()
            pygame.mixer.music.stop()

        if puntaje != 0 and (puntaje % 50) == 0 and puntaje != ultimo_puntaje:
            nivel += 1
            ultimo_puntaje = puntaje
            numero_enemigos -= nivel

        superficie.fill(COLOR_FONDO)

        dibujar_tablero(puntaje, nivel, puntaje_maximo, fuente_puntos)
        superficie.blit(imagen_jugador, rectangulo_jugador)

        for e in enemigos[:]:
            if e['rect'].top > ventana['alto']:
                enemigos.remove(e)
                puntaje += 1
        for e in enemigos:
            superficie.blit(e['superficie'], e['rect'])

        pygame.display.flip()
        reloj.tick(60)
    return close


if __name__ == "__main__":
    pygame.init()
    superficie = pygame.display.set_mode((ventana['ancho'], ventana['alto']))
    pygame.display.set_caption('Evasor')
    fuente_puntos = pygame.font.SysFont('Impact', 20)
    reloj = pygame.time.Clock()
    game_loop = False
    salir = False

    pantallaInicial(superficie, "Evasor", 'Presione a para comenzar.')
    while not game_loop:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                game_loop = True
            if evento.type == KEYDOWN:
                if evento.key == ord('a'):
                    salir = main()
                    if salir:
                        game_loop = True
                    else:
                        pantallaInicial(superficie, "Game Over", 'Presione a para comenzar.')
        reloj.tick(60)
    pygame.quit()

'''
https://www.gamedeveloperstudio.com/ - Game Developer Studio
https://freesound.org -level failed
https://opengameart.org/content/copycat syncopika
'''
