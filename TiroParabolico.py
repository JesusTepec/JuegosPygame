import pygame
import math

black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
background = (200, 200, 200)


def printos(surface, text, x, y, color, font):
    text_in_lines = text.split('\n')
    for line in text_in_lines:
        new = font.render(line, 1, color)
        surface.blit(new, (x, y))
        y += new.get_height()


def arrow(screen, color, x, y, ang):
    pygame.draw.line(screen, color, (x, y),
    (x + 20 * math.cos(math.radians(ang + 150.0)),
    y - 20 * math.sin(math.radians(ang + 150.0))))

    pygame.draw.line(screen, color, (x, y),
    (x + 20 * math.cos(math.radians(ang + 210.0)),
    y - 20 * math.sin(math.radians(ang + 210.0))))


def vector(screen, color, x, y, ang):
    w = x + v0 * 10 * math.cos(math.radians(ang))
    z = y - v0 * 10 * math.sin(math.radians(ang))
    x, y, w, z = int(x), int(y), int(w), int(z)
    arrow(screen, color, w, z, ang)
    pygame.draw.line(screen, blue, (x, y), (w, z))


pygame.init()

size = width, height = 640, 480

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Inicializar")


radio = 10
x = 10
y = height - radio

pygame.font.init()
font = pygame.font.Font(None, 30)

clock = pygame.time.Clock()

t = 0.0
dt = 0.5

v0 = 25.0
a = 1.0
ang = 45.0

vx = 0
vy = 0

lock = True
lock1 = False
second = False
gameOver = False
while not gameOver:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    teclado = pygame.key.get_pressed()
    if(tuple(set(teclado)) == (0, 1) and lock):
        if (teclado[pygame.K_UP]):
            ang += 1
            if(ang >= 90):
                ang = 90
        if (teclado[pygame.K_DOWN]):
            ang -= 1
            if(ang < 0):
                ang = 0
        if (teclado[pygame.K_RIGHT] and v0 < 100):
            v0 += 1
        if (teclado[pygame.K_LEFT] and v0 > 1):
            v0 -= 1
        if (teclado[pygame.K_SPACE]):
            lock = False
            lock1 = True
            vy0 = v0*math.sin(math.radians(ang))
    if (teclado[pygame.K_ESCAPE]):
        break
    vx0 = v0*math.cos(math.radians(ang))
    vy = a*t - v0*math.sin(math.radians(ang))
    if(lock1):
        y = (height - radio) - vy0*t + .5*a*(t**2)
        x = radio + vx0*t
        t += dt
        if(y > (height - radio)):
            y = height - radio
            t = 0
            lock1 = False
            second = True
    if(second):
        printos(screen, "Continue? Y/N", 0, 60, green, font)
        if(teclado[pygame.K_y]):
            lock = True
            second = False
            x = radio
        elif(teclado[pygame.K_n]):
            break

    printos(screen, "x = %d y = %d ang = %d v0 = %d vx = %d vy = %d"%(x - radio, height - radio - y, ang, v0, vx0, vy), 0, 0, green, font)
    pygame.draw.circle(screen, blue, (int(x), int(y)), radio)
    vector(screen, blue, x, y, ang)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()