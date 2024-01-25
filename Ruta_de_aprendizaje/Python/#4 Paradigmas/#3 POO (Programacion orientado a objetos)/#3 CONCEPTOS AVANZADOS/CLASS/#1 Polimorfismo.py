"""
El polimorfismo es un concepto fundamental de la programación orientada a objetos (POO). Se refiere a la capacidad de un objeto de tomar muchas formas.

En términos más concretos, el polimorfismo permite que una interfaz única represente a una clase general de acciones. Esto significa que se puede usar un solo tipo de objeto para representar diferentes tipos de objetos y realizar diferentes acciones dependiendo del tipo de objeto.

poli es muchas y morphos es formas, por lo que polimorfismo significa muchas formas.

Todas las variables en python son polimorficas porque pueden contener objetos de diferentes tipos. A este se le llama polimorfismo en tiempo de ejecución o de inclusión. El polimorfismo en tiempo de ejecución es la capacidad de un objeto de tomar muchas formas diferentes. Osea que un objeto puede cambiar de tipo en tiempo de ejecución. Ejemplo la variable x puede ser un entero, una cadena, un booleano, etc.
"""


class Gato:
    def __init__(self: object) -> None:
        pass
    
    def Sonido(self: object) -> str:
        return "Miau"
    
class Perro:
    def __init__(self: object) -> None:
        pass
    
    def Sonido(self: object) -> str:
        return "Guau"

Gatito: object = Gato()
Perrito: object = Perro()

print(Gatito.Sonido())
print(Perrito.Sonido())
# Ambos objetos tienen el mismo metodo pero cada uno lo ejecuta de manera diferente, esto es polimorfismo

# Si hacemos este codigo en cualquiera de los lenguages de tipado estatico, nos daria un error ya que varias clases no pueden tener el mismo metodo, pero en python si se puede

def Hacer_Sonido(Animal: object) -> str:
    return Animal.Sonido()

Hacer_Sonido(Animal=Gatito)
# Esto es polimorfismo de funcion, ya que el metodo Hacer_Sonido puede recibir cualquier objeto que tenga el metodo Sonido y ejecutarlo sin problemas

