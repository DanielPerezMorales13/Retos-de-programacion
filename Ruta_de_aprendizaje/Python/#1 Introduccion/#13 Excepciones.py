# Tema: Excepciones

numeroUno: int = 5
numeroDos: int = 1
numeroTres: str = "1"

# Excepción base: try except

"""
Para manejar las excepciones se utiliza la palabra reservada try seguida de dos puntos y en la siguiente línea se escribe el código que se quiere ejecutar y que puede producir una excepción

Si se produce una excepción se ejecuta el código que está dentro del bloque except y si no se produce una excepción se ejecuta el código que está dentro del bloque else

El bloque finally se ejecuta siempre
"""
try:
    # Este código puede producir una excepción
    print(numeroUno + numeroTres, end="\n")
    print("No se ha producido un error", end="\n")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error", end="\n")

# Flujo completo de una excepción: try except else finally

"""
>>> Primero se ejecuta el código que está dentro del bloque try 

>>> y si se produce una excepción se ejecuta el código que está dentro del bloque except 

>>> y si no se produce una excepción se ejecuta el código que está dentro del bloque else

>>> para finalizar se ejecuta el código que está dentro del bloque finally
"""
try:
    # Este código puede producir una excepción
    print(numeroUno + numeroTres, end="\n")
    print("No se ha producido un error", end="\n")
except:
    print("Se ha producido un error", end="\n")
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente", end="\n")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa", end="\n")

# Excepciones por tipo

"""
Podemos capturar excepciones por tipo, para ello debemos indicar el tipo de excepción que queremos capturar después de la palabra reservada except
"""

try:
    print(numeroUno + numeroTres, end="\n")
    print("No se ha producido un error", end="\n")
except ValueError:
    print("Se ha producido un ValueError", end="\n")
except TypeError:
    print("Se ha producido un TypeError", end="\n")

# Captura de la información de la excepción

"""
Podemos capturar la información de la excepción con la palabra reservada as que se utiliza después del tipo de excepción para asignar la información de la excepción a una variable y así poder utilizarla dentro del bloque except. la variable que se utiliza para capturar la información de la excepción puede tener cualquier nombre
"""

try:
    print(numeroUno + numeroTres, end="\n")
    print("No se ha producido un error", end="\n")
except ValueError as error:
    # ValueError es una excepción que se produce cuando se intenta convertir un valor a un tipo de dato que no es compatible con el valor que se quiere convertir. Este error lo almacena la variable error
    print(error, end="\n")
except Exception as error_random:
    # Exception es la clase base de todas las excepciones de Python y se utiliza para capturar cualquier excepción que no se haya capturado antes
    print(error_random, end="\n")

# otra manera para capturar myltiples excepciones

try:
    print(numeroUno + numeroTres, end="\n")
    print("No se ha producido un error", end="\n")
except (ValueError,Exception) as error:
    # En este caso se capturan dos tipos de excepciones en un solo bloque except con una tupla de excepciones separadas por comas y se asigna la información de la excepción a la variable error
    print(error, end="\n")

