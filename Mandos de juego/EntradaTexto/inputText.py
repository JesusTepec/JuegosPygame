import pygame
from pygame.locals import *

COLOR_FONDO = (10, 4, 32)

pygame.init()
dimensiones = [600, 600]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Entrada de texto")
imagen_fondo = pygame.image.load("../img/panelInset_brown.png")


def dibujar_texto(screen, texto, fuente, pos):
    text = fuente.render(texto, 1, (255, 255, 255))
    screen.blit(text, pos)


def inputText():
    cerrar = False
    game_over = False
    clock = pygame.time.Clock()
    pos = [152, 18]
    texto = ""
    fondo = pygame.transform.scale(imagen_fondo, [360, 50])
    fuenteLabel = pygame.font.SysFont('Barber Street_PersonalUseOnly', 50)
    fuenteInput = pygame.font.SysFont('Pacifico Regular', 30)
    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
                cerrar = True
            if event.type == KEYDOWN:
                if (97 <= event.key <= 122) or event.key == 32:
                    caracter = chr(event.key)
                    texto += caracter
                if event.key == 8:
                    ultimo = len(texto) - 1
                    texto = texto[0:ultimo]
                if event.key == 13:
                    game_over = True

        pantalla.fill(COLOR_FONDO)
        dibujar_texto(pantalla, "Nombre:", fuenteLabel, [5, 20])
        pantalla.blit(fondo, [142, 20])
        dibujar_texto(pantalla, texto, fuenteInput, pos)
        pygame.display.flip()
        clock.tick(60)
    return [texto, cerrar]


def juego(nombre):
    game_over = False
    clock = pygame.time.Clock()
    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
        pantalla.fill(COLOR_FONDO)
        fuenteLabel = pygame.font.SysFont('Barber Street_PersonalUseOnly', 80)
        dibujar_texto(pantalla, "Hola " + nombre, fuenteLabel, [200, 200])
        pygame.display.flip()
        clock.tick(60)
    return game_over

def main():
    game_over = False
    clock = pygame.time.Clock()
    nombre = inputText()
    if not nombre[1]:
        while not game_over:
            for event in pygame.event.get():
                if event.type == QUIT:
                    break
            game_over = juego(nombre[0])
            clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
