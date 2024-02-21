# Tema: Tipos de errores

# SyntaxError
# print "¡Hola python3!" # Descomentar para Error
import math
from math import pi

print("¡Hola comunidad!", end="\n")

# NameError
lenguage: str = "Español"  # Comentar para Error
print(lenguage, end="\n")

# IndexError
lista: list[str] = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(lista[0], end="\n")
print(lista[4], end="\n")
print(lista[-1], end="\n")
# print(lista[5]) # Descomentar para Erro,end="\n"r

# ModuleNotFoundError
# import maths # Descomentar para Error

# AttributeError
# print(math.PI) # Descomentar para Erro,end="\n"r
print(math.pi, end="\n")

# KeyError
diccionario: dict[str : str | int] = {
    "Nombre": "Daniel",
    "Apellido": "PErez",
    "Edad": 18,
    1: "Python",
}
print(diccionario["Edad"], end="\n")
# print(diccionario["Apelido"]) # Descomentar para Erro,end="\n"r
print(diccionario["Apellido"], end="\n")

# TypeError
# print(lista["0"]) # Descomentar para Erro,end="\n"r
print(lista[0], end="\n")
print(lista[False], end="\n")  # False = 0

# ImportError
# from math import PI # Descomentar para Error
print(pi, end="\n")

# ValueError
# integer = int("10 Años")
integer: int = int("10")  # Descomentar para Error
print(type(integer), end="\n")

# ZeroDivisionError
# print(4/0) # Descomentar para Erro,end="\n"r
print(4 / 2, end="\n")
