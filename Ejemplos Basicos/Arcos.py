import pygame
import math

ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

pygame.init()

pantalla = pygame.display.set_mode([400, 200])
pygame.display.set_caption("Arcos")

reloj = pygame.time.Clock()
game_over = False

while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
    pantalla.fill([255, 255, 255])
    pygame.draw.arc(pantalla, ROJO, [50, 10, 300, 300], 0, math.radians(180))
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()