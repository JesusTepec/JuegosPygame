import pygame

NEGRO = (0, 0, 0)


class Protagonista(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        self.width = 90
        self.height = 90
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

