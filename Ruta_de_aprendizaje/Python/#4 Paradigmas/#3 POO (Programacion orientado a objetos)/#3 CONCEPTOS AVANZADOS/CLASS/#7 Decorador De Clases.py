"""
Al decorar una clase, se crea una nueva clase que hereda de la clase original.
Esto significa que la nueva clase tiene todos los atributos y métodos de la clase original.
Por lo tanto, podemos agregar nuevos métodos y atributos a la clase decorada.
"""


def decorador_clase(clase: object) -> object:
    class NuevaClase(clase):
        def __init__(self: object, nombre: str = "Daniel") -> None:
            self.nombre = nombre

        def nueva_funcion(self: object) -> str:
            return "Esta es una nueva función en la clase decorada"

    return NuevaClase


@decorador_clase
class MiClase:
    def __init__(self: object) -> None:
        pass

    def funcion_original(self: object) -> str:
        return "Esta es la función original de la clase"


# Crear una instancia de la clase decorada
objeto: object = MiClase()

# Llamar a las funciones
print(objeto.funcion_original())  # Imprime "Esta es la función original de la clase"
print(
    objeto.nueva_funcion()
)  # Imprime "Esta es una nueva función en la clase decorada"
