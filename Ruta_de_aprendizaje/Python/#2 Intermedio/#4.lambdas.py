from typing import List

# Tema: Lambdas en Python

"""
Las funciones lambda son funciones anónimas que se pueden utilizar para realizar operaciones en una sola línea. 
Las funciones lambda se utilizan para realizar operaciones simples y no requieren un nombre para ser utilizadas.
"""


# Funcion normal
def sumarDosValores(primer_valor: int, segundo_valor: int) -> int:
    return primer_valor + segundo_valor


print(
    f"funcion normal sumarDosValores = {sumarDosValores(primer_valor=2, segundo_valor=4)}",
    end="\n",
)


# Funcion normal
def multiplicarValor(primer_valor: int, segundo_valor: int) -> int:
    return primer_valor * segundo_valor


print(
    f"funcion normal multiplicarValor = {multiplicarValor(primer_valor=2, segundo_valor=4)}",
    end="\n",
)


def sumarTresValores(valor) -> int:
    return lambda primer_valor, segundo_valor: primer_valor + segundo_valor + valor


print(
    f"funcion lambda sumarTresValores = {sumarTresValores(valor=3)(primer_valor=2, segundo_valor=4)}",
    end="\n",
)

# Lambda
# * La función lambda se puede asignar a una variable

"""
Suma dos valores y retorna el resultado
>>> Suma dos valores y retorna el resultado
los valores son x e y
estos valores pueden ser de cualquier tipo de dato que se pueda sumar 
"""
sumar: callable = lambda x, y: x + y
print(f"sumar = {sumar(x=2, y=4)}", end="\n")

"""
>>> convertirMayusculas: callable = lambda palabra: palabra.upper()
>>> lo que hace esta función es convertir una palabra a mayúsculas
"""
convertirMayusculas: callable = lambda palabra: palabra.upper()
print(f"convertirMayusculas = {convertirMayusculas(palabra='hola')}", end="\n")

"""
lambda iterable: iterable % 2 == 0, lista_numeros

La función filter() devuelve un iterador que filtra los elementos de una secuencia, para los que la función de filtro devuelve True.

La función filter() toma dos argumentos:
>>> Una función
>>> Una secuencia

Lo que hace internamente la función filter es recorrer la secuencia y aplicar la función a cada elemento.

Si la función devuelve True, el elemento se incluye en la secuencia de salida. Si la función devuelve False, el elemento se excluye de la secuencia de salida.

otra manera de enterderlo seria:

lista_numeros: List[int] = [1, 2, 3, 4, 5, 6]
lista_filtrada: List[int] = []
for iterable in lista_numeros:
    if iterable % 2 == 0:
        print(iterable,end="\n")
        lista_filtrada.append(iterable)
        # osea que es True
"""
lista_numeros: List[int] = [1, 2, 3, 4, 5, 6]
filtar_lista: filter = filter(lambda iterable: iterable % 2 == 0, lista_numeros)
print(f"filtar_lista = {list(filtar_lista)}", end="\n")


"""
map es una función que toma dos argumentos:
>>> Una función
>>> Una secuencia

La función map() aplica una función a todos los elementos de una secuencia dada.
>>> la diferencia entre map y filter es que map retorna un iterador con los resultados de aplicar la función a cada elemento de la secuencia. y filter retorna un iterador con los elementos de la secuencia que cumplen una condición.

otra manera de entenderlo seria:
lista_numeros: List[int] = [1, 2, 3, 4, 5]
lista_mapeada: List[int] = []
for iterable in lista_numeros:
    print(iterable**2,end="\n")
    lista_mapeada.append(iterable**2)
    # osea que es True
"""
lista_numeros: List[int] = [1, 2, 3, 4, 5]
lista_mapeada: map = map(lambda x: x**2, lista_numeros)
print(f"lista_mapeada = {list(lista_mapeada)}", end="\n")
