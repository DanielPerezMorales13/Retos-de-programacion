# Definición

"""
Los diccionarios son una estructura de datos que nos permite almacenar valores de diferente tipo, a diferencia de las listas, en lugar de acceder a los valores por un índice, lo hacemos por una llave. Las llaves pueden ser de tipo string o numérico. Los diccionarios son estructuras de datos mutables. Los diccionarios se definen con llaves {}. O también con la función dict(). 

La clave de un diccionario puede ser de cualquier tipo inmutable, como los números, cadenas o tuplas. Si intentamos usar como clave un tipo mutable como las listas, obtendremos un error de tipo TypeError. La clave es un identificador único para cada elemento dentro de un diccionario. Si intentamos crear un diccionario con dos claves iguales, se sobrescribirá el valor de la primera clave.

>>> ventajas de los diccionarios:

- Los diccionarios son estructuras de datos muy eficientes para buscar y almacenar valores.

- Los diccionarios son estructuras de datos muy flexibles para representar información.

- Los diccionarios son estructuras de datos muy eficientes para representar información proveniente de bases de datos.

>>> desventajas de los diccionarios:

- Los diccionarios no tienen un orden definido, por lo que no podemos esperar que los elementos se mantengan en un orden específico.

- Los diccionarios no son estructuras de datos eficientes en el uso de memoria, debido a que almacenan la información en forma de clave:valor, por lo que cada elemento del diccionario almacena dos valores.

"""
# | es el operador de unión de tipos de datos que se utiliza para indicar que un parámetro puede ser de varios tipos de datos
dicccionario: dict[str | int | float | bool, str | int | float | bool] = dict()
otro_dicccionario: dict[str | int | float | bool, str | int | float | bool] = {}
otra_forma: dict[str, str] = dict(
    Nombre="Daniel",
    Apellido="Perez",
    Edad=35,
    Lenguajes={"Python", "Rust", "Typescript"},
    Altura=1.77,
)


print(type(dicccionario), end="\n")
print(type(otro_dicccionario), end="\n")

otro_dicccionario: dict[str, str | int] = {
    "Nombre": "Daniel",
    "Apellido": "Perez",
    "Edad": 35,
    1: "Python",
}

dicccionario: dict[str, str | int] = {
    "Nombre": "Daniel",
    "Apellido": "Perez",
    "Edad": 35,
    "Lenguajes": {"Python", "Rust", "Typescript"},
    1: 1.77,
}

print(otro_dicccionario, end="\n")
print(dicccionario, end="\n")

print(
    len(otro_dicccionario), end="\n"
)  # Cantidad de elementos en el diccionario en total serian 4. Nombre, Apellido, Edad, 1 no se cuentan los valores de los conjuntos
print(
    len(dicccionario), end="\n"
)  # Cantidad de elementos en el diccionario en total serian 5. Nombre, Apellido, Edad, Lenguajes, 1 no se cuentan los valores de los conjuntos

# Búsqueda
"""
Para buscar un valor en un diccionario, debemos usar la llave correspondiente. Si la llave no existe, obtendremos un error de tipo KeyError. Para evitar este error, podemos usar el método get, que recibe como parámetro la llave a buscar y un valor por defecto que se retornará en caso de que la llave no exista.

Usamos el [] para buscar un valor en un diccionario, pero también para insertar o actualizar un valor. Si la llave existe, se actualizará el valor, si la llave no existe, se insertará el valor.
"""
print(dicccionario[1], end="\n")
print(dicccionario["Nombre"], end="\n")


# El operador de pertenencia in nos permite saber si una llave existe en un diccionario. Nos retorna True si la llave existe y False si no existe. Si queremos saber si un valor existe en un diccionario, debemos usar el método values.
print("Perez" in dicccionario, end="\n")
print("Apellido" in dicccionario, end="\n")

# Inserción
"""
Para insertar un valor en un diccionario, debemos usar el [] y asignarle un valor. Si la llave existe, se actualizará el valor, si la llave no existe, se insertará el valor.
"""
dicccionario["Calle"] = "Calle DaniDev"
print(dicccionario, end="\n")

# Actualización
"""
Para actualizar un valor en un diccionario, debemos usar el [] y asignarle un valor. Si la llave existe, se actualizará el valor, si la llave no existe, se insertará el valor.
"""
dicccionario["Nombre"] = "Benjamin"
print(dicccionario["Nombre"], end="\n")

# Eliminación

"""
Para eliminar un valor en un diccionario, debemos usar el método pop, que recibe como parámetro la llave a eliminar y retorna el valor eliminado. Si la llave no existe, obtendremos un error de tipo KeyError. Para evitar este error, podemos usar el método pop, que recibe como parámetro la llave a eliminar y un valor por defecto que se retornará en caso de que la llave no exista. También podemos usar la palabra reservada del, que recibe como parámetro la llave a eliminar. Si la llave no existe, obtendremos un error de tipo KeyError. Para evitar este error, podemos usar el método pop, que recibe como parámetro la llave a eliminar y un valor por defecto que se retornará en caso de que la llave no exista.
"""
del dicccionario["Calle"]
print(dicccionario, end="\n")

# Esta variable almacenara el valor eliminado de la llave "Nombre" en caso de que exista, en caso de que no exista almacenara None
valor_eliminado: str | None = dicccionario.pop("Nombre", None)
print(dicccionario, end="\n")

print(valor_eliminado, end="\n")


# Otras operaciones
"""
el metodo items() nos permite obtener una lista de tuplas, donde cada tupla contiene la llave y el valor de cada elemento del diccionario. 
El método keys() nos permite obtener una lista con todas las llaves del diccionario. 

El método values() nos permite obtener una lista con todos los valores del diccionario.
"""
print(dicccionario.items(), end="\n")
print(dicccionario.keys(), end="\n")
print(dicccionario.values(), end="\n")

lista: list[str, int] = ["Nombre", 1, "Piso"]

"""
El método fromkeys() nos permite crear un diccionario a partir de una lista de llaves. El método fromkeys() recibe como primer parámetro la lista de llaves y como segundo parámetro un valor por defecto para todas las llaves. Si no se especifica el segundo parámetro, el valor por defecto será None.

Poner entre parentesis la lista, tupla o conjunto, es para que el metodo fromkeys() reciba un iterable, y no una lista de argumentos.
"""
nuevo_diccionario: dict[str | int, int | str] = dict.fromkeys(
    (lista), "Valor por defecto"
)
print(nuevo_diccionario, end="\n")
nuevo_diccionario: dict[str | int, int | str] = dict.fromkeys(
    ("Nombre", 1, "Piso"), None
)
print((nuevo_diccionario), end="\n")
nuevo_diccionario: dict[str | int, int | str] = dict.fromkeys((dicccionario), None)
print((nuevo_diccionario), end="\n")

nuevo_diccionario: dict[str | int, int | str] = dict.fromkeys(dicccionario, "DaniDev")
print((nuevo_diccionario), end="\n")

valor: dict = nuevo_diccionario.values()
print(type(valor), end="\n")

print(nuevo_diccionario.values(), end="\n")
"""
Esta linea de codigo nos permite obtener una lista de los valores del diccionario, sin repetir ninguno, es decir, si hay dos valores iguales, solo se mostrara uno.

list() convierte el objeto en una lista
dict.fromkeys() convierte el objeto en un diccionario
.values() obtiene los valores del diccionario
keys() obtiene las llaves del diccionario

"""
print(list(set(nuevo_diccionario.values())), end="\n")
print(tuple(nuevo_diccionario), end="\n")
print(set(nuevo_diccionario), end="\n")

