import pygame

NEGRO = (0, 0, 0)
AMARILLO = (255, 255, 0)
CIAN = (0, 255, 255)

pygame.init()

screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption("Get Pixeles")

screen.fill(NEGRO)
pygame.draw.rect(screen, AMARILLO, [10, 10, 140, 300], 0)
pygame.draw.rect(screen, CIAN, [150, 10, 140, 300], 0)

data_pixeles = pygame.PixelArray(screen)
for x in range(0, 100):
    for y in range(0, 100):
        data_pixeles[x][y] = (255, 0, 0)
del data_pixeles
pygame.display.update()

clock = pygame.time.Clock()
gameloop = False
while not gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = True

    clock.tick(60)

pygame.quit()