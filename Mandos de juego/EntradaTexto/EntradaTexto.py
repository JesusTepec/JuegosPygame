import pygame
from pygame.locals import *

COLOR_FONDO = (10, 4, 32)

pygame.init()
dimensiones = [600, 600]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Entrada de texto")
imagen_fondo = pygame.image.load("../img/panelInset_brown.png")


def dibujar_texto(screen, texto, pos):
    fuente = pygame.font.SysFont('Barber Street_PersonalUseOnly', 50)
    #fuente = pygame.font.SysFont('HelloChristmas', 50)
    #fuente = pygame.font.SysFont('Pacifico Regular', 50)
    #fuente = pygame.font.SysFont('Amazing Kids', 40)
    text = fuente.render(texto, 1, (255, 255, 255))
    screen.blit(text, pos)


def main():
    game_over = False
    clock = pygame.time.Clock()
    pos = [30, 30]
    lineas = [{'texto': "", 'pos': [30, 30]}]
    liena_actual = 0
    fondo = pygame.transform.scale(imagen_fondo, [390, 390])
    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
            if event.type == KEYDOWN:
                if (97 <= event.key <= 122) or event.key == 32:
                    caracter = chr(event.key)
                    lineas[liena_actual]['texto'] += caracter
                if event.key == 8:
                    ultimo = len(lineas[liena_actual]['texto']) - 1
                    lineas[liena_actual]['texto'] = lineas[liena_actual]['texto'][0:ultimo]
                if event.key == 13:
                    pos[1] = pos[1] + 40
                    lineas.append({'texto': "", 'pos': [pos[0], pos[1]]})
                    liena_actual += 1
                print(event.key)

        pantalla.fill(COLOR_FONDO)
        pantalla.blit(fondo, [5, 5])
        for linea in lineas:
            dibujar_texto(pantalla, linea['texto'], linea['pos'])
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
