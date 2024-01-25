def decorador(funcion: callable) -> callable:
    def funcion_modificada() -> None:
        print("Antes de ejecutar la funcion")
        funcion()
        print("Despues de ejecutar la funcion")

    return funcion_modificada


def saludo() -> None:
    print("Hola Daniel")


saludo_modificado: callable = decorador(funcion=saludo)
saludo_modificado()

# Manera mas facil de entender los decoradores pero no es la mas optima
