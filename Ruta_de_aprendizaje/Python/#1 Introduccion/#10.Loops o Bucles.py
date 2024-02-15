# Tema: Loops o bucles

# While

"""
El while es un bucle que se ejecuta mientras se cumpla una condición y se detiene cuando la condición no se cumple más 
"""
condicion: int = 0

while condicion < 10:
    print(condicion, end="\n")
    condicion += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10", end="\n")

print("La ejecución continúa", end="\n")

"""
Si queremos detener la ejecución del bucle while podemos usar la palabra reservada break que se utiliza para detener la ejecución del bucle
"""

# Bucle infinito
while True:
    print("Esto es un bucle infinito que se detiene con break", end="\n")
    break

while condicion < 20:
    condicion += 1
    if condicion == 15:
        print("Se detiene la ejecución", end="\n")
        break
    print(condicion, end="\n")

print("La ejecución continúa", end="\n")

# For
"""
for es una palabra reservada de python que se utiliza para hacer bucles o loops que se ejecutan mientras haya elementoos en un iterable y se detienen cuando no hay más elementoos en el iterable. Un iterable es un objeto que se puede recorrer elementoo a elementoo. Los iterables pueden ser listas, tuplas, sets, diccionarios, etc.
"""
lista: list[int] = [35, 24, 62, 52, 30, 30, 17]

"""
la estructura de un for es la siguiente 
>>> for es una palabra reservada de python que se utiliza para hacer bucles o loops

>>> elemento es una variable que se utiliza para almacenar el elemento del iterable puede tener cualquier nombre que no sea una palabra reservada de python

>>> in es el operador de pertenencia que se utiliza para saber si un elemento pertenece a un iterable o no. Pero también se puede utilizar para recorrer un iterable asignando cada elemento a una variable que se puede utilizar dentro del bucle

>>> lista es el iterable que se va a recorrer
"""
for elemento in lista:
    print(elemento, end="\n")

tupla: tuple[int, str] = (35, 1.77, "Daniel", "Perez", "Daniel")

for elemento in tupla:
    print(elemento, end="\n")

conjunto: set[str, int] = {"Daniel", "Moure", 35}

for elemento in conjunto:
    print(elemento, end="\n")

diccionario: dict[str, str | int] = {
    "Nombre": "Daniel",
    "Apellido": "Moure",
    "Edad": 35,
    1: "Python",
}

for elemento in diccionario:
    print(elemento, end="\n")
    if elemento == "Edad":
        break
else:
    print("El bluce for para diccionario ha finalizado", end="\n")

print("La ejecución continúa", end="\n")

for elemento in diccionario:
    print(elemento, end="\n")
    if elemento == "Edad":
        continue
    print("Se ejecuta", end="\n")
else:
    print("El bluce for para diccionario ha finalizado", end="\n")
