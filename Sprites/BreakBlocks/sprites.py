import pygame

ROJO = (180, 20, 40)


class Bloque(pygame.sprite.Sprite):

    def __init__(self, color):
        super().__init__()
        self.color = color
        self.image = pygame.Surface([60, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def get_color(self):
        return self.color


class Protagonista(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.color = ROJO
        self.image = pygame.Surface([40, 20])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]

    def change_color(self, color):
        self.color = color
        self.image.fill(color)

    def get_color(self):
        return self.color


class Proyectil(pygame.sprite.Sprite):

    def __init__(self, color):
        super().__init__()
        self.color = color
        self.image = pygame.Surface([8, 16])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 4

    def get_color(self):
        return self.color
