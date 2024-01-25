"""
El encapsulamiento es un mecanismo que permite restringir el acceso a métodos y variables de un objeto, evitando que se puedan manipular por fuera de la clase.

El guion bajo es una convención utilizada para indicar que un atributo o método es privado en Python. Sin embargo, es importante tener en cuenta que esta convención no impide el acceso a estos elementos desde fuera de la clase. El encapsulamiento en Python se basa en la convención y en la responsabilidad del programador de no acceder directamente a los atributos o métodos privados desde fuera de la clase.

Existe 3 tipos de encapsulamiento:

>>> - Publico: Cualquier atributo o método puede ser llamado desde cualquier parte, ya sea dentro de la clase o fuera de ella. Este es el comportamiento por defecto en Python

>>> - Protegido: Los atributos o métodos solo pueden ser llamados dentro de la clase o de sus subclases. Para definir un atributo o método como protegido se debe escribir el nombre del atributo o método iniciando con un guion bajo.

>>> - Privado: Los atributos o métodos solo pueden ser llamados dentro de la clase. Para definir un atributo o método como privado se debe escribir el nombre del atributo o método iniciando con dos guiones bajos.

Las ventajas del encapsulamiento son: 

>>> - Evitar que los atributos o métodos sean llamados desde cualquier parte del programa, lo cual puede llevar a comportamientos inesperados.

>>> - Dar un control más estricto sobre cómo se manipulan los datos de una clase.

>>> - Facilitar la modificación de la implementación interna de una clase sin afectar 
el resto del programa.

>>> - Ayudar a proteger la integridad de los datos de una clase.

>>> - Ocultar la complejidad al usuario de una clase, mostrando solo los métodos que son necesarios para interactuar con dicha clase.
"""

# Para poder ejecutar metodo privado desde fuera de la clase se debe crear un metodo publico o protegido que llame al metodo privado


class MiClase:
    def __init__(self: object) -> None:
        self.atributo_publico = "Soy un atributo publico"
        self._atributo_protegido = "Soy un atributo protegido"
        self.__atributo_privado = "Soy un atributo inalcanzable desde fuera de la clase"

    def Metodo_Publico(self: object) -> str:
        return "Soy un metodo publico"

    def _Metodo_Protegido(self: object) -> str:
        return "Soy un metodo protegido"

    def __Metodo_Privado(self: object) -> str:
        return "Soy un metodo inalcanzable desde fuera de la clase"

    def Get_Funcion_Metodo_Privado(self: object) -> str:
        return self.__Metodo_Privado()


objeto: object = MiClase()
print(objeto.Get_Funcion_Metodo_Privado())
print(objeto.atributo_publico)  # se puede acceder a un atributo publico
print(objeto._atributo_protegido)  # se puede acceder a un atributo protegido
# print(objeto.__atributo_privado) # no se puede acceder a un atributo privado

print(objeto.Metodo_Publico())  # se puede acceder a un metodo publico
print(objeto._Metodo_Protegido())  # se puede acceder a un metodo protegido
# print(objeto.__metodo_privado()) # no se puede acceder a un metodo privado
