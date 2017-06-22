import pygame
import random

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)

class Bloque(pygame.sprite.Sprite):

	def __init__(self, image, largo, alto):
		super().__init__()

		self.image = pygame.image.load(image).convert()
		#self.image.fill(color)
		self.image.set_colorkey(NEGRO)
		self.rect = self.image.get_rect()
		self.limite_izquierdo = 0
		self.limite_derecho = 0
		self.limite_superior = 0
		self.limite_inferior = 0
		self.cambio_x = 0
		self.cambio_y = 0

	def update(self):
		self.rect.x += self.cambio_x
		self.rect.y += self.cambio_y
		if self.rect.right >= self.limite_derecho or self.rect.left <= self.limite_izquierdo:
			self.cambio_x *= -1 
		if self.rect.bottom >= self.limite_inferior or self.rect.top <= self.limite_superior:
		    self.cambio_y *= -1

def dibujarTexto(screen, texto):
	text = fuente.render(texto, 1, AZUL)
	screen.blit(text, [660, 30])


pygame.init()
dimensiones = [900, 700]

pantalla = pygame.display.set_mode(dimensiones)
pygame.mouse.set_visible(False);
fuente = pygame.font.SysFont("Arial", 25)

listaBloques = pygame.sprite.Group()
listaSprites = pygame.sprite.Group()
imagePersonaje = "image/ufoRed.png";
imageEnergia = "image/powerupYellow_bolt.png";
sonidoEnergia = pygame.mixer.Sound("sound/coin2.wav")

for i in range(50):
	bloque = Bloque(imageEnergia, 20, 15)

	bloque.rect.x = random.randrange(dimensiones[0])
	bloque.rect.y = random.randrange(dimensiones[1])
	 
	bloque.cambio_x = random.randrange(-2,7)
	bloque.cambio_y = random.randrange(-2,7)
	bloque.limite_izquierdo = 0
	bloque.limite_superior = 0
	bloque.limite_derecho = dimensiones[0]
	bloque.limite_inferior = dimensiones[1]

	listaBloques.add(bloque)
	listaSprites.add(bloque)

protagonista = Bloque(imagePersonaje, 20, 15)
listaSprites.add(protagonista)

game_over = False

reloj = pygame.time.Clock()
marcador = 0

while not game_over:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			game_over = True
	
	pantalla.fill(BLANCO)

	pos = pygame.mouse.get_pos()

	protagonista.rect.x = pos[0]
	protagonista.rect.y = pos[1]

	listaImpactos = pygame.sprite.spritecollide(protagonista, listaBloques, True)
	for bloque in listaImpactos:
		sonidoEnergia.play()
		marcador +=1
	listaBloques.update()
	dibujarTexto(pantalla, str(marcador))
	listaSprites.draw(pantalla)

	reloj.tick(60)

	pygame.display.flip()

pygame.quit()
















