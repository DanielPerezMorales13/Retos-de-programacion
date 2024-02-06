"""/*
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 */
"""

# comentario de una linea ==> URL: https://www.python.org/

"""
comentario 
de 
multiples
lineas
"""

# tipos de datos

def main() -> str:
    string: str = "Daniel Perez"
    integer: int = 18
    boolean: bool = True 
    boolean: bool = False
    return "Hola Python"

if __name__ == "__main__":
    print(main())

