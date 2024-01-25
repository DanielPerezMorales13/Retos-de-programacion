"""
Los getters y setters son métodos que nos permiten acceder y modificar atributos privados de una clase.
"""


class Persona:
    def __init__(self: object, nombre: str, edad: int) -> None:
        self.__nombre = nombre
        self.__edad = edad

    # Getters para obtener los valores de los atributos privados
    def Get_Nombre(self: object) -> str:
        return self.__nombre

    def Get_Edad(self: object) -> int:
        return self.__edad

    # Setters para modificar los valores de los atributos privados
    def Set_Nombre(self: object, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre
    
    def Set_Edad(self: object,nueva_edad: int) -> None:
        self.__edad = nueva_edad


Daniel = Persona(nombre="Daniel", edad=20)

# Getters para obtener los valores de los atributos privados
print(Daniel.Get_Nombre())

# Setters para modificar los valores de los atributos privados

# Forma correcta para modificar los atributos privados
Daniel.Set_Nombre(nuevo_nombre="Benjamin")

Daniel.__nombre = "Benjamin" # No se puede modificar el atributo privado de esta forma
print(Daniel.Get_Nombre())
