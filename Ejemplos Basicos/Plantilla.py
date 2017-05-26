# -*- coding: utf-8 -*-
import pygame
import math


def gradToRad(grados):
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
dimensiones = [300, 300]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("--------Arcos------")  # Titulo

#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.
juego_terminado = False

# Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
x = 10
y = 10
posCircle = [0, 0]
# -------- Bucle principal del Programa -----------
while juego_terminado is False:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():  # El usuario realizó alguna acción
        if evento.type == pygame.QUIT:  # Si el usuario hizo click sobre salir
            juego_terminado = True
            # Marcamos que hemos acabado y abandonamos este bucle

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ

    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
    pantalla.fill(AMARILLO)
    #pygame.draw.rect(pantalla, ROJO, [150, 50, 400, 400])
    #pygame.draw.circle(pantalla, AZUL, [350, 250], 200, 2)
    #pygame.draw.line(pantalla, VERDE, [10, 10], [650, 470], 4)
    #pygame.draw.ellipse(pantalla, COLOR, [50, 50, 600, 400])
    pygame.draw.arc(pantalla, ROJO, [50, 20, 200, 200], 0, 2 * math.pi)
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'ciclará'
pygame.quit()
