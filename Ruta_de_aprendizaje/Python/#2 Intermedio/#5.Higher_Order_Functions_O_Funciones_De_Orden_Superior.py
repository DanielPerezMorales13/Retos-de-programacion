from functools import reduce

# Tema: Higher Order Functions o Funciones de Orden Superior

"""
Funciones de orden superior son funciones que toman otras funciones como argumentos o devuelven otras funciones como resultado.
Las funciones de orden superior son una característica importante de los lenguajes de programación funcional.
"""


def sumarUno(valor: int) -> int:
    return valor + 1


def sumarCinco(valor: int) -> int:
    return valor + 5


def sumarDosValoresAñadirValor(
    primer_valor: int, segundo_valor: int, funcionSuma: callable
) -> int:
    return funcionSuma(primer_valor + segundo_valor)


print(
    sumarDosValoresAñadirValor(primer_valor=5, segundo_valor=2, funcionSuma=sumarUno),
    end="\n",
)
print(
    sumarDosValoresAñadirValor(primer_valor=5, segundo_valor=2, funcionSuma=sumarCinco),
    end="\n",
)


def sumarDiez(valor_original: int) -> callable:
    def add(valor: int) -> int:
        return valor + 10 + valor_original

    return add


añadirFuncion: callable = sumarDiez(valor_original=10)
print(añadirFuncion(5), end="\n")
print((sumarDiez(valor_original=5))(valor=1), end="\n")

# Built-in Higher Order Functions o Funciones de Orden Superior Integradas

lista_numeros: list[int] = [2, 5, 10, 21, 3, 30]

# Map
"""
map() es una función que toma dos argumentos:
>>> Una función
>>> Una secuencia
La función map() toma una función y una secuencia y devuelve un iterador que produce los resultados de aplicar la función a cada elemento de la secuencia.
"""


def multiplicarDos(numero: int) -> int:
    return numero * 2


print(list(map(multiplicarDos, lista_numeros)), end="\n")
print(list(map(lambda numero: numero * 2, lista_numeros)), end="\n")

# Filter
"""
filter() es una función que toma dos argumentos:
>>> Una función
>>> Una secuencia
La función filter() toma una función y una secuencia y devuelve un iterador que produce todos los elementos de la secuencia para los que la función devuelve True.
"""


def filtrarMayorQueDiez(numero: int):
    if numero > 10:
        return True
    return False


print(list(filter(filtrarMayorQueDiez, lista_numeros)), end="\n")
print(list(filter(lambda numero: numero > 10, lista_numeros)), end="\n")


"""
reduce() es una función que toma dos argumentos:
>>> Una función
>>> Una secuencia
La función reduce() toma una función y una secuencia y devuelve un solo valor calculado a partir de la secuencia.
La función reduce() se encuentra en el módulo functools.
"""
# Reduce


def sumarDosValores(primer_valor: int, segundo_valor: int) -> int:
    return primer_valor + segundo_valor


print(reduce(sumarDosValores, lista_numeros), end="\n")

print(sum(lista_numeros, start=0), end="\n")
