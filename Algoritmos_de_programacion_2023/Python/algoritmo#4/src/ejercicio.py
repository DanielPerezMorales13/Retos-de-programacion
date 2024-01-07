"""
#4
¿ES UN NÚMERO PRIMO?
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */

"""


def EsPrimo(numero: int) -> bool:
    string: str = ""
    contador: int = 0
    for a in range(1, 100, 1):
        string = str(numero / a)
        string += "0"
        indice: int = string.index(".")
        if string[indice + 1] == "0" and string[indice + 2] == "0": contador += 1
        else: continue
    else:
        if contador == 1 or contador > 2: return False
        elif contador == 2: return True


def main() -> None:
    for a in range(1, 100, 1):
        booleano: bool = EsPrimo(numero=a)
        print(f"{a} = {'Es primo' if booleano else 'No es primo'}")
    else: return None


if __name__ == "__main__": main()
