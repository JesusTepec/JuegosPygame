import pygame
import modulos.Roca
import random

COLOR_ROCA_NORMAL = (125, 124, 105)
FONDO = (255, 224, 135)
pygame.init()

pantalla_largo = 700
pantalla_alto = 400
pantalla = pygame.display.set_mode([pantalla_largo,pantalla_alto])

listaRocas = pygame.sprite.Group()
sprites = pygame.sprite.Group()

listaRocas.add(modulos.Roca.Roca(COLOR_ROCA_NORMAL, 50, 120));

game_over = False
reloj = pygame.time.Clock()

while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True

    pantalla.fill(FONDO)

    listaRocas.draw(pantalla)

    reloj.tick(60)
    pygame.display.flip()

pygame.quit()
