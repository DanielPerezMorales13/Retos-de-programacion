# Tema: Listas

# Definición

"""
Las listas son una colección de elementos ordenados que se pueden modificar y eliminar y que pueden tener elementos de diferentes tipos

Ventajas de las listas:
- Se pueden modificar
- Se pueden eliminar
- Se pueden ordenar
- Se pueden invertir
- Se pueden copiar
- Se pueden crear sublistas
- Se pueden concatenar
- Se pueden desempaquetar
- Se pueden crear listas vacias
- Se pueden crear listas con elementos de diferentes tipos
- Se pueden crear listas con elementos repetidos

Desventajas de las listas:
- El acceso a los elementos es mas lento que en las tuplas
- Ocupan mas espacio en memoria que las tuplas
- No se pueden utilizar como claves en un diccionario porque son mutables
- No se pueden utilizar como elementos de una lista porque son mutables

Mutables: Son los objetos que se pueden modificar
Inmutables: Son los objetos que no se pueden modificar
"""

lista: list = list()
otra_lista: list = []

print(len(lista), end="\n")

lista: list[int] = [35, 24, 62, 52, 30, 30, 17]

print(lista, end="\n")
print(len(lista), end="\n")

otra_lista: list[int, float, str] = [35, 1.77, "Daniel", "Perez"]

print(type(lista), end="\n")
print(type(otra_lista), end="\n")

# Acceso a elementos y búsqueda de elementos mediante índices
"""
Los índices son la posición de un elemento dentro de una lista
Ejemplo:
lista = [35, 24, 62, 52, 30, 30, 17]
para acceder al elementos:
35 usamos el índice positivo 0 o el indice negativo -7
24 usamos el índice positivo 1 o el indice negativo -6
62 usamos el índice positivo 2 o el indice negativo -5
52 usamos el índice positivo 3 o el indice negativo -4
30 usamos el índice positivo 4 o el indice negativo -3
30 usamos el índice positivo 5 o el indice negativo -2
17 usamos el índice positivo 6 o el indice negativo -1

Los índices pueden ser positivos o negativos
Los índices positivos empiezan desde 0
Los índices negativos empiezan desde -1
"""

print(otra_lista[0], end="\n")
print(otra_lista[1], end="\n")
print(otra_lista[-1], end="\n")
print(otra_lista[-4], end="\n")
# .count() devuelve el número de veces que aparece un elemento en una lista puede ser un número o una cadena
print(lista.count(30))
# print(otra_lista[4]) Si el índice no existe en la lista IndexError
# print(otra_lista[-5]) Si el índice no existe en la lista genera un error IndexError

print(otra_lista.index("Daniel"), end="\n")

# Desempaquetado de listas
"""
otra_lista = [35, 1.77, "Daniel", "Perez"]
edad:int = 35
ancho:float = 1.77
nombre:str = "Daniel"
segundo_nombre:str = "Perez"
"""
edad, ancho, nombre, segundo_nombre = otra_lista
print(nombre, end="\n")

# Otra forma de desempaquetar listas es:
nombre, ancho, edad, segundo_nombre = (
    otra_lista[2],
    otra_lista[1],
    otra_lista[0],
    otra_lista[3],
)
print(edad, end="\n")

# Concatenación de listas

# Al hacer una suma de listas se concatenan
# [35, 24, 62, 52, 30, 30, 17] + [35, 1.77, "Daniel", "Perez"]
# [35, 24, 62, 52, 30, 30, 17, 35, 1.77, "Daniel", "Perez"]
print(lista + otra_lista, end="\n")
# print(lista - otra_lista) No se puede restar listas SyntaxError

# Creación, inserción, actualización y eliminación

# El metodo append() agrega un elemento al final de la lista
otra_lista.append("Daniel")
print(otra_lista, end="\n")

# El metodo insert() agrega un elemento en la posición que se le indique
# insert(posición, elemento)
"""
otra_lista = [35, 1.77, "Daniel", "Perez"]

otra_lista.insert(1, "Rojo")
otra_lista = [35, "Rojo", 1.77, "Daniel", "Perez"]
"""
otra_lista.insert(1, "Rojo")
print(otra_lista, end="\n")

# Cambiar un elemento de la lista mediante su índice
"""
otros_lista = [35, "Rojo", 1.77, "Daniel", "Perez"]

lista  35  "Rojo"  1.77  "Daniel"  "Perez"
indice  0     1      2       3         4

otra_lista[1] = "Azul"
otra_lista = [35, "Azul", 1.77, "Daniel", "Perez"]

"""
otra_lista[1] = "Azul"
print(otra_lista, end="\n")


# El metodo remove() elimina un elemento de la lista mediante su valor si hay más de un elemento con el mismo valor elimina el primero que encuentre si no encuentra el elemento genera un error ValueError.
otra_lista.remove("Azul")
print(otra_lista, end="\n")

lista.remove(30)
print(lista, end="\n")

# El metodo pop() elimina un elemento de la lista mediante su índice si no se le indica un índice elimina el último elemento de la lista

# lista.pop(-1) es lo mismo que lista.pop() elimina el último elemento de la lista
# lista.pop(0) elimina el primer elemento de la lista
# lista.pop(2) elimina el elemento en la posición 2 de la lista
# lista.pop(3) elimina el elemento en la posición 3 de la lista
print(lista.pop(), end="\n")
print(lista, end="\n")

# Se puede guardar el elemento que se elimina en una variable de esta forma
pop_elemento = lista.pop(2)
print(pop_elemento, end="\n")
print(lista, end="\n")

# la palabra reservada del elimina una variable o un elemento de una lista mediante su índice
del lista[2]
print(lista, end="\n")

# Operaciones con listas

nueva_lista: list[any] = lista.copy()

# El metodo clear() elimina todos los elementos de una lista y la deja vacia
lista.clear()
print(lista, end="\n")
print(nueva_lista, end="\n")

# El metodo reverse() invierte el orden de los elementos de una lista
# El metodo sort() ordena los elementos de una lista de menor a mayor si la lista tiene elementos de diferentes tipos genera un error TypeError
# El metodo sort() no se puede usar con listas que tengan elementos de diferentes tipos
# Tener en cuenta que sort() ordena las strings basándose en el orden lexicográfico, que puede no coincidir con el orden alfabético si las strings contienen caracteres no alfabéticos.

# El metodo sort() no retorna nada y modifica la lista original. Tiene como parámetros reverse y key. reverse es un booleano que si es True ordena la lista de mayor a menor y si es False ordena la lista de menor a mayor. key es una función que se le pasa como argumento y que se usa para ordenar la lista.
nueva_lista.reverse()

print(nueva_lista, end="\n")

nueva_lista.sort()
print(nueva_lista, end="\n")

# Sublistas

print(nueva_lista[1:3])

# Cambio de tipo de dato
# No todos los lenguages de programación permiten cambiar el tipo de dato de una variable
lista: str = "Hola Python"
print(lista, end="\n")
print(type(lista), end="\n")

"""
[:] Devuelve una copia de la lista completa
[::] Devuelve una copia de la lista completa
[::1] Devuelve una copia de la lista completa
"""
print(nueva_lista[:], end="\n")
print(nueva_lista[::], end="\n")
print(nueva_lista[::1], end="\n")

"""
Con los las listas pasa algo curioso y es que si asignamos una lista a otra lista y cambiamos un elemento de la lista original se cambia en la lista copia

ejemplo:
lista: list[int] = [1, 2, 3]
copia_lista: list[int] = lista

lista[0] = 4
print(lista) # [4, 2, 3]
print(copia_lista) # [4, 2, 3]

Esto pasa porque las listas son mutables y cuando se asigna una lista a otra lista se asigna la referencia de memoria de la lista original a la lista copia y cuando se cambia un elemento de la lista original se cambia en la lista copia porque ambas listas apuntan a la misma referencia de memoria
"""
