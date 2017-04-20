import pygame

NEGRO = (0, 0, 0)

pygame.init()

pantalla = pygame.display.set_mode([500, 400])
pygame.display.set_caption("Imagenes y sonido")

reloj = pygame.time.Clock()
pygame.mouse.set_visible(False)

imagen_fondo = pygame.image.load("images/saturn.jpg").convert()
imagen_protagonista = pygame.image.load("images/player.png").convert()
imagen_protagonista.set_colorkey(NEGRO)
pulsar_sonido = pygame.mixer.Sound("sound/laser4.wav")
pygame.mixer.music.load('sound/little town-orchestral.ogg')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

game_over = False
while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pulsar_sonido.play()
        elif evento.type == pygame.constants.USEREVENT:
            pygame.mixer.music.load('sound/MainTheme.wav')
            pygame.mixer.music.play()
    posicion_jugador = pygame.mouse.get_pos()
    pantalla.fill([255, 255, 255])
    """"""""""""""""""""""""""
    pantalla.blit(imagen_fondo, [0, 0])
    pantalla.blit(imagen_protagonista, posicion_jugador)
    """"""""""""""""""""""""""
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()