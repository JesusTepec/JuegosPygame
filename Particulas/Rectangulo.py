import pygame
import random

COLOR = (26, 150, 120)

class Rectangulo():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = random.randrange(3, 10)
        self.height = self.width
        self.move_x = random.randrange(-3, 5)
        self.move_y = random.randrange(-3, 5)
        self.color = COLOR

    def mover(self):
        self.x += self.move_x
        self.y += self.move_y

    def draw(self, pantalla):
        pygame.draw.rect(pantalla, self.color, [self.x, self.y, self.width, self.height])
