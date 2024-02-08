from typing import Union

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router: APIRouter = APIRouter(
    prefix="/userdb",
    tags=["userdb"],
    responses={
        404: {"description": "Not found"},
    },
)


# Entidad de usuario
class Users(BaseModel):

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


@router.get(path="/")
async def root() -> str:
    return "hola FastAPI"


@router.get(path="/")
async def users() -> list[Users]:
    return users_list


# Query params
@router.get(path="/{identificador}")
async def user(identificador: int) -> Union[Users, dict[str, str | int]]:
    user_variable: filter = filter(
        lambda user: user.identificador == identificador, users_list
    )
    try:
        return list(user_variable)[0]
    except IndexError:
        return dict(error="IndexError")


@router.get(path="/")
async def user(identificador: int) -> Union[Users, dict[str, str | int]]:
    return buscar_usuario(identificador_int=identificador)


@router.post(path="/", response_model=Users, status_code=201)
async def user(usuario: Users) -> Users | HTTPException:
    if type(buscar_usuario(usuario.identificador)) == Users:
        raise HTTPException(
            status_code=404,
            detail="El usuario ya existe",
            headers={"X-Error": "Hay un error"},
        )
    users_list.append(usuario)
    return usuario


@router.put(path="/")
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


@router.delete(path="/{identificador}")
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
