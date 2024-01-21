"""
"DIP": "Dependency Inversion Principle" Significa en español Principio de inversion de dependencias.

La idea de este principio es que los modulos de alto nivel no deben depender de los modulos de bajo nivel. Ambos deben depender de abstracciones. Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones. 
"""

"""
class Dictionario:
    def __init__(self: object, palabra: str) -> None:
        pass

    def Verifica_Palabra(self: object) -> None:
        # logica para verificar si la palabra existe en el diccionario
        return None


class CorrectorOrtografico:
    def __init__(self: object) -> None:
        # A esto se le llama
        self.diccionario: object = Dictionario()

    def Corregir_Texto(self: object, texto: str) -> None:
        # usamos el diccionario para corregir el texto
        return None

"""

"""
En este ejemplo la clase CorrectorOrtografico depende de la clase Dictionario
y esto no es bueno porque si queremos cambiar la clase Dictionario tendriamos que cambiar la clase CorrectorOrtografico y esto no es bueno porque no se cumple el principio de inversion de dependencias.
"""


from abc import ABC, abstractmethod


class VerificadorOrtografico(ABC):
    @abstractmethod
    def __init__(self: object) -> None:
        # A esto se le llama
        self.diccionario: object = Dictionario()

    @abstractmethod
    def Verifica_Palabra(self: object, palabra: str) -> None:
        # Logica para verificar si la palabra existe en el diccionario
        pass


class Dictionario(VerificadorOrtografico):
    def __init__(self: object, palabra: str) -> None:
        pass

    def Verifica_Palabra(self: object) -> None:
        # logica para verificar si la palabra existe en el diccionario
        pass


class ServicioOnline(VerificadorOrtografico):
    def __init__(self: object, palabra: str) -> None:
        pass

    def Verifica_Palabra(self: object) -> None:
        # logica para verificar desde el servicio online
        pass


class CorrectorOrtografico:
    def __init__(self: object, verificador) -> None:
        # A esto se le llama
        self.verificador: any = verificador

    def Corregir_Texto(self: object, texto: str) -> None:
        # usamos el diccionario para corregir el texto
        pass


corrector_one: object = CorrectorOrtografico(verificador=ServicioOnline())
corrector_dos: object = CorrectorOrtografico(verificador=Dictionario())

"""
Ahora la clase CorrectorOrtografico no depende de la clase Dictionario, ahora depende de la clase VerificadorOrtografico y esto es bueno porque si queremos cambiar la clase Dictionario por otra clase que tenga la misma funcionalidad no tendriamos que cambiar la clase CorrectorOrtografico y esto es bueno porque se cumple el principio de inversion de dependencias. 

Tambien la clase CorrectorOrtografico depende de la abstraccion VerificadorOrtografico y esto es bueno porque si queremos cambiar la clase Dictionario por otra clase que tenga la misma funcionalidad no tendriamos que cambiar la clase CorrectorOrtografico y esto es bueno porque se cumple el principio de inversion de dependencias.
"""
