#Ejemplo 1 - circulo cae
import pygame
import math

def gToR(grados):
    return (grados * math.pi) / 180
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
a = 200
b = 200
r = 100
v_x = 1
v_y = 1
t1 = 0
t = 0
# -------- Bucle principal del Programa -----------
while juego_terminado is False:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():  # El usuario realizó alguna acción
        if evento.type == pygame.QUIT:  # Si el usuario hizo click sobre salir
            juego_terminado = True
            # Marcamos que hemos acabado y abandonamos este bucle

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
    #t1 = math.sqrt(math.pow(r, 2) - math.pow((x - a), 2))
    #if x > 199 or x == 0:
        #v_x *= -1
        #v_y *= -1
    #y = (t1 * v_y) + b
    x = r * math.cos(gToR(t)) + a
    y = r * math.sin(gToR(t)) + b
    pygame.draw.line(pantalla, VERDE, [a, b], [x, y], 2)
    y = int(y)
    x = int(x)
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
    #pantalla.fill(BLANCO)

    pygame.draw.rect(pantalla, ROJO, [x, y, 5, 5], 0)
  #  x += v_x
    t += 0.1
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(100)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'ciclará'
pygame.quit()
