#Ejemplo 3 - Tablero
import pygame

# Definir Colores
COLOR = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AMARILLO = (255, 255, 0)

pygame.init()

# Establecemos las dimensiones de la pantalla [largo,altura]
dimenciones = [400, 400]
pantalla = pygame.display.set_mode(dimenciones)
pygame.display.set_caption("TABLERO")  # Titulo

#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.
juego_terminado = False

# Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
color = 0
# -------- Bucle principal del Programa -----------
while juego_terminado is False:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():  # El usuario realizó alguna acción
        if evento.type == pygame.QUIT:  # Si el usuario hizo click sobre salir
            juego_terminado = True
            # Marcamos que hemos acabado y abandonamos este bucle

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ

    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
    pantalla.fill(BLANCO)
    color = 0
    for i in range(0, dimenciones[0], 50):
        for j in range(0, dimenciones[1], 50):
            if color % 2 == 0:
                pygame.draw.rect(pantalla, NEGRO, [i, j, 50, 50], 0)
            else:
                pygame.draw.rect(pantalla, BLANCO, [i, j, 50, 50], 0)
            color += 1
        color += 1
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(5)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'ciclará'
pygame.quit()
