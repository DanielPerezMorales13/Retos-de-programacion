from abc import ABC

from fastapi import APIRouter, Depends, FastAPI, HTTPException, Response, status
from fastapi.datastructures import Default
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from fastapi.utils import generate_unique_id
from pydantic import BaseModel

from libraries import (
    filtracion_por_identificador,
    filtracion_por_letra,
    filtracion_por_nombre,
)

BEARER: str = "Bearer"
WWW_AUTENTICATE: str = "WWW-Autenticate"

"""
JSONResponse es una clase que representa una respuesta JSON. Se utiliza para devolver una respuesta JSON desde una ruta de FastAPI.

JSON es un formato de intercambio de datos que se utiliza en las API REST.
JSON significa Notación de Objetos JavaScript que en español significa Notación de Objetos JavaScript. JSON es un formato de intercambio de datos que se utiliza en las API REST. JSON es un formato de texto que es fácil de leer y escribir para los humanos y fácil de analizar y generar para las máquinas.

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

oauth2: OAuth2PasswordBearer = OAuth2PasswordBearer(
    tokenUrl="login",
    auto_error=True,
    description="Iniciar sesión para obtener un token de acceso",
    scheme_name=None,
    scopes=None,
)


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


@app.post(
    path="/login/",
    tags=["Login"],
    status_code=status.HTTP_200_OK,
    response_model=dict[str, str],
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
) -> dict[str, str] | HTTPException:
    identficador: dict | None = lista_clientes.get(str(formulario.client_id))

    if not identficador:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Identificador no existe",
            headers=dict(WWW_AUTENTICATE=BEARER),
        )
    """
    >>> ya que el metodo get() de un diccionario devuelve None si la clave no existe, podemos usarlo para verificar si un usuario existe en el diccionario.
    
    ya que si una variabe es None, es igual a if variable == None o if variable is None o if not variable o if variable == False
    
    
    >>> if not usuario: es igual a if usuario == False
    
    >>> if usuario: es igual a if usuario == True
    """
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
    # ! No he encontrado la manera de implemtar esto aun
    """
    email: dict | None = (
        lista_clientes[str(formulario.client_id)].get("email")
        if formulario.email == lista_clientes[str(formulario.client_id)].get("email")
        else None
    )
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo no existe",
            headers=dict(WWW_AUTENTICATE=BEARER),
        )
    """
    contraseña = await buscarContraseñaUsuario(
        identificador=formulario.client_id,
        usuario=formulario.username,
    )
    if not formulario.password == contraseña:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrecta",
            headers=dict(WWW_AUTENTICATE=BEARER),
        )
    # Nuestro token es Numero
    return dict(token_acceso=(formulario.client_id), tipo_token="bearer")


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


@app.get(
    path="/users/me/",
    tags=["Usuario actual"],
    status_code=status.HTTP_200_OK,
    response_model=dict[str, str | int | bool] | Cliente,
    callbacks=None,
    dependencies=None,
    deprecated=None,
    description="Usuario actual en el sistema",
    summary="Usuario actual en el sistema",
    response_description="Usuario actual en el sistema",
    response_model_include=None,
    response_model_exclude=None,
    response_model_by_alias=True,
    response_model_exclude_none=False,
    name="Usuario actual en el sistema",
    operation_id=None,
    generate_unique_id_function=Default(generate_unique_id),
    responses=None,
    include_in_schema=True,
    response_class=Default(JSONResponse),
    openapi_extra=None,
    response_model_exclude_defaults=False,
    response_model_exclude_unset=False,
)
async def me(
    usuario: dict[str, str | int | bool] | Cliente = Depends(
        dependency=usuarioActual,
        use_cache=True,
    )
) -> dict[str, str | int | bool] | HTTPException | Cliente:
    return usuario
    ...


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
# dict()
global lista_clientes
lista_clientes: dict = dict()


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
