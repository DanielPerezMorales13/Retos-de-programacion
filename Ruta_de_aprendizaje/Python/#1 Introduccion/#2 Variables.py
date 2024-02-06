# Tema: Variables

string: str = "My String variable"
print(string)

integer: int = 5
print(integer)

convercion_de_integer_a_string: str = str(integer)
print(
    convercion_de_integer_a_string,
    end="\n",
)
print(
    type(convercion_de_integer_a_string),
    end="\n",
)

booleano: bool = False
print(
    booleano,
    end="\n",
)

flotante: float = 1.2
# Concatenación de variables en un print
print(string, convercion_de_integer_a_string, booleano, flotante, end="\n")
print("Este es el valor de:", booleano, end="\n")

# Algunas funciones del sistema

"""
len() es una función que nos permite saber la longitud de una cadena de texto
"""
print(len(string), end="\n")

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!

nomber, segundo_nombre, alias, edad = "Daniel", "Perez", "DaniDev", 35
print(
    "Me llamo:",
    nomber,
    segundo_nombre,
    ". Mi edad es:",
    edad,
    ". Y mi alias es:",
    alias,
    end="\n",
)

# Inputs
nombre = str(input("¿Cuál es tu nombre? "))
edad = int(input("¿Cuántos años tienes? "))
print(nombre)
print(edad)

# Cambiamos su tipo
nombre: str = 35
# Esto es un error de tipo de dato en python
# pero no da error en tiempo de ejecución por que es un lenguaje interpretado y no compilado
edad: int = "Daniel"
print(nomber)
print(edad)

"""
Cambiamos su tipo en python las variables son dinámicas
Lo que quiere decir que podemos cambiar el tipo de dato de una variable en cualquier momento

En otros lenguajes de programación, las variables son estáticas
Lo que quiere decir que una vez que le asignamos un tipo de dato a una variable, no podemos cambiarlo
"""
direccion: str = "Mi dirección"
direccion: bool = True
direccion: int = 5
direccion: float = 1.2
print(type(direccion), end="\n")


# Constantes
""" 
En python no existen las constantes, pero se pueden simular con mayúsculas y guiones bajos. Se usa para indicar que una variable no debe ser modificada en el futuro

Las constantes se suelen definir al principio del archivo o al principio de una clase Y puden tener cualquier tipo de dato
"""
FLOTANTE: float = 1.2
CADENA: str = "Mi cadena"
BOOLEANO: bool = True
ENTERO: int = 5
print(ENTERO, end="\n")
