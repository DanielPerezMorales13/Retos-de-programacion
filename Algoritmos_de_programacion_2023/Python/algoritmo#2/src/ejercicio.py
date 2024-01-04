"""#2
¿ES UN ANAGRAMA?
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */

"""
import os
def borrar() -> None: os.system(command="cls" if os.name == "nt" else "clear") # linux y mac posix 

def anagrama(str1: str, str2: str) -> bool:
    return f"Es Anagrama =  {sorted(str1, reverse=False) == sorted(str2, reverse=False)}"

def main() -> None:
    print(anagrama(str1=str(input("Primera palabra: ").lower()), str2=str(input("Segunda palabra: ").lower())))

if __name__ == "__main__":
    borrar()
    main()
