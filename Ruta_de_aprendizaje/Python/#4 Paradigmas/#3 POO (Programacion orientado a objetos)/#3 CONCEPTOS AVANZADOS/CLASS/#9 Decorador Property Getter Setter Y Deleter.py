""" 
@property es un decorador reservado en Python que nos permite definir métodos getter, setter y deleter para atributos de clase. Esto nos permite acceder a los atributos de una clase como si fueran públicos, pero sin perder la seguridad de que sean privados.

Ademas de que accedemos a el como si fuera un atributo, al llamarlo no es necesario poner los parentesis.
"""


class Persona:
    def __init__(self: object, nombre: str, edad: int) -> None:
        self.__nombre: str = nombre
        self.__edad: int = edad

    @property
    # Getter
    # Estamos oculatando el nombre real del atributo y lo estamos reemplazando por el nombre del decorador ademas obtenemos el valor del atributo tambien de que no es necesario poner los parentesis al llamarlo
    def nombre(self: object) -> str:
        return self.__nombre

    @nombre.setter
    # Setter
    # Ponemos nombre.setter para que sepa que es el setter del atributo nombre lo que hace es cambiar el valor del atributo ademas de que no es necesario poner los parentesis al llamarlo
    def nombre(self: object, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre

    @nombre.deleter
    # deleter
    # Ponemos nombre.deleter para que sepa que es el deleter del atributo nombre lo que hace es eliminar el atributo ademas de que no es necesario poner los parentesis al llamarlo
    def nombre(self: object) -> None:
        del self.__nombre


daniel: object = Persona(nombre="Daniel", edad=20)
print(daniel.nombre)
daniel.nombre = "Benjamin"
del daniel.nombre
try: print(daniel.nombre)
except AttributeError: print("El atributo nombre ha sido eliminado")
else: print("El atributo nombre no ha sido eliminado")
finally: print("Fin del programa")
