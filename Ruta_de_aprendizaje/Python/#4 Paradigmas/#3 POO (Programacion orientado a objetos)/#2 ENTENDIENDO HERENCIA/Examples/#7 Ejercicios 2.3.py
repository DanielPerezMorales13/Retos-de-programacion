"""
Ejercicio de herencia multiple y MRO:

Imagina que estas modelando animales en un zoológico. Crear tres clases: "Animal", "Mamifero" y "Ave". La clase "Animal debe tener un metodo llamado "comer". La clase  "Mamifero" debe tener un metodo llamado "amamantar" y la clase "Ave" un metodo llamado "Volar" 

Ahora, crea un clase "Murcielago" que herede de "Mamifero" y "Ave", en ese orden, y por lo tanto debe ser capaz de "amamantar" y "volar", ademas de "comer".

Finalmente, juega con el orden de herencia y observa como cambia el comportamiento el MRO y el comportamiento de los métodos al usar super().
"""


class Animal:
    def __init__(self: object) -> None:
        pass

    def Comer(self: object) -> str:
        return "Comiendo"


class Mamifero(Animal):
    def __init__(self: object) -> None:
        pass

    def Amamantar(self: object) -> str:
        return "Amamantando"


class Ave(Animal):
    def __init__(self: object) -> None:
        pass

    def Volar(self: object) -> str:
        return "Volando"

class Murcielago(Mamifero,Ave):
    def __init__(self: object) -> None:
        super().__init__()
        pass

Murcielagito: object = Murcielago()

print(Murcielagito.Comer())
print(Murcielagito.Amamantar())
print(Murcielagito.Volar())