"""
En programación orientada a objetos, el tipo declarado de una variable es el tipo que se especifica en su declaración. El tipo real o actual de una variable es el tipo del objeto al que hace referencia en tiempo de ejecución.
"""


class Animal:
    def __init__(self: object) -> None:
        pass

    def sonido(self: object) -> str:
        pass


class Gato(Animal):
    def __init__(self: object) -> None:
        super().__init__()
        pass

    def sonido(self: object) -> str:
        return "Miau"


class Perro(Animal):
    def __init__(self: object) -> None:
        super().__init__()
        pass

    def sonido(self: object) -> str:
        return "Guau"


# Tipo declarado: Animal
# Tipo real: Gato
animal1: Animal = Gato()

# Tipo declarado: Animal
# Tipo real: Perro
animal2: Animal = Perro()

print(animal1.sonido())  # Imprime "Miau"
print(animal2.sonido())  # Imprime "Guau"
