import pygame

FONDO = (30, 155, 255)
ROJO = (232, 47, 28)


def colisiono(mouse, objeto):
    if (mouse[0] > objeto[0] and mouse[0] < objeto[0] + objeto[2]) and (mouse[1] > objeto[1] and mouse[1] < objeto[1] + objeto[3]):
        return True
    return False


def reproducirSonido(audio):
    audio.play()


def buscarPulsado(posMouse, listaRects):
    for cuadro in listaRects:
        if(colisiono(posMouse, cuadro[1] + cuadro[2])):
            reproducirSonido(cuadro[3])


def cargarImages():
    img = []
    img.append(pygame.image.load("images/giraffe.png"))
    img.append(pygame.image.load("images/hippo.png"))
    img.append(pygame.image.load("images/parrot.png"))
    return img


def cargarSonidos():
    sounds = []
    sounds.append(pygame.mixer.Sound('sound/boop.wav'))
    sounds.append(pygame.mixer.Sound('sound/fire.wav'))
    sounds.append(pygame.mixer.Sound('sound/laser4.wav'))
    return sounds

pygame.init()

dimensiones = [400, 300]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption(" Click Play Sound")
imgs = cargarImages()
sounds = cargarSonidos()
listaRects = [
    [imgs[0],[20, 20], [80, 80], sounds[0]],
    [imgs[1],[125, 50], [100, 100], sounds[1]],
    [imgs[2], [230, 150], [120, 120], sounds[2]]
]

game_over = False
reloj = pygame.time.Clock()

while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
        if evento.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            buscarPulsado(pos, listaRects)
    pantalla.fill(FONDO)
    for cuadro in listaRects:
        picture = pygame.transform.scale(cuadro[0], cuadro[2])
        pantalla.blit(picture, cuadro[1])
    pygame.display.flip()
    reloj.tick(10)

pygame.quit()
