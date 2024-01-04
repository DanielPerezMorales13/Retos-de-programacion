"""#1
EL FAMOSO "FIZZ BUZZ"
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */"""
import os
FIZZ = "fizz"
BUZZ = "buzz"
FIIZBUZZ = "fizzbuzz"


def borrar() -> None: os.system(command="cls" if os.name == "nt" else "clear") # linux y mac posix 
def main() -> None:
    for i in range(0,100):
        if i % 3 == 0 and i % 5 == 0: print(f"{i} {FIIZBUZZ}")
        elif i % 3 == 0: print(f"{i} {FIZZ}")
        elif i % 5 == 0: print(f"{i} {BUZZ}")
        else: print(f"{i}")
if __name__ == "__main__":
    borrar()
    main()
