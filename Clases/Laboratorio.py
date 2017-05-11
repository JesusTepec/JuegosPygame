import pygame
import random

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

class Rectangulo():
	"""docstring for Rectanguulo"""
	def __init__(self):
		self.x = 0
		self.y = 0
		self.width = random.randrange(20, 70)
		self.height = random.randrange(20, 70)
		self.move_x = random.randrange(-3, 3)
		self.move_y = random.randrange(-3, 3)
		self.color = [0, 0, 0]

	def setPosition(self, x, y):
		self.x = x
		self.y = y

	def setColor(self, color):
		self.color = color

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])
	
	def move(self):
		self.x += self.move_x
		self.y += self.move_y


class Elipse(Rectangulo):

	def draw(self, screen):
		pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.width, self.height])


pygame.init()
   
dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones) 
pygame.display.set_caption("Mi Primer juego en Informática")
 
hecho = False
 
reloj = pygame.time.Clock()
rectangulos = []
for i in range(500):
	obj = Rectangulo()
	obj.setColor([
		random.randrange(255),
		random.randrange(255),
		random.randrange(255)
	])
	obj.setPosition(random.randrange(700), random.randrange(500))
	rectangulos.append(obj)
for i in range(500):
	obj = Elipse()
	obj.setColor([
		random.randrange(255),
		random.randrange(255),
		random.randrange(255)
	])
	obj.setPosition(random.randrange(700), random.randrange(500))
	rectangulos.append(obj)

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True

    pantalla.fill(BLANCO)
    for rect in rectangulos:
    	rect.move()
    	rect.draw(pantalla)
    pygame.display.flip()
 	
    reloj.tick(60)
     
pygame.quit()