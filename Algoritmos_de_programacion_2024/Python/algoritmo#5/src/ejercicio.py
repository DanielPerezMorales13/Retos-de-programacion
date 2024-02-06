"""
# #04 CADENAS DE CARACTERES

## Ejercicio

```
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
```
"""

"""
Operaciones
"""

string1: str = "Hola"
string2: str = "Python"

"""
>>> Se pueden concatenar cadenas usando el operador +.
>>> sumar cadenas es equivalente a concatenarlas. 
string1 + ", " + string2 + "!" = "Hola, Python!"

"""
# Concatenación
print(string1 + ", " + string2 + "!", end="\n")

# Repetición
"""
>>> Se pueden repetir cadenas usando el operador *.
string1 * 3 = "HolaHolaHola"
"""
print(string1 * 3, end="\n")

# Indexación
"""
Se puede acceder a caracteres específicos de una cadena usando el indexado (subíndices) [].
>>> Los índices comienzan en 0.
>>> Los índices negativos cuentan desde el final de la cadena.
>>> Los índices negativos comienzan en -1.
string1[0] = "H" + string1[1] = "o" + string1[2] = "l" + string1[3] = "a"
"""
print(string1[0] + string1[1] + string1[2] + string1[3], end="\n")

# Longitud
"""
Se puede obtener la longitud de una cadena usando la función len().
>>> La longitud de una cadena es la cantidad de caracteres que contiene.
>>> len retorna un entero.
>>> Empieza a contar desde 1.
len(string2) = 6

"""
print(len(string2), end="\n")

# Slicing (porción)

"""
Se puede obtener una porción de una cadena usando la notación de rebanado (slicing) [].
>>> El slicing devuelve una nueva cadena.
>>> El slicing tiene la forma [inicio:fin:salto].
>>> El slicing tiene la forma [inicio:fin].
>>> El slicing tiene la forma [:fin].
>>> El slicing tiene la forma [inicio:].
>>> El slicing tiene la forma [:].

string2[2:6] = "thon"
string2[2:] = "thon"
string2[0:2] = "Py"
string2[:2] = "Py"
"""
print(string2[2:6], end="\n")
print(string2[2:], end="\n")
print(string2[0:2], end="\n")
print(string2[:2], end="\n")

# Busqueda
"""
Busqueda de subcadenas
>>> Se puede buscar una subcadena en una cadena usando el operador in.
>>> in retorna True si la subcadena está presente en la cadena.
>>> in retorna False si la subcadena no está presente en la cadena.
>>> in es sensible a mayúsculas y minúsculas.
"a" in string1 = True
"i" in string1 = False
"""
print("a" in string1, end="\n")
print("i" in string1, end="\n")

# Reemplazo
"""
Mediante el método replace() se pueden reemplazar subcadenas en una cadena.
string1 = "hola"
string1.replace("o", "a") = "Hala"
"""
print(string1.replace("o", "a"), end="\n")

# División
"""
El método split() divide una cadena en una lista de subcadenas.
>>> El método split() tiene dos paramtros sep y maxsplit.
>>> sep= Es el delimitador de la división de la cadena.
>>> maxsplit= Es el número máximo de divisiones que se realizarán.

"""
print(string2.split(sep="t", maxsplit=1), end="\n")


"""
El metodo .upper() convierte una cadena a mayúsculas.
El metodo .lower() convierte una cadena a minúsculas.
El metodo .title() convierte la primera letra de cada palabra a mayúsculas.
El metodo .capitalize() convierte la primera letra de la cadena a mayúsculas.
"""
# Mayúsculas, minúsculas y letras en mayúsculas
print(string1.upper(), end="\n")
print(string1.lower(), end="\n")
print("daniel perez".title(), end="\n")
print("daniel perez".capitalize(), end="\n")


"""
El metodo .strip() elimina los espacios al principio y al final de una cadena.
"""
# Eliminación de espacios al principio y al final
print(" Daniel Perez ".strip(), end="\n")

"""
El metodo .startswith() verifica si una cadena comienza con una subcadena.
El metodo .endswith() verifica si una cadena termina con una subcadena.
"""
# Búsqueda al principio y al final
print(string1.startswith("Ho"), end="\n")
print(string1.startswith("Py"), end="\n")
print(string1.endswith("la"), end="\n")
print(string1.endswith("thon"), end="\n")

string3: str = "Daniel Perez @Perezdev"

# Búsqueda de posición
"""
El metodo .find() busca la primera ocurrencia de una subcadena en una cadena.
"""
print(string3.find("Perez"), end="\n")
print(string3.find("Perez"), end="\n")
print(string3.find("M"), end="\n")
print(string3.lower().find("m"), end="\n")

# Búsqueda de ocurrencias
"""
Se pueden usar varios metodos ala vez.
El metodo .count() cuenta el número de ocurrencias de una subcadena en una cadena.
Si no se encuentra la subcadena, retorna 0
Osea, cuenta cuantas veces aparece una subcadena en una cadena.
string3 = "Daniel Perez @Perezdev"
string3.count("e") = 3
"""
print(string3.lower().count("e"), end="\n")

# Formateo
"""
Se puede formatear una cadena usando el método format().
>>> El método format() reemplaza los corchetes {} con los argumentos pasados a format().
>>> El método format() puede tomar argumentos posicionales o nombrados.
>>> El método format() puede tomar argumentos de palabras clave.
"""
print("Saludo: {}, lenguje: {}!".format(string1, string2), end="\n")
print("Saludo: {0}, lenguje: {1}!".format(string1, string2), end="\n")
print(
    "Saludo: {palabra1}, lenguje: {palabra2}!".format(
        palabra1=string1, palabra2=string2
    ),
    end="\n",
)


"""
El operador % se puede usar para formatear una cadena.
>>> El operador % toma un formato y un argumento.
>>> El operador % puede tomar varios argumentos.
opeadoraes con %
>>> %s: cadena
>>> %d: entero
>>> %f: flotante
>>> %x: hexadecimal
>>> %o: octal
>>> %e: notación científica
>>> %g: notación científica o decimal
>>> %%: signo de porcentaje
"""
print("Saludo: %s, lenguje: %s!" % (string1, string2), end="\n")
print("Suma: %d + %d = %d" % (2, 3, 2 + 3), end="\n")
print("Suma: %f + %f = %f" % (2.5, 3.5, 2.5 + 3.5), end="\n")
print("Suma: %x + %x = %x" % (2, 3, 2 + 3), end="\n")
print("Suma: %o + %o = %o" % (2, 3, 2 + 3), end="\n")
print("Suma: %e + %e = %e" % (2, 3, 2 + 3), end="\n")
print("Suma: %g + %g = %g" % (2, 3, 2 + 3), end="\n")
print("Porcentaje: %% %d" % 100, end="\n")

"""
f-strings
>>> Las f-strings son cadenas formateadas.
>>> Las f-strings tienen la forma f"{}".
>>> Las f-strings pueden tomar expresiones.
>>> Las f-strings pueden tomar variables.
>>> Las f-strings pueden tomar funciones.
>>> Las f-strings pueden tomar métodos.
>>> Las f-strings pueden tomar operaciones.
"""
print(f"Saludo: {string1}, lenguje: {string2}!", end="\n")

# Tranformación en lista de caracteres
"""
Se puede transformar una cadena en una lista de caracteres usando la función list().
>>> La lista de caracteres es una lista de cadenas.
>>> La lista de caracteres es una lista de longitud 1.
>>> La lista de caracteres es una lista de caracteres.

string3 = "Daniel Perez @Perezdev"
list(string3) = ['D', 'a', 'n', 'i', 'e', 'l', ' ', 'P', 'e', 'r', 'e', 'z', ' ', '@', 'P', 'e', 'r', 'e', 'z', 'd', 'e', 'v']
"""
print(list(string3), end="\n")

# Transformación de lista en cadena
"""
El método join() une una lista de cadenas en una sola cadena.
>>> El método join() toma una lista de cadenas.
>>> "separador".join(lista)
"""
lista1: list[str] = [string1, ", ", string2, "!"]
print("".join(lista1), end="\n")

# Transformaciones numéricas
"""
El método int() convierte una cadena en un entero.
"""
string4: str = "123456"
string4 = int(string4)
print(string4, end="\n")


"""
El método float() convierte una cadena en un flotante.
"""
string5 = "123456.123"
string5 = float(string5)
print(string5, end="\n")

# Comprobaciones varias
"""
El método .isalnum() verifica si una cadena es alfanumérica. Osea, si solo contiene letras y números.
El método .isalpha() verifica si una cadena es alfabética. Osea, si solo contiene letras.
El método .isnumeric() verifica si una cadena es numérica. Osea, si solo contiene números.
"""
string4 = "123456"
print(string1.isalnum(), end="\n")
print(string1.isalpha(), end="\n")
print(string4.isalpha(), end="\n")
print(string4.isnumeric(), end="\n")


def vericarString(palabra: str) -> dict[str, bool]:
    resultado: dict[str, bool] = dict()
    lista: list[str] = list(palabra)
    listaCaracteresRepetido: list[str] = list()
    contador: int = 0
    if palabra == palabra[::-1]:
        resultado["Palíndromos"] = True
    else:
        resultado["Palíndromos"] = False

    for caracter in lista:
        if caracter in palabra:
            contador += 1
        else:
            pass
    else:
        if len(palabra) == contador:
            resultado["Anagramas"] = True
        else:
            resultado["Anagramas"] = False
        contador: int = 0
    for caracter in lista:
        if caracter in palabra:
            if caracter in listaCaracteresRepetido:
                resultado["Isogramas"] = False
                break
            else:
                listaCaracteresRepetido.append(caracter)
                resultado["Isogramas"] = True

    return resultado


print(vericarString(palabra="perro"))
