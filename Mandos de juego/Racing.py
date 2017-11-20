import pygame

NEGRO = (10, 8 ,12)
BLANCO = (255, 255, 255)
VERDE = (90, 232, 64)
ROJO = (255, 20, 20)
AZUL = (10, 222, 255)


def dibujarPista():
    pygame.draw.rect(pantalla, NEGRO, [160, 0, 160, 620])
    for i in range(10, 610, 20):
        pygame.draw.rect(pantalla, BLANCO, [234, i, 6, 8])

pygame.init()

dimensiones = [480, 620]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Animaciones")

autos = [[190, 0, 20, 25], [270, -160, 20, 25], [190, -360, 20, 25]]
auto = [190, 610, 20, 25]

x_speed = 0
y_speed = 0
mouse_pos = [200, 100]

hecho = False
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
    # El usuario pulsa una tecla
    if evento.type == pygame.KEYDOWN:
        # Resuelve que ha sido una tecla de flecha, por lo que
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
        # Si se trata de una tecla de flecha, devuelve el vector a cero
        if evento.key == pygame.K_LEFT:
            x_speed = 0
        if evento.key == pygame.K_RIGHT:
            x_speed = 0
        if evento.key == pygame.K_UP:
            y_speed = 0
        if evento.key == pygame.K_DOWN:
            y_speed = 0
    pantalla.fill(VERDE)
    dibujarPista()
    mouse_pos = pygame.mouse.get_pos()
    auto[0] += mouse_pos[0]
    auto[1] += mouse_pos[1]
    pygame.draw.rect(pantalla, ROJO, autos[0])
    pygame.draw.rect(pantalla, ROJO, autos[1])
    pygame.draw.rect(pantalla, AZUL, auto)
    autos[0][1] += 2
    autos[1][1] += 2
    pygame.display.flip()
    reloj.tick(20)

pygame.quit()
