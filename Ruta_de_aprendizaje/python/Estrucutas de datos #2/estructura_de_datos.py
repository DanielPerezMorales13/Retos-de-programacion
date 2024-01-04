"""Listas: Una lista es una colección ordenada y mutable de elementos. Los elementos pueden ser de cualquier tipo y una lista puede contener elementos de diferentes tipos.

existen distintos tipos de lista unidimensional, bidimensional, tridimensional, etc.
Para trabajar con datos multidimensionales, a menudo es más conveniente utilizar una biblioteca como NumPy
"""

# Lista unidimensional
my_list: list[int | str] = [1, 2, 3, "a", "b", "c"]
my_list: list[int | str] = list([1, 2, 3, "a", "b", "c"])

# Lista bidimensional
bidimensional_list: list[list[int | str]] = [
    [1, 2, 3, "a", "b", "c"], 
    [1, 2, 3, "a", "b", "c"]
]

# Lista tridimensional
tridimensional_list: list[list[list[int | str]]] = [
    [
        [1, 2, 3, "a", "b", "c"], 
        [1, 2, 3, "a", "b", "c"]
    ],
    [
        [1, 2, 3, "a", "b", "c"], 
        [1, 2, 3, "a", "b", "c"]
    ]
]

# Lista cuatridimensional
cuatridimensional_list = [
    [
        [[1, 2], [3, 4]], 
        [[5, 6], [7, 8]], 
        [[9, 10], [11, 12]]
    ], 
    [
        [[13, 14], [15, 16]], 
        [[17, 18], [19, 20]], 
        [[21, 22], [23, 24]]
    ]
]

# print(cuatridimensional_list[-1][1][0][-1]) # Imprime: 18
"""
Tuplas: Una tupla es similar a una lista, pero es inmutable. Esto significa que una vez que se crea una tupla, no puede ser modificada.

Al igual que las listas, las tuplas pueden contener elementos de diferentes tipos. Las tuplas se utilizan a menudo para devolver múltiples valores de una función.

Trabajar con tuplas de más de tres dimensiones puede ser confuso y es raro en la mayoría de las aplicaciones.
"""

# Tupla unidimensional
my_tuple: tuple[int | str] = (1, 2, 3, "a", "b", "c")
my_tuple: tuple[int | str] = tuple([1, 2, 3, "a", "b", "c"])
my_tuple: tuple[int | str] = 1, 2, 3, "a", "b", "c"

# Tupla bidimensional
bidimensional_tuple: tuple[tuple[int | str]] = (
    (1, 2, 3, "a", "b", "c"), 
    (1, 2, 3, "a", "b", "c")
)

# Tupla tridimensional
tridimensional_tuple: tuple[tuple[tuple[int | str]]] = (
    (
        (1, 2, 3, "a", "b", "c"), 
        (1, 2, 3, "a", "b", "c")
    ),
    (
        (1, 2, 3, "a", "b", "c"), 
        (1, 2, 3, "a", "b", "c")
    )
)

# Tupla cuatridimensional
cuatridimensional_tuple: tuple[tuple[tuple[tuple[int | str]]]] = (
    (
        (
            (1, 2), 
            (3, 4)
        ), 
        (
            (5, 6), 
            (7, 8)
        ), 
        (
            (9, 10), 
            (11, 12)
        )
    ), 
    (
        (
            (13, 14), 
            (15, 16)
        ), 
        (
            (17, 18), 
            (19, 20)
        ), 
        (
            (21, 22), 
            (23, 24)
        )
    )
)
"""
Diccionarios: Un diccionario es una colección desordenada de pares clave-valor. Las claves en un diccionario deben ser únicas.
Al igual que las listas, los diccionarios pueden contener elementos de diferentes tipos. Los diccionarios se utilizan a menudo para representar datos estructurados como objetos JSON.
"""
# Diccionario unidimensional
my_dict: dict[str, any] = {"name": "John", "age": 30, "city": "New York"}
my_dict: dict[str, any] = dict({"name": "John", "age": 30, "city": "New York"})
my_dict: dict[str, any] = dict(name="John", age=30, city="New York")

# Diccionario bidimensional
bidimensional_dict: dict[str, dict[str, any]] = {
    "person1": {"name": "John", "age": 30, "city": "New York"},
    "person2": {"name": "Jane", "age": 25, "city": "London"}
}

# print(my_dict["person1"]["name"]) # Imprime: John

# Diccionario tridimensional
tridimensional_dict = {
    "USA": {
        "John": {"age": 30, "city": "New York"},
        "Jane": {"age": 28, "city": "Los Angeles"},
        "Mike": {"age": 35, "city": "Chicago"}
    },
    "UK": {
        "Alice": {"age": 32, "city": "London"},
        "Bob": {"age": 34, "city": "Manchester"}
    }
}
# print(tridimensional_dict["USA"]["John"]["city"]) # Imprime: New York

# Diccionario cuatridimensional
cuatridimensional_dict = {
    "2020": {
        "USA": {
            "John": {"age": 30, "city": "New York"},
            "Jane": {"age": 28, "city": "Los Angeles"},
            "Mike": {"age": 35, "city": "Chicago"}
        },
        "UK": {
            "Alice": {"age": 32, "city": "London"},
            "Bob": {"age": 34, "city": "Manchester"}
        }
    },
    "2021": {
        "USA": {
            "John": {"age": 31, "city": "New York"},
            "Jane": {"age": 29, "city": "Los Angeles"},
            "Mike": {"age": 36, "city": "Chicago"}
        },
        "UK": {
            "Alice": {"age": 33, "city": "London"},
            "Bob": {"age": 35, "city": "Manchester"}
        }
    }
}

# print(cuatridimensional_dict["2020"]["USA"]["John"]["city"]) # Imprime: New York

# ! No son comunes los diccionarios de más de 2 dimensiones

"""
Conjuntos: Un conjunto es una colección desordenada de elementos únicos.
"""
# set unidimensional
my_set: set = {1, 2, 3, "a", "b", "c"}
my_set: set = set((1, 2, 3, "a", "b", "c"))
my_set: set = set([1, 2, 3, "a", "b", "c"])

# print(my_set) # Imprime: {1, 2, 3, 'a', 'b', 'c'} no se puedo acceder a los elementos de un set por su indice

#for element in my_set:
    #print(element) # Imprime: 1 2 3 a b c
    
# set bidimensional
bidimensional_set: set = {
    (1, 2, 3, "a", "b", "c"), 
    (11, 22, 33, "aa", "bb", "cc")
}
for element in bidimensional_set:
    print(element) # Imprime: (1, 2, 3, 'a', 'b', 'c') (1, 2, 3, 'a', 'b', 'c')

"""
Cadenas: Una cadena es una secuencia de caracteres.
"""
my_string: str = "Hello, World!"
my_string: str = str("Hello, World!")
my_string: str = str(10)

"""
Además de estas estructuras de datos incorporadas, Python también tiene varias estructuras de datos más avanzadas disponibles a través de módulos como collections (por ejemplo, namedtuple, deque, Counter) y numpy (por ejemplo, array, matrix).
"""
