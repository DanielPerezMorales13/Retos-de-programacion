"""
El polimorfismo de coerción, también conocido como polimorfismo ad hoc o polimorfismo de sobrecarga de operadores, es un tipo de polimorfismo donde los operadores o funciones pueden tener diferentes comportamientos dependiendo del tipo de sus argumentos.
"""


def main() -> None:
    num1: int = 5
    num2: float = 6.5
    print(f"Type: {type(num1)}")
    print(f"Type: {type(num2)}")

    resultado: float = num1 + num2
    print(resultado)
    print(f"Type: {type(resultado)}")
    # En este caso resultado es un float porque el operador + esta sobrecargado para que cuando se le pase un int y un float el resultado sea un float



if __name__ == "__main__":
    main()
