"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
De:
http://programarcadegames.com/python_examples/f.php?lang=es&lang=es&file=maze_runner.py
 
Vídeo explicativo: http://youtu.be/5-SbFanyUkQ
 
Parte de la serie:
http://programarcadegames.com/python_examples/f.php?lang=es&file=move_with_paredes_example.py
http://programarcadegames.com/python_examples/f.php?lang=es&file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?lang=es&file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?lang=es&file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?lang=es&file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/
"""
import pygame
  
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
VIOLETA = (255, 0, 255)
  
 
class Pared(pygame.sprite.Sprite):
    """Esta clase representa la barra inferior que controla el protagonista """
     
    def __init__(self, x, y, largo, alto, color):
        """ Función Constructor """
         
        # Llama al constructor padre
        super().__init__()
  
        # Crea una pared AZUL, con las dimensiones especificadas en los parámetros
        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)
  
        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
class Protagonista(pygame.sprite.Sprite):
    """ Esta clase representa la barra inferior que controla el 
    protagonista """
     
    # Establecemos el vector velocidad
    cambio_x = 0
    cambio_y = 0
  
    def __init__(self, x, y):
        """ Función Constructor """
 
        # Llama al constructor padre
        super().__init__()
   
        # Establecemos el alto y largo
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLANCO)
  
        # Establece como origen la esquina superior izquierda.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
      
    def cambiovelocidad(self, x, y):
        """ Cambia la velocidad del protagonista. Es llamada con una pulsación del teclado. """
        self.cambio_x += x
        self.cambio_y += y
          
    def mover(self, paredes):
        """ Encuentra una nueva posición para el protagonista """
         
        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x
         
        # Hemos chocado contra la pared después de esta actualización?
        lista_impactos_bloques = pygame.sprite.spritecollide(self, paredes, False)
        for bloque in lista_impactos_bloques:
            # Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado izquierdo del objeto que hemos tocado.
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            else:
                # En caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
                self.rect.left = bloque.rect.right
  
        # Desplazar arriba/izquierda
        self.rect.y += self.cambio_y
          
        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, paredes, False) 
        for bloque in lista_impactos_bloques:
                 
            # Reseteamos nuestra posición basándonos en la parte superior/inferior del objeto.
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top 
            else:
                self.rect.top = bloque.rect.bottom            
  
class Cuarto():
    """ Clase base para todos los cuartos. """
     
    #Cada cuarto tiene una lista de paredes, y de los sprites enemigos.
    pared_lista = None
    sprites_enemigos = None
     
    def __init__(self):
        """ Constructor, creamos nuestras listas. """
        self.pared_lista = pygame.sprite.Group()
        self.sprites_enemigos = pygame.sprite.Group()
     
class Cuarto1(Cuarto):
    """Esto crea todas las paredes del cuarto 1"""
    def __init__(self):
        super().__init__()
        # Crear las paredes. (x_pos, y_pos, largo, alto)
         
        # Esta es la lista de las paredes. Cada una se especifica de la forma [x, y, largo, alto]
        paredes = [ [0,0,20,250,BLANCO],
                  [0,350,20,250,BLANCO],
                  [780,0,20,250,BLANCO],
                  [780,350,20,250,BLANCO],
                  [20,0,760,20,BLANCO],
                  [20,580,760,20,BLANCO],
                  [390,50,20,500,AZUL]
                ]
         
        # Iteramos a través de la lista. Creamos la pared y la añadimos a la lista.
        for item in paredes:
            pared = Pared(item[0],item[1],item[2],item[3],item[4])
            self.pared_lista.add(pared)
         
class Cuarto2(Cuarto):
    """Esto crea todas las paredes del cuarto 2"""
    def __init__(self):
        super().__init__()
         
        paredes = [ [0,0,20,250,ROJO],
                  [0,350,20,250,ROJO],
                  [780,0,20,250,ROJO],
                  [780,350,20,250,ROJO],
                  [20,0,760,20,ROJO],
                  [20,580,760,20,ROJO],
                  [190,50,20,500,VERDE],
                  [590,50,20,500,VERDE]
                ]
         
        for item in paredes:
            pared = Pared(item[0],item[1],item[2],item[3],item[4])
            self.pared_lista.add(pared)
             
 
class Cuarto3(Cuarto):
    """Esto crea todas las paredes del cuarto 3"""
    def __init__(self):
        super().__init__()
     
        paredes = [ [0,0,20,250,VIOLETA],
                  [0,350,20,250,VIOLETA],
                  [780,0,20,250,VIOLETA],
                  [780,350,20,250,VIOLETA],
                  [20,0,760,20,VIOLETA],
                  [20,580,760,20,VIOLETA]
                ]
         
        for item in paredes:
            pared = Pared(item[0],item[1],item[2],item[3],item[4])
            self.pared_lista.add(pared)
         
        for x in range(100,800, 100):
            for y in range(50, 451, 300):
                pared = Pared(x, y, 20, 200,ROJO)
                self.pared_lista.add(pared)
         
        for x in range(150,700, 100):
            pared = Pared(x, 200, 20, 200,BLANCO)
            self.pared_lista.add(pared)
 
def main():
    """ Programa Principal """
     
    # Llamamos a esta función para que la biblioteca Pygame pueda autoiniciarse.
    pygame.init()
      
    # Creamos una pantalla de 800x600
    pantalla = pygame.display.set_mode([800, 600])
      
    # Creamos el título de la ventana
    pygame.display.set_caption('Maze Runner')
      
    # Creamos al objeto pala protagonista
    protagonista = Protagonista(50, 50)
    desplazarsprites = pygame.sprite.Group()
    desplazarsprites.add(protagonista)
      
    cuartos = []
     
    cuarto = Cuarto1()
    cuartos.append(cuarto)
     
    cuarto = Cuarto2()
    cuartos.append(cuarto)
     
    cuarto = Cuarto3()
    cuartos.append(cuarto)
     
    cuarto_actual_no = 0
    cuarto_actual = cuartos[cuarto_actual_no]
     
    reloj = pygame.time.Clock()
      
    puntuacion = 0
     
    hecho = False
      
    while not hecho:
         
        # --- Procesamiento de Eventos ---
         
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                hecho = True
      
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    protagonista.cambiovelocidad(-5,0)
                if evento.key == pygame.K_RIGHT:
                    protagonista.cambiovelocidad(5,0)
                if evento.key == pygame.K_UP:
                    protagonista.cambiovelocidad(0,-5)
                if evento.key == pygame.K_DOWN:
                    protagonista.cambiovelocidad(0,5)
                      
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT:
                    protagonista.cambiovelocidad(5,0)
                if evento.key == pygame.K_RIGHT:
                    protagonista.cambiovelocidad(-5,0)
                if evento.key == pygame.K_UP:
                    protagonista.cambiovelocidad(0,5)
                if evento.key == pygame.K_DOWN:
                    protagonista.cambiovelocidad(0,-5)
                     
        # --- Lógica del Juego ---
         
        protagonista.mover(cuarto_actual.pared_lista)
         
        if protagonista.rect.x < -15:
            if cuarto_actual_no == 0:
                cuarto_actual_no = 2
                cuarto_actual = cuartos[cuarto_actual_no]
                protagonista.rect.x = 790
            elif cuarto_actual_no == 2:
                cuarto_actual_no = 1
                cuarto_actual = cuartos[cuarto_actual_no]
                protagonista.rect.x = 790
            else:
                cuarto_actual_no = 0
                cuarto_actual = cuartos[cuarto_actual_no]
                protagonista.rect.x = 790
                 
        if protagonista.rect.x > 801:
            if cuarto_actual_no == 0:
                cuarto_actual_no = 1
                cuarto_actual = cuartos[cuarto_actual_no]
                protagonista.rect.x = 0
            elif cuarto_actual_no == 1:
                cuarto_actual_no = 2
                cuarto_actual = cuartos[cuarto_actual_no]
                protagonista.rect.x = 0
            else:
                cuarto_actual_no = 0
                cuarto_actual = cuartos[cuarto_actual_no]
                protagonista.rect.x = 0
     
        # --- Dibujamos ---
        pantalla.fill(NEGRO)
         
        desplazarsprites.draw(pantalla)
        cuarto_actual.pared_lista.draw(pantalla)
         
        pygame.display.flip()
      
        reloj.tick(60)
                  
    pygame.quit()
 
if __name__ == "__main__":
    main()