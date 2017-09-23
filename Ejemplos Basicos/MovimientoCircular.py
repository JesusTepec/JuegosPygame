# -*- coding: utf-8 -*-
import pygame
import math

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)


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
    t = 0
    while juego_terminado is False:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_terminado = True
        t += 20
        if t >= 360:
            t = 0
        x = round(50 * math.cos(math.radians(t)) + 100)
        y = round(50 * math.sin(math.radians(t)) + 100)
        pantalla.fill(NEGRO)
        pygame.draw.circle(pantalla, AZUL, [100, 100], 2)
        pygame.draw.line(pantalla, VERDE, [100, 100], [150, 100])
        pygame.draw.circle(pantalla, ROJO, [x, y], 5)
        pygame.display.flip()
        reloj.tick(20)
    pygame.quit()


if __name__ == "__main__":
    main()