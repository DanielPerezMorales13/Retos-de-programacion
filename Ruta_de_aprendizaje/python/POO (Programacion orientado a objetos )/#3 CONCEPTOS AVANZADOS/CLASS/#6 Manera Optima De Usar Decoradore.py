# Este tipo de decorador se le conoce como decorador de funcion
def decorador(funcion: callable) -> callable:
    def funcion_modificada() -> None:
        print("Antes de ejecutar la funcion")
        funcion()
        print("Despues de ejecutar la funcion")

    return funcion_modificada


@decorador
def saludo() -> None:
    print("Hola Daniel")


# Mofiicamos la funcion saludo con el decorador
saludo()

# Manera mas optima de usar los decoradores
