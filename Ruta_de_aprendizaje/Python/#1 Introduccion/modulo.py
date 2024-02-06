# Tema: Mis propios modulos
# Módulo para pruebas


def sumarValores(
    numeroUno: str | int | float,
    numeroDos: str | int | float,
    numeroTres: str | int | float,
) -> None:
    print(numeroUno + numeroDos + numeroTres, end="\n")


def imprimirValor(valor: str | int | float | bool | list | tuple | dict | set) -> None:
    print(valor, end="\n")
