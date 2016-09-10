# -*- coding: utf-8 -*-
import pygame
import math

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
CUERPO = (60, 250, 40)
NEGRO = (0, 0, 0)

def gToR(grados):
    #Converir grados a radianes (tambien se puede usar Math)
    return (grados * math.pi) / 180


def dibujaAlien(pantalla, x, y):
    pygame.draw.polygon(pantalla, CUERPO, [[x, y], [x + 10, y],
        [x + 10, y + 10], [x + 20, y + 10], [x + 20, y + 20],
        [x + 30, y + 20], [x + 30, y + 10], [x + 40, y + 10],
        [x + 40, y], [x + 50, y], [x + 50, y + 10], [x + 40, y + 10],
        [x + 40, y + 20], [x + 50, y + 20], [x + 50, y + 30], [x + 60, y + 30],
        [x + 60, y + 40], [x + 70, y + 40], [x + 70, y + 80],
        [x + 60, y + 80], [x + 60, y + 50], [x + 50, y + 50], [x + 50, y + 80],
        [x + 30, y + 80], [x + 30, y + 70], [x + 40, y + 70], [x + 40, y + 60],
        [x + 10, y + 60], [x + 10, y + 70], [x + 20, y + 70], [x + 20, y + 80],
        [x, y + 80], [x, y + 50], [x - 10, y + 50], [x - 10, y + 80],
        [x - 20, y + 80], [x - 20, y + 40], [x - 10, y + 40], [x - 10, y + 30],
        [x, y + 30], [x, y + 20], [x + 10, y + 20], [x + 10, y + 10],
        [x, y + 10]])
    pygame.draw.rect(pantalla, NEGRO, [x + 10, y + 30, 10, 10])
    pygame.draw.rect(pantalla, NEGRO, [x + 30, y + 30, 10, 10])


def xyCircunferencia(t, centro, radio):
    x = radio * math.cos(t) + centro[0]
    y = radio * math.sin(t) + centro[1]
    return [round(x), round(y)]


def main():
    pygame.init()
    dimensiones = [500, 600]
    pantalla = pygame.display.set_mode(dimensiones)
    pygame.display.set_caption("-------- Animación ------")
    juego_terminado = False
    reloj = pygame.time.Clock()
    x = 10
    y = 10
    t = 0
    while juego_terminado is False:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_terminado = True
        t += 10
        if t >= 360:
            t = 0
        x, y = xyCircunferencia(math.radians(t), [200, 100], 90)
        pantalla.fill(NEGRO)
        dibujaAlien(pantalla, x, y)
        pygame.display.flip()
        reloj.tick(20)
    pygame.quit()


if __name__ == "__main__":
    main()