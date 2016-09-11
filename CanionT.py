# -*- coding: utf-8 -*-
import pygame
import math

BLANCO = (255, 255, 255)
MARRON = (108, 59, 42)
GRAFITO = (40, 40, 40)
NEGRO = (0, 0, 0)
AZUL = (127, 181, 181)

dimensiones = [400, 300]


def gToR(grados):
    #Converir grados a radianes (tambien se puede usar Math.radians)
    return (grados * math.pi) / 180


def dibujaCanion(pantalla, xy, angulo):
    x, y = xy
    CoordCanion = puntosCanion(xy, angulo, 30, 18)
    pygame.draw.circle(pantalla, MARRON, xy, 20)
    pygame.draw.rect(pantalla, NEGRO, [x - 30, y, 60, 40])
    pygame.draw.line(pantalla, GRAFITO, CoordCanion[0], CoordCanion[1], 6)
    return CoordCanion[0]


def puntosCanion(ab, angulo, radio1, radio2):
    puntos = []
    puntos.append(xyCircunferencia(angulo, ab, radio1))
    puntos.append(xyCircunferencia(angulo, ab, radio2))
    return puntos


def xyCircunferencia(t, centro, radio):
    t = math.radians(t)
    x = radio * math.cos(t) + centro[0]
    y = radio * math.sin(t) + centro[1]
    return [round(x), round(y)]


def main():
    pygame.init()
    pantalla = pygame.display.set_mode(dimensiones)
    pygame.display.set_caption("-------- Animación ------")
    juego_terminado = False
    reloj = pygame.time.Clock()
    a = 185
    av = 1
    xv = 1
    yv = 1
    disparo = False
    CoordCanion = puntosCanion([200, dimensiones[1] - 10], 290, 30, 18)
    x, y = CoordCanion[0]
    while juego_terminado is False:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_terminado = True
        a += av
        if a > 355 or a < 185:
            av *= -1
        pantalla.fill(AZUL)
        dibujaCanion(pantalla, [200, dimensiones[1] - 10], a)
        if a > 290:
            disparo = True

        if x > 395 or x < 5:
            xv *= -1
        if y > 295 or y < 5:
            yv *= -1
        if disparo:
            pygame.draw.circle(pantalla, (255, 0, 0), [x, y], 4)
            x += xv
            y -= yv
        pygame.display.flip()
        reloj.tick(20)
    pygame.quit()


if __name__ == "__main__":
    main()