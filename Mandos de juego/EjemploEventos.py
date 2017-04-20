import pygame

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)


def drawBall(pantalla, xy, color):
    pygame.draw.circle(pantalla, color, xy, 20)


def dibujaHombrePalitos(pantalla, x, y):
    '''Funcion que dibuja un hombre de palitos'''
    pygame.draw.ellipse(pantalla, NEGRO, [1 + x, y, 10, 10], 0)
    pygame.draw.line(pantalla, NEGRO, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(pantalla, NEGRO, [5 + x, 17 + y], [x, 27 + y], 2)
    pygame.draw.line(pantalla, ROJO, [5 + x, 17 + y], [5 + x, 7 + y], 2)
    pygame.draw.line(pantalla, ROJO, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(pantalla, ROJO, [5 + x, 7 + y], [1 + x, 17 + y], 2)


def main():
    pygame.init()
    pantalla = pygame.display.set_mode([400, 300])
    pygame.display.set_caption("mov ball")
    gameOver = False

    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while not gameOver:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                gameOver = True

        pos = pygame.mouse.get_pos()

        pantalla.fill(BLANCO)
        dibujaHombrePalitos(pantalla, pos[0], pos[1])
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()