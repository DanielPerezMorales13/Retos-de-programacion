# Tema: Regular Expressions (RegEx) - Expresiones Regulares

"""
re es un módulo que permite trabajar con expresiones regulares.
Las expresiones regulares son patrones utilizados para encontrar una determinada combinación de caracteres dentro de una cadena de texto.
"""
import re

# match

"""
El metodo match() busca un patrón al principio de una cadena de texto. Si el patrón es encontrado, devuelve un objeto match, en caso contrario devuelve None.

los parámetros son:

>>> pattern: El patrón a buscar en la cadena de texto.

>>> string: La cadena de texto en la que se buscará el patrón.

>>> flags: Opcional. Se utiliza para especificar diferentes banderas. Por ejemplo, re.I es para que no sea sensible a mayúsculas y minúsculas.

todas las banderas o flags disponibles en el módulo re son:

>>> re.I o re.IGNORECASE: No es sensible a mayúsculas y minúsculas. Por ejemplo, "LECCIÓN" y "lección" son iguales.

>>> re.M o re.MULTILINE: Permite que el patrón busque en todas las líneas de la cadena de texto. Por ejemplo, ^ busca al principio de cada línea.

>>> re.S o re.DOTALL: Permite que el patrón busque en todas las líneas de la cadena de texto, incluyendo saltos de línea. Por ejemplo, . busca cualquier carácter, incluyendo saltos de línea.

>>> re.X o re.VERBOSE: Permite que el patrón sea más legible, ya que ignora los espacios en blanco y los comentarios. Por ejemplo, "a b" es igual a "ab".

>>> re.A o re.ASCII: Hace que el patrón busque en la cadena de texto utilizando el código ASCII. Por ejemplo, \w no incluirá caracteres acentuados.

>>> re.U o re.UNICODE: Hace que el patrón busque en la cadena de texto utilizando el código Unicode. Por ejemplo, \w incluirá caracteres acentuados.

>>> re.LOCALE: Hace que el patrón busque en la cadena de texto utilizando el código de localización. Por ejemplo, \w incluirá caracteres acentuados.

>>> re.DEBUG: Muestra información de depuración.

>>> El flag por defecto es 0, que no tiene ninguna bandera activada.
"""

string: str = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
otra_string: str = "Esta no es la lección número 6: Manejo de ficheros"

match: re.Match = re.match(pattern="Esta es la lección", string=string, flags=re.I)
# flags=re.I es para que no sea sensible a mayúsculas y minúsculas
# flags=re.IGNORECASE es para que no sea sensible a mayúsculas y minúsculas

"""
Si imprimo match, me mostrará el objeto match, que es un objeto que contiene la información de la coincidencia encontrada. Si no encuentra ninguna coincidencia, me mostrará None.

<re.Match object; span=(0, 18), match='Esta es la lección'>

donde:

re.Match object es el tipo de objeto.

span=(0, 18) es la posición inicial y final del patrón encontrado.

match='Esta es la lección' es la cadena de texto que coincide con el patrón.

>>> Si imprimo match.group(), me mostrará la cadena de texto que coincide con el patrón.

>>> Si imprimo match.span(), me mostrará la posición inicial y final del patrón encontrado.

"""
print(match, end="\n")

print(match.group(), end="\n")

"""
El método span() devuelve una tupla con la posición inicial y final del patrón encontrado.
print(match.span(), end="\n") # (0, 18)
"""
empieza, termina = match.span()
print(string[empieza:termina:1], end="\n")

match = re.match(pattern="Esta no es la lección", string=otra_string, flags=0)
# # if not(match == None): # Otra forma de comprobar el None
# if match != None: # Otra forma de comprobar el None
if match is not None:
    print(match, end="\n")
    empieza, termina = match.span()
    print(otra_string[empieza:termina:1], end="\n")

print(re.match(pattern="Expresiones Regulares", string=string, flags=0), end="\n")


# search

"""
El método search() busca un patrón en toda la cadena de texto. Si el patrón es encontrado, devuelve un objeto match, en caso contrario devuelve None. Si el patrón es encontrado más de una vez, devuelve el primer objeto match encontrado.

Los parámetros son:

>>> pattern: El patrón a buscar en la cadena de texto.

>>> string: La cadena de texto en la que se buscará el patrón.

>>> flags: Opcional. Se utiliza para especificar diferentes banderas. Por ejemplo, re.I es para que no sea sensible a mayúsculas y minúsculas.
"""
search: re.Match = re.search("lección", string, re.I)
print(search, end="\n")

"""
El método span() devuelve una tupla con la posición inicial y final del patrón encontrado.

Se le pasa el objeto match que se obtiene con el método search().
"""
empieza, termina = search.span()
print(string[empieza:termina:1], end="\n")

# findall
"""
El método findall() busca un patrón en toda la cadena de texto. Si el patrón es encontrado, devuelve una lista con todas las coincidencias encontradas, en caso contrario devuelve una lista vacía.

los parámetros son:

>>> pattern: El patrón a buscar en la cadena de texto.

>>> string: La cadena de texto en la que se buscará el patrón.

>>> flags: Opcional. Se utiliza para especificar diferentes banderas. Por ejemplo, re.I es para que no sea sensible a mayúsculas y minúsculas.
"""

findall: list[str] = re.findall(pattern="lección", string=string, flags=re.IGNORECASE)
print(findall, end="\n")

# split

"""
El metodo split() divide la cadena de texto en una lista, utilizando el patrón como separador. Si el patrón no es encontrado, devuelve una lista con la cadena de texto original. Si el patrón es encontrado, devuelve una lista con las partes de la cadena de texto que no contienen el patrón. 

los parámetros son:
>>> pattern: El patrón a buscar en la cadena de texto.
>>> string: La cadena de texto que se dividirá.
>>> maxsplit: Opcional. Especifica el número máximo de divisiones que se realizarán. Por defecto es 0, que no tiene límite.
"""
print(re.split(pattern=":", string=string, flags=0, maxsplit=0), end="\n")

# sub

"""
El método sub() reemplaza todas las coincidencias de un patrón en una cadena de texto, con otra cadena de texto. Si el patrón no es encontrado, devuelve la cadena de texto original. Si el patrón es encontrado, devuelve la cadena de texto con las coincidencias reemplazadas.

los parámetros son:

>>> pattern: El patrón a buscar en la cadena de texto.

>>> repl: La cadena de texto que reemplazará las coincidencias del patrón.

>>> string: La cadena de texto en la que se buscará el patrón.

>>> count: Opcional. Especifica el número máximo de reemplazos que se realizarán. Por defecto es 0, que no tiene límite.

>>> flags: Opcional. Se utiliza para especificar diferentes banderas. Por ejemplo, re.I es para que no sea sensible a mayúsculas y minúsculas.
"""


"""
En esta expresión regular, [lL]ección, [lL] significa que puede ser l o L, y ección significa que tiene que ser ección.
"""
print(
    re.sub(pattern="[l|L]ección", repl="LECCIÓN", string=string, count=0, flags=0),
    end="\n",
)

print(
    re.sub(
        pattern="Expresiones Regulares", repl="RegEx", string=string, count=0, flags=0
    ),
    end="\n",
)


# Regular Expressions Patterns o Patrones de Expresiones Regulares

# Para aprender y validar expresiones regulares: https://regex101.com o https://pythex.org/

"""
Se le pone una r al principio de la cadena de texto, para que sea una cadena de texto cruda o raw string. Esto es para que los caracteres especiales no sean interpretados como tal. Por ejemplo, \n es un salto de línea, pero r"\n" es el texto \n.
"""

"""
Cadenas de texto crudas (raw strings): En Python, las cadenas de texto crudas se crean anteponiendo una 'r' al principio de la cadena. Esto evita que los caracteres de escape (como '\n' para un salto de línea, '\t' para un tabulador, etc.) sean interpretados. Esto es especialmente útil en las expresiones regulares, donde los caracteres de escape son comunes.
"""

"""
En esta expresión regular, [lL]ección, [lL] significa que puede ser l o L, y ección significa que tiene que ser ección.
"""

pattern: str = r"[lL]ección"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")

"""
En esta expresión regular, [lL]ección|Expresiones, [lL] significa que puede ser l o L, ección significa que tiene que ser ección, | significa o, y Expresiones significa que tiene que ser Expresiones. O sea, que tiene que ser lección o Lección, o Expresiones. Si no se pone |, tiene que ser lección o Lección y Expresiones. Si se pone |, tiene que ser lección o Lección o Expresiones. Si en la cadena de texto hay lección, Lección o Expresiones, se mostrará en la lista.
"""
pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")

string: str = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
otra_string: str = "Esta no es la lección número 6: Manejo de ficheros"

"""
El [0-9] significa que tiene que ser un número del 0 al 9. Si en la cadena de texto hay un número del 0 al 9, se mostrará en la lista.
"""
pattern: str = r"[0-9]"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")

print(re.search(pattern=pattern, string=string, flags=0), end="\n")

"""
El \d significa que tiene que ser un dígito. Si en la cadena de texto hay un dígito, se mostrará en la lista. Es lo mismo que [0-9].
"""
pattern: str = r"\d"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")

"""
El \D significa que tiene que ser un carácter que no sea un dígito. Si en la cadena de texto hay un carácter que no sea un dígito, se mostrará en la lista.
"""
pattern: str = r"\D"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")

"""
La expresión regular \w significa que tiene que ser un carácter alfanumérico o un guión bajo. Si en la cadena de texto hay un carácter alfanumérico o un guión bajo, se mostrará en la lista.

los caracteres alfanuméricos son las letras del alfabeto (mayúsculas y minúsculas) y los números y el guión bajo.
"""

pattern: str = r"\w"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")

"""
La expresión regular \W significa que tiene que ser un carácter que no sea alfanumérico o un guión bajo. Si en la cadena de texto hay un carácter que no sea alfanumérico o un guión bajo, se mostrará en la lista.

los caracteres alfanuméricos son las letras del alfabeto (mayúsculas y minúsculas) y los números y el guión bajo.
"""

pattern: str = r"\W"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")

"""
La expresión regular \s significa que tiene que ser un espacio en blanco. Si en la cadena de texto hay un espacio en blanco, se mostrará en la lista.

los espacios en blanco son los espacios, los saltos de línea y los tabuladores.
"""

pattern: str = r"\s"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")

"""
La expresión regular \S significa que tiene que ser un carácter que no sea un espacio en blanco. Si en la cadena de texto hay un carácter que no sea un espacio en blanco, se mostrará en la lista.
"""

pattern: str = r"\S"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")

"""
La expresión regular ^ significa que tiene que ser el principio de la cadena de texto. Si en la cadena de texto hay un carácter que esté al principio, se mostrará en la lista.

Si en la cadena de texto hay un carácter que no esté al principio, no se mostrará en la lista.
"""

# Busca el primer carácter de la cadena de texto que sea una E
pattern: str = r"^E"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")


"""
La expresión regular $ significa que tiene que ser el final de la cadena de texto. Si en la cadena de texto hay un carácter que esté al final, se mostrará en la lista.

Si en la cadena de texto hay un carácter que no esté al final, no se mostrará en la lista.
"""

# Busca el último carácter de la cadena de texto que sea una s
pattern: str = r"s$"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")

"""
La expresión regular . significa que tiene que ser cualquier carácter. Si en la cadena de texto hay cualquier carácter, se mostrará en la lista.
"""

pattern: str = r"."
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")

"""
La expresión regular .* significa que tiene que ser cualquier carácter, cero o más veces. Si en la cadena de texto hay cualquier carácter, cero o más veces, se mostrará en la lista.
"""

pattern: str = r".*"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")

"""
La expresión regular .+ significa que tiene que ser cualquier carácter, una o más veces. Si en la cadena de texto hay cualquier carácter, una o más veces, se mostrará en la lista.
"""

pattern: str = r".+"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")

"""
La expresión regular .{1,3} significa que tiene que ser cualquier carácter, de 1 a 3 veces. Si en la cadena de texto hay cualquier carácter, de 1 a 3 veces, se mostrará en la lista.
"""

pattern: str = r".{1,3}"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")

"""
La expresión regular [l].* significa que tiene que ser una l, cero o más veces. Si en la cadena de texto hay una l, cero o más veces, se mostrará en la lista. El punto significa cualquier carácter. El asterisco significa cero o más veces.
"""
pattern: str = r"[l].*"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")

"""
Otra forma sería [l].+ que significa que tiene que ser una l, una o más veces. Si en la cadena de texto hay una l, una o más veces, se mostrará en la lista. El punto significa cualquier carácter. El más significa una o más veces.
"""

pattern: str = r"[l].+"
print(re.findall(pattern=pattern, string=string, flags=0), end="\n")


email: str = "danielperez13@danieldev.com"

"""
Esta expresión regular es para validar un email. Si el email es válido, se mostrará en la lista.

r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"

>>> r significa que es una cadena de texto cruda o raw string.

>>> ^ significa que tiene que ser el principio de la cadena de texto.

>>> [a-zA-Z0-9_.+-] a-z significa que tiene que ser una letra minúscula, A-Z significa que tiene que ser una letra mayúscula, 0-9 significa que tiene que ser un número del 0 al 9, _ significa que tiene que ser un guión bajo, . significa que tiene que ser un punto, + significa que tiene que ser uno o más caracteres, - significa que tiene que ser un guión. Se pone entre corchetes [] para que sea uno de esos caracteres. Si no se pone entre corchetes, tiene que ser exactamente ese carácter.

>>> + significa que tiene que ser uno o más caracteres.

>>> @ significa que tiene que ser un arroba.

>>> [a-zA-Z0-9-] a-z significa que tiene que ser una letra minúscula, A-Z significa que tiene que ser una letra mayúscula, 0-9 significa que tiene que ser un número del 0 al 9, - significa que tiene que ser un guión. Se pone entre corchetes [] para que sea uno de esos caracteres. Si no se pone entre corchetes, tiene que ser exactamente ese carácter.

>>> + significa que tiene que ser uno o más caracteres.

>>> \. significa que tiene que ser un punto. Se pone una barra invertida \ delante del punto para que sea un punto. Si no se pone la barra invertida, significa cualquier carácter.

>>> [a-zA-Z-.] a-z significa que tiene que ser una letra minúscula, A-Z significa que tiene que ser una letra mayúscula, - significa que tiene que ser un guión, . significa que tiene que ser un punto. Se pone entre corchetes [] para que sea uno de esos caracteres. Si no se pone entre corchetes, tiene que ser exactamente ese carácter.

>>> + significa que tiene que ser uno o más caracteres.

>>> $ significa que tiene que ser el final de la cadena de texto.
"""
pattern: str = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern=pattern, string=email, flags=0), end="\n")
print(re.search(pattern=pattern, string=email, flags=0), end="\n")
print(re.findall(pattern=pattern, string=email, flags=0), end="\n")

email: str = "danielperez@danieldev.com.io"
print(re.findall(pattern=pattern, string=email, flags=0), end="\n")
