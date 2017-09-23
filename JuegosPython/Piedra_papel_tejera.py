#encoding:UTF-8
import random

aleatorio = random.randrange(0, 3)
elijePc = ""
print("1)Piedra")
print("2)Papel")
print("3)Tijera")
opcion = int(input("Que elijes: "))

if opcion == 1:
    elijeUsuario = "piedra"
elif opcion == 2:
    elijeUsuario = "papel"
elif opcion == 3:
    elijeUsuario = "tijera"
print("Tu elijes: " + elijeUsuario)

if aleatorio == 0:
    elijePc = "piedra"
elif aleatorio == 1:
    elijePc = "papel"
elif aleatorio == 2:
    elijePc = "tijera"
print("PC elijio: " + elijePc)

print("...")
if elijePc == "piedra" and elijeUsuario == "papel":
    print("Ganaste, papel envulve piedra")
elif elijePc == "papel" and elijeUsuario == "tijera":
    print("Ganaste, Tijera corta papel")
elif elijePc == "tijera" and elijeUsuario == "piedra":
    print("Ganaste, Piedra pisa tijera")
if elijePc == "papel" and elijeUsuario == "piedra":
    print("perdiste, papel envulve piedra")
elif elijePc == "tijera" and elijeUsuario == "papel":
    print("perdiste, Tijera corta papel")
elif elijePc == "piedra" and elijeUsuario == "tijera":
    print("perdiste, Piedra pisa tijera")
elif elijePc == elijeUsuario:
    print("empate")