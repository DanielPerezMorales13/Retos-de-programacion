# import asyncio

from fastapi import HTTPException

# * Estas funciones sera implementadas en el modulo de prueba.py


async def filtrarPorLetra(
    letra: str, listaClientes: dict[str, str | int]
) -> dict[str, str | int] | HTTPException:
    """
    Funcion que recibe un paremtro letra que es de tipo str y lo filtra por nombre y lo retorna
    """
    # ! gestionar el error si el nombre no existe
    if len(letra) > 1 or len(letra) == 0:
        raise HTTPException(
            status_code=400,
            detail="Debe ingresar solo una letra y no mas",
            headers={"X-Error": "Error de entrada de datos"},
        )
    elif letra.isnumeric() == True:
        raise HTTPException(
            status_code=400,
            detail="Debe ingresar una letra y no un numero",
            headers={"X-Error": "Error de entrada de datos"},
        )
    diccionario_filtrado: dict[str, str | int] = dict()

    for nombre in listaClientes.keys():
        if listaClientes[nombre].nombre.lower()[0] == letra[0].lower():
            diccionario_filtrado[nombre] = listaClientes[nombre]
        else:
            continue
    else:
        return (
            diccionario_filtrado
            if len(diccionario_filtrado) > 0
            else dict(
                mensaje="No se encontraros nombres que empiecen con letra %s" % letra
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
            "nombre": "dani",
            "email": "danna@.com",
            "telefono": 12345678,
        },
        "4": {
            "identificador": 4,
            "nombre": "dora",
            "email": "danna@.com",
            "telefono": 12345678,
        },
        "5": {
            "identificador": 5,
            "nombre": "donald",
            "email": "daniel@.com",
            "telefono": 12345678,
        },
    }

    print(asyncio.run(filtrarPorLetra(letra="D", listaClientes=listaClientes)))
    """
    pass
