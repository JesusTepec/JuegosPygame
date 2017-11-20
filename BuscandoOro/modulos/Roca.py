import pygame


class Roca(pygame.sprite.Sprite):
    """Clase Roca as Sprite obtaculo principal."""
    def __init__(self, color, largo, alto):

        super().__init__()

        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)
        self.rect = self.image.get_rect()
