import pygame
import random
import Moneda
from Enemigo import Enemigo
import Protagonista

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
COLOR_FUENTE = (255, 122, 88)
# FONDO = (43, 109, 216)
FONDO = (2, 8, 34)


def dibujarTexto(screen, texto, pos):
    fuente = pygame.font.SysFont('Barber Street_PersonalUseOnly', 100)
    text = fuente.render(texto, 1, COLOR_FUENTE)
    screen.blit(text, pos)


def dibujar_marcador(screen, texto, pos):
    fuente = pygame.font.SysFont('Impact', 30)
    text = fuente.render(texto, 1, COLOR_FUENTE)
    screen.blit(text, pos)


def colisiono(mouse, objeto):
    if (objeto[0] < mouse[0] < objeto[0] + objeto[2]) and (objeto[1] < mouse[1] < objeto[1] + objeto[3]):
        return True
    return False


def boton(pos, texto, press):
    if press:
        boton_normal = pygame.image.load("../image/buttonLong_beige_pressed.png").convert()
    else:
        boton_normal = pygame.image.load("../image/buttonLong_beige.png").convert()
    boton_normal.set_colorkey(NEGRO)
    picture = pygame.transform.scale(boton_normal, [235, 50])
    pantalla.blit(picture, pos)
    fuente = pygame.font.SysFont('Impact', 35)
    text = fuente.render(texto, 1, COLOR_FUENTE)
    pantalla.blit(text, [pos[0] + 10, pos[1]])
    return [pos[0], pos[1], 235, 50]


def crearbloques(cantidad):
    for i in range(cantidad):
        moneda = Moneda.Moneda(imageEnergia, dimensiones)
        moneda.rect.x = random.randrange(dimensiones[0])
        moneda.rect.y = random.randrange(dimensiones[1])
        moneda.cambio_x = random.randrange(-2, 7)
        moneda.cambio_y = random.randrange(-2, 7)
        listaBloques.add(moneda)
        listaSprites.add(moneda)


def crearEnemigos():
    enemigo = Enemigo(imageEnemigo, dimensiones)
    listaEnemigos.add(enemigo)
    listaSprites.add(enemigo)


def nuevo_juego():
    crearbloques(50)
    crearEnemigos()
    listaSprites.add(protagonista)


def main():
    game_over = False

    marcador = 0
    perdiste = 0
    btnJugar = None

    nuevo_juego()
    btn_jugar_click = False

    pygame.mouse.set_pos(dimensiones[0] - 20, dimensiones[1] - 20)
    pygame.mixer.music.play()
    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            elif evento.type == pygame.USEREVENT:
                pygame.mixer.music.play()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                btn_jugar_click = colisiono(pos, btnJugar)
            if evento.type == pygame.MOUSEBUTTONUP:
                btn_jugar_click = False

        pantalla.fill(FONDO)
        pos = pygame.mouse.get_pos()

        protagonista.rect.x = pos[0]
        protagonista.rect.y = pos[1]

        listaImpactos = pygame.sprite.spritecollide(protagonista, listaBloques, True)
        if pygame.sprite.spritecollide(protagonista, listaEnemigos, True):
            listaSprites.empty()
            listaBloques.empty()
            perdiste = True
        if perdiste:
            dibujarTexto(pantalla, "Game Over", [310, 300])
            if btn_jugar_click:
                boton([390, 400], "Jugar de nuevo", True)
                nuevo_juego()
                perdiste = False
                marcador = 0
            else:
                btnJugar = boton([390, 400], "Jugar de nuevo", False)
        for bloque in listaImpactos:
            sonidoEnergia.play()
            marcador += 1
        if marcador == 50:
            dibujarTexto(pantalla, "You Win", [330, 300])
            listaSprites.empty()
            listaBloques.empty()
            listaEnemigos.empty()
            if btn_jugar_click:
                boton([390, 400], "Jugar de nuevo", True)
                nuevo_juego()
                marcador = 0
            else:
                btnJugar = boton([390, 400], "Jugar de nuevo", False)

        listaBloques.update()
        listaEnemigos.update()
        dibujar_marcador(pantalla, str(marcador), [760, 30])
        listaSprites.draw(pantalla)

        reloj.tick(60)
        pygame.display.flip()


pygame.init()
dimensiones = [900, 700]

pantalla = pygame.display.set_mode(dimensiones)
# pygame.mouse.set_visible(False);
imagePersonaje = "../image/planet-3.png"
imageEnergia = "../image/powerupYellow_bolt.png"
imageEnemigo = "../image/p2.png"
sonidoEnergia = pygame.mixer.Sound("../sound/coin2.wav")
pygame.mixer.music.load('../sound/Nowhere_Land.mp3')
listaBloques = pygame.sprite.Group()
listaSprites = pygame.sprite.Group()
listaEnemigos = pygame.sprite.Group()
protagonista = Protagonista.Protagonista(imagePersonaje)
btn_jugar_click = False
game_over = False
reloj = pygame.time.Clock()
while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            btn_jugar_click = colisiono(pos, btnJugar)
        if evento.type == pygame.MOUSEBUTTONUP:
            btn_jugar_click = False

    pantalla.fill(FONDO)
    dibujarTexto(pantalla, "Recolector Espacial", [170, 300])
    pygame.draw.rect(pantalla, [200, 240, 30], [10, 10, dimensiones[0] - 20, dimensiones[1] - 20], 10)
    if btn_jugar_click:
        boton([350, 450], "   Nuevo Juego", True)
        main()
        break
    else:
        btnJugar = boton([350, 450], "   Nuevo Juego", False)
    reloj.tick(60)
    pygame.display.flip()

pygame.quit()
