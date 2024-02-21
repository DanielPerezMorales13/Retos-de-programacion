# Tema: Ejercicios

import os


def borrar() -> None:
    os.system(command="clear" if os.name == "posix" else "cls")


def main() -> None:
    borrar()
    print(
        """Ejericios:
1. EL FAMOSO "FIZZ BUZZ”
2. ¿ES UN ANAGRAMA?
3. LA SUCESIÓN DE FIBONACCI
4. ¿ES UN NÚMERO PRIMO?
5. INVIRTIENDO CADENAS
6. Salir

""",
        end="\n",
    )
    eleccion: str = str(input("Elige un ejercicio: "))
    match eleccion:
        case "1":
            """
            EL FAMOSO "FIZZ BUZZ”:
            Escribe un programa que muestre por consola (con un print) los
            números de 1 a 100 (ambos incluidos y con un salto de línea entre
            cada impresión), sustituyendo los siguientes:
            - Múltiplos de 3 por la palabra "fizz".
            - Múltiplos de 5 por la palabra "buzz".
            - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
            """

            for index in range(1, 101, 1):
                if index % 3 == 0 and index % 5 == 0:
                    print("fizzbuz", end="\n")
                elif index % 3 == 0:
                    print("fizz", end="\n")
                elif index % 5 == 0:
                    print("buzz", end="\n")
                else:
                    print(index, end="\n")

        case "2":
            """
            ¿ES UN ANAGRAMA?
            Escribe una función que reciba dos palabras (String) y retorne
            verdadero o falso (Bool) según sean o no anagramas.
            - Un Anagrama consiste en formar una palabra reordenando TODAS
            las letras de otra palabra inicial.
            - NO hace falta comprobar que ambas palabras existan.
            - Dos palabras exactamente iguales no son anagrama.
            """

            palabra_one: str = str(input("ingrese la primera palabra: "))
            palabra_two: str = str(input("ingrese la palabra dos: "))

            if palabra_one.lower() == palabra_two.lower():
                print("No son anagramas")
            print(
                "Es anagrama"
                if sorted(palabra_one.lower(), reverse=False)
                == sorted(palabra_two.lower(), reverse=False)
                else "No es anagrama"
            )

        case "3":
            """
            LA SUCESIÓN DE FIBONACCI
            Escribe un programa que imprima los 50 primeros números de la sucesión
            de Fibonacci empezando en 0.
            - La serie Fibonacci se compone por una sucesión de números en
            la que el siguiente siempre es la suma de los dos anteriores.
            0, 1, 1, 2, 3, 5, 8, 13...
            """

            inicio: int = 0
            siguiente: int = 1

            for index in range(0, 50, 1):
                print(inicio, end="\n")
                fibonacci_num = inicio + siguiente
                inicio = siguiente
                siguiente = fibonacci_num

        case "4":
            """
            ¿ES UN NÚMERO PRIMO?
            Escribe un programa que se encargue de comprobar si un número es o no primo.
            Hecho esto, imprime los números primos entre 1 y 100.
            """

            for numero in range(1, 101):
                if numero >= 2:
                    es_divisible: bool = False
                    for index in range(2, numero):
                        if numero % index == 0:
                            es_divisible = True
                            break
                    if not es_divisible:
                        print(numero, end="\n")

        case "5":
            """
            INVIRTIENDO CADENAS
            Crea un programa que invierta el orden de una cadena de texto
            sin usar funciones propias del lenguaje que lo hagan de forma automática.
            - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
            """

            texto: str = str(input("Ingrese el texto: "))
            texto_len: int = len(texto)
            texto_reversa: str = ""
            for index in range(0, texto_len, 1):
                texto_reversa += texto[texto_len - index - 1]
            print(texto_reversa, end="\n")

        case "6":
            """
            Salir
            """
            exit(code="Saliendo...")
        case _:
            print("Opción no valida", end="\n")

    str(input("Presione una tecla para continuar..."))
    main()


if __name__ == "__main__":
    main()
