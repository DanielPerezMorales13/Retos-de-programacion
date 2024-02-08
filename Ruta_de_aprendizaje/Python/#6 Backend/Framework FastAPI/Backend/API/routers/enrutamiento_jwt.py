from abc import ABC
from datetime import datetime, timedelta

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.datastructures import Default
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.utils import generate_unique_id
from jose import constants, jwt
from libraries import (
    filtracion_por_identificador,
    filtracion_por_letra,
    filtracion_por_nombre,
)
from passlib.context import CryptContext
from pydantic import BaseModel

# ! https://jwt.io/
# pip3 install python-jose[cryptography]

# pip3 install passlib[bcrypt]

"""
{
  "identificador": 1,
  "nombre": "daniel",
  "email": "daniel@yahoo.com",
  "telefono": 88042474,
  "activo": true,
  "contraseña": "12345678"
}
"""

oauth2: OAuth2PasswordBearer = OAuth2PasswordBearer(
    tokenUrl="login",
    auto_error=True,
    description="Ingresar credenciales",
    scopes=None,
    scheme_name="Bearer",
)


class ClienteIdentficador(ABC):
    identificador: int


class Cliente(BaseModel, ClienteIdentficador):
    nombre: str
    email: str
    telefono: int
    activo: bool
    contraseña: str


"""
En informática, "kebab case" es un estilo de nomenclatura en el que las palabras se unen con guiones. Es similar al estilo "snake case", pero en lugar de usar guiones bajos, se utilizan guiones.

El estilo "kebab case" se utiliza a menudo para nombrar variables, funciones y métodos en lenguajes de programación. También se utiliza para nombrar archivos y directorios.
"""

CLAVE_SECRETA: str = "da460600cb4df0a1547d98fa9f4e37de97610ef68bfb13f754a417d6428dec47"
DURACION_TOKEN_ACCESO: int = 1
BEARER: str = "Bearer"
WWW_AUTENTICATE: str = "WWW-Autenticate"


oauth2 = OAuth2PasswordBearer(
    tokenUrl="login",
    auto_error=True,
    description="Ingresar credenciales",
    scopes=None,
    scheme_name="Bearer",
)


ALGORITMO: str = constants.ALGORITHMS.HS256

"""
La variable crypt es un objeto de la clase CryptContext que nos permite encriptar y desencriptar contraseñas.

>>> `schemes=["bcrypt"]`: Esto especifica que quieres usar el esquema de hashing `bcrypt`. `bcrypt` es un método de hashing de contraseñas que es considerado seguro y eficaz.

>>> `deprecated="auto"`: Esto especifica que quieres que FastAPI te avise si el esquema de hashing que estás utilizando se vuelve obsoleto. Si el esquema de hashing se vuelve obsoleto, es posible que sea menos seguro y que se recomiende cambiar a un esquema más seguro.

"""
crypt: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")
"""
jwt significa JSON Web Token. Es un estándar abierto que define una forma segura y compacta para transmitir información entre partes como un objeto JSON. Esta información puede ser verificada y confiable porque está firmada digitalmente. Los JWT se pueden firmar utilizando un algoritmo (por ejemplo, HMAC con SHA-256 o RSA) y, por lo tanto, se pueden verificar la procedencia de los datos.
"""

"""
JSON x
{
  "identificador": 1,
  "nombre": "daniel",
  "email": "daniel@yahoo.com",
  "telefono": 88042474,
  "activo": true,
  "contraseña": "12345678"
}
"""
app: FastAPI = FastAPI(
    callbacks=None,
    title="Api de clientes",
    version="0.1.0",
    openapi_url="/openapi.json",
    contact=None,
    debug=False,
    default_response_class=Default(JSONResponse),
    dependencies=None,
    docs_url="/docs",
    redoc_url="/redoc",
    terms_of_service=None,
    openapi_tags=None,
    description="FastAPI",
    deprecated=None,
    webhooks=None,
    exception_handlers=None,
    extra=None,
    generate_unique_id_function=Default(generate_unique_id),
    include_in_schema=True,
    license_info=None,
    lifespan=None,
    middleware=None,
    swagger_ui_parameters=None,
    on_shutdown=None,
    on_startup=None,
    openapi_prefix="",
    redirect_slashes=True,
    responses=None,
    root_path="",
    root_path_in_servers=True,
    routes=None,
    separate_input_output_schemas=True,
    servers=None,
    summary=None,
    swagger_ui_init_oauth=None,
    swagger_ui_oauth2_redirect_url="/docs/oauth2-redirect",
)


lista_clientes: dict[str, dict] = dict()
# 123456
# 654321


@app.get(
    path="/",
    tags=["Inicio"],
    status_code=status.HTTP_200_OK,
    response_model=dict[str, str],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Pagina de inicio",
    summary="Inicio",
    response_description="Pagina de inicio",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Inicio",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def root():
    return dict(mensaje="Pagina de inicio")


class ClienteIdentficador(ABC):
    identificador: int


class ClienteNombre(
    BaseModel,
    ClienteIdentficador,
):
    nombre: str


class ClienteEmail(
    BaseModel,
    ClienteIdentficador,
):
    email: str


class ClienteTelefono(
    BaseModel,
    ClienteIdentficador,
):
    telefono: int


class Cliente(BaseModel, ClienteIdentficador):
    nombre: str
    email: str
    telefono: int
    activo: bool
    contraseña: str


# Cambiar contraseña
class ClienteContraseña(
    BaseModel,
    ClienteIdentficador,
):
    contraseña: str


"""
La clase `OAuth2PasswordRequestForm` en FastAPI es una clase de ayuda que se utiliza para manejar formularios de autenticación en el flujo de contraseña de OAuth2. Tiene los siguientes campos:

1. `username`: Este es el nombre de usuario para la autenticación. Es un campo obligatorio.

2. `password`: Este es el campo de la contraseña para la autenticación. También es un campo obligatorio.

3. `scope`: Este es un campo opcional que puede contener una lista de espacios de nombres de alcance. Los alcances son cadenas que indican qué permisos tiene un token de acceso.

4. `grant_type`: Este campo siempre es `"password"` para `OAuth2PasswordRequestForm`. Indica que se está utilizando el flujo de contraseña de OAuth2, que implica que el cliente (la aplicación) está haciendo una solicitud de token de acceso proporcionando las credenciales del usuario (nombre de usuario y contraseña).

5. `client_id`: Este es un campo opcional que puede contener el ID del cliente. En el contexto de OAuth2, el cliente es la aplicación que está haciendo la solicitud de token de acceso.

6. `client_secret`: Este es un campo opcional que puede contener el secreto del cliente. El secreto del cliente es una especie de contraseña que la aplicación (cliente) utiliza para autenticarse ante el servidor de autorización.
"""

"""
El objeto OAuth2PasswordRequestForm es una clase especial en FastAPI que se utiliza para manejar formularios de autenticación. Esta clase tiene tres atributos: username, password y scope.

Si necesitamos un campo email en tu formulario, tendrás que crear una clase personalizada que herede de OAuth2PasswordRequestForm y añadir el campo email a esa clase. 
"""


"""
En Python, `...` es conocido como el operador "Ellipsis". Es un objeto incorporado y es una instancia de la clase `Ellipsis`. En la mayoría de los contextos, no tiene un uso práctico directo, pero puede ser utilizado como un marcador de posición cuando se está escribiendo código.

Aquí tienes un ejemplo de su uso en la definición de una función:

```python
def my_function():
    ...
```

En este caso, `...` se utiliza como un marcador de posición para indicar que la implementación de la función aún no está completa.
"""


"""
En Python, el asterisco (`*`) tiene varios usos dependiendo del contexto. Aquí te dejo algunos ejemplos:

1. **Desempaquetado de listas o tuplas**: Cuando se coloca delante de una lista o una tupla, el asterisco desempaqueta sus elementos.

```python
numbers = [1, 2, 3, 4, 5]
print(*numbers)  # Esto imprimirá: 1 2 3 4 5
```

2. **Recogida de argumentos posicionales en funciones**: En la definición de una función, un parámetro con un asterisco recoge todos los argumentos posicionales que no han sido capturados por otros parámetros.

```python
def func(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

func(1, 2, 3, 4, 5)  # Esto imprimirá: 1, 2, (3, 4, 5)
```

3. **Forzar argumentos de palabras clave**: Si se coloca un asterisco solo en la definición de una función, todos los argumentos que siguen deben ser especificados como argumentos de palabras clave.

```python
def func(*, arg1, arg2):
    print(arg1)
    print(arg2)

func(arg1="hello", arg2="world")  # Esto es correcto
func("hello", "world")  # Esto dará un error
```

Estos son solo algunos ejemplos de cómo se puede utilizar el asterisco (`*`) en Python.
"""


async def buscarContraseñaUsuario(
    identificador: str,
    usuario: str,
) -> str:
    for identificador_cliente in lista_clientes.keys():
        if (
            identificador_cliente == str(identificador)
            and lista_clientes[identificador_cliente].nombre == usuario
        ):
            return lista_clientes[identificador_cliente].contraseña
        else:
            continue
    else:
        return "Contraseña incorrecta"


async def usuarioActual(
    token: str | None = Depends(
        dependency=oauth2,
        use_cache=True,
    )
) -> dict[str, str | int | bool] | HTTPException:
    # return dict(mensaje=token)
    """
    Error
    {
        "mensaje": "'1'"
    }
    """
    identificador: str | None = await buscarUsuario(id_usuario=token)
    if identificador == dict(mensaje="Identificador de cliente no encontrado"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Identificador de cliente no encontrado {token}",
            headers=dict(WWW_AUTENTICATE=BEARER),
        )
    if lista_clientes[token].activo == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario inactivo",
            headers=dict(WWW_AUTENTICATE=BEARER),
        )

    # Recordar lo que los valores booleanos en opson True y False
    # Recordar lo que los valores booleanos en python son True y False pero en JSON son true y false por lo que no es necesario convertirlo a str para que sea serializable en JSON .y se pueden representar como 1 y 0
    return lista_clientes[token]


"""
async def me(user: User = Depends(dependency=usuario_actual)) -> User:
    return user
"""
# * En Python, las claves de los diccionarios son siempre de tipo str cuando se convierten a JSON. Esto se debe a que JSON, que es el formato de intercambio de datos que se utiliza en las API REST, solo permite claves de tipo str.


"""
{
    "1": {
        "identificador": 1,
        "nombre": "Daniel Perez",
        "email": "danielbperez13@gmial.com",
        "telefono": 12345678,
        "activo": True,
        "contraseña": "12345678"
    }
}
"""
"""
{
    "1": {
        "identificador": 1,
        "nombre": "benjamin",
        "email": "benjamin@yahoo.com",
        "telefono": 12345678,
        "activo": True,
        "contraseña": "12345678",
    },
    "2": {
        "identificador": 2,
        "nombre": "daniel",
        "email": "daniel@yahoo.com",
        "telefono": 12345678,
        "activo": True,
        "contraseña": "12345678",
    },
    "3": {
        "identificador": 3,
        "nombre": "DaNna",
        "email": "danna@yahoo.com",
        "telefono": 12345678,
        "activo": True,
        "contraseña": "12345678",
    },
    "4": {
        "identificador": 4,
        "nombre": "Matias",
        "email": "matias@yahoo.com",
        "telefono": 12345678,
        "activo": False,
        "contraseña": "12345678",
    },
    "5": {
        "identificador": 5,
        "nombre": "maRIO",
        "email": "maRIO@yahoo.com",
        "telefono": 12345678,
        "activo": False,
        "contraseña": "12345678",
    },
    "6": {
        "identificador": 6,
        "nombre": "BoaNerje",
        "email": "boanerje@yahoo.com",
        "telefono": 12345678,
        "activo": False,
        "contraseña": "12345678",
    },
    "7": {
        "identificador": 7,
        "nombre": "Coby",
        "email": "Matias@gmail.com",
        "telefono": 12345678,
        "activo": False,
        "contraseña": "12345678",
    },
}
"""


@app.get(
    path="/cliente/identificadores_mayor/{identificador}",
    status_code=status.HTTP_200_OK,
    response_model=dict,
    tags=["Clientes mayores"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Buscar clientes con identificadores mayores a un numero",
    summary="Clientes mayores de un identificador",
    response_description="Clientes mayores de un identificador",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Clientes mayores de un identificador",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def clientes(identificador: int) -> dict | dict[str, str]:
    return await filtracion_por_identificador.filtrarPorIdentificadorMayor(
        identificador=identificador, listaClientes=lista_clientes
    )


# Query parameters
@app.get(
    path="/cliente/identificadores_mayor/",
    status_code=status.HTTP_200_OK,
    response_model=dict,
    tags=["Clientes mayores query parameters"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Buscar clientes con identificadores mayores a un numero en query parameters",
    summary="Clientes mayores de un identificador query parameters",
    response_description="Clientes mayores de un identificador query parameters",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Clientes mayores de un identificador query parameters",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def clientes(identificador: int) -> dict | dict[str, str]:
    return await filtracion_por_identificador.filtrarPorIdentificadorMayor(
        identificador=identificador, listaClientes=lista_clientes
    )


@app.get(
    path="/cliente/identificadores_menores/{identificador}",
    status_code=status.HTTP_200_OK,
    response_model=dict,
    tags=["Clientes menores"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Buscar clientes con identificadores menores a un numero",
    summary="Clientes menores de un identificador",
    response_description="Clientes menores de un identificador",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Clientes menores de un identificador",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def clientes(identificador: int) -> dict | dict[str, str]:
    return await filtracion_por_identificador.filtrarPorIdentificadorMenor(
        identificador=identificador, listaClientes=lista_clientes
    )


# Query parameters
@app.get(
    path="/cliente/identificadores_menores/",
    status_code=status.HTTP_200_OK,
    response_model=dict,
    tags=["Clientes menores query parameters"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Buscar clientes con identificadores menores a un numero en query parameters",
    summary="Clientes menores de un identificador query parameters",
    response_description="Clientes menores de un identificador query parameters",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Clientes menores de un identificador query parameters",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def clientes(identificador: int) -> dict | dict[str, str]:
    return await filtracion_por_identificador.filtrarPorIdentificadorMenor(
        identificador=identificador, listaClientes=lista_clientes
    )


@app.get(
    path="/cliente/buscar_nombres/{usuario}",
    status_code=status.HTTP_200_OK,
    response_model=dict,
    tags=["Buscar clientes por nombre"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Buscar clientes por nombre de usuario en path parameters",
    summary="Clientes por nombre de usuario en path parameters",
    response_description="Clientes por nombre de usuario en path parameters",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Clientes por nombre de usuario en path parameters",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def clientes(usuario: str) -> dict | dict[str, str]:
    return await filtracion_por_nombre.filtrarPorNombre(
        usuario=usuario, listaClientes=lista_clientes
    )


# Query parameters
@app.get(
    path="/cliente/buscar_nombres/",
    status_code=status.HTTP_200_OK,
    response_model=dict,
    tags=["Buscar clientes por nombre"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Buscar clientes por nombre de usuario en query parameters",
    summary="Clientes por nombre de usuario en query parameters",
    response_description="Clientes por nombre de usuario en query parameters",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Clientes por nombre de usuario en query parameters",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def clientes(usuario: str) -> dict | dict[str, str]:
    return await filtracion_por_nombre.filtrarPorNombre(
        usuario=usuario, listaClientes=lista_clientes
    )


@app.get(
    path="/cliente/buscar_nombres_por_letra/{letra}",
    status_code=status.HTTP_200_OK,
    response_model=dict,
    tags=["Buscar clientes por nombre por letra en path parameters"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Buscar clientes por nombre de usuario por letra en path parameters",
    summary="Clientes por nombre de usuario por letra en path parameters",
    response_description="Clientes por nombre de usuario por letra en path parameters",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Clientes por nombre de usuario por letra en path parameters",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def clientes(letra: str) -> dict | dict[str, str] | HTTPException:
    return await filtracion_por_letra.filtrarPorLetra(
        letra=letra, listaClientes=lista_clientes
    )


# Query parameters
@app.get(
    path="/cliente/buscar_nombres_por_letra/",
    status_code=status.HTTP_200_OK,
    response_model=dict,
    tags=["Buscar clientes por nombre por letra en query parameters"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Buscar clientes por nombre de usuario por letra en query parameters",
    summary="Clientes por nombre de usuario por letra en query parameters",
    response_description="Clientes por nombre de usuario por letra en query parameters",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Clientes por nombre de usuario por letra en query parameters",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def clientes(letra: str) -> dict | dict[str, str] | HTTPException:
    return await filtracion_por_letra.filtrarPorLetra(
        letra=letra, listaClientes=lista_clientes
    )


# El parametro response_model es para indicar que tipo de dato va a devolver
@app.get(
    path="/total_clientes/",
    status_code=status.HTTP_200_OK,
    response_model=dict,
    tags=["Total de clientes en el sistema"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Total de clientes en el sistema registrados",
    summary="Total de clientes en el sistema registrados",
    response_description="Total de clientes en el sistema registrados",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Total de clientes en el sistema registrados",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def clientes() -> dict:
    return (
        lista_clientes if len(lista_clientes) > 0 else dict(mensaje="No hay clientes")
    )


# Los métodos y funciones no son serializables en JSON.

# Para solucionar este problema, necesitas asegurarte de que todos los datos que estás intentando devolver desde tu endpoint sean serializables en JSON. Esto generalmente significa que deben ser instancias de tipos de datos simples como dict, list, str, int, float, bool, None, o instancias de clases que hereden de pydantic.BaseModel.


@app.get(
    path="/cliente/{identificador}/",
    status_code=status.HTTP_200_OK,
    response_model=Cliente | dict[str, str | int],
    tags=["Clientes por identificador en path parameters"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Clientes por identificador en path parameters",
    summary="Clientes por identificador en path parameters",
    response_description="Clientes por identificador en path parameters",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Clientes por identificador en path parameters",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def clientes(identificador: int) -> Cliente | dict[str, str | int]:
    # retorna "<class 'prueba.Cliente'>" o "<class 'dict'>"
    return await buscarUsuario(id_usuario=identificador)
    """
    >>> intentar ejecutar una tarea asíncrona desde dentro de un bucle de eventos ya en ejecución. En FastAPI, cada ruta se ejecuta dentro de un bucle de eventos, por lo que no puedes usar asyncio.run() dentro de una ruta.

    >>> En lugar de usar asyncio.run(), puedes simplemente await la coroutine directamente.
    
    >>> Coroutine es un tipo especial que representa una función asíncrona o una coroutine.
    """


async def buscarUsuario(id_usuario: int | str) -> dict[str, str | int] | Cliente:
    if str(id_usuario) not in lista_clientes:
        return dict(mensaje="Identificador de cliente no encontrado")
    return lista_clientes.get(str(id_usuario))


# Query parameters
@app.get(
    path="/cliente/",
    status_code=status.HTTP_200_OK,
    response_model=Cliente | dict[str, str | int],
    tags=["Clientes por identificador en query parameters"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Clientes por identificador en query parameters",
    summary="Clientes por identificador en query parameters",
    response_description=" Clientes por identificador en query parameters",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Clientes por identificador en query parameters",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def clientes(
    identificador: int,
) -> Cliente | dict[str, str | int]:
    return await buscarUsuario(id_usuario=identificador)
    """
    >>> Coroutine es un tipo especial que representa una función asíncrona o una coroutine.
    
    >>> Los dos primeros argumentos Any, Any representan los tipos de los argumentos de entrada y salida de la función send() de la coroutine. En la mayoría de los casos, estos son Any porque no se utilizan directamente.
    """


async def comprobarDatoUsuario(user: Cliente) -> dict[str, str] | HTTPException:
    if (
        len(str(user.telefono)) != 8
        or str(user.telefono).isdigit() == False
        or "@" not in user.email
        or "." not in user.email
        or ".com" not in user.email
        or len(user.nombre) < 3
        or len(user.email) < 3
        or user.nombre.isalpha() == False
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "El telefono debe tener 8 numeros"
                if len(str(user.telefono)) != 8
                else (
                    "El telefono debe tener solo numeros"
                    if str(user.telefono).isdigit() == False
                    else (
                        "El email debe tener un @"
                        if "@" not in user.email
                        else (
                            "El email debe tener un . (punto)"
                            if "." not in user.email
                            else (
                                "El email debe tener un .com"
                                if ".com" not in user.email
                                else (
                                    "El nombre debe tener mas de 3 caracteres"
                                    if len(user.nombre) < 3
                                    else (
                                        "El email debe tener mas de 3 caracteres"
                                        if len(user.email) < 3
                                        else "El nombre debe tener solo letras"
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            headers=dict(X_Error="Error"),
        )
        # Podemos usar parentesis para darle formato a la condicion pero no es necesario en mi caso es mas facil de leer sin parentesis. Con parentesis seria asi

    # * El método isalpha() de Python para verificar si una cadena contiene solo letras y no números. Este método devuelve True si todos los caracteres en la cadena son letras y False de lo contrario.
    # el método find() de Python para verificar si una cadena contiene ciertos caracteres. Este método devuelve el índice de la primera aparición del carácter especificado. Si el carácter no se encuentra, devuelve -1. Ejemplo de uso: "hola".find("o") devuelve 1. "hola".find("x") devuelve -1.
    else:
        return dict(mensaje="Cliente creado correctamente")


"""
! Aunque el usuario ponga el identificador como type: int, el identificador se va a guardar como type: str en el diccionario. Igual ocurre con el telefono

"""


# type: [int-str]
@app.post(
    path="/cliente/",
    response_model=Cliente | dict[str, str | int],
    status_code=status.HTTP_201_CREATED,
    tags=["Crear clientes en el sistema"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Crear clientes en el sistema",
    summary="Crear clientes en el sistema",
    response_description="Cliente creado correctamente",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Crear clientes en el sistema",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def clientes(usuario: Cliente) -> dict[str, str] | HTTPException:
    if str(usuario.identificador) in lista_clientes:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El cliente ya existe",
            headers=dict(X_Error="Error"),
        )
    diccionario: dict[str, str] = await comprobarDatoUsuario(user=usuario)
    if (
        "mensaje" in diccionario.keys()
        and "Cliente creado correctamente" in diccionario.values()
    ):
        usuario.contraseña = jwt.encode(
            claims=dict(contraseña=usuario.contraseña),
            key=CLAVE_SECRETA,
            algorithm=ALGORITMO,
            headers={"typo": "JWT"},
        )
        lista_clientes[str(usuario.identificador)] = usuario
        return diccionario


@app.put(
    path="/cliente/",
    response_model=dict[str, str],
    status_code=status.HTTP_200_OK,
    tags=["Actualizar clientes en el sistema"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Actualizar clientes en el sistema",
    summary="Actualizar clientes en el sistema",
    response_description="Cliente actualizado correctamente",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Actualizar clientes en el sistema",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def clientes(usuario: Cliente) -> dict[str, str]:
    # Enumerate() es una función incorporada de Python que toma una colección (por ejemplo, una lista) y devuelve un objeto enumerado.
    # enumerate() empieza a contar desde 0 por defecto, pero puedes especificar el valor inicial con el argumento opcional start.

    """
    >>> El método keys() devuelve una vista de todas las claves en el diccionario, y el método values() devuelve una vista de todos los valores en el diccionario. Por lo tanto, no puedes comparar directamente estos resultados con una cadena.
    """
    diccionario: dict[str, str] = await comprobarDatoUsuario(user=usuario)
    if (
        "mensaje" in diccionario.keys()
        and "Cliente creado correctamente" in diccionario.values()
        and len(lista_clientes) > 0
    ):
        for indice, actualizar_datos in enumerate(
            iterable=lista_clientes.keys(), start=1
        ):
            if actualizar_datos == str(usuario.identificador):
                lista_clientes[str(indice)] = usuario
                return dict(mensaje="Cliente actualizado correctamente")
        else:  # if not existe es igual a if existe == False por que not es un operador de negacion que niega el valor de la variable
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Error al actualizar el cliente",
                headers=dict(X_Error="Error"),
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error al actualizar el cliente",
            headers=dict(X_Error="Error"),
        )


@app.patch(
    path="/cliente/nombre/",
    status_code=status.HTTP_200_OK,
    response_model=dict[str, str],
    tags=["Actualizar nombre de clientes en el sistema"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Actualizar nombre de clientes en el sistema en path parameters",
    summary="Actualizar nombre de clientes en el sistema en path parameters",
    response_description="Nombre del cliente actualizado correctamente",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Actualizar nombre de clientes en el sistema en path parameters",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def cliente(usuarioNombre: ClienteNombre) -> dict[str, str] | HTTPException:
    if (
        str(usuarioNombre.identificador) not in lista_clientes
        or len(lista_clientes) == 0
    ):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Identificador de cliente no encontrado",
            headers=dict(X_Error="Error"),
        )

    elif (usuarioNombre.nombre).isalpha() == False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre debe tener solo letras",
            headers=dict(X_Error="Error"),
        )
    elif len(usuarioNombre.nombre) < 3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre debe tener mas de 3 caracteres",
            headers=dict(X_Error="Error"),
        )
    """
    para cambiar el nombre de un cliente en el diccionario se hace de la siguiente manera
    
    >>> lista_clientes es un diccionario donde la clave es el identificador del cliente y el valor es un diccionario con los datos del cliente
    
    >>> UsuarioNombre es un objeto de tipo ClienteNombre que tiene dos atributos, identificador y nombre
    
    >>> [str(usuarioNombre.identificador)] es el identificador del cliente que se quiere cambiar el nombre
    
    >>> ["nombre"] es la clave del diccionario que se quiere cambiar en el diccionario que tiene como clave el identificador del cliente
    
    >>> usuarioNombre.nombre es el nuevo nombre que se le quiere dar al cliente
    """
    lista_clientes[str(usuarioNombre.identificador)].nombre = usuarioNombre.nombre
    return dict(mensaje="Nombre del cliente actualizado correctamente")


@app.patch(
    path="/cliente/email/",
    status_code=status.HTTP_200_OK,
    response_model=dict[str, str],
    tags=["Actualizar email de clientes en el sistema"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Actualizar email de clientes en el sistema",
    summary="Actualizar email de clientes en el sistema",
    response_description="",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Actualizar email de clientes en el sistema",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def cliente(usuarioEmail: ClienteEmail) -> dict[str, str] | HTTPException:
    if (
        str(usuarioEmail.identificador) not in lista_clientes
        or len(lista_clientes) == 0
    ):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Identificador de cliente no encontrado",
            headers=dict(X_Error="Error"),
        )
    elif len(usuarioEmail.email) < 3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El email debe tener mas de 3 caracteres",
            headers=dict(X_Error="Error"),
        )
    elif ".com" not in usuarioEmail.email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El email debe tener un .com",
            headers=dict(X_Error="Error"),
        )
    elif "." not in usuarioEmail.email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El email debe tener un . (punto)",
            headers=dict(X_Error="Error"),
        )
    elif "@" not in usuarioEmail.email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El email debe tener un @",
            headers=dict(X_Error="Error"),
        )
    lista_clientes[str(usuarioEmail.identificador)].email = usuarioEmail.email
    return dict(mensaje="Email del cliente actualizado correctamente")


@app.patch(
    path="/cliente/telefono/",
    status_code=status.HTTP_200_OK,
    response_model=dict[str, str],
    tags=["Actualizar telefono de clientes en el sistema"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Actualizar telefono de clientes en el sistema",
    summary="Actualizar telefono de clientes en el sistema",
    response_description="Telefono del cliente actualizado correctamente",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Actualizar telefono de clientes en el sistema",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def cliente(usuarioTelefono: ClienteTelefono) -> dict[str, str] | HTTPException:
    if (
        str(usuarioTelefono.identificador) not in lista_clientes
        or len(lista_clientes) == 0
    ):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Identificador de cliente no encontrado",
            headers=dict(X_Error="Error"),
        )
    lista_clientes[str(usuarioTelefono.identificador)].telefono = (
        usuarioTelefono.telefono
    )
    return dict(mensaje="Telefono del cliente actualizado correctamente")


"""
Cuando se realiza una petición DELETE exitosa en HTTP, el código de estado más comúnmente devuelto es el 204, que significa "No Content". Este código indica que la petición se ha completado con éxito, pero no hay ninguna representación para devolver (es decir, el cuerpo de la respuesta está vacío).
"""


"""
>>> devolver un cuerpo de respuesta con un código de estado HTTP 204. Según el estándar HTTP, el código de estado 204 (No Content) no debe tener un cuerpo de respuesta.

>>> Estoy devolviendo un diccionario con un mensaje después de eliminar un cliente. Esto no es permitido cuando se usa el código de estado 204. para solucionar este problema, necesitas devolver un cuerpo de respuesta vacío. Un codigo de estado 200 (OK) con un cuerpo de respuesta vacío es una solución alternativa.
"""


@app.delete(
    path="/cliente/{identificador}/",
    status_code=status.HTTP_200_OK,
    response_model=dict[str, str],
    tags=["Eliminar clientes en el sistema"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Eliminar clientes en el sistema",
    summary="Eliminar clientes en el sistema",
    response_description="Cliente eliminado correctamente",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Eliminar clientes en el sistema",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def cliente(identificador: int) -> dict[str, str]:
    if str(identificador) not in lista_clientes:
        return dict(mensaje="Identificador de cliente no encontrado")
    del lista_clientes[str(identificador)]
    # lista_clientes.pop(str(identificador))
    # clave,valor = lista_clientes.popitem()
    # lista_clientes.clear()
    return dict(mensaje="Cliente eliminado")


# Query parameters
@app.delete(
    path="/cliente/",
    status_code=status.HTTP_200_OK,
    response_model=dict[str, str],
    tags=["Eliminar clientes en el sistema"],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Eliminar clientes en el sistema",
    summary="Eliminar clientes en el sistema",
    response_description="Cliente eliminado correctamente",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Eliminar clientes en el sistema",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def cliente(identificador: int) -> dict[str, str]:
    if str(identificador) not in lista_clientes:
        return dict(mensaje="Identificador de cliente no encontrado")
    del lista_clientes[str(identificador)]
    # lista_clientes.pop(str(identificador))
    # clave,valor = lista_clientes.popitem()
    # lista_clientes.clear()
    return dict(mensaje="Cliente eliminado")


# real
@app.post(
    path="/login/",
    tags=["Login"],
    status_code=status.HTTP_200_OK,
    response_model=dict,
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Iniciar sesión para obtener un token de acceso",
    summary="Iniciar sesión",
    response_description="Token de acceso",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Iniciar sesión",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
# * Dependencias de ruta en FastAPI son funciones que se ejecutan antes de que la función de ruta real se ejecute. Pueden ser funciones asíncronas y regulares.
async def login(
    formulario: OAuth2PasswordRequestForm = Depends(
        dependency=OAuth2PasswordRequestForm, use_cache=True
    )
) -> dict | HTTPException:
    identficador: dict | None = lista_clientes.get(str(formulario.client_id))

    if not identficador:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Identificador no existe {formulario.client_id}",
            headers=dict(WWW_AUTENTICATE=BEARER),
        )
    """
    >>> ya que el metodo get() de un diccionario devuelve None si la clave no existe, podemos usarlo para verificar si un usuario existe en el diccionario.
    
    ya que si una variabe es None, es igual a if variable == None o if variable is None o if not variable o if variable == False
    
    
    >>> if not usuario: es igual a if usuario == False
    
    >>> if usuario: es igual a if usuario == True
    """
    # lista_clientes[str(formulario.client_id)].nombre
    # if formulario.username == lista_clientes[str(formulario.client_id)].nombre
    usuario: dict | None = (
        lista_clientes[str(formulario.client_id)].nombre
        if formulario.username == lista_clientes[str(formulario.client_id)].nombre
        else None
    )
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no existe",
            headers=dict(WWW_AUTENTICATE=BEARER),
        )
    contraseña = await buscarContraseñaUsuario(
        identificador=formulario.client_id,
        usuario=formulario.username,
    )

    """
    La funcion verify() de la clase CryptContext nos permite verificar si una contraseña es correcta o no.
    
    >>> el parametro category nos permite especificar el algoritmo de encriptacion que vamos a utilizar
    
    >>> el parametro secret nos permite especificar la contraseña que queremos verificar
    
    >>> el parametro secret_hash nos permite especificar la contraseña encriptada que queremos verificar
    
    >>> el parametro scheme nos permite especificar el algoritmo de encriptacion que vamos a utilizar
    
    >>> si la contraseña es correcta, la funcion verify() nos devuelve True
    """

    """
    crypt.verify() verifica una contraseña que ha sido codificada como un token JWT, pero crypt.verify() está diseñado para trabajar con hashes bcrypt, no con tokens JWT.
    
    Para verificar un token JWT, necesitas decodificarlo con la misma clave secreta que usaste para codificarlo. 
    """
    try:
        decodificar_jwt: dict = jwt.decode(
            token=contraseña, key=CLAVE_SECRETA, algorithms=[ALGORITMO]
        )

        if not crypt.verify(
            secret=formulario.password,
            hash=decodificar_jwt.get("contraseña"),
            scheme="bcrypt",
            category="bcrypt",
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales incorrecta",
                headers=dict(WWW_AUTENTICATE=BEARER),
            )
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrecta",
            headers=dict(WWW_AUTENTICATE=BEARER),
        )
    """
    sub es el identificador del usuario
    exp es el tiempo de expiracion del token
    """
    # Nuestro token es Numero

    token_acceso_unica: dict = dict(
        sub=formulario.username,
        exp=datetime.utcnow()
        + timedelta(
            minutes=DURACION_TOKEN_ACCESO,
            days=0,
            seconds=0,
            microseconds=0,
            milliseconds=0,
            hours=0,
            weeks=0,
        ),
    )
    """
    jwt.encode() es una función que nos permite generar un token JWT.
    acepta los siguientes parámetros:
    >>> access_token: es el payload del token que queremos generar. el payload es la información que queremos que contenga el token.
    
    >>> key: es la clave secreta que vamos a utilizar para firmar el token. esta clave secreta debe ser segura y no debe ser compartida con nadie. si alguien tiene acceso a esta clave secreta, podrá falsificar tokens.
    
    >>> algorithm: es el algoritmo de encriptación que vamos a utilizar para firmar el token. este algoritmo debe ser seguro y no debe estar obsoleto.
    
    >>> claims: es un diccionario que contiene la información que queremos que contenga el token. este diccionario puede contener cualquier información que queramos, pero debe ser un diccionario válido. a diferencia del payload, este diccionario no es encriptado y puede ser leído por cualquiera.
    
    >>> headers: es un diccionario que contiene la información que queremos que contenga el token. este diccionario puede contener cualquier información que queramos, pero debe ser un diccionario válido. a diferencia del payload, este diccionario no es encriptado y puede ser leído por cualquiera.
    """
    # access_token=token_acceso_unica,  # payload
    return dict(
        token_acceso=jwt.encode(
            key=CLAVE_SECRETA,
            algorithm=ALGORITMO,
            claims=token_acceso_unica,
            headers={"typo": "JWT"},
        ),
        tipo_token="bearer",
    )


"""
El campo at_hash es una abreviatura de Access Token Hash. Es un hash del token de acceso, que se utiliza en los flujos de autenticación OpenID Connect para validar los tokens de acceso.

Cuando un cliente recibe un token de acceso y un token de identidad desde el servidor de autorización, puede validar el token de acceso utilizando el valor at_hash en el token de identidad. El cliente calcula un hash del token de acceso y lo compara con el valor at_hash en el token de identidad. Si los dos valores coinciden, el cliente puede estar seguro de que el token de acceso es válido.

access_token=formulario.password,
"""


async def buscarContraseñaUsuario(
    identificador: str,
    usuario: str,
) -> str:
    # and lista_clientes[identificador_cliente].nombre == usuario
    for identificador_cliente in lista_clientes.keys():
        if (
            identificador_cliente == str(identificador)
            and lista_clientes[identificador_cliente].nombre == usuario
        ):
            return lista_clientes[identificador_cliente].contraseña
            # return lista_clientes[identificador_cliente].contraseña
        else:
            continue
    else:
        return "Contraseña incorrecta"


# openssl rand -hex 32 # Generar clave secreta


async def autenticarUsuario(
    token: str = Depends(oauth2),
):  # -> Cliente | HTTPException
    excepcion = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:

        usuario = jwt.decode(
            token=token,
            key=CLAVE_SECRETA,
            algorithms=[ALGORITMO],
        ).get("sub")

        """if not usuario:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Credenciales de autenticación inválidas",
                headers=dict(WWW_AUTENTICATE=BEARER),
            )"""

    except jwt.JWTError:
        raise excepcion

    """
    lista_clientes.values() nos devuelve una lista con los valores del diccionario lista_clientes.
    """
    for cliente in lista_clientes.values():
        if cliente.nombre == usuario and cliente.activo == True:
            return cliente
        else:
            continue
    else:
        return dict(mensaje="Usuario inactivo")


"""async def buscarUsuario(
    usuario: Cliente | None = Depends(dependency=autenticarUsuario, use_cache=True),
) -> Cliente | None | HTTPException:
    if not usuario.activo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo",
            headers=dict(WWW_AUTENTICATE=BEARER),
        )
    return usuario"""


@app.get(
    path="/users/me",
    tags=["Usuarios"],
    status_code=status.HTTP_200_OK,
    response_model=Cliente | dict[str, str],
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Obtener información del usuario autenticado",
    summary="Información del usuario autenticado",
    response_description="Token de acceso",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Información del usuario autenticado",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def clientes(
    usuario: Cliente | dict[str, str] = Depends(
        dependency=autenticarUsuario, use_cache=True
    ),
) -> Cliente | dict[str, str] | HTTPException:
    return usuario


"""
GnuPG, también conocido como GPG, es una implementación completa y libre del estándar OpenPGP, que fue definido por el RFC4880. OpenPGP es un estándar para el cifrado de datos y la comunicación segura. GnuPG permite cifrar y firmar tus datos y comunicaciones, y cuenta con un sistema versátil de gestión de claves.

GnuPG, que significa GNU Privacy Guard, es un software de cifrado y firma de clave pública que proporciona autenticación y seguridad para las comunicaciones y la transmisión de datos. Es una alternativa de código abierto al programa PGP (Pretty Good Privacy) de Symantec.

GnuPG es una herramienta de línea de comandos con características para facilitar la integración con otras aplicaciones. Una gran cantidad de aplicaciones de front-end y bibliotecas están disponibles. Las versiones de GnuPG en desarrollo añaden soporte para los protocolos de cifrado modernos S/MIME y Secure Shell (ssh).

Por lo tanto, GnuPG es una herramienta esencial para proteger tus datos y tu comunicación.

pymongo es un paquete de Python que permite interactuar con la base de datos MongoDB. pymongo es el controlador oficial de Python para MongoDB. pymongo es un paquete de Python que permite interactuar con la base de datos MongoDB. pymongo es el controlador oficial de Python para MongoDB.
"""