"""
Built-in Functions -> Funciones integradas en python
--------------------------------------------------------------|
A            | B             | C             | D              |
abs()        | bin()         | callable()    | delattr()      |
aiter()      | bool()        | chr()         | dict()         |
all()        | breakpoint()  | classmethod() | dir()          |
anext()      | bytearray()   | compile()     | divmod()       |
any()        | bytes()       | complex()     |                |
ascii()      |               |               |                |
--------------------------------------------------------------|
E            | F             | G             | H              |
enumerate()  | filter()      | getattr()     | hasattr()      |
eval()       | float()       | globals()     | hash()         |
exec()       | format()      |               | help()         |   
             | frozenset()   |               | hex()          |
--------------------------------------------------------------|
I            | L            | M             | N               |   
id()         | len()        | map()         | next()          |
input()      | list()       | max()         |                 |
int()        | locals()     | memoryview()  |                 |
isinstance() |              | min()         |                 |
issubclass() |              |               |                 |
iter()       |              |               |                 |
--------------------------------------------------------------|
O            | P             | R             | S              |
object()     | pow()         | range()       | set()          |
oct()        | print()       | repr()        | setattr()      |
open()       | property()    | reversed()    | slice()        |
ord()        |               | round()       | sorted()       |
             |               |               | staticmethod() |
             |               |               | str()          |
             |               |               | sum()          |
             |               |               | super()        |
--------------------------------------------------------------|
T            | U             | V             | Z              |
tuple()      | type()        | vars()        | zip()          |
type()       |               |               |                |
--------------------------------------------------------------|
_            |               |               |                |
__import__() |               |               |                |
--------------------------------------------------------------|
"""


def ABS() -> None:
    # abs()
    """
    La función abs() en Python devuelve el valor absoluto de un número.
    El valor absoluto de un número es su distancia desde 0 en la línea de números reales,
    sin tener en cuenta la dirección. Por lo tanto, abs(-5) es 5 y abs(5) también es 5.
    """
    print(abs(-5))  # Imprime: 5
    print(abs(5))  # Imprime: 5
    print(abs(0))  # Imprime: 0


def AITER() -> None:
    # aiter()
    """
    La función aiter() es una función incorporada en Python que se utiliza en el contexto de la programación asíncrona. Esta función se utiliza para obtener un objeto iterador asíncrono de un objeto iterable asíncrono.

    Un objeto iterable asíncrono es un objeto que define un método __aiter__() que devuelve un objeto iterador asíncrono. Un objeto iterador asíncrono es un objeto que define un método __anext__() que devuelve un objeto Future.
    """


def ALL() -> None:
    # all()

    """
    La función all() en Python toma un iterable (como una lista o un conjunto) y devuelve True si todos los elementos del iterable son verdaderos (o si el iterable está vacío)
    """
    # Todos los elementos son verdaderos
    print(all([True, True, True]))  # Imprime: True

    # Uno de los elementos es falso
    print(all([True, False, True]))  # Imprime: False

    # El iterable está vacío
    print(all([]))  # Imprime: True


def ANEXT() -> None:
    """a función anext() es una función de la biblioteca estándar asyncio de Python. Se utiliza para obtener el próximo elemento de un iterador asíncrono."""


def ANY() -> None:
    """La función any() en Python toma un iterable (como una lista o un conjunto) y devuelve True si al menos uno de los elementos del iterable es verdadero. Si el iterable está vacío, devuelve False."""
    # Al menos un elemento es verdadero
    print(any([False, False, True]))  # Imprime: True

    # Todos los elementos son falsos
    print(any([False, False, False]))  # Imprime: False

    # El iterable está vacío
    print(any([]))  # Imprime: False


def ASCII() -> None:
    r"""La función ascii() en Python convierte un objeto en una cadena de caracteres ASCII. Los caracteres no ASCII se escapan con secuencias de escape \x, \u o \U."""
    no_ascii_string: str = "Héllo, Wórld!"
    ascii_string: str = ascii(no_ascii_string)
    print(ascii_string)  # Imprime: 'H\\xe9llo, W\\xf3rld!'


def BIN() -> None:
    """La función bin() en Python convierte un número entero en una cadena binaria."""
    number: int = 10
    binary_number: str = bin(number)
    print(binary_number)  # Imprime: '0b1010'


def BOOL() -> None:
    """La función bool() en Python convierte un valor en un valor booleano (True o False)."""
    # Cuando se usa en un valor no vacío o no cero, bool() devuelve True
    print(bool(10))  # Imprime: True
    print(bool("Hello"))  # Imprime: True

    # Cuando se usa en un valor vacío o cero, bool() devuelve False
    print(bool(0))  # Imprime: False
    print(bool(0.0))  # Imprime: False
    print(bool(""))  # Imprime: False
    print(bool(False))  # Imprime: False


def BREAKPOINT() -> None:
    """La función breakpoint() en Python se utiliza para establecer un punto de interrupción en el código, que permite la depuración interactiva. Cuando se ejecuta el código y se alcanza el punto de interrupción, la ejecución se detiene y puedes examinar el estado del programa."""
    queso: int = 10
    pan: int = 20
    breakpoint()  # La ejecución se detendrá aquí si estás utilizando un depurador
    total: int = queso + pan
    print(total)
    """pdb es el acrónimo de Python DeBugger. Es un módulo incorporado en Python que se utiliza para la depuración de código. Proporciona una interfaz interactiva para ejecutar código, evaluar expresiones, inspeccionar variables, controlar la ejecución del programa y mucho más."""


def BYTEARRAY() -> None:
    """La función bytearray() en Python crea y devuelve un objeto bytearray, que es una matriz de bytes."""
    # Crear un bytearray a partir de una lista list() o tuple() o un set() de enteros
    lista_bytearray: bytearray = bytearray([65, 66, 67, 68])
    print(lista_bytearray)  # Imprime: bytearray(b'ABCD')

    # Crear un bytearray a partir de una cadena de caracteres
    lista_bytearray: bytearray = bytearray("Hello, World!", "utf-8")
    print(lista_bytearray)  # Imprime: bytearray(b'Hello, World!')
    print(type(lista_bytearray))  # Imprime: <class 'bytearray'>

    # La b antes de la cadena en bytearray(b'ABCD') indica que la cadena es una cadena de bytes, no una cadena de texto normal.


def BYTES() -> None:
    """La función bytes() en Python crea y devuelve un objeto de bytes, que es una secuencia inmutable de bytes."""
    # Crear un objeto de bytes a partir de una lista de enteros
    byte: bytes = bytes([65, 66, 67, 68])
    print(byte)  # Imprime: b'ABCD'

    # Crear un objeto de bytes a partir de una cadena de caracteres
    byte:bytes = bytes("Hello, World!", "utf-8") # tambien utf-16
    print(byte)  # Imprime: b'Hello, World!'



if __name__ == "__main__":
    # ABS()
    # todo AITER() pendiente
    # ALL()
    # todo ANEXT() pendiente
    # ANY()
    # ASCII()
    # BIN()
    # BOOL()
    # BREAKPOINT()
    # BYTEARRAY()
    BYTES()
