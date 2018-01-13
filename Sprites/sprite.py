import pygame
import random
import math

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
COLOR_FUENTE = (255, 122, 88)
FONDO = (43, 109, 216)

class Enemigo (pygame.sprite.Sprite):

	def __init__(self, image, largo, alto):
		super().__init__()
		self.image = pygame.image.load(image).convert()
		self.image.set_colorkey(NEGRO)
		self.rect = self.image.get_rect()
		self.centro_x = 0
		self.centro_y = 0
		self.angulo = 2 * math.pi
		self.radio = 0
		self.velocidad = 0.05
		self.cambio_x = 5
		self.cambio_y = 5

	def update(self):
		self.centro_x += self.cambio_x
		self.centro_y += self.cambio_y

		self.rect.x = self.radio * math.sin(self.angulo) + self.centro_x
		self.rect.y = self.radio * math.cos(self.angulo) + self.centro_y

		if self.rect.right >= dimensiones[0] or self.rect.left <= 0:
			self.cambio_x *= -1
		if self.rect.bottom >= dimensiones[1] or self.rect.top <= 0:
		    self.cambio_y *= -1
		self.angulo += self.velocidad

class Bloque(pygame.sprite.Sprite):

	def __init__(self, image, largo, alto):
		super().__init__()
		self.image = pygame.image.load(image).convert()
		self.image.set_colorkey(NEGRO)
		self.rect = self.image.get_rect()
		self.limite_izquierdo = 10
		self.limite_derecho = dimensiones[0]
		self.limite_superior = 10
		self.limite_inferior = dimensiones[1]
		self.cambio_x = 0
		self.cambio_y = 0

	def update(self):
		self.rect.x += self.cambio_x
		self.rect.y += self.cambio_y
		if self.rect.right >= self.limite_derecho or self.rect.left <= self.limite_izquierdo:
			self.cambio_x *= -1
		if self.rect.bottom >= self.limite_inferior or self.rect.top <= self.limite_superior:
		    self.cambio_y *= -1

def dibujarTexto(screen, texto, pos):
	fuente = pygame.font.SysFont('Barber Street_PersonalUseOnly', 100)
	text = fuente.render(texto, 1, COLOR_FUENTE)
	screen.blit(text, pos)

def dibujarMarcador(screen, texto, pos):
	fuente = pygame.font.SysFont('Impact', 30)
	text = fuente.render(texto, 1, COLOR_FUENTE)
	screen.blit(text, pos)

def colisiono(mouse, objeto):
    if (mouse[0] > objeto[0] and mouse[0] < objeto[0] + objeto[2]) and (mouse[1] > objeto[1] and mouse[1] < objeto[1] + objeto[3]):
        return True
    return False

def boton(pos, texto, press):
	if(press):
		botonNormal = pygame.image.load("image/buttonLong_beige_pressed.png").convert()
	else:
		botonNormal = pygame.image.load("image/buttonLong_beige.png").convert()
	botonNormal.set_colorkey(NEGRO)
	picture = pygame.transform.scale(botonNormal, [235, 50])
	pantalla.blit(picture, pos)
	fuente = pygame.font.SysFont('Impact', 35)
	text = fuente.render(texto, 1, COLOR_FUENTE)
	pantalla.blit(text, [pos[0] + 10, pos[1]])
	return [pos[0], pos[1], 235, 50]

pygame.init()
dimensiones = [900, 700]

pantalla = pygame.display.set_mode(dimensiones)
#pygame.mouse.set_visible(False);
listaBloques = pygame.sprite.Group()
listaSprites = pygame.sprite.Group()
imagePersonaje = "image/ufoRed.png";
imageEnergia = "image/powerupYellow_bolt.png";
imageEnemigo = "image/meteorGrey_big4.png";
sonidoEnergia = pygame.mixer.Sound("sound/coin2.wav")
pygame.mixer.music.load('sound/Nowhere_Land.mp3')
#pygame.mixer.music.play()

for i in range(50):
	bloque = Bloque(imageEnergia, 20, 15)

	bloque.rect.x = random.randrange(dimensiones[0])
	bloque.rect.y = random.randrange(dimensiones[1])

	bloque.cambio_x = random.randrange(-2,7)
	bloque.cambio_y = random.randrange(-2,7)

	listaBloques.add(bloque)
	listaSprites.add(bloque)

protagonista = Bloque(imagePersonaje, 20, 15)
listaSprites.add(protagonista)
enemigo = Enemigo(imageEnemigo, 20, 15)
enemigo.centro_x = random.randrange(50, dimensiones[0] - 200)
enemigo.centro_y = random.randrange(50, dimensiones[1] - 200)
enemigo.radio = random.randrange(10, 100)
enemigo.angulo = random.random() * 2 * math.pi
listaSprites.add(enemigo)

game_over = False

reloj = pygame.time.Clock()
marcador = 0
perdiste = 0
btnJugarClick = False
btnJugar = None

while not game_over:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			game_over = True
		#elif evento.type == pygame.constants.USEREVENT:
			#pygame.mixer.music.play()
		if evento.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			btnJugarClick = colisiono(pos, btnJugar)
		if evento.type == pygame.MOUSEBUTTONUP:
			btnJugarClick = False

	pantalla.fill(FONDO)
	pos = pygame.mouse.get_pos()

	protagonista.rect.x = pos[0]
	protagonista.rect.y = pos[1]

	listaImpactos = pygame.sprite.spritecollide(protagonista, listaBloques, True)
	if pygame.sprite.collide_rect(protagonista, enemigo):
		listaSprites.empty()
		listaBloques.empty()
		perdiste = True
	if perdiste:
		dibujarTexto(pantalla, "Game Over", [310, 300])
	for bloque in listaImpactos:
	#	sonidoEnergia.play()
		marcador += 1
	if marcador == 50:
		dibujarTexto(pantalla, "You Win", [330, 300])
		listaSprites.empty()
		listaBloques.empty()
		if(btnJugarClick):
			boton([390, 400], "Jugar de nuevo", True)
		else:
			btnJugar = boton([390, 400], "Jugar de nuevo", False)

	listaBloques.update()
	enemigo.update()
	dibujarMarcador(pantalla, str(marcador), [760, 30])
	listaSprites.draw(pantalla)

	reloj.tick(60)

	pygame.display.flip()

pygame.quit()
