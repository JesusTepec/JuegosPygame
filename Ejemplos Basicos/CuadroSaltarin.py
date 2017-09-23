#autor: Jesús Tepec
import pygame

# Constantes
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

pygame.init()

# Configuraciones
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Animaciones")

#Variables
hecho = False
rect_x = 10
rect_y = 10
rect_mov_x = 2
rect_mov_y = 2
ancho = 50
# Se usa para establecer cuan rápido se actualiza la pantalla

reloj = pygame.time.Clock()

# -------- Bucle principal del Programa -----------
while not hecho:
    # ---EVENTOS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
    if(rect_y > dimensiones[1] - ancho or rect_y < 0):
        rect_mov_y = rect_mov_y * -1
    if(rect_x > dimensiones[0] - ancho or rect_x < 0):
        rect_mov_x = rect_mov_x * -1
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, AZUL, [rect_x, rect_y, ancho, ancho])
    pygame.draw.circle(pantalla, NEGRO, (rect_x + 10, rect_y + 10), 5, 0)
    pygame.draw.circle(pantalla, NEGRO, (rect_x - 10 + ancho, rect_y + 10), 5, 0)
    pygame.draw.circle(pantalla, (255, 0, 0), (rect_x + 25, rect_y + 25), 5, 0)
    rect_x += rect_mov_x
    rect_y += rect_mov_y
    pygame.display.flip()

    reloj.tick(60)

pygame.quit()