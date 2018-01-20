import pygame
import random

COLOR_FONDO = (10, 4, 32)
COLORES_CELULAS = [(70, 12, 46), (4, 66, 36)]

pygame.init()

dimensiones = [1000, 800]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Cell drag")


def coordsAleatorias():
    x = random.randrange(15, dimensiones[0] -15)
    y = random.randrange(15, dimensiones[1] -15)
    return [x, y]


def colorAleatorio():
    r = random.randrange(155)
    g = random.randrange(55)
    b = random.randrange(75)
    return (r, g, b)


def dibujarCelula(centro, radio, color):
    pygame.draw.circle(pantalla, color[0], centro, radio, 0)
    pygame.draw.circle(pantalla, color[1], centro, radio, 1)


def crearCelulas(cantidad, centro):
    lista_celulas = []
    for i in range(0, cantidad):
        lista_celulas.append( [[centro[0], centro[1]], random.randrange(4, 12), [random.randrange(-4, 4, 2), random.randrange(-4, 4, 2)], [colorAleatorio(), colorAleatorio()]])
    return lista_celulas


def main():
    game_over = False
    clock = pygame.time.Clock()
    centro = [100, 100]
    objetivo = [200, 300]
    avance = [1, 1]
    lista_celulas = []
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    objetivo = event.pos
                    if objetivo[0] - centro[0] < 0:
                        avance[0] = -1
                    elif objetivo[0] - centro[0] > 0:
                        avance[0] = 1
                    if objetivo[1] - centro[1] < 0:
                        avance[1] = -1
                    elif objetivo[1] - centro[1] > 0:
                        avance[1] = 1
                if event.button == 3:
                    lista_celulas = crearCelulas(10, [centro[0], centro[1]])

        pantalla.fill(COLOR_FONDO)
        dibujarCelula(centro, 30, COLORES_CELULAS)

        if abs(objetivo[0] - centro[0]) != 0:
            centro[0] += avance[0]
        if abs(objetivo[1] - centro[1]) != 0:
            centro[1] += avance[1]

        for cell in lista_celulas:
            dibujarCelula(cell[0], cell[1], cell[3])
            cell[0][0] += cell[2][0]
            cell[0][1] += cell[2][1]

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main()
