#Ejemplo 1 - circulo cae
import pygame

# Definir Colores
COLOR = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AMARILLO = (255, 255, 0)

pygame.init()

# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Mi Primer juego en pygame")  # Titulo

#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.
juego_terminado = False

# Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
y = 0
x = 0
v_x = 1

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
    pygame.draw.circle(pantalla, ROJO, [x, y], 10, 0)
    y += 1
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(50)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'ciclará'
pygame.quit()
