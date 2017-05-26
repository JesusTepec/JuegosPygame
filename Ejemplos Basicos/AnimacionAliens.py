# -*- coding: utf-8 -*-
import pygame
import math

ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)
CUERPO = (60, 250, 40)
NEGRO = (0, 0, 0)


def gToR(grados):
    #Converir grados a radianes (tambien se puede usar Math.radians)
    return (grados * math.pi) / 180


def xyCircunferencia(t, centro, radio):
    x = radio * math.cos(t) + centro[0]
    y = radio * math.sin(t) + centro[1]
    return [round(x), round(y)]


def dibujaNave(pantalla, x, y):
    pygame.draw.rect(pantalla, ROJO, [x - 15, y + 40, 10, 10])
    pygame.draw.rect(pantalla, ROJO, [x + 6, y + 40, 10, 10])
    pygame.draw.polygon(pantalla, BLANCO, [[x - 20, y + 40],
         [x, y], [x + 20, y + 40]])


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
    pos = [101, 500]
    posNave = [100, 500, 1]
    while juego_terminado is False:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_terminado = True
        x, y = xyCircunferencia(gToR(t), [150, 120], 50)
        t += 1
        if(pos[1] <= 0):
            pos[1] = 500
            pos[0] = posNave[0]
        pos[1] -= 2

        if posNave[0] > dimensiones[0] - 100 or posNave[0] < 100:
            posNave[2] *= -1
        posNave[0] += posNave[2]
        pantalla.fill(NEGRO)
        dibujaNave(pantalla, posNave[0], posNave[1])
        pygame.draw.circle(pantalla, ROJO, pos, 5)
        dibujaAlien(pantalla, x, y)
        dibujaAlien(pantalla, x + 100, y)
        dibujaAlien(pantalla, x + 200, y)
        dibujaAlien(pantalla, x + 300, y)
        pygame.display.flip()
        reloj.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()