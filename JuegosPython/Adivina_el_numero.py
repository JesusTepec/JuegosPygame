# -*- coding: utf-8 -*-
import random

intentosRealizados = 0

print('Hola! Cual es tu nombre?')
miNombre = raw_input()
numero = random.randint(1, 20)
print("Muy bien, " + miNombre + ", estoy pensado un numero entre 1 y 20")

while intentosRealizados < 6:
    print('adivina el numero.')
    intento = input()
    intento = int(intento)

    intentosRealizados = intentosRealizados + 1

    if intento < numero:
        print('Tu numero es muy pequeño.')

    if intento > numero:
        print('Tu numero es muy grande.')

    if intento == numero:
        break

if intento == numero:
    intentosRealizados = str(intentosRealizados)
    print 'Bien echo, ' + miNombre + ' has adivinado mi numero en ',
    print intentosRealizados + ' intentos!'

if intento != numero:
    number = str(numero)
    print('Lo siento, el numero que estaba pensado es: ' + number)