import pygame

ROJO = (255, 0, 0)


def main():
    pygame.init()
    size = (400, 500)
    pos = [-100, -100]
    pantalla = pygame.display.set_mode(size)
    pygame.display.set_caption("Click mouse")
    #pygame.mouse.set_visible(False)
    reloj = pygame.time.Clock()
    game_over = False
    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            pos = pygame.mouse.get_pos()
        pantalla.fill((255, 255, 255))
        pygame.draw.rect(pantalla, ROJO, [pos[0], pos[1], 10, 22], 0)
        pygame.display.flip()
        reloj.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()