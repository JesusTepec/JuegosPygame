"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""
 
import pygame
import random
  
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
  
  
class Bloque(pygame.sprite.Sprite):  
    """
    Esta clase representa la pelota.        
    Deriva de la clase "Sprite" en Pygame
    """
     
    def __init__(self, color, width, height):
        """Constructor. Le pasa el color al bloque,
        así como la posición de x,y """
        # Llama a la clase constructor padre (Sprite)
        super().__init__()
 
        # Crea una imagen del bloque y lo rellena de color.
        # También podríamos usar una imagen guardada en disco.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
  
        # Extraemos el objeto rectángulo que posee las dimensiones
        # de la imagen.
        # Estableciendo los valores para rect.x and rect.y actualizamos
        # la posición de este objeto.
        self.rect = self.image.get_rect()
 
        # Variables de instancia que controlan los bordes
        # donde rebotamos
        self.limite_izquierdo = 0
        self.limite_derecho = 0
        self.limite_superior = 0
        self.limite_inferior = 0
 
        # Variables de instancia que controlan nuestras
        # velocidades y dirección actuales
        self.cambio_x = 0
        self.cambio_y = 0
            
 
    # Llamada para cada fotograma.
    def update(self):
        self.rect.x += self.cambio_x
        self.rect.y += self.cambio_y
         
        if self.rect.right >= self.limite_derecho or self.rect.left <= self.limite_izquierdo:
            self.cambio_x *= -1
 
        if self.rect.bottom >= self.limite_inferior or self.rect.top <= self.limite_superior:
            self.cambio_y *= -1
             
class Protagonista(Bloque):
    """ La clase protagonista deriva de Bloque, pero sobrescribe su
    funcionalidad de 'update' por una nueva función de desplazamiento
    que moverá el bloque con el ratón. """
    def update(self):
        # Obtiene la posición actual del ratón. La devuelve en forma de 
        # una lista de dos números.
        pos = pygame.mouse.get_pos()
          
      # Extraemos x e y de la lista, tal como si extrajéramos letras de una cadena de texto (string).
      # Coloca al objeto protagonista en la posición del ratón.
        self.rect.x = pos[0]
        self.rect.y = pos[1]        
         
#Iniciamos Pygame
pygame.init()
  
# Establecemos el largo y alto de la pantalla
largo_pantalla = 700
alto_pantalla = 400
pantalla=pygame.display.set_mode([largo_pantalla,alto_pantalla])
  
# Esta es una lista de 'sprites.' Cada bloque en el programa es 
# añadido a esta lista. La lista bes gestionada por la clase llamada  'Group.'
bloque_lista = pygame.sprite.Group()
  
# This is a list of every sprite. All bloques and the protagonista bloque as well.
listade_todoslos_sprites = pygame.sprite.Group()
  
for i in range(50):
    #  Esto representa un bloque
    bloque = Bloque(NEGRO, 20, 15)
  
    # Establece una ubicación aleatoria para el bloque
    bloque.rect.x = random.randrange(largo_pantalla)
    bloque.rect.y = random.randrange(alto_pantalla)
     
    bloque.cambio_x = random.randrange(-3,4)
    bloque.cambio_y = random.randrange(-3,4)
    bloque.limite_izquierdo = 0
    bloque.limite_superior = 0
    bloque.limite_derecho = largo_pantalla
    bloque.limite_inferior = alto_pantalla
     
    #Añade el bloque a la lista de objetos
    bloque_lista.add(bloque)
    listade_todoslos_sprites.add(bloque)
      
      
  
# Crea un bloque protagonista de color rojo
protagonista = Protagonista(ROJO, 20, 15)
listade_todoslos_sprites.add(protagonista)
  
#Iteramos hasta que el usuario haga click sobre el botón de salir.
hecho = False
  
# Lo usamos para gestionar cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
  
puntuacion = 0
  
# --------  Bucle Principal del Programa  -----------
while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            hecho = True
  
    # Limpiamos la pantalla
    pantalla.fill(BLANCO)
     
    # Llamamos al método update() para cada sprite en la lista
    listade_todoslos_sprites.update()
      
    # Observamos si el bloque protagonista ha colisionado con algo
    bloques_hit_list = pygame.sprite.spritecollide(protagonista, bloque_lista, True)  
      
    #Comprobamos la lista de colisiones
    for bloque in bloques_hit_list:
        puntuacion += 1
        print( puntuacion )
         
    # Dibujamos todos los sprites
    listade_todoslos_sprites.draw(pantalla)
      
    # Limitamos a 60 fotogramas por segundo
    reloj.tick(60)
  
    #Avanzamos y actualizamos la pantalla con todo lo que hemos dibujado.
    pygame.display.flip()
  
pygame.quit()