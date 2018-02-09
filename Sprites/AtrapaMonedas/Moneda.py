import pygame

NEGRO = (0, 0, 0)


class Moneda(pygame.sprite.Sprite):

    def __init__(self, image, limites):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), [20, 20]).convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.limite_izquierdo = 10
        self.limite_derecho = limites[0]
        self.limite_superior = 10
        self.limite_inferior = limites[1]
        self.cambio_x = 0
        self.cambio_y = 0

    def update(self):
        self.rect.x += self.cambio_x
        self.rect.y += self.cambio_y
        if self.rect.right >= self.limite_derecho or self.rect.left <= self.limite_izquierdo:
            self.cambio_x *= -1
        if self.rect.bottom >= self.limite_inferior or self.rect.top <= self.limite_superior:
            self.cambio_y *= -1
