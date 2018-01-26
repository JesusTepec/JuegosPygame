import pygame
import random

COLOR_FONDO = (10, 4, 32)
COLORES_CELULA = [(70, 12, 46), (4, 66, 36)]

pygame.init()

dimensiones = [1000, 800]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Cell Mov")

def colorAleatorio():
    r = random.randrange(155)
    g = random.randrange(55)
    b = random.randrange(75)
    return (r, g, b)

def dibujarCelula(centro, radio, color):
    pygame.draw.circle(pantalla, color[0], centro, radio, 0)
    pygame.draw.circle(pantalla, color[1], centro, radio, 1)

def main():
    game_over = False
    clock = pygame.time.Clock()
    centro = [100, 100]
    press = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    press = True
                if event.button == 3:
                    COLORES_CELULA[0] = colorAleatorio()
                    COLORES_CELULA[1] = colorAleatorio()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    press = False            

        pantalla.fill(COLOR_FONDO)

        if press:
            pos = pygame.mouse.get_pos()
            dibujarCelula(pos, 60, COLORES_CELULA)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main()
