import pygame
import random
import Rectangulo

FONDO = (14, 16, 30)
cantidad_particulas = 50

def creaParticulas(x, y):
    particulasLista = []
    for i in range(cantidad_particulas):
        rectangulo = Rectangulo.Rectangulo()
        rectangulo.x = x
        rectangulo.y = y
        rectangulo.color = colorAleatorio()
        particulasLista.append(rectangulo)
    return particulasLista

def colorAleatorio():
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    return (r, g, b)

def posicionAleatoria():
    return [random.randrange(700), random.randrange(500)]


def reasignaPosicion():
    lista_particulas[i].x = random.randrange(dimensiones[0])
    lista_particulas[i].move_x = random.randrange(-4, 5)
    lista_particulas[i].y = random.randrange(dimensiones[1])
    lista_particulas[i].move_y = random.randrange(-4, 5)

def main():
    """Funcion Principal"""
    pygame.init()
    dimensiones = [700, 500]
    pantalla = pygame.display.set_mode(dimensiones)
    pygame.display.set_caption("Particulas")
    hecho = False

    lista_particulas = []
    x, y = posicionAleatoria()
    lista_particulas.append(creaParticulas(x, y))

    reloj = pygame.time.Clock()
    while not hecho:
        for evento in pygame.event.get():
           if evento.type == pygame.QUIT:
               hecho = True
           elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
               x, y = evento.pos
               lista_particulas.append(creaParticulas(x, y))
        pantalla.fill(FONDO)

        i = 0
        for sub_lista in lista_particulas:
            j = 0
            for particula in sub_lista:
                particula.draw(pantalla)
                particula.mover()
                if particula.x > dimensiones[0] or particula.x < 0 or particula.y > dimensiones[1] or particula.y < 0 or particula.move_x == 0 or particula.move_y == 0:
                    lista_particulas[i].pop(j)
                j += 1
            if(len(sub_lista) == 0):
                x, y = posicionAleatoria()
                lista_particulas[i] = creaParticulas(x, y)
            i += 1
        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
