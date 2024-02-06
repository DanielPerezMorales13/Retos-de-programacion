# import asyncio


async def filtrarPorIdentificadorMayor(
    identificador: int, listaClientes: dict[str, dict[str | int]]
) -> dict[str, dict[str | int]]:
    """
    Funcion que recibe un paremetro identificador que es de tipo int y lo filtra por identificadores mayores e iguales a el  y lo retorna
    """
    # ! gestionar el error si el identificador no existe

    diccionario_filtrado: dict[str, dict[str | int]] = dict()
    for identificador_clave in listaClientes.keys():
        if int(identificador_clave) >= identificador:
            diccionario_filtrado[identificador_clave] = listaClientes[
                identificador_clave
            ]
        else:
            continue
    else:
        return (
            diccionario_filtrado
            if len(diccionario_filtrado) > 0
            else dict(
                mensaje="No se encontraron identificadores mayores o iguales a el"
            )
        )


async def filtrarPorIdentificadorMenor(
    identificador: int, listaClientes: dict[str, dict[str | int]]
) -> dict[str, dict[str | int]]:
    """
    Funcion que recibe un paremetro identificador que es de tipo int y lo filtra por identificadores menores e iguales a el  y lo retorna
    """
    # ! gestionar el error si el identificador no existe

    diccionario_filtrado: dict[str, dict[str | int]] = dict()
    for identificador_clave in listaClientes.keys():
        if int(identificador_clave) <= identificador:
            diccionario_filtrado[identificador_clave] = listaClientes[
                identificador_clave
            ]
        else:
            continue
    else:
        return (
            diccionario_filtrado
            if len(diccionario_filtrado) > 0
            else dict(
                mensaje="No se encontraron identificadores menores o iguales a el"
            )
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
    print(
        asyncio.run(
            filtrarPorIdentificadorMayor(identificador=3, listaClientes=listaClientes)
        )
    )"""
    pass
