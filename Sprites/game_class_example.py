"""
 Muestra la forma correcta de organizar un juego utilizando una clase juego
  
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Vídeo explicativo: http://youtu.be/O4Y5KrNgP_c
"""
 
import pygame
import random
 
#--- Constantes Globales ---
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
 
LARGO_PANTALLA  = 700
ALTO_PANTALLA = 500
 
# --- Clases ---
 
class Bloque(pygame.sprite.Sprite):
     
    """ Este clase representa aun sencillo bloque que es recogido por el protagonista. """
     
    def __init__(self):
         
        """ Constructor; crea la imagen del bloque. """
        super().__init__() 
        self.image = pygame.Surface([20, 20])
        self.image.fill(NEGRO)
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
         
        """ La llamamos cuando el bloque es 'recogido' o se va fuera de 
            la pantalla. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(LARGO_PANTALLA)        
 
    def update(self):
         
        """ Se le llama automáticamente cuando necesitamos mover el bloque. """
        self.rect.y += 1
         
        if self.rect.y > ALTO_PANTALLA + self.rect.height:
             
            self.reset_pos()
 
class Protagonista(pygame.sprite.Sprite):
    """ Esta clase representa al protagonista. """
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface([20, 20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Actualiza la posición del protagonista. """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]        
 
class Juego(object):
    """ Esta clase representa una instancia del juego. Si necesitamos reiniciar el juego,
        solo tendríamos que crear una nueva instancia de esta clase."""
 
    def __init__(self):
        """ Constructor. Crea todos nuestros atributos e inicializa
        el juego. """
     
        self.puntuacion = 0
        self.game_over = False
         
        # Creamos la lista de sprites
        self.bloque_lista = pygame.sprite.Group()
        self.listade_todoslos_sprites = pygame.sprite.Group()
         
        #  Creamos los bloques de sprites
        for i in range(50):
             
            bloque = Bloque()
         
            bloque.rect.x = random.randrange(LARGO_PANTALLA)
            bloque.rect.y = random.randrange(-300, ALTO_PANTALLA)
             
            self.bloque_lista.add(bloque)
            self.listade_todoslos_sprites.add(bloque)
         
        # Creamos al protagonista
        self.protagonista = Protagonista()
        self.listade_todoslos_sprites.add(self.protagonista)
 
    def procesa_eventos(self):
        """ Procesa todos los eventos. Devuelve un "True" si precisamos
            cerrar la ventana. """
 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return True
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
         
        return False
 
    def logica_de_ejecucion(self):
        """
        Este método se ejecuta para cada fotograma. 
        Actualiza posiciones y comprueba colisiones.
        """
        if not self.game_over:
             
            # Mueve todos los sprites
            self.listade_todoslos_sprites.update()
             
            # Observa por si el bloque protagonista ha colisionado con algo.
            lista_impactos_bloques = pygame.sprite.spritecollide(self.protagonista, self.bloque_lista, True)  
          
            # Comprueba la lista de colisiones.
            for bloque in lista_impactos_bloques:                
                self.puntuacion += 1
                print( self.puntuacion )
                 
            if len(self.bloque_lista) == 0:
                self.game_over = True
                 
    def display_frame(self, pantalla):
         
        """ Muestra todo el juego sobre la pantalla. """
        pantalla.fill(BLANCO)
         
        if self.game_over:
             
            #fuente = pygame.font.Font("Serif", 25)
            fuente = pygame.font.SysFont("Arial", 35)
            texto = fuente.render("Game Over, haz click para volver a jugar", True, NEGRO)
            centrar_x = (LARGO_PANTALLA // 2) - (texto.get_width() // 2)
            centrar_y = (ALTO_PANTALLA // 2) - (texto.get_height() // 2)
            pantalla.blit(texto, [centrar_x, centrar_y])
         
        if not self.game_over:            
            self.listade_todoslos_sprites.draw(pantalla)
             
        pygame.display.flip()
     
         
def main():
     
    """Función principal del programa. """
    # Iniciamos Pygame y disponemos la ventana
    pygame.init()
      
    dimensiones = [LARGO_PANTALLA, ALTO_PANTALLA]
    pantalla = pygame.display.set_mode(dimensiones)
     
    pygame.display.set_caption("Mi Juego")
    pygame.mouse.set_visible(False)
     
    # Crea los objetos y dispone los datos
    hecho = False
    reloj = pygame.time.Clock()
     
    # Crea una instancia de la clase Juego
    juego = Juego()
 
    # Bucle principal
    while not hecho:        
         
        # Procesa los eventos (pulsaciones del teclado, clicks del ratón, etc.)
        hecho = juego.procesa_eventos()
         
        # Actualiza las posiciones de los objetos y comprueba colisiones
        juego.logica_de_ejecucion()
         
        # Dibuja el fotograma actual
        juego.display_frame(pantalla)
         
        # Hace una pausa hasta el siguiente fotograma
        reloj.tick(60)
         
    # Cierra la ventana y sale    
    pygame.quit()
 
# Llama a la función principal y arranca el juego
if __name__ == "__main__":
     
    main()