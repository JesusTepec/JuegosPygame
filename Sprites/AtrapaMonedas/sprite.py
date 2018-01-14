import pygame
import random
import Moneda
import Enemigo

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
COLOR_FUENTE = (255, 122, 88)
#FONDO = (43, 109, 216)
FONDO = (2, 8, 34)


def dibujarTexto(screen, texto, pos):
    fuente = pygame.font.SysFont('Barber Street_PersonalUseOnly', 100)
    text = fuente.render(texto, 1, COLOR_FUENTE)
    screen.blit(text, pos)

def dibujarMarcador(screen, texto, pos):
    fuente = pygame.font.SysFont('Impact', 30)
    text = fuente.render(texto, 1, COLOR_FUENTE)
    screen.blit(text, pos)

def colisiono(mouse, objeto):
    if (mouse[0] > objeto[0] and mouse[0] < objeto[0] + objeto[2]) and (mouse[1] > objeto[1] and mouse[1] < objeto[1] + objeto[3]):
        return True
    return False

def boton(pos, texto, press):
    if(press):
        botonNormal = pygame.image.load("../image/buttonLong_beige_pressed.png").convert()
    else:
        botonNormal = pygame.image.load("../image/buttonLong_beige.png").convert()
        botonNormal.set_colorkey(NEGRO)
        picture = pygame.transform.scale(botonNormal, [235, 50])
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
        moneda.cambio_x = random.randrange(-2,7)
        moneda.cambio_y = random.randrange(-2,7)
        listaBloques.add(moneda)
        listaSprites.add(moneda)

def crearEnemigos():
    enemigo = Enemigo.Enemigo(imageEnemigo, dimensiones)
    listaEnemigos.add(enemigo)
    listaSprites.add(enemigo)
pygame.init()
dimensiones = [900, 700]

pantalla = pygame.display.set_mode(dimensiones)
#pygame.mouse.set_visible(False);
imagePersonaje = "../image/planet-3.png";
imageEnergia = "../image/powerupYellow_bolt.png";
imageEnemigo = "../image/p2.png";
sonidoEnergia = pygame.mixer.Sound("../sound/coin2.wav")
pygame.mixer.music.load('../sound/Nowhere_Land.mp3')
listaBloques = pygame.sprite.Group()
listaSprites = pygame.sprite.Group()
listaEnemigos = pygame.sprite.Group()
crearbloques(50)
crearEnemigos()
pygame.mixer.music.play()

protagonista = Moneda.Moneda(imagePersonaje, dimensiones)
listaSprites.add(protagonista)


game_over = False

reloj = pygame.time.Clock()
marcador = 0
perdiste = 0
btnJugarClick = False
btnJugar = None

while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
        elif evento.type == pygame.constants.USEREVENT:
            pygame.mixer.music.play()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            btnJugarClick = colisiono(pos, btnJugar)
        if evento.type == pygame.MOUSEBUTTONUP:
            btnJugarClick = False

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
    for bloque in listaImpactos:
        sonidoEnergia.play()
        marcador += 1
    if marcador == 50:
        dibujarTexto(pantalla, "You Win", [330, 300])
        listaSprites.empty()
        listaBloques.empty()
        listaEnemigos.empty()
        if(btnJugarClick):
            boton([390, 400], "Jugar de nuevo", True)
        else:
            btnJugar = boton([390, 400], "Jugar de nuevo", False)

    listaBloques.update()
    listaEnemigos.update()
    dibujarMarcador(pantalla, str(marcador), [760, 30])
    listaSprites.draw(pantalla)

    reloj.tick(60)

    pygame.display.flip()


pygame.quit()
