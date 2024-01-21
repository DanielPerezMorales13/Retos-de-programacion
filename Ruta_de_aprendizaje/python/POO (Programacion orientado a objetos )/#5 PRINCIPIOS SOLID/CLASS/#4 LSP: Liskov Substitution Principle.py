"""
"LSP": "Liskov Substitution Principle" Significa en español Principio de sustitucion de Liskov. Se le llama asi por la matematica Barbara Liskov.

Este principio dice que una clase base debe poder ser sustituida por sus clases derivadas. Es decir que una clase derivada debe poder ser sustituida por su clase base sin afectar el funcionamiento del sistema.
"""

"""

Este codigo tiene un problema ya que la clase Pinguino no puede volar y la clase Ave si puede volar. Entonces la clase Pinguino no puede ser sustituida por la clase Ave sin afectar el funcionamiento del sistema.

class Ave:
    def __init__(self: object) -> None:
        pass

    def Volar(self: object) -> str:
        return "Estoy volando"


class Pinguino(Ave):
    def __init__(self: object) -> None:
        pass

    # ave = Ave es una variable de parametro que es de tipo Ave

    def Volar(self: object) -> str:
        return "No puedo volar"


def Hacer_Volar(ave=Ave) -> str:
    return ave.Volar()

print(Hacer_Volar(ave=Pinguino()))
"""

"""
En este codigo se soluciona el problema de la clase Pinguino que no puede volar. Se crea una clase AveVoladora que puede volar y una clase AveNoVoladora que no puede volar. Estas dos clases heredan de la clase Ave. Entonces la clase AveVoladora y la clase AveNoVoladora pueden ser sustituidas por la clase Ave sin afectar el funcionamiento del sistema.
"""

class Ave:
    def __init__(self: object) -> None:
        pass
    
    # Aqui podemos hacer todo lo que puede hacer un ave

class AveVoladora(Ave):
    def __init__(self: object) -> None:
        pass

    def Volar(self: object) -> str:
        return "Estoy volando"

class AveNoVoladora(Ave):
    def __init__(self: object) -> None:
        pass

    def Volar(self: object) -> str:
        return "No puedo volar"