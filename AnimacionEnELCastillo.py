#Introducción a los grafico en python
#Dibujando escenario
#autor: Jesús Tepec

import pygame
import random

AZULNOCHE = (9, 35, 67)
VERDEPASTO = (17, 99, 67)
VERDE = (10, 255, 10)
BLANCO = (222, 224, 200)
GRIS = (186, 186, 177)
GrisCastillo = (158, 158, 158)
NEGRO = (2, 3, 3)
ROJO = (255, 0, 0)
CAFE = (90, 50, 15)
TRUENO = (19, 45, 77)

Dimensiones = (500, 600)


def dibujar_castillo(pantalla, pos):
    for x in range(0, 70, 20):
        pygame.draw.rect(pantalla, GrisCastillo, [290 + x, 220, 10, 10])
        pygame.draw.rect(pantalla, NEGRO, [290 + x, 220, 10, 10], 1)
    pygame.draw.rect(pantalla, GrisCastillo, [250, 200, 40, 105], 0)
    pygame.draw.rect(pantalla, NEGRO, [250, 200, 40, 105], 2)
    pygame.draw.rect(pantalla, NEGRO, [262, 210, 16, 16], 0)
    pygame.draw.rect(pantalla, GrisCastillo, [290, 230, 70, 75], 0)
    pygame.draw.rect(pantalla, NEGRO, [290, 230, 70, 75], 2)
    pygame.draw.rect(pantalla, GrisCastillo, [360, 200, 40, 105], 0)
    pygame.draw.rect(pantalla, NEGRO, [360, 200, 40, 105], 2)
    pygame.draw.rect(pantalla, NEGRO, [372, 210, 16, 16], 0)
    pygame.draw.polygon(pantalla, NEGRO, [[248, 200], [270, 178], [292, 200]])
    pygame.draw.polygon(pantalla, NEGRO, [[358, 200], [380, 178], [402, 200]])
    pygame.draw.circle(pantalla, CAFE, [325, 270], 15, 0)
    pygame.draw.circle(pantalla, NEGRO, [325, 270], 15, 2)
    pygame.draw.rect(pantalla, CAFE, [310, 270, 30, 30], 0)
    pygame.draw.rect(pantalla, NEGRO, [310, 270, 30, 30], 1)
    pygame.draw.circle(pantalla, CAFE, [325, 270], 13, 0)


def dibujar_fondo(pantalla, pos):
    ancho = Dimensiones[0]
    alto = Dimensiones[1]
    h1 = Dimensiones[1] / 2 + 50
    h2 = Dimensiones[1] / 2 - 50
    pygame.draw.rect(pantalla, AZULNOCHE, [0, 0, ancho, h1], 0)
    pygame.draw.rect(pantalla, VERDEPASTO, [0, h2 + 100, ancho, h2], 0)
    for y in range(int(h2) + 100, alto, 7):
        for x in range(0, ancho, 4):
            pygame.draw.line(pantalla, VERDE, [x, y + 5], [x + 2, y], 1)


def dibujar_luna(pantalla, pos):
    x = pos[0]
    y = pos[1]
    pygame.draw.circle(pantalla, BLANCO, pos, 20, 0)  # grande
    pygame.draw.circle(pantalla, GRIS, [x - 10, y - 10], 4, 1)
    pygame.draw.circle(pantalla, GRIS, [x + 11, y - 1], 3, 1)
    pygame.draw.circle(pantalla, GRIS, [x - 1, y + 10], 5, 1)


def dibujar_lluvia(pantalla, limites, listaPuntos):

        for i in range(len(listaPuntos)):
            r = listaPuntos[i][2]
            x = listaPuntos[i][0]
            y = listaPuntos[i][1]
            pygame.draw.circle(pantalla, BLANCO, [x, y], r, 0)
            listaPuntos[i][1] += 1
            if listaPuntos[i][1] > limites[1]:
                y = random.randrange(-50, -10)
                listaPuntos[i][1] = y
                x = random.randrange(50, limites[0])
                listaPuntos[i][0] = x


def crearPuntosAletorios(cantidad, rangos):
    listaPuntos = []
    for i in range(cantidad):
        radio = 1
        x = random.randrange(1, 390)
        y = random.randrange(0, 300)
        listaPuntos.append([x, y, radio])
    return listaPuntos


def dibujarTexto(pantalla, texto, color):
    Fuente = pygame.font.Font('AliceandtheWickedMonster.ttf', 25)
    Texto = Fuente.render(texto, True, color)
    pantalla.blit(Texto, [250, 10])


def main():
    pygame.init()
    pantalla = pygame.display.set_mode(Dimensiones)
    pygame.display.set_caption("Dark castle----")

    game_over = False
    reloj = pygame.time.Clock()

    listaPuntos = crearPuntosAletorios(15, [390, 200])

    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
        pantalla.fill((255, 255, 255))
        #---Fondo------
        dibujar_fondo(pantalla, [0, 0])
        #---Luna-------
        dibujar_luna(pantalla, [25, 25])
        #---Luvia------
        dibujar_lluvia(pantalla, [390, 300], listaPuntos)
        #---Castillo---
        dibujar_castillo(pantalla, [400, 300])

        pygame.display.flip()
        reloj.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()