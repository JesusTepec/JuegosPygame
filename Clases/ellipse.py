import pygame
import Rectangulo


COLOR_PARTICULA = (224, 255, 130)

class Elipse(Rectangulo.Rectangulo):
    """docstring for Elipse."""

    def draw(self, pantalla):
        pygame.draw.ellipse(pantalla, self.color, [self.x, self.y, self.width, self.height], 0);
