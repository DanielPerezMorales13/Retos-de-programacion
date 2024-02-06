# Tema: Sets


# Definición

"""
Los sets son una colección de elementos desordenados que no se pueden modificar ni eliminar y que no pueden tener elementos de diferentes tipos

Ventajas de los sets:
- El acceso a los elementos es mas rápido que en las listas
- Ocupan menos espacio en memoria


Desventajas de los sets:
- Son desordenados
"""

conjunto: set = set()
otro_conjunto: set = {}

print(type(conjunto), end="\n")

"""
Si se inicializa un set con {} se inicializa como un diccionario
"""
print(type(otro_conjunto), end="\n")  # Inicialmente es un diccionario

otro_conjunto = {"Daniel", "Perez", 35}
print(type(otro_conjunto), end="\n")

print(len(otro_conjunto), end="\n")


"""
Para añadir elementos a un set se usa el método add
"""
otro_conjunto.add("DaniDev")

print(otro_conjunto, end="\n")  # Un set no es una estructura ordenada

otro_conjunto.add("DaniDev")  # Un set no admite repetidos

print(otro_conjunto, end="\n")

# Búsqueda
"""
Para buscar un elemento en un set se usa la palabra reservada in
Que in es un operador de pertenencia
"""
print("Daniel" in otro_conjunto, end="\n")
print("Dani" in otro_conjunto, end="\n")

# Eliminación

"""
Para eliminar un elemento de un set se usa el método remove() se le pasa como argumento el elemento a eliminar
"""
otro_conjunto.remove("Daniel")
print(otro_conjunto)

"""
Para eliminar todos los elementos de un set se usa el método clear()
"""
otro_conjunto.clear()
print(len(otro_conjunto), end="\n")

# Eliminación del set completo con el operador del que es un operador de eliminación

del otro_conjunto
# print(otro_conjunto) NameError: name 'otro_conjunto' is not defined

# Transformación
"""
Podemos convertir un set a una lista con la función list()
"""
conjunto: set[str, int] = {"Daniel", "Perez", 35}
lista: list[str, int] = list(conjunto)
print(lista, end="\n")
print(lista[0], end="\n")

otro_conjunto: set[str] = {"Rust", "Typescript", "Python"}

# Otras operaciones

"""
El método union() une dos sets y retorna un nuevo set con los elementos de ambos sets sin repetir los elementos repetidos. Se toma como parámetro el set con el que se quiere unir

"""
nuevo_set: set[str, int] = conjunto.union(otro_conjunto)
print(nuevo_set.union(nuevo_set).union(conjunto).union({"JavaScript", "Java"}))

"""
El método difference() retorna un nuevo set con los elementos que no se repiten entre dos sets

En este caso los elementos que no se repiten entre nuevo_set y conjunto
"""
print(nuevo_set.difference(conjunto), end="\n")
