import pygame
import random

NEGRO = (10, 8 ,12)
BLANCO = (255, 255, 255)
VERDE = (90, 232, 64)
ROJO = (255, 20, 20)
AZUL = (10, 222, 255)
COLOR_FUENTE = (255, 122, 88)

def dibujarTexto(screen, texto, pos):
    fuente = pygame.font.SysFont('Barber Street_PersonalUseOnly', 50)
    text = fuente.render(texto, 1, COLOR_FUENTE)
    screen.blit(text, pos)

def dibujarPista():
    pygame.draw.rect(pantalla, NEGRO, [160, 0, 160, dimensiones[1]])
    for i in range(10, dimensiones[1], 20):
        pygame.draw.rect(pantalla, BLANCO, [234, i, 6, 8])

def rectCollider(objeto1, objeto2):
    colisiono = False
    if (objeto2[0] + objeto2[2] > objeto1[0] and objeto2[0] < objeto1[0] + objeto1[2]):
        if(objeto2[1] + objeto2[3] > objeto1[1] and objeto2[1] < objeto1[1] + objeto1[3]):
            colisiono = True
    if (objeto2[0] < objeto1[0] and objeto2[0] + objeto2[2] > objeto1[0] + objeto1[2]):
        if (objeto2[1] < objeto1[1] and objeto2[1] + objeto2[3] > objeto1[1] + objeto1[3]):
            colisiono = True
    if (objeto1[0] < objeto2[0] and objeto1[0] + objeto1[2] > objeto2[0] + objeto2[2]):
        if (objeto1[1] < objeto2[1] and objeto1[1] + objeto1[3] > objeto2[1] + objeto2[3]):
            colisiono = True
    return colisiono

pygame.init()

dimensiones = [480, 720]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Animaciones")

autos = [[185, 0, 35, 50], [255, -180, 35, 50], [185, -340, 35, 50], [255, -490, 35, 50]]
auto = [185, 600, 40, 54]

x_speed = 0
y_speed = 0

velocidad = 4

game_over = False
salir = False
reloj = pygame.time.Clock()

while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
            salir = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                x_speed = -4
            if evento.key == pygame.K_RIGHT:
                x_speed = 4
            if evento.key == pygame.K_UP:
                y_speed = -4
            if evento.key == pygame.K_DOWN:
                y_speed = 4
        if evento.type == pygame.KEYUP:
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
    pygame.draw.rect(pantalla, AZUL, auto)
    if (auto[0] + 40) < 319 and auto[0] > 161:
        auto[0] += x_speed
    else:
        x_speed *= -1
        auto[0] = 162
    auto[1] += y_speed
    for autoObjeto in autos:
        game_over = rectCollider(auto, autoObjeto)
        if autoObjeto[1] > dimensiones[1]:
            autoObjeto[1] = random.randrange(-150, -100)
        pygame.draw.rect(pantalla, ROJO, autoObjeto)
        autoObjeto[1] += velocidad
    velocidad += 0.0005
    pygame.display.flip()
    reloj.tick(60)

if game_over == True:
    game_over = False
    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
        pantalla.fill(VERDE)
        dibujarPista()
        dibujarTexto(pantalla, "GAME OVER", [140, 400])
        pygame.display.flip()
        reloj.tick(60)
    pygame.quit()
