# import asyncio

# * Estas funciones sera implementadas en el modulo de prueba.py


async def filtrarPorNombre(
    usuario: str, listaClientes: dict[str, str | int]
) -> dict[str, str | int]:
    """
    Funcion que recibe un paremtro usuario que es de tipo str y lo filtra por nombre y lo retorna
    """
    # ! gestionar el error si el nombre no existe
    diccionario_filtrado: dict[str, str | int] = dict()

    for nombre in listaClientes.keys():
        if listaClientes[nombre].nombre.capitalize() == usuario.capitalize():
            diccionario_filtrado[nombre] = listaClientes[nombre]
        else:
            continue
    else:
        return (
            diccionario_filtrado
            if len(diccionario_filtrado) > 0
            else dict(mensaje="No se encontro el usuario")
        )


if __name__ == "__main__":
    """listaClientes: dict = {
        "1": {
            "identificador": 1,
            "nombre": "daniel",
            "email": "daniel@.com",
            "telefono": 12345678,
        },
        "2": {
            "identificador": 2,
            "nombre": "danna",
            "email": "danna@.com",
            "telefono": 12345678,
        },
        "3": {
            "identificador": 3,
            "nombre": "dannA",
            "email": "danna@.com",
            "telefono": 12345678,
        },
        "4": {
            "identificador": 4,
            "nombre": "Danna",
            "email": "danna@.com",
            "telefono": 12345678,
        },
        "5": {
            "identificador": 5,
            "nombre": "Daniel",
            "email": "daniel@.com",
            "telefono": 12345678,
        },
    }

    print(asyncio.run(filtrarPorNombre(usuario="daniel", listaClientes=listaClientes)))
    """
    pass
