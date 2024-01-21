def decorador1(funcion: callable) -> callable:
    def funcion_interna() -> None:
        print("Decorador 1 antes de la ejecución de la función")
        funcion()
        print("Decorador 1 después de la ejecución de la función")

    return funcion_interna


def decorador2(funcion: callable) -> callable:
    def funcion_interna() -> None:
        print("Decorador 2 antes de la ejecución de la función")
        funcion()
        print("Decorador 2 después de la ejecución de la función")

    return funcion_interna


@decorador1
@decorador2
def saludo() -> None:
    print("¡Hola!")


saludo()

"""
saludo está decorado con @decorador1 y @decorador2, la salida completa será:

>>> Decorador 1 antes de la ejecución de la función
>>> Decorador 2 antes de la ejecución de la función
>>> ¡Hola!
>>> Decorador 2 después de la ejecución de la función
>>> Decorador 1 después de la ejecución de la función

La salida que ves es el resultado de aplicar dos decoradores, decorador1 y decorador2, a la función saludo. Los decoradores en Python se aplican de abajo hacia arriba. Por lo tanto, primero se aplica decorador2, luego decorador1.

Cuando llamas a la función saludo(), esto es lo que sucede:

Debido al decorador decorador1, se imprime "Decorador 1 antes de la ejecución de la función".

Luego, se llama a la función saludo. Pero saludo ha sido decorada con decorador2, por lo que en lugar de ejecutar saludo directamente, se ejecuta el código del decorador decorador2.

Dentro de decorador2, se imprime "Decorador 2 antes de la ejecución de la función", luego se ejecuta la función original saludo (que imprime "¡Hola!"), y finalmente se imprime "Decorador 2 después de la ejecución de la función".

Después de que se completa la ejecución de decorador2 y saludo, se vuelve al decorador decorador1, donde se imprime "Decorador 1 después de la ejecución de la función".


Se puedes aplicar tantos decoradores como desees a una función en Python.
"""
