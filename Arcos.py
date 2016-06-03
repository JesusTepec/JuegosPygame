import pygame
import math

pygame.init()

pantalla = pygame.display.set_mode([400, 500])
pygame.display.set_caption("Arcos")

reloj = pygame.time.Clock()
game_over = False

while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
    pantalla.fill([255, 255, 255])
    pygame.draw.rect(pantalla, (0, 0, 0), [10, 10, 200, 200], 2)
    pygame.draw.arc(pantalla, (0, 0, 0), [10, 10, 200, 200], 0, math.pi, 4)
    pygame.draw.arc(pantalla, (0, 150, 0), [10, 10, 200, 200], math.pi, 2 * math.pi, 4)
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()