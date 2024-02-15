# Tema: Clases

# Definición
"""
Paradigma: orientado a objetos es un paradigma de programación que se basa en objetos
"""


class PersonaaVacia:
    # constructor
    def __init__(self: object) -> None:
        pass  # Para poder dejar la clase vacía


print(PersonaaVacia, end="\n")  # Nos imprime el tipo de dato de la clase
print(PersonaaVacia(), end="\n")  # Nos imprime el objeto de la clase

# Clase con constructor, funciones y popiedades privadas y públicas


class Persona:
    # Constructo
    def __init__(self: object, nombre: str, segundo_nombre, alias: str = "Sin alias"):
        self.full_nombre: str | int = (
            f"{nombre} {segundo_nombre} ({alias})"  # Propiedad pública
        )
        self.__nombre: str = nombre  # Propiedad privada

    def Get_nombre(self: object) -> str:
        return self.__nombre

    def Caminar(self: object) -> None:
        print(f"{self.full_nombre} está caminando", end="\n")


persona: Persona = Persona(nombre="Daniel", segundo_nombre="Benjamin")
print(persona.full_nombre, end="\n")
print(persona.Get_nombre(), end="\n")
persona.Caminar()

otra_persona: Persona = Persona(
    nombre="Daniel", segundo_nombre="Benajamin", alias="DanielDev"
)
print(otra_persona.full_nombre, end="\n")
otra_persona.Caminar()
# sobreescribimos la propiedad full_nombre
otra_persona.full_nombre: str = "Daniel Benjamin Perez Morales"
print(otra_persona.full_nombre, end="\n")

otra_persona.full_nombre: int = 100
print(otra_persona.full_nombre, end="\n")
