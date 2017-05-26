import pygame
from pygame.locals import *
from math import sin, cos, radians

# Aceleracion que produce la fuerza de la gravedad
gravedad = 0.2

# Vector velocidad en coordenadas polares
velocidad_inicial = 12.5 # Modulo (unos 63 m/s)
angulo_inicial = 45 # Direccion

# El punto donde comienza el movimiento el proyectil
posicion_inicial = [50, 550]

def main():
   pygame.init()
   screen = pygame.display.set_mode ((800,600)) # Define una pantalla con resolucion de 800x600
   proyectil = pygame.image.load("flor.png").convert_alpha() # Carga la imagen
   proyectil_rect = proyectil.get_rect() # Crea una superficie a partir de la imagen

   proyectil_rect.center = posicion_inicial # Situa el proyectil en su posicion inicial

   # Pasa de coordenadas polares a coordenadas cartesianas
   velocidad_inicial_x = cos(radians(angulo_inicial)) * velocidad_inicial
   velocidad_inicial_y = sin(radians(angulo_inicial)) * velocidad_inicial

   # Pone signo a las velocidades dependiendo de su direccion
   velocidad_x = +velocidad_inicial_x
   velocidad_y = -velocidad_inicial_y

   velocidad = [velocidad_x, velocidad_y] # Crea una lista con las dos componentes del vector

   clock = pygame.time.Clock() # Se utiliza para limitar los fotogramas por segundos
   while True:
      clock.tick(10) # Limita la ejecucion a 10 fotogramas por segundo
      velocidad[1] += gravedad # Incrementa la velocidad con el valor de la gravedad,
      #                          que solo actua en la componente "y" (acelera el cuerpo)

      # Incrementa la posicion del cuerpo sumandole las componentes de la velocidad
      # Funciana igual utilizando un metodo o otro
      #proyectil_rect.move_ip(velocidad[0], velocidad[1])
      proyectil_rect.center = [proyectil_rect.center[0] + velocidad[0], proyectil_rect.center[1] + velocidad[1]]


      # Descomentado imprime un fondo negro pero sin imprimirlo se puede apreciar mejor el movimiento
      #screen.fill((0,0,0))

      screen.blit (proyectil, proyectil_rect) # Imprime la imagen del proyectil en su posicion
      pygame.display.update() # Actualiza la pantalla

if __name__ == '__main__': main() # Ejecuta la funcion