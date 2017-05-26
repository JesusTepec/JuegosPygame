#-*-coding:utf8-*-
import pygame
import random

AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)


def main():
    dimensiones = (400, 500)
    pantalla = pygame.display.set_mode(dimensiones)
    pygame.display.set_caption("Mi primer juego en Python")

    reloj = pygame.time.Clock()
    game_over = False
    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
        pantalla.fill(AZUL)
        for i in range(2):
            x = random.randrange(1, dimensiones[1])
            pygame.draw.rect(pantalla, BLANCO, [x, 6, 10, 10], 0)
        pygame.display.flip()
        reloj.tick(50)
    pygame.quit()

#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
