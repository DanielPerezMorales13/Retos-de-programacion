"""
#3
LA SUCESIÓN DE FIBONACCI
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
"""
import os


def borrar() -> None:
    os.system(command="cls" if os.name == "nt" else "clear")  # linux y mac posix


def fibonacci(lista: list[int], new_number: int = 0) -> list[int]:
    print(new_number)
    new_number: int = lista[-1] + lista[-2]
    lista.append(new_number)
    try:
        fibonacci(lista, new_number)
    except RecursionError:
        exit(code="Fin del programa")


def main() -> None:
    lista: list[int] = list([0, 1])
    fibonacci(lista=lista)


if __name__ == "__main__":
    borrar()
    main()
