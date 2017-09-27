import pygame

FONDO = (30, 155, 255)
ROJO = (232, 47, 28)

def cargarImages():
    img = []
    img.append(pygame.image.load("images/giraffe.png"))
    img.append(pygame.image.load("images/hippo.png"))
    img.append(pygame.image.load("images/parrot.png"))
    return img
pygame.init()

dimensiones = [400, 300]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption(" Click Play Sound")
imgs = cargarImages()
listaRects = [
    [imgs[0],[20, 20], [50, 50]],
    [imgs[1],[125, 50], [100, 100]],
    [imgs[2], [230, 150], [120, 120]]
]

game_over = False
reloj = pygame.time.Clock()

while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
        if evento.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

    pantalla.fill(FONDO)
    for cuadro in listaRects:
        #pygame.draw.rect(pantalla, ROJO, cuadro)
        picture = pygame.transform.scale(cuadro[0], cuadro[2])
        pantalla.blit(picture, cuadro[1])
    pygame.display.flip()
    reloj.tick(10)

pygame.quit()
