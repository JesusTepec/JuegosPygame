import pygame
import random

PARTICLE_COLOR = (26, 150, 120)

class Rectangulo():
    """docstring for Rectangulo."""
    def __init__(self):
        self.x = random.randrange(700)
        self.y = random.randrange(500)
        self.width = random.randrange(2, 8)
        self.height = self.width
        self.moveX = random.randrange(-3, 3)
        self.moveY = random.randrange(-3, 3)
        self.color = PARTICLE_COLOR

    def update(self):
        self.x += self.moveX
        self.y += self.moveY

    def draw(self, pantalla):
        pygame.draw.rect(pantalla, self.color, [self.x, self.y, self.width, self.height], 0)
