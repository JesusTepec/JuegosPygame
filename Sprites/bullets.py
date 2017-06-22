""" 
Nos enseña como disparar proyectiles
  
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Vídeo explicativo: http://youtu.be/PpdJjaiLX6A
"""
import pygame
import random
 
# Definimos algunos colores
NEGRO    = (   0,   0,   0)
BLANCO    = ( 255, 255, 255)
ROJO      = ( 255,   0,   0)
AZUL     = (   0,   0, 255)
 
# --- Clases
 
class Bloque(pygame.sprite.Sprite):
    """ Esta clase representa al bloque. """
    def __init__(self, color):
        # Llama al constructor de la clase padre (Sprite)
        super().__init__() 
 
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
 
class Protagonista(pygame.sprite.Sprite):
    """ Esta clase representa al Protagonista. """
     
    def __init__(self):
        """ Configuramos al protagonista. """
        # Llama al constructor de la clase padre (Sprite)
        super().__init__() 
 
        self.image = pygame.Surface([20, 20])
        self.image.fill(ROJO)
 
        self.rect = self.image.get_rect()
         
    def update(self):
        """ Actualiza la ubicación del protagonista. """
        # Obtiene la posición actual del ratón. La devuelve como una lista de 
        # dos números.
        pos = pygame.mouse.get_pos()
     
        # Sitúa la posición x del protagonista en la posición x del ratón
        self.rect.x = pos[0] 
         
class Proyectil(pygame.sprite.Sprite):
    """ Esta clase representa al proyectil . """
    def __init__(self):
        #  Llama al constructor de la clase padre (Sprite)
        super().__init__() 
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(NEGRO)
 
        self.rect = self.image.get_rect()
         
    def update(self):
        """ Desplaza al proyectil. """
        self.rect.y -= 3
                 
 
# --- Creamos la ventana
 
# Iniciamos Pygame
pygame.init()
 
# Establecemos las dimensiones de la pantalla
largo_pantalla = 700
alto_pantalla = 400
pantalla = pygame.display.set_mode([largo_pantalla, alto_pantalla])
 
# --- Lista de sprites
 
# Esta es una lista de cada sprite, así como de todos los bloques y del protagonista.
lista_de_todos_los_sprites = pygame.sprite.Group()
 
# Lista de cada bloque en el juego
lista_bloques = pygame.sprite.Group()
 
# Lista de cada proyectil
lista_proyectiles = pygame.sprite.Group()
 
# --- Creamos los sprites
 
for i in range(50):
    # Esto representa un bloque
    bloque = Bloque(AZUL)
 
    # Configuramos una ubicación aleatoria para el bloque
    bloque.rect.x = random.randrange(largo_pantalla)
    bloque.rect.y = random.randrange(350)
     
    # Añadimos el bloque a la lista de objetos
    lista_bloques.add(bloque)
    lista_de_todos_los_sprites.add(bloque)
 
# Creamos un bloque protagonista ROJO
protagonista = Protagonista()
lista_de_todos_los_sprites.add(protagonista)
 
# Iteramos hasta que el usuario presione el botón de salir.
hecho = False
 
# Para controlar la tasa de refresco de la pantalla
reloj = pygame.time.Clock()
 
puntuacion = 0
protagonista.rect.y = 370
 
# -------- Bucle Principal -----------
while not hecho:
    # --- Procesamiento de Eventos
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            hecho = True
             
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Disparamos un proyectil si el usuario presiona el botón del ratón
            proyectil = Proyectil()
            # Configuramos el proyectil de forma que esté donde el protagonista
            proyectil.rect.x = protagonista.rect.x
            proyectil.rect.y = protagonista.rect.y
            # Añadimos el proyectil a la lista
            lista_de_todos_los_sprites.add(proyectil)
            lista_proyectiles.add(proyectil)
 
    # --- Lógica del Juego
     
    # Llamamos al método update() en todos los sprites
    lista_de_todos_los_sprites.update()
     
    # Calculamos la mecánica para cada proyectil
    for proyectil in lista_proyectiles:
 
        # Vemos si alcanza a un bloque
        lista_bloques_alcanzados = pygame.sprite.spritecollide(proyectil, lista_bloques, True)
         
        # Por cada bloque alcanzado, eliminamos el proyectil y aumentamos la puntuación
        for bloque in lista_bloques_alcanzados:
            lista_proyectiles.remove(proyectil)
            lista_de_todos_los_sprites.remove(proyectil)
            puntuacion += 1
            print( puntuacion )
             
        # Eliminamos el proyectil si vuela fuera de la pantalla
        if proyectil.rect.y < -10:
            lista_proyectiles.remove(proyectil)
            lista_de_todos_los_sprites.remove(proyectil)
         
    # --- Dibujamos un marco
 
    # Limpiamos la pantalla
    pantalla.fill(BLANCO)
         
    # Dibujamos todos los sprites
    lista_de_todos_los_sprites.draw(pantalla)
 
    # Avanzamos y actualizamos la pantalla con todo lo que hemos dibujado.
    pygame.display.flip()
     
    # --- Limitamos a 20 fps
    reloj.tick(20)
 
pygame.quit()