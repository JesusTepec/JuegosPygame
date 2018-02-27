import pygame

NEGRO = (0, 0, 0)


class Protagonista(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), [50, 50])
        self.rect = self.image.get_rect()

