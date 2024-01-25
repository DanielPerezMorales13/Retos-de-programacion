"""
Duck Typing es un concepto en Python que se refiere a la idea de que no importa el tipo de objeto con el que estás trabajando, sino qué operaciones o comportamientos puedes hacer con él. Si un objeto se comporta como un pato (es decir, tiene los mismos métodos y propiedades), entonces puedes tratarlo como un pato.
"""


class Pato:
    def __init__(self: object) -> None:
        pass

    def hablar(self: object) -> str:
        return "¡Cuac!"


class Perro:
    def __init__(self: object) -> None:
        pass

    def hablar(self: object) -> str:
        return "¡Guau!"


def hacer_hablar(Animal: object):
    # No importa el tipo de 'Animal' mientras tenga un método 'hablar'
    print(Animal.hablar())


pato: object = Pato()
perro: object = Perro()

# Aunque 'pato' y 'perro' son de diferentes tipos,
# ambos tienen un método 'hablar', por lo que podemos usarlos
# de manera intercambiable en la función 'hacer_hablar'

hacer_hablar(Animal=pato)  # Imprime: ¡Cuac!
hacer_hablar(Animal=perro)  # Imprime: ¡Guau!

# En este ejemplo, la función hacer_hablar puede tomar cualquier objeto que tenga un método hablar. No importa si el objeto es un Pato o un Perro, siempre que tenga un método hablar, se puede usar en hacer_hablar. Esto es Duck Typing.
