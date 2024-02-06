from typing import Union

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router: APIRouter = APIRouter(tags=["users"])

# Iniciar el servidor de desarrollo de FastAPI
# uvicorn users:router --reload --port 8000 --host 127.0.0.1
# uvicorn nombre_fichero:nombre_instancia_de_FastAPI --reload --port numero_puerto --host numero_host

# Detener el servidor de desarrollo de FastAPI
# Ctrl + C


# Entidad de usuario
class Users(BaseModel):
    """
    Pydantic genera automáticamente un método __init__ que toma estos cuatro argumentos y los utiliza para inicializar los atributos del objeto.
    """

    identificador: int
    name: str
    segundo_name: str
    web: str
    age: int


users_list: list[Users] = [
    Users(
        identificador=1,
        name="Daniel",
        segundo_name="Benjamin",
        web="https://www.Daniel.dev",
        age=18,
    ),
    Users(
        identificador=2,
        name="Danna",
        segundo_name="Isabella",
        web="https://www.Danna.com",
        age=18,
    ),
    Users(
        identificador=3,
        name="Nuria",
        segundo_name="Raquel",
        web="https://www.Raquel.com",
        age=40,
    ),
]


@router.get(path="/usersjson")
async def usersJson() -> list[dict[str, int | str]]:
    # creamos json manualmente
    return [
        {
            "identificador": 1,
            "name": "Daniel",
            "segundo_name": "Benjamin",
            "web": "https://www.Daniel.com",
            "age": 18,
        },
        {
            "identificador": 2,
            "name": "Danna",
            "segundo_name": "Perez",
            "web": "https://www.Danna.com",
            "age": 18,
        },
        {
            "identificador": 3,
            "name": "Carol",
            "segundo_name": "Morales",
            "web": "https://www.Carol.com",
            "age": 18,
        },
    ]


@router.get(path="/")
async def root() -> str:
    return "hola FastAPI"


@router.get(path="/users")
async def users() -> list[Users]:
    return users_list


"""
Podemos usar el tipo de dato Union para indicar que el tipo de dato que retornara

Union[Users, dict] -> Union[Users, dict[str, str]] -> Union[Users, dict[str, int | str]]
"""

"""
Podemos pasar parametros a la ruta de la siguiente manera
"""


# Query params
@router.get(path="/user/{identificador}")
async def user(identificador: int) -> Union[Users, dict[str, str | int]]:
    user_variable: filter = filter(
        lambda user: user.identificador == identificador, users_list
    )
    try:
        return list(user_variable)[0]
    except IndexError:
        return dict(error="IndexError")


# https://survey.stackoverflow.co/2023/#most-popular-technologies-language
"""
los path son la ruta de la url 
y la query son los parametros que se pasan por la url
"""

"""

Hacer esto se le conoce como query params que en español seria parametros de consulta que se pasan por la url

El ? es para indicar que es un parametro de consulta y el & es para indicar que es otro parametro de consulta

identificador=1 -> es el parametro de consulta

1 es el valor del parametro de consulta

http://127.0.0.1:8000/userquery/?identificador=1 

FastAPI automaticamente convierte el tipo de dato de la query a int
Por eso es importante que el tipo de dato de la query sea el mismo que el tipo de dato del parametro de la ruta

http://127.0.0.1:8000/userquery/?identificador="1" esto no funcionaria porque el tipo de dato de la query es str y el tipo de dato del parametro de la ruta es int

{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "query",
        "identificador"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "\"1\"",
      "url": "https://errors.pydantic.dev/2.5/v/int_parsing"
    }
  ]
}

Esto nos retornaria al hacer la petición
"""


@router.get(path="/user/")
async def user(identificador: int) -> Union[Users, dict[str, str | int]]:
    return buscar_usuario(identificador_int=identificador)


# alas rutas tambien se les llama endpoints o puntos finales
"""
Al hacer una peticion post debemos darle un cuerpo a la peticion que se le conoce como body en formato json
formato json es un formato de intercambio de datos que es muy utilizado en la web para enviar y recibir datos de un servidor a un cliente y viceversa. La estructura de un json es muy similar a la de un diccionario de python

body que se le enviara a la peticion post en formato json, Esto tenemos que ponerlo en el body de la peticion post en formato json. En thunder client o postman o cualquier cliente http que usemos para hacer peticiones http
{
    "identificador": 4,
    "name": "NuevoNombre",
    "segundo_name": "NuevoApellido",
    "web": "https://www.nuevoweb.com",
    "age": 30
}
"""


# El status_code es para indicar el codigo de estado de la peticion post que se le enviara al cliente que hizo la peticion post en este caso el status_code es 201 que significa que la peticion post fue exitosa y se creo un recurso nuevo en el servidor
@router.post(path="/user/", response_model=Users, status_code=201)
async def user(usuario: Users) -> Users | HTTPException:
    if type(buscar_usuario(usuario.identificador)) == Users:
        raise HTTPException(
            status_code=404,
            detail="El usuario ya existe",
            headers={"X-Error": "Hay un error"},
        )
    users_list.append(usuario)
    return usuario


@router.put(path="/user/")
# La peticion put es para actualizar un recurso
async def user(usuario: Users) -> dict[str, str] | list[Users]:
    buscar: bool = False
    for indice, actualizar_datos in enumerate(users_list):
        if actualizar_datos.identificador == usuario.identificador:
            users_list[indice]: Users = usuario
            buscar: bool = True
    else:
        # Si buscar es igual a False
        if buscar == False:
            return dict(error="No se actualizado el usuario")
        else:
            return users_list


@router.delete(path="/user/{identificador}")
# Lo recomendable es el parametro de la ruta sea el identificador del usuario. No el usuario completo
async def user(identificador: int) -> dict[str, str]:
    buscar: bool = False
    for indice, actualizar_datos in enumerate(users_list):
        if actualizar_datos.identificador == identificador:
            del users_list[indice]
            buscar: bool = True
    if buscar:
        return dict(mensaje="Usuario eliminado correctamente")
    else:
        return dict(error="No se encontro el usuario")


def buscar_usuario(identificador_int: int) -> Union[Users, dict[str, str]]:
    user_variable: filter = filter(
        lambda Users: Users.identificador == identificador_int, users_list
    )
    try:
        return list(user_variable)[0]
    except IndexError:
        return dict(error="IndexError No se encontro el usuario")


"""
CRUD -> Create, Read, Update, Delete
>>> Create -> Crear
>>> Read -> Leer o consultar
>>> Update -> Actualizar o modificar
>>> Delete -> Borrar o eliminar 
"""

"""
>>> Las query se utilizan para filtrar los datos que se retornan en la peticion get ejemplo seria retornar los usuarios que tengan una edad mayor a 18 años

>>> las rutas se utilizan para obtener un recurso en especifico ejemplo seria obtener un usuario en especifico por su identificador
"""
