import pygame

pygame.init()

pantalla = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Mueve figura")
reloj = pygame.time.Clock()
game_over = False

x_coord = 100
y_coord = 100
x_speed = 2
y_speed = 2
while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True

        # El usuario pulsa una tecla
        if evento.type == pygame.KEYDOWN:
            # Resuelve que ha sido una tecla de direccion, por lo que
            # ajusta la velocidad.
            if evento.key == pygame.K_LEFT:
                x_speed = -3
            if evento.key == pygame.K_RIGHT:
                x_speed = 3
            if evento.key == pygame.K_UP:
                y_speed = -3
            if evento.key == pygame.K_DOWN:
                y_speed = 3

        # El usuario suelta la tecla
        if evento.type == pygame.KEYUP:
            # Si se trata de una tecla de direccion, devuelve el vector a cero
            if evento.key == pygame.K_LEFT:
                x_speed = 0
            if evento.key == pygame.K_RIGHT:
                x_speed = 0
            if evento.key == pygame.K_UP:
                y_speed = 0
            if evento.key == pygame.K_DOWN:
                y_speed = 0

    # Mueve el objeto de acuerdo a la velocidad del vector.
    x_coord += x_speed
    y_coord += y_speed
    pantalla.fill((255, 255, 255))
    pygame.draw.rect(pantalla, (0, 0, 255), [x_coord, y_coord, 20, 40], 0)
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()