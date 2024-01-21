"""#01
OPERADORES Y ESTRUCTURAS DE CONTROL
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""
import os


def borrar() -> None:
    os.system(command="cls" if os.name == "nt" else "clear")


def main() -> None:
    print("operadores aritmeticos".title())
    # Operadores aritméticos
    a = 10
    b = 3
    print(a + b)  # Suma
    print(a - b)  # Resta
    print(a * b)  # Multiplicación
    print(a / b)  # División
    print(a % b)  # Módulo
    print(a**b)  # Exponenciación
    print(a // b)  # División entera
    str(input(""))
    borrar()

    print("operadores de comparacion".title())
    # Operadores de comparación
    print(a == b)  # Igual a
    if a == b:
        pass
    print(a != b)  # No igual a
    if a != b:
        pass
    print(a > b)  # Mayor que
    if a > b:
        pass
    print(a < b)  # Menor que
    if a < b:
        pass
    print(a >= b)  # Mayor o igual que
    if a >= b:
        pass
    print(a <= b)  # Menor o igual que
    if a <= b:
        pass
    str(input(""))
    borrar()

    print("operadores lógicos".title())
    # Operadores lógicos
    print(True and False)  # AND lógico
    print(True or False)  # OR lógico
    print(not True)  # NOT lógico
    str(input(""))
    borrar()

    print("operadores de asignacion".title())
    # Operadores de asignación
    a = 10  # Asignación
    a += 5  # Suma y asignación
    a -= 2  # Resta y asignación
    a *= 3  # Multiplicación y asignación
    a /= 2  # División y asignación
    a %= 3  # Módulo y asignación
    a **= 2  # Exponenciación y asignación
    a //= 2  # División entera y asignación
    str(input(""))
    borrar()

    print("operadores de identidad".title())
    # Operadores de identidad
    print(a is b)  # is
    print(a is not b)  # is not
    str(input(""))
    borrar()

    print("operadores de pertenecia".title())
    # Operadores de pertenencia
    lista = [1, 2, 3, 4, 5]
    print(3 in lista)  # in
    print(6 not in lista)  # not in
    str(input(""))
    borrar()

    print("operadores de bits".title())
    # Operadores de bits
    a = 60  # 60 = 0011 1100
    b = 13  # 13 = 0000 1101
    print(a & b)  # AND de bits
    print(a | b)  # OR de bits
    print(a ^ b)  # XOR de bits
    print(~a)  # NOT de bits
    print(a << 2)  # Desplazamiento a la izquierda
    print(a >> 2)  # Desplazamiento a la derecha
    str(input(""))
    borrar()


def ejercicio() -> None:
    """
        Crea un programa que imprima por consola todos los números comprendidos
    * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
    """
    for iterable in range(10, 56):
        if iterable % 2 == 0 and iterable != 16 and iterable % 3 != 0:
            print(iterable)


if __name__ == "__main__":
    main()
    # ejercicio()
