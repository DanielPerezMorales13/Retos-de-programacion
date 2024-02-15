# Tema: Funciones
"""
Paradigma: funcional es un paradigma de programación que se basa en funciones y en la programación declarativa
"""
# Definición
"""
Para definir una función se utiliza la palabra reservada def
seguido del nombre de la función y los paréntesis de apertura y cierre

la estructura de una función es la siguiente

>>> def es una palabra reservada de python que se utiliza para definir una función
>>> my_funcion es el nombre de la función puede tener cualquier nombre que no sea una palabra reservada de python
>>> () son los paréntesis de apertura y cierre de la función y dentro de ellos se pueden poner los parámetros de entrada de la función

>>> -> es el operador de retorno que se utiliza para indicar el tipo de dato que retornará la función y se puede omitir si la función no retorna nada o podemos poner None si la función no retorna nada 

>>> None es un tipo de dato que se utiliza para indicar que una variable no tiene ningún valor podemos decir que es el equivalente a null en otros lenguajes de programación
"""


def my_funcion() -> None:
    print("Esto es una función", end="\n")


my_funcion()
my_funcion()
my_funcion()

# Función con parámetros de entrada/argumentos

# | es el operador de unión de tipos de datos que se utiliza para indicar que un parámetro puede ser de varios tipos de datos


def sumarDosValores(primer_valor: int | str | float, segundo_valor: int | str | float):
    print(primer_valor + segundo_valor, end="\n")


sumarDosValores(primer_valor=5, segundo_valor=7)
sumarDosValores(primer_valor=54754, segundo_valor=71231)
sumarDosValores(primer_valor="5", segundo_valor="7")
sumarDosValores(primer_valor=1.4, segundo_valor=5.2)

# Función con parámetros de entrada/argumentos y retorno


def sumarDosValoresConRetorno(primer_valor, segundo_valor) -> int | float | str:
    suma: int | float | str = primer_valor + segundo_valor
    return suma


# Podemos asignar el valor que retorna una función a una variable para utilizarlo más tarde Si la función no retorna nada la variable tendrá el valor None
resultado: int | float | str = sumarDosValores(1.4, 5.2)
print(resultado, end="\n")

resultado = sumarDosValoresConRetorno(10, 5)
print(resultado, end="\n")

# Función con parámetros de entrada/argumentos por clave


def imprimir_nombre(nombre: str, segundo_nombre: str):
    print(f"{nombre} {segundo_nombre}", end="\n")


imprimir_nombre(segundo_nombre="Benjamin", nombre="Perez")

# Función con parámetros de entrada/argumentos por defecto


# Podemos indicarle a un parámetro que tenga un valor por defecto si no se le pasa ningún valor al llamar la función y si se le pasa un valor al llamar la función se sobreescribirá el valor por defecto del parámetro por el valor que se le pasó al llamar la función


def imprimirConValoresPorDefecto(
    nombre, segundo_nombre, alias: str | int | float | bool = "Sin alias"
):
    print(f"{nombre} {segundo_nombre} {alias}", end="\n")


imprimirConValoresPorDefecto("Perez", "Benjamin")
imprimirConValoresPorDefecto("Perez", "Benjamin", "BenjaminDev")

# Función con parámetros de entrada/argumentos arbitrarios

"""
* es el operador de parámetros de entrada/argumentos arbitrarios que se utiliza para indicar que la función puede recibir un número indeterminado de parámetros de entrada/argumentos y se pueden utilizar en la función como una tupla de datos y se puede utilizar cualquier nombre para el parámetro de entrada/argumento arbitrario
"""


def imprimirTextoEnMayuscula(*textos):
    print(type(textos), end="\n")
    for texto in textos:
        print(texto.upper(), end="\n")


imprimirTextoEnMayuscula("Hola", "Python", "BenjaminDev")
imprimirTextoEnMayuscula("Hola")

"""
Función con parámetros de entrada/argumentos arbitrarios por clave
"""


def imprimirTextoEnMayusculaPorClave(**textos):
    print(type(textos), end="\n")
    for texto in textos:
        print(texto.upper(), end="\n")


# Podemos pasar los parámetros de entrada/argumentos arbitrarios por clave de la siguiente manera clave=valor

"""
Otra manera es crear un diccionario y pasarle el diccionario a la función de la siguiente manera **diccionario o el nombre que le hayamos puesto al parámetro de entrada/argumento arbitrario por clave
"""

diccionario: dict[str, str] = {
    "texto1": "Hola",
    "texto2": "Rust",
    "texto3": "DanielDev",
}
imprimirTextoEnMayusculaPorClave(**diccionario)

imprimirTextoEnMayusculaPorClave(texto1="Hola", texto2="Python", texto3="BenjaminDev")


"""
>>> Con el operador * que se llama operador de desempaquetado podemos pasar una lista o una tupla a una funcion.

>>> Con el operador ** que se llama operador de desempaquetado podemos pasar un diccionario a una funcion.

Podemos tener ambos operadores en una misma función
"""


def imprimirTextoEnMayusculaConDesempaquetado(*textos, **textos_por_clave):
    print(type(textos), end="\n")
    print(type(textos_por_clave), end="\n")
    for texto in textos:
        print(texto.upper(), end="\n")
    for texto in textos_por_clave:
        print(texto.upper(), end="\n")


imprimirTextoEnMayusculaConDesempaquetado(
    "Hola", "Python", "BenjaminDev", **diccionario
)


imprimirTextoEnMayusculaConDesempaquetado(
    "Hola",
    "Python",
    "BenjaminDev",
    texto1="Hola",
    texto2="Python",
    texto3="BenjaminDev",
)

"""
function asynchroneas  funciones asincronas

>>> Es una función que se ejecuta de manera asincrona lo que significa que se ejecuta en un hilo diferente al hilo principal y se puede ejecutar al mismo tiempo que otras funciones asincronas o funciones sincronas es decir que no se bloquea el hilo principal, esto es muy util para hacer peticiones a una API o a una base de datos sin bloquear el hilo principal

>>> Para definir una función asincrona se utiliza la palabra reservada async seguido de la palabra reservada def y el nombre de la función y los paréntesis de apertura y cierre

>>> para ejecutar una función asincrona se utiliza la palabra reservada await seguido del nombre de la función y los paréntesis de apertura y cierre

Para usar funciones asiincronas se debe de usar el modulo asyncio
"""

import asyncio


async def my_funcion_asincrona(nombre: str) -> str:
    return "Esto es una función asincrónica {}".format(nombre)


# Ejecutar la función asincrona
resultado_de_funcion_asincrona: str = asyncio.run(
    main=my_funcion_asincrona(nombre="BenjaminDev")
)
print(resultado_de_funcion_asincrona, end="\n")
print(asyncio.run(main=my_funcion_asincrona(nombre="DanielDev")), end="\n")
