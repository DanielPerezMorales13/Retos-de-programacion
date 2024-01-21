"""
Las clases abstractas se crean a traves del modulo abc y heredando de la clase ABC. Los metodos abstractos se crean a traves del decorador abstractmethod del modulo abc.
"""

from abc import ABC, abstractmethod

# abc: Modulo que contiene la clase ABC y el decorador abstractmethod.
# abstractmethod: Decorador para declarar un metodo abstracto.


class Persona(ABC):
    @abstractmethod
    def __init__(
        self: object, nombre: str, edad: int, sexo: str, trabajo: str, actividad: str
    ) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.sexo: str = sexo
        self.trabajo: str = trabajo
        self.actividad: str = actividad

    @abstractmethod
    def Hacer_Actividad(self: object) -> None:
        pass

    def presentarse(self: object) -> str:
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.sexo} y trabajo como {self.trabajo}"


class Estudiante(Persona):
    def __init__(
        self: object, nombre: str, edad: int, sexo: str, trabajo: str, actividad: str
    ) -> None:
        super().__init__(
            nombre=nombre, edad=edad, sexo=sexo, trabajo=trabajo, actividad=actividad
        )

    def Hacer_Actividad(self: object) -> str:
        return f"Estoy estudiando {self.actividad}"


daniel: object = Estudiante(
    nombre="Daniel",
    edad=18,
    sexo="hombre",
    trabajo="programador",
    actividad="programacion",
)


class Trabajador(Persona):
    def __init__(
        self: object, nombre: str, edad: int, sexo: str, trabajo: str, actividad: str
    ) -> None:
        super().__init__(nombre, edad, sexo, trabajo, actividad)

    def Hacer_Actividad(self: object) -> str:
        return f"Actualmente estoy trabajando como {self.trabajo}"


daniel: object = Estudiante(
    nombre="Daniel",
    edad=18,
    sexo="hombre",
    trabajo="programador",
    actividad="programacion",
)

danna: object = Trabajador(
    nombre="Danna",
    edad=18,
    sexo="mujer",
    trabajo="musicologa",
    actividad="cantante",
)

print(daniel.presentarse())
print(daniel.Hacer_Actividad())

print(danna.presentarse())
print(danna.Hacer_Actividad())

# si la clase no fuera abstracta, se podria crear un objeto de la clase Persona, pero como es abstracta, no se puede crear un objeto de esta clase. Ademas si no fuera abastracta el decorador abstractmethod no tendria sentido perderia su poder.

# las ventajas de las clases abstractas es que se puede crear una clase base con metodos abstractos y que las clases hijas hereden de esta clase base y tengan que implementar los metodos abstractos de la clase base.
