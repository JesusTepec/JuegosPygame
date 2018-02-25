# G A T O

import random


def dibujarTablero(tablero):
    print('   |   |')
    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
    print('   |   |')


def ingresaLetraJugador():
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('Deseas ser X o O')
        letra = input().upper()
    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def quienComienza():
    if random.randint(0, 1) == 0:
        return 'La compu'
    else:
        return 'El jugador'


def jugarDeNuevo():
    print('Desas volver a jugar? (si/no)?')
    return input().lower().startswith('s')

def hacerJugada(tablero, letra, jugada):
    tablero[jugada] = letra


def esGanador(tablero, letra):
    return ((tablero[7] == letra and tablero[8] == letra and tablero[9] == letra) or
    (tablero[4] == letra and tablero[5] == letra and tablero[6] == letra) or
    (tablero[1] == letra and tablero[2] == letra and tablero[3] == letra) or
    (tablero[7] == letra and tablero[4] == letra and tablero[1] == letra) or
    (tablero[8] == letra and tablero[5] == letra and tablero[2] == letra) or
    (tablero[9] == letra and tablero[8] == letra and tablero[3] == letra) or
    (tablero[7] == letra and tablero[5] == letra and tablero[3] == letra) or
    (tablero[9] == letra and tablero[5] == letra and tablero[1] == letra))


def obtenerDuplicadoTablero(tablero):
    dupTablero = []

    for i in tablero:
        dupTablero.append(i)

    return dupTablero


def hayEspacioLibre(tablero, jugada):
    return tablero[jugada] == ' '


def obtenerJugadaJugador(tablero):
    jugada = ' '
    while jugada not in '1 2 3 4 5 6 7 8 9'.split() or not hayEspacioLibre(tablero, int(jugada)):
        print('Cual es tu proxima jugada? (1-9)')
        jugada = input()
    return int(jugada)

def elegirAzarDeLista(tablero, listaJugada):
    jugadasPosibles = []
    for i in listaJugada:
        if hayEspacioLibre(tablero, i):
            jugadasPosibles.append(i)
    if len(jugadasPosibles) != 0:
        return random.choice(jugadasPosibles)
    else:
        return None

def obtenerJugadaComputadora(tablero, letraComputadora):
    if letraComputadora == 'X':
        letraJugador = 'O'
    else:
        letraJugador = 'X'

    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraComputadora, i)
            if esGanador(copia, letraComputadora):
                return i

    for i in  range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraJugador, i)
            if esGanador(copia, letraJugador):
                return i
    jugada = elegirAzarDeLista(tablero, [1, 3, 7, 9])
    if jugada != None:
        return jugada
    if hayEspacioLibre(tablero, 5):
        return 5
    return elegirAzarDeLista(tablero, [2, 4, 6, 8])

def tableroCompleto(tablero):
    for i in range(1, 10):
        if hayEspacioLibre(tablero, i):
            return False
    return True

print('Bienvenido al juego del gato')
while True:
    elTablero = [' '] * 10
    letraJugador, letraComputadora = ingresaLetraJugador()
    turno = quienComienza()
    print(turno + ' ira primero.')
    juegoEnCurso = True

    while juegoEnCurso:
        if turno == 'El jugador':
            dibujarTablero(elTablero)
            jugada = obtenerJugadaJugador(elTablero)
            hacerJugada(elTablero, letraJugador, jugada)
            if esGanador(elTablero, letraJugador):
                dibujarTablero(elTablero)
                print('Felicidades, has ganado!')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('Es un empate!')
                    break;
                else:
                    turno = 'La computadora'
        else:
            jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
            hacerJugada(elTablero, letraComputadora, jugada)

            if esGanador(elTablero, letraComputadora):
                dibujarTablero(elTablero)
                print('La computadora te ha vencido! Has perdido.')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('Es un empate!')
                    break
                else:
                    turno = 'El jugador'
    if not jugarDeNuevo():
        break