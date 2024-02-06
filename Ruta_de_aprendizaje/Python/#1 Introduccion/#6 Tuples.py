# Tema: Tuplas

# Definición

"""
En python las tuplas son inmutables, es decir, no se pueden modificar, son una colección de elementos ordenados que no se pueden modificar ni eliminar

Ventajas de las tuplas:
- El acceso a los elementos es mas rápido que en las listas
- Ocupan menos espacio en memoria
- Formatean Strings
- Pueden utilizarse como claves en un diccionario
- Pueden utilizarse como elementos de una lista

Desventajas de las tuplas:
- No se pueden modificar
- No se pueden eliminar
- No se pueden ordenar
- No se pueden invertir
- No se pueden copiar
- No se pueden crear sublistas
- No se pueden concatenar
- No se pueden desempaquetar

Mutables: Son los objetos que se pueden modificar
Inmutables: Son los objetos que no se pueden modificar
"""

tupla: tuple = tuple()
otra_tupla = ()

tupla: tuple[int, str] = (35, 1.77, "Daniel", "Perez", "Daniel")
otra_tupla: tuple[int] = (35, 60, 30)

print(tupla, end="\n")
print(type(tupla), end="\n")

# Acceso a elementos y búsqueda

print(tupla[0], end="\n")
print(tupla[-1], end="\n")
# print(tupla[4]) IndexError
# print(tupla[-6]) IndexError

print(tupla.count("Daniel"), end="\n")
print(tupla.index("Perez"), end="\n")
print(tupla.index("Daniel"), end="\n")

# tupla[1] = 1.80 'tuple' object does not support item assignment

# Concatenación

sumar_tuplas: tuple[int, str] = tupla + otra_tupla
print(sumar_tuplas, end="\n")

"""
Tambien se pueden usar el slicing en las tuplas
"""

print("xd = ",sumar_tuplas[3:6], end="\n")

# Tupla mutable con conversión a lista

"""
Para convertir una tupla a lista se utiliza la función list()
Para convertir una lista a tupla se utiliza la función tuple()

"""
tupla: list[int, str] = list(tupla)
print(type(tupla), end="\n")

tupla[4] = "Daniel"
tupla.insert(1, "Azul")
tupla: tuple[int, str] = tuple(tupla)
print(tupla, end="\n")
print(type(tupla), end="\n")

# Eliminación

# del tupla[2] TypeError: 'tuple' object doesn't support item deletion
# Que significa que no se puede eliminar un elemento en una tupla

del tupla
# print(tupla) NameError: name 'tupla' is not defined
# Que significa que no se puede imprimir una tupla que no existe
