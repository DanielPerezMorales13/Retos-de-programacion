"""
SRP": "Single Responsability Principle" Significa en español Principio de responsabilidad unica. 

>>> Este principio dice que una clase debe tener una sola responsabilidad y no muchas responsabilidades.

>>> Este principio evita que los desarrolladores creen clases con muchas responsabilidades y que sean dificiles de mantener y de entender.
"""


class TanqueCombustible:
    def __init__(self: object) -> None:
        self.combustible: int = 100

    def Agregar_Combustible(self: object, cantidad: int) -> None:
        self.combustible += cantidad
        return None

    def Obtener_Combustible(self: object) -> int:
        return self.combustible

    def Usar_Combustible(self: object, cantidad: int) -> None:
        self.combustible -= cantidad
        return None


class Auto:
    def __init__(self: object, tanque: object) -> None:
        self.posicion: int = 0
        self.tanque: object = tanque

    def Mover(self: object, distancia: int) -> str:
        if self.tanque.Obtener_Combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.Usar_Combustible(cantidad=distancia / 2)
            return "Has movido el auto exitosamente"
        else:
            return "No hay suficiente combustible"

    def Obtener_Posicion(self: object) -> int:
        return self.posicion


tanque = TanqueCombustible()
mi_auto: object = Auto(tanque=tanque)
print(mi_auto.Obtener_Posicion())

print(mi_auto.Mover(distancia=10))

print(mi_auto.Obtener_Posicion())

print(mi_auto.Mover(distancia=20))

print(mi_auto.Obtener_Posicion())

print(mi_auto.Mover(distancia=60))

print(mi_auto.Obtener_Posicion())

print(mi_auto.Mover(distancia=100))

print(mi_auto.Obtener_Posicion())

print(mi_auto.Mover(distancia=100))

print(mi_auto.Obtener_Posicion())
