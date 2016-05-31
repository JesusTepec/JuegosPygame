#___Ejemplo de Funciones___
import pygame

AZUL = (0, 0, 255)
AZULCIELO = (150, 200, 255)
ARENA = (255, 204, 154)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)


def dibujar_escena(dimensiones, pantalla):
    x = dimensiones[0]
    y = dimensiones[1]
    pygame.draw.rect(pantalla, AZUL, [0, (y / 2), x, (y / 2)], 0)
    pygame.draw.rect(pantalla, AZULCIELO, [0, 0, x, (y / 2)], 0)
    pygame.draw.rect(pantalla, ARENA, [0, y - 100, x, (y / 5)], 0)


def pelota(pantalla, pos, radio):
    x = pos[0]
    y = pos[1]
    p_r = 3
    pygame.draw.circle(pantalla, ROJO, pos, radio, 0)
    pygame.draw.circle(pantalla, BLANCO, [x + radio / 2, y + radio / 3], p_r, 0)
    pygame.draw.circle(pantalla, BLANCO, [x - radio / 4, y + radio / 5], p_r, 0)
    pygame.draw.circle(pantalla, BLANCO, [x, y], p_r, 0)
    pygame.draw.circle(pantalla, BLANCO, [x + radio / 3, y - radio / 4], p_r, 0)
    pygame.draw.circle(pantalla, BLANCO, [x + radio / 4, y - radio / 2], p_r, 0)


def palmera(pantalla, pos):
    cafe = (204, 102, 0)
    x = pos[0]
    y = pos[1]
    pygame.draw.rect(pantalla, cafe, [pos[0], pos[1] - 90, 10, 90], 0)
    pygame.draw.line(pantalla, VERDE, [x + 5, y - 90], [x - 20, y - 70], 5)
    pygame.draw.line(pantalla, VERDE, [x + 5, y - 90], [x - 30, y - 70], 5)
    pygame.draw.line(pantalla, VERDE, [x + 5, y - 90], [x - 10, y - 70], 5)
    pygame.draw.line(pantalla, VERDE, [x + 5, y - 90], [x - 0, y - 70], 5)
    pygame.draw.line(pantalla, VERDE, [x + 5, y - 90], [x + 10, y - 70], 5)
    pygame.draw.line(pantalla, VERDE, [x + 5, y - 90], [x + 20, y - 70], 5)
    pygame.draw.line(pantalla, VERDE, [x + 5, y - 90], [x + 30, y - 70], 5)
    pygame.draw.line(pantalla, VERDE, [x + 5, y - 90], [x + 40, y - 70], 5)
    pygame.draw.line(pantalla, VERDE, [x + 5, y - 90], [x - 40, y - 70], 5)
    pygame.draw.line(pantalla, VERDE, [x + 5, y - 90], [x - 50, y - 70], 5)
    pygame.draw.line(pantalla, VERDE, [x + 5, y - 90], [x + 50, y - 70], 5)


def main():
    dimensiones = (400, 500)
    pantalla = pygame.display.set_mode(dimensiones)
    pygame.display.set_caption("Ejemplo 2")
    reloj = pygame.time.Clock()
    game_over = False
    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
        pantalla.fill(AZUL)
        dibujar_escena(dimensiones, pantalla)
        palmera(pantalla, [40, dimensiones[1] - 20])
        pelota(pantalla, [40, 200], 20)
        pygame.display.flip()
        reloj.tick(50)
    pygame.quit()

#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()