"""
Herencias - Ejercicio 2

Ejercicio de herencia y uso de super:

Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales: Persona y Estudiante. La clase Persona tendrá los atributos de nombre y edad y un método que imprima el nombre y la edad de la persona. La clase Estudiante heredará de la clase Persona y también tendrá un atributo adicional: grado y un método que imprima el grado del estudiante.
Deberás utilizar super en el método de inicialización (init) para reutilizar el código de la clase padre (Persona). Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus métodos para asegurarte de que todo funciona correctamente.
"""


class Persona:
    def __init__(self: object, nombre: str, edad: int) -> None:
        self.nombre: str = nombre
        self.edad: int = edad

    def Datos_Persona(self: object) -> str:
        return f"""
Nombre: {self.nombre}
Edad: {self.edad}
    """


class Estudiante(Persona):
    def __init__(self: object, nombre: str, edad: int, grado: str) -> None:
        super().__init__(nombre, edad)
        self.grado: str = grado

    def Grado(self: object) -> str:
        # return "Grado: {grado_actual}".format(grado_actual=self.grado)  formato de impresion con .format y asignacion de variables 
        
        # return "Grado: {}".format(self.grado) formato de impresion con .format 
        
        # return "Grado: {0}".format(self.grado) formato de impresion con .format y asignacion de orden de impresion con {0} {1} {2} etc
        
        # return "Grado: %s" % (self.grado) formato de impresion con %s 
        
        return f"Grado: {self.grado}" # formato de impresion con f-string


Daniel: object = Estudiante(nombre="Daniel", edad=20, grado="10mo grado")
print(Daniel.nombre)
print(Daniel.edad)
print(Daniel.Datos_Persona())
print(Daniel.Grado())