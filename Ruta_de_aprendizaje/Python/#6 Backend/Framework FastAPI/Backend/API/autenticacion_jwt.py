from datetime import datetime, timedelta

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.datastructures import Default
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.utils import generate_unique_id
from jose import jwt
from passlib.context import CryptContext

# ! https://jwt.io/
# pip3 install python-jose[cryptography]

# pip3 install passlib[bcrypt]
"""
En informática, "kebab case" es un estilo de nomenclatura en el que las palabras se unen con guiones. Es similar al estilo "snake case", pero en lugar de usar guiones bajos, se utilizan guiones.

El estilo "kebab case" se utiliza a menudo para nombrar variables, funciones y métodos en lenguajes de programación. También se utiliza para nombrar archivos y directorios.
"""

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


ALGORITMO: str = "HS256"

"""
La variable crypt es un objeto de la clase CryptContext que nos permite encriptar y desencriptar contraseñas.

>>> `schemes=["bcrypt"]`: Esto especifica que quieres usar el esquema de hashing `bcrypt`. `bcrypt` es un método de hashing de contraseñas que es considerado seguro y eficaz.

>>> `deprecated="auto"`: Esto especifica que quieres que FastAPI te avise si el esquema de hashing que estás utilizando se vuelve obsoleto. Si el esquema de hashing se vuelve obsoleto, es posible que sea menos seguro y que se recomiende cambiar a un esquema más seguro.

"""
crypt: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")
"""
jwt significa JSON Web Token. Es un estándar abierto que define una forma segura y compacta para transmitir información entre partes como un objeto JSON. Esta información puede ser verificada y confiable porque está firmada digitalmente. Los JWT se pueden firmar utilizando un algoritmo (por ejemplo, HMAC con SHA-256 o RSA) y, por lo tanto, se pueden verificar la procedencia de los datos.
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


lista_clientes: dict[str, dict] = {
    "1": {
        "identificador": 1,
        "nombre": "daniel",
        "email": "daniel@yahoo.com",
        "telefono": 88042474,
        "activo": True,
        "contraseña": "$2a$12$oMz4.7Vqz1rsv.dWIlsHveUY1onIDXxAkqtxLd1HbssvuHXnUGJyO",
    }
}
# 123456


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
        lista_clientes[str(formulario.client_id)].get("nombre")
        if formulario.username
        == lista_clientes[str(formulario.client_id)].get("nombre")
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

    if not crypt.verify(
        hash=contraseña,
        secret=formulario.password,
        scheme="bcrypt",
        category="bcrypt",
    ):
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

    token_acceso_unica = dict(
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
    return dict(
        token_acceso=jwt.encode(
            access_token=formulario.password,  # payload
            key="secret",  # key
            algorithm=ALGORITMO,
            claims=token_acceso_unica,
            headers=None,
        ),
        tipo_token="bearer",
    )


async def buscarContraseñaUsuario(
    identificador: str,
    usuario: str,
) -> str:
    # and lista_clientes[identificador_cliente].nombre == usuario
    for identificador_cliente in lista_clientes.keys():
        if (
            identificador_cliente == str(identificador)
            and lista_clientes[identificador_cliente].get("nombre") == usuario
        ):
            return lista_clientes[identificador_cliente].get("contraseña")
            # return lista_clientes[identificador_cliente].contraseña
        else:
            continue
    else:
        return "Contraseña incorrecta"
