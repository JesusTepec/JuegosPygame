personas = []
print("Ingresa los siguientes datos.")
for i in range(2):
    nombre = raw_input("Nombre: ")
    personas.append([nombre, 2])

for i in range(len(personas)):
    print(personas[i])