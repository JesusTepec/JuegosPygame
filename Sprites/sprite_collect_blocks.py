"""
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
# Vídeo explicativo: http://youtu.be/4W2AqUetBi4
"""
 
import pygame
import random
 
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
 
class Bloque(pygame.sprite.Sprite):
    """
    Esta clase representa la pelota        
    Deriva de la clase "Sprite" en Pygame
    """
     
    def __init__(self, color, largo, alto):
        """ Constructor. Pasa el color al bloque, 
        y su posición x e y """
         
        # Llama al constructor de la clase padre (Sprite) 
        super().__init__() 
 
        # Crea una imagen del bloque y lo rellena de color.
        # Esto podría ser también una imagen cargada desde el disco duro.
        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)
 
        # Obtenemos el objeto rectángulo que posee las dimensiones de la imagen
        # Actualizamos la posición de ese objeto estableciendo los valores para 
        # rect.x y rect.y
        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, pantalla_largo)

    def update(self):
        self.rect.y += 1
        if(self.rect.y > 410):
            self.reset_pos()
 
# Inicializamos Pygame
pygame.init()
 
# Establecemos el alto y largo de la pantalla
pantalla_largo = 700
pantalla_alto = 400
pantalla=pygame.display.set_mode([pantalla_largo,pantalla_alto])
 
# Esta es una lista de 'sprites.' Cada bloque en el programa es
# añadido a la lista. La lista es gestionada por una clase llamada 'Group.'
bloque_lista = pygame.sprite.Group()
 
# Esta es una lista de cada uno de los sprites. Así como del resto de bloques y el bloque protagonista..
listade_todoslos_sprites = pygame.sprite.Group()
 
for i in range(50):
    # Esto representa un bloque
    bloque = Bloque(NEGRO, 20, 15)
 
    # Establecemos una ubicación aleatoria para el bloque
    bloque.rect.x = random.randrange(pantalla_largo)
    bloque.rect.y = random.randrange(pantalla_alto)
     
    # Añadimos el  bloque a la lista de objetos
    bloque_lista.add(bloque)
    listade_todoslos_sprites.add(bloque)
 
# Creamos un bloque protagonista ROJO
protagonista = Bloque(ROJO, 20, 15)
listade_todoslos_sprites.add(protagonista)
 
#Iteramos hasta que el usuario pulse el botón de salida
hecho = False
 
#  Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
 
marcador = 0
 
# -------- Bucle principal del Programa -----------
while not hecho:
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario pulsó salir
            hecho = True # Marcamos que hemos terminado y salimos del bucle
 
    # Limpiamos la pantalla
    pantalla.fill(BLANCO)
    bloque_lista.update()
    pos = pygame.mouse.get_pos()
    protagonista.rect.x = pos[0]
    protagonista.rect.y = pos[1]
    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, bloque_lista, False)  
    for bloque in lista_impactos_bloques:
        marcador += 1
        print( marcador )
        bloque.reset_pos()
    listade_todoslos_sprites.draw(pantalla)
     
    # Limitamos a 60 fotogramas por segundo
    reloj.tick(60)
 
    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
 
pygame.quit()