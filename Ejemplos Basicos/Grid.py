#Grid on Pygame
import pygame

AZUL = (255, 255, 255)
BLACK = (0, 0, 0)
tamCuadro = 100

pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Grid on PYGAME")
clock = pygame.time.Clock()
gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    screen.fill(BLACK)
    for i in range(1, size[0], tamCuadro + 1):
        for j in range(1, size[1], tamCuadro + 1):
            pygame.draw.rect(screen, AZUL, [i, j, tamCuadro , tamCuadro], 0)
    pygame.display.flip()
    clock.tick(5)
pygame.quit()
