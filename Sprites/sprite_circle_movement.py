""" 
 Mover un sprite en círculos.
  
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
import random
import math
 
# Definimos algunos colores
 
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO= (255, 0, 0)
AZUL = (0, 0, 255)
 
 
class Bloque(pygame.sprite.Sprite):
    """ Esta clase representa la pelota que se mueve en círculos. """
 
     
     
    def __init__(self, color, largo, alto):
        """ Constructor que crea la imagen de la pelota. """
        super().__init__() 
        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)
        self.rect = self.image.get_rect()
 
        # Este es el "centro" que el sprite orbitará
        self.centrar_x = 0
        self.centrar_y = 0
 
        # Ángulo actual en radianes
        self.angulo = 0
     
        #Cuán lejos orbitamos desde el centro, en píxeles
        self.radio = 0
     
        # Cuán rápido orbitamos, en radianes por fotograma
        self.velocidad = 0.05
         
    def update(self):
        """ Actualizamos la posición de la pelota. """
        # Calculamos un nuevo x, y
        self.rect.x = self.radio * math.sin(self.angulo) + self.centrar_x
        self.rect.y = self.radio * math.cos(self.angulo) + self.centrar_y
         
        # Incrementamos el ángulo para la siguiente ronda.
        self.angulo += self.velocidad
 
class Protagonista(pygame.sprite.Sprite):
    """ Clase que representa al protagonista. """
    def __init__(self, color, largo, alto):
        """ Creamos la imagen del protagonista. """
        super().__init__() 
        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)
        self.rect = self.image.get_rect()
         
    def update(self):
        """Determinamos que el usuario tiene que estar allí donde se encuentre el ratón. """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
         
# Inicializamos Pygame
pygame.init()
 
# Establecemos el alto y largo de la pantalla
LARGO_PANTALLA = 700
ALTO_PANTALLA = 400
pantalla = pygame.display.set_mode([LARGO_PANTALLA, ALTO_PANTALLA])
 
# Esta es una lista con los 'sprites.'Cada bloque en el programa es
# añadido a la lista. La lista es gestionada por la clase llamada 'Group.'
listade_bloques = pygame.sprite.Group()
 
# Esta es una lista de cada sprite. En ella están todos los bloques, incluido el del protagonista.
listade_todoslos_sprites = pygame.sprite.Group()
 
for i in range(50):
    # Esto representa un bloque
    bloque = Bloque(NEGRO, 20, 15)
 
    #Establecemos una ubicación central aleatoria para que orbite el bloque.
    bloque.centrar_x = random.randrange(LARGO_PANTALLA)
    bloque.centrar_y = random.randrange(ALTO_PANTALLA)
    # Radio aleatorio, desde 10 a 200
    bloque.radio = random.randrange(10, 200)
    # Ángulo de inicio aleatorio, desde 0 a 2pi
    bloque.angulo = random.random() * 2 * math.pi
    # radianes por fotograma.
    bloque.velocidad = 0.008
    # Añadimos el bloque a la lista de objetos.
    listade_bloques.add(bloque)
    listade_todoslos_sprites.add(bloque)
 
# Creamos un bloque protagonista ROJO
protagonista = Protagonista(ROJO, 20, 15)
listade_todoslos_sprites.add(protagonista)
 
# Iteramos hasta que el usuario haga click sobre el botón de salir.
hecho = False
 
# Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
 
puntuacion = 0
 
# -------- Bucle principal del Programa-----------
while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            hecho = True
 
    listade_todoslos_sprites.update()
            
    # Limpiamos la pantalla
    pantalla.fill(BLANCO)
     
    # Observamos por si el bloque protagonista ha colisionado contra algo.
    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, listade_bloques, True)  
     
    # Comprobamos la lista de colisiones
    for bloque in lista_impactos_bloques:
        puntuacion += 1
        print( puntuacion )
     
    #Dibujamos todos los sprites
    listade_todoslos_sprites.draw(pantalla)
     
    # Avanzamos y actualizamos la pantalla que ya hemos dibujado
    pygame.display.flip()
 
    # Limitamos a 60 fps
    reloj.tick(60)
 
pygame.quit()