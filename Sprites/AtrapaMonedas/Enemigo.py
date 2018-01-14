import pygame
import math
import random

NEGRO = (0, 0, 0)

class Enemigo (pygame.sprite.Sprite):

	def __init__(self, image, limites):
		super().__init__()
		self.image = pygame.image.load(image).convert()
		self.image.set_colorkey(NEGRO)
		self.rect = self.image.get_rect()
		self.centro_x = random.randrange(50, limites[0] - 200)
		self.centro_y = random.randrange(50, limites[1] - 200)
		self.angulo = random.random() * 2 * math.pi
		self.radio = random.randrange(10, 100)
		self.velocidad = 0.05
		self.cambio_x = 5
		self.cambio_y = 5
		self.limites = limites

	def update(self):
		self.centro_x += self.cambio_x
		self.centro_y += self.cambio_y

		self.rect.x = self.radio * math.sin(self.angulo) + self.centro_x
		self.rect.y = self.radio * math.cos(self.angulo) + self.centro_y

		if self.rect.right >= self.limites[0] or self.rect.left <= 0:
			self.cambio_x *= -1
		if self.rect.bottom >= self.limites[1] or self.rect.top <= 0:
		    self.cambio_y *= -1
		self.angulo += self.velocidad
