"""
"ISP": "Interface Segregation Principle" Significa en español Principio de segregacion de interfaces. 

Este principio dice que una clase no debe depender de metodos que no usa. Es decir que una clase no debe depender de metodos que no usa para que sea facil de mantener y de cambiar.

Este principio se puede aplicar en lenguajes de programacion que no tienen interfaces como Python. En Python se puede aplicar este principio con clases abstractas.

Este principio nos permite que los usuario no dependan de metodos que no usan. Es decir que los usuario no dependan de metodos que no usan para que sea facil de mantener y de cambiar.
"""

"""
from abc import ABC, abstractmethod


class Trabajador(ABC):
    @abstractmethod
    def __init__(self: object) -> None:
        pass

    @abstractmethod
    def Comer(self: object) -> None:
        pass

    @abstractmethod
    def Trabajar(self: object) -> None:
        pass

    @abstractmethod
    def Dormir(self: object) -> None:
        pass


class Humano(Trabajador):
    def __init__(self: object) -> None:
        pass

    def Comer(self: object) -> str:
        return "Estoy comiendo"

    def Trabajar(self: object) -> str:
        return "Estoy trabajando"

    def Dormir(self: object) -> str:
        return "Estoy durmiendo"


class Robot(Trabajador):
    def __init__(self: object) -> None:
        pass

    def Comer(self: object) -> None:
        return None

    def Trabajar(self: object) -> str:
        return "El robot esta trabajando"

    def Dormir(self: object) -> None:
        return None


robot: Trabajador = Robot()

"""

"""
Este codigo no se puede ejecutar porque la clase Robot no tiene el metodo Comer y Dormir.
Esto viola el principio de segregacion de interfaces porque la clase Robot depende de metodos que no usa.
Para solucionar este problema se puede crear una clase abstracta que tenga los metodos Comer y Dormir y que las clases Humano y Robot hereden de la clase abstracta.
"""

from abc import ABC, abstractmethod


class Trabajador(ABC):
    @abstractmethod
    def __init__(self: object) -> None:
        pass

    @abstractmethod
    def Trabajar(self: object) -> None:
        pass


class Comedor(ABC):
    @abstractmethod
    def __init__(self: object) -> None:
        pass

    @abstractmethod
    def Comer(self: object) -> None:
        pass


class Dormidor(ABC):
    @abstractmethod
    def __init__(self: object) -> None:
        pass

    @abstractmethod
    def Dormir(self: object) -> None:
        pass


class Humano(Trabajador, Comedor, Dormidor):
    def __init__(self: object) -> None:
        Trabajador.__init__(self=self)
        Comedor.__init__(self=self)
        Dormidor.__init__(self=self)

    def Comer(self: object) -> str:
        return "El humano comiendo"

    def Trabajar(self: object) -> str:
        return "El humano esta trabajando"

    def Dormir(self: object) -> str:
        return "El humano durmiendo"


class Robot(Trabajador):
    def __init__(self: object) -> None:
        pass

    def Trabajar(self: object) -> str:
        return "El robot esta trabajando"


humano: object = Humano()
print(humano.Trabajar())
print(humano.Comer())
print(humano.Dormir())

robot: Trabajador = Robot()
print(robot.Trabajar())
print(robot.Comer())  # Da error porque la clase Robot no tiene el metodo Comer


"""
Este la manera correcta de aplicar el principio de segregacion de interfaces.
Ya que la clase Robot no depende de metodos que no usa.
Se creo una clase abstracta para los metodos Comer y Dormir.
Esto para que la clase Robot no dependa de metodos que no usa.
"""
