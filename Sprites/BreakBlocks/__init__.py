import pygame
import random
from sprites import *

COLOR_FONDO = (40, 40, 220)
ROJO = (180, 20, 40)
COLOR_PROYECTIL = (120, 130, 20)
AMARILLO = (200, 200, 10)

ANCHO_PANTALLA = 700
ALTO_PANTALLA = 500


class Juego(object):

    def __init__(self):

        self.game_over = False
        self.puntuacion = 0
        self.lista_colores = [(200, 50, 10), (220, 250, 10), (20, 230, 10), (250, 200, 10)]
        self.lista_sprites = pygame.sprite.Group()
        self.lista_bloques = pygame.sprite.Group()
        self.lista_proyectiles = pygame.sprite.Group()

        for y in range(10, 125, 25):
            for x in range(10, 680, 62):
                bloque = Bloque(self.lista_colores[random.randint(0, 3)])
                bloque.position(x, y)
                self.lista_bloques.add(bloque)
                self.lista_sprites.add(bloque)

        self.protagonista = Protagonista()
        self.protagonista.rect.y = 470
        self.lista_sprites.add(self.protagonista)

    def procesa_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
                else:
                    proyectil = Proyectil(self.protagonista.get_color())
                    proyectil.rect.x = (self.protagonista.rect.x + self.protagonista.image.get_width() / 2) - 4
                    proyectil.rect.y = self.protagonista.rect.y
                    self.lista_sprites.add(proyectil)
                    self.lista_proyectiles.add(proyectil)
                    self.protagonista.change_color(self.lista_colores[random.randint(0, 3)])

        return False

    def logica_ejecucion(self):
        if not self.game_over:
            self.lista_sprites.update()
            for proyectil in self.lista_proyectiles:
                lista_bloques_alcanzados = pygame.sprite.spritecollide(proyectil, self.lista_bloques, False)

                for bloque in lista_bloques_alcanzados:
                    self.lista_proyectiles.remove(proyectil)
                    self.lista_sprites.remove(proyectil)
                    if proyectil.get_color() == bloque.get_color():
                        self.lista_sprites.remove(bloque)
                        self.lista_bloques.remove(bloque)
                        self.puntuacion += 1

                if proyectil.rect.y < -10:
                    self.lista_proyectiles.remove(proyectil)
                    self.lista_sprites.remove(proyectil)
            if len(self.lista_bloques) == 0:
                self.game_over = True

    def display_frame(self, pantalla):
        pantalla.fill(COLOR_FONDO)
        if self.game_over:
            fuente = pygame.font.SysFont("Dimitri Swank", 45)
            texto = fuente.render("..::BREAK-BLOCKs::..", True, AMARILLO)
            centrar_x = (ANCHO_PANTALLA // 2) - (texto.get_width() // 2)
            centrar_y = (ALTO_PANTALLA // 2) - (texto.get_height() // 2)
            pantalla.blit(texto, [centrar_x, centrar_y])
            fuente = pygame.font.SysFont("Dimitri Swank", 25)
            texto = fuente.render("Haz click para volver a jugar", True, AMARILLO)
            centrar_x = (ANCHO_PANTALLA // 2) - (texto.get_width() // 2)
            pantalla.blit(texto, [centrar_x, centrar_y + 50])

        if not self.game_over:
            self.lista_sprites.draw(pantalla)
        pygame.display.flip()


def main():
    pygame.init()

    dimensiones = [ANCHO_PANTALLA, ALTO_PANTALLA]
    pantalla = pygame.display.set_mode(dimensiones)

    pygame.display.set_caption(".::BREAK-BLOCK::.")
    #pygame.mouse.set_visible(False)
    game_loop = False
    reloj = pygame.time.Clock()

    juego = Juego()

    while not game_loop:
        game_loop = juego.procesa_eventos()
        juego.logica_ejecucion()
        juego.display_frame(pantalla)
        reloj.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()