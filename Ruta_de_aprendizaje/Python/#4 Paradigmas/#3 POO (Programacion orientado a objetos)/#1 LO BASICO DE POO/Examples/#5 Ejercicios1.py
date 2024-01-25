"""
crear una clase estudiante con los siguientes atributos:
nombre, edad y grado

metodos:

estudiar: imprime f"el estudiante {} esta estudiando"
debemos preguntarle al usuario si quiere que el estudiante estudie, si la respuesta es si, entonces llamamos al metodo estudiar, si la respuesta es no, entonces no llamamos al metodo estudiar.
"""

import os


def borrar() -> None:
    os.system(command="cls" if os.name == "nt" else "clear")


class Estudiante:
    def __init__(self: object, nombre: str, edad: int, grado: str) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.grado: str = grado

    def Estudiar(self: object) -> str:
        return f"El estudiante {self.nombre} esta estudiando"


nombre: str = str(input("Ingrese el nombre del estudiante: ")).capitalize()

while True:
    try:
        edad: int = int(input("Ingrese la edad del estudiante: "))
        break
    except ValueError:
        borrar()
grado: str = str(input("Ingrese el grado del estudiante: ")).lower()

estudiante: object = Estudiante(nombre=nombre, edad=edad, grado=grado)

borrar()
print(
    f"""
El Estudiante {estudiante.nombre},
Tiene {estudiante.edad} años,
Y esta en el grado {estudiante.grado}
"""
)

while True:
    if preguntar := str(input("Quieres estudiar (SI/NO)")) == "si":
        print(estudiante.Estudiar())
        break
    elif preguntar == "no":
        break
    else:
        borrar()
