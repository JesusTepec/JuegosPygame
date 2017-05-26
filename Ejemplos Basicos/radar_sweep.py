"""
 Cómo hacer un barrido de radar.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""
# Importamos las bibliotecas pygame y math
import pygame
import math

# Inicializamos el motor de juegos
pygame.init()

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

PI = 3.141592653

# Establecemos la altura y largo de la pantalla
dimensiones = [400, 400]
pantalla = pygame.display.set_mode(dimensiones)

# Usado para gestionar cuán rápido se actualiza la pantalla
reloj = pygame.time.Clock()

#Iteramos hasta que el usuario haga click sobre el botón de cerrar
hecho = False

angulo = 0

while not hecho:
    for evento in pygame.event.get():   # El usuario hizo algo
        if evento.type == pygame.QUIT:  # Si el usuario hace click sobre cerrar
            hecho = True

    # Limpia la pantalla y establece su color de fondo
    pantalla.fill(BLANCO)

    # Dimensiones del barrido del radar
    # Empezamos arriba a la izquierda en las coordenadas 20,20
    # Largo/Alto de 250
    dimensiones_caja = [20, 20, 250, 250]

    # Dibujamos el borde de un círculo para 'barrerlo'
    pygame.draw.circle(pantalla, VERDE, [145, 145], 125, 2)
    pygame.draw.ellipse(pantalla, VERDE, dimensiones_caja, 2)
    # Dibujamos una caja negra alrededor del círculo
    pygame.draw.rect(pantalla, NEGRO, dimensiones_caja, 2)

    # Calculamos las coordenadas finales (x,y) de nuestro 'barrido',
    # basándonos en el ángulo actual
    x = 125 * math.sin(angulo) + 145
    y = 125 * math.cos(angulo) + 145

    # Dibujamos una línea desde el centro ubicado en las coordenadas (145, 145)
    # hacia el punto final que hemos calculado arriba
    pygame.draw.line(pantalla, VERDE, [145, 145], [x, y], 2)

    # Incrementamos el ángulo en 0.05 radianes
    angulo = angulo + .05

    # Si no consigues un barrido completo, reinicia el ángulo en 0

    if angulo > 2 * PI:
        angulo = angulo - 2 * PI

    # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # Limitamos a 60 fotogramas por segundo
    reloj.tick(60)

# Pórtate bien con el IDLE. Si nos olvidamos de esta línea, el programa se 'colgará'
# en la salida..
pygame.quit()