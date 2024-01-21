"""
# 02
FUNCIONES Y ALCANCE
/*

* EJERCICIO:
* - Crea ejemplos de funciones básicas que representen las diferentes
* posibilidades del lenguaje:
* Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
* - Comprueba si puedes crear funciones dentro de funciones.
* - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
* - Pon a prueba el concepto de variable LOCAL y GLOBAL.
* - Debes hacer print por consola del resultado de todos los ejemplos.
* (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 * - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 * - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 * - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 * - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

"""

VARIABLE_GLOBAL: int = 10


def funcion() -> any:
    def funcion_interna() -> None:
        print("Funcion interna")

        def funcion_interna_interna() -> None:
            print("Funcion interna interna")

        funcion_interna_interna()

    funcion_interna()
    return funcion_interna


def funcion_con_parametros_sin_retorno(parametro1: int, parametro2: int) -> None:
    global VARIABLE_GLOBAL
    VARIABLE_GLOBAL += parametro1 + parametro2


def funcion_con_parametros_con_retorno(parametro1: int, parametro2: int) -> int:
    global VARIABLE_GLOBAL
    VARIABLE_GLOBAL += parametro1 + parametro2
    return VARIABLE_GLOBAL


def funcion_sin_parametros_con_retorno() -> float:
    variable: float = 10.00
    return variable


def funcion_sin_parametros_ni_retorno() -> None:
    print("Hola mundo")


def main(str1: str, str2: str) -> int:
    contador: int = 0
    for iterable in range(1, 100, 1):
        if iterable % 3 == 0 and iterable % 5 == 0:
            print(f"{str1},{str2}")
        elif iterable % 3 == 0:
            print(f"{str1}")
        elif iterable % 5 == 0:
            print(f"{str2}")
        else:
            print(iterable)
            contador += 1
    else:
        return f"El numero de vesces que el numero se imprimio fue {contador}"


# El operador * en la definición de una función en Python se llama operador de desempaquetado o "unpacking operator". Se utiliza para permitir que una función acepte un número arbitrario de argumentos posicionales. los datos se pasan como una tupla y se pueden acceder en la función como una tupla.

# El operador ** en la definición de una función en Python se llama operador de desempaquetado o "unpacking operator". Se utiliza para permitir que una función acepte un número arbitrario de argumentos de palabras clave y valor


def funcion_con_parametros_args(*args: tuple) -> None:
    for a in args:
        print(f"Hola {a.lower()}")

# El operador ** en la definición de una función en Python se llama operador de desempaquetado de diccionarios o "dictionary unpacking operator". Se utiliza para permitir que una función acepte un número arbitrario de argumentos de palabras clave.

def funcion_con_parametros_clave_valor(**kwargs) -> None:
    for key,value in kwargs.items():
        print(f"{key} : {value}")
    """for a in enumerate(kwargs):
        print(a)"""

if __name__ == "__main__":
    # print(funcion_con_parametros_con_retorno(parametro1=10, parametro2=10))
    # print(main(str1="Primer", str2="Segundo"))
    # funcion_con_parametros_args("Daniel", "Benjamin", "Danna", "Perez", "Morales")
    funcion_con_parametros_clave_valor(nombre="Daniel", apellido="Perez", edad=20, sexo="Masculino")
