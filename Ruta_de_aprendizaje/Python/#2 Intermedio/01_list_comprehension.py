# Tema: List Comprehension o Comprensión de listas


"""
List Comprehension o Comprensión de listas
>>> La comprensión de listas es una forma concisa de crear listas. Además, es más rápida que la creación de listas con un bucle for. Y tambien se puede utilizar para crear conjuntos, tuplas y diccionarios.

>>> Las listas son una de las estructuras de datos más utilizadas en Python y la comprensión de listas es una forma de crear listas de forma concisa.

Estructura:
[expresión for elemento in iterable]
"""

# Ejemplo 1 con datos int
lista: list[int] = [0, 1, 2, 3, 4, 5, 6, 7]
print(f"{lista}", end="\n")

rango: range = range(8)
print(f"list(rango) -> {list(rango)}", end="\n")
print(f"type(rango) -> {type(rango)}", end="\n")

# Definición

lista_comprimida: list[int] = [int(iterable) + 1 for iterable in range(0, 8, 1)]
print(f"lista comprimida = {lista_comprimida}", end="\n")

lista_comprimida: list[int] = [int(iterable) * 2 for iterable in range(0, 8, 1)]
print(f"lista comprimida = {lista_comprimida}", end="\n")

lista_comprimida: list[int] = [int(iterable) * iterable for iterable in range(0, 8, 1)]
print(f"lista comprimida = {lista_comprimida}", end="\n")


def sumarCinco(numero: int) -> int:
    return numero + 5


# Tambien se pueden utilizar funciones en la comprensión de listas

lista_comprimida: list[int] = [
    sumarCinco(numero=int(iterable)) for iterable in range(0, 8, 1)
]
print(f"lista comprimida = {lista_comprimida}", end="\n")

conjuntos_comprimidos: set[int] = {int(iterable) for iterable in range(0, 8, 1)}
print(f"conjuntos comprimidos = {conjuntos_comprimidos}", end="\n")

tuplas_comprimidas: tuple[int] = tuple(int(iterable) for iterable in range(0, 8, 1))
print(f"tuplas comprimidas = {tuplas_comprimidas}", end="\n")

diccionario_comprimido: dict[int, int] = {
    int(iterable): int(iterable) for iterable in range(0, 8, 1)
}
print(f"diccionario comprimido = {diccionario_comprimido}", end="\n")


# Ejemplo 2 con datos str

lista: list[str] = ["hola", "mundo", "como", "estas"]
print(f"{lista}", end="\n")

lista_comprimida: list[str] = [str(iterable) for iterable in lista]
print(f"lista comprimida = {lista_comprimida}", end="\n")

tuplas_comprimidas: tuple[str] = tuple(str(iterable) for iterable in lista)

print(f"tuplas comprimidas = {tuplas_comprimidas}", end="\n")

conjuntos_comprimidos: set[str] = {str(iterable) for iterable in lista}

print(f"conjuntos comprimidos = {conjuntos_comprimidos}", end="\n")

diccionario_comprimido: dict[str, str] = {
    str(iterable): str(iterable) for iterable in lista
}
print(f"diccionario comprimido = {diccionario_comprimido}", end="\n")


"""
tambien se pueden utilizar condicionales en la comprensión de listas
"""

lista_comprimida: list[int] = [
    int(iterable) for iterable in range(0, 8, 1) if iterable % 2 == 0
]
print(f"lista comprimida = {lista_comprimida}", end="\n")

tuplas_comprimidas: tuple[int] = tuple(
    int(iterable) for iterable in range(0, 8, 1) if iterable % 3 == 0
)

print(f"tuplas comprimidas = {tuplas_comprimidas}", end="\n")

conjuntos_comprimidos: set[int] = {
    int(iterable) for iterable in range(0, 8, 1) if iterable % 4 == 0
}

print(f"conjuntos comprimidos = {conjuntos_comprimidos}", end="\n")

diccionario_comprimido: dict[int, int] = {
    int(iterable): int(iterable) for iterable in range(0, 8, 1) if iterable % 5 == 0
}

lista_buena: list[int] = ["b", "c", "d", "a", "i"]
lista_mala: list[str] = ["a", "e", "i", "o", "u"]
"""
Lo que estas haciendo es recorrer la lista_mala y si el elemento esta en la lista_buena lo agregas a la lista_comprimida
"""
lista_comprimida: list[str] = [
    str(iterable) for iterable in lista_mala if iterable in lista_buena
]

print(f"lista comprimida = {lista_comprimida}", end="\n")

tuplas_comprimidas: tuple[str] = tuple(
    str(iterable) for iterable in lista_mala if iterable in lista_buena
)

print(f"tuplas comprimidas = {tuplas_comprimidas}", end="\n")

conjuntos_comprimidos: set[str] = {
    str(iterable) for iterable in lista_mala if iterable in lista_buena
}

print(f"conjuntos comprimidos = {conjuntos_comprimidos}", end="\n")

diccionario_comprimido: dict[str, str] = {
    str(iterable): str(iterable) for iterable in lista_mala if iterable in lista_buena
}

"""
tambien se pueden pasar estructuras anidadas en la comprensión de listas aunque no es tan común
"""
"""
En este caso estamos creando una lista de listas de enteros
En la primera iteración se crea una lista de enteros del 0 al 7 y se agrega a la lista_comprimida
En la segunda iteración se dice que se repita la primera iteración 3 veces creando una lista de listas de enteros

se puede crear otra variable o utilizar la misma variable para la comprensión de listas si una variable no se utiliza se puede utilizar el guion bajo
"""
lista_comprimida: list[list[int]] = [
    [int(iterable) for iterable in range(0, 8, 1)] for _ in range(0, 3, 1)
]
print(f"lista comprimida = {lista_comprimida}", end="\n")

tuplas_comprimidas: tuple[tuple[int]] = tuple(
    [tuple(int(iterable) for iterable in range(0, 8, 1)) for _ in range(0, 3, 1)]
)

print(f"tuplas comprimidas = {tuplas_comprimidas}", end="\n")
