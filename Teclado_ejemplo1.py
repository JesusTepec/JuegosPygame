import pygame

pygame.init()

pantalla = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Mueve figura")
reloj = pygame.time.Clock()
game_over = False

x_coord = 100
y_coord = 0
y_speed = 0
while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                y_speed = 3
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_DOWN:
                y_speed = 0
    y_coord += y_speed
    pantalla.fill((255, 255, 255))
    pygame.draw.rect(pantalla, (0, 0, 255), [x_coord, y_coord, 20, 40], 0)
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()
