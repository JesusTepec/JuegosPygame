import pygame
import random
import Rectangulo
import ellipse


FONDO = (14, 16 ,30)
cantidad_particulas = 50

def creaParticulas(x, y):
    particulasLista = []
    '''
    for i in range(cantidad_particulas):
        rectangulo = Rectangulo.Rectangulo()
        rectangulo.color = colorAleatorio()
        particulasLista.append(rectangulo)
    '''
    for i in range(cantidad_particulas):
        elipse = ellipse.Elipse()
        elipse.x = random.randrange(x - 10, x + 10)
        elipse.y = random.randrange(y - 10, y + 10)
        elipse.color = colorAleatorio()
        particulasLista.append(elipse)
    return particulasLista

def colorAleatorio():
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    return (r, g, b)
pygame.init()

def reasignaPosicion(i):
    ''' Resigna aleatoreamente las posiciones'''
    lista_particulas[i].x = random.randrange(dimensiones[0])
    lista_particulas[i].moveX = random.randrange(-3, 3)
    lista_particulas[i].y = random.randrange(dimensiones[1])
    lista_particulas[i].moveY = random.randrange(-3, 3)


dimensiones = [700,500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Particles")

hecho = False

reloj = pygame.time.Clock()

lista_particulas = []

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            x, y = evento.pos
            lista_particulas.append(creaParticulas(x, y))
    # ---

    # ---
    pantalla.fill(FONDO)
    #---
    i = 0
    for sub_lista in lista_particulas:
        j = 0
        for particula in sub_lista:
            particula.draw(pantalla)
            particula.update()
            if particula.x > dimensiones[0] or particula.x < 0:
                lista_particulas[i].pop(j)
            if particula.y > dimensiones[1] or particula.y < 0:
                lista_particulas[i].pop(j)
            if particula.moveX == 0 or particula.moveY == 0:
                lista_particulas[i].pop(j)
            j += 1
        if(len(sub_lista) == 0):
            lista_particulas.pop(i)
        i += 1

    #---
    pygame.display.flip()
    reloj.tick(30)
pygame.quit()
