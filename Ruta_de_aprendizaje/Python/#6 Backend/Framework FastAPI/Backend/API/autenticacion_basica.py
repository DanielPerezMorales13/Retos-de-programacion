"""
>>> Autenticación: La autenticación es el proceso de verificar la identidad de un usuario. La autenticación se utiliza para verificar que un usuario es quien dice ser. La autenticación se utiliza para verificar que un usuario tiene permiso para acceder a una ruta de una API.

>>> Autorización: La autorización es el proceso de verificar que un usuario tiene permiso para acceder a una ruta de una API. La autorización se utiliza para verificar que un usuario tiene permiso para acceder a una ruta de una API.

La autenticación y la autorización son dos conceptos diferentes, pero relacionados. La autenticación se utiliza para verificar la identidad de un usuario. La autorización se utiliza para verificar que un usuario tiene permiso para acceder a una ruta de una API.<
"""

from fastapi import Depends, FastAPI, HTTPException, status

"""
OOAuth2PasswordBearer es una clase que proporciona una forma de declarar "bearer" token OAuth2 security en tu API. Se utiliza para proteger las rutas y asegurarse de que el cliente que hace la solicitud proporciona un token válido.

OAuth2PasswordRequestForm es una clase que define un formulario de solicitud de contraseña OAuth2. Se utiliza para generar un formulario de solicitud de token en la documentación interactiva de tu API.


"""
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app: FastAPI = FastAPI()

# oauth2 es un estandard de autenticacion que permite a los usuarios dar acceso a aplicaciones de terceros a su informacion sin compartir su contraseña
"""
>>> la variable oauth2 es una instancia de la clase OAuth2PasswordBearer. Esta instancia se utiliza para declarar un esquema de autenticación OAuth2 en tu API. La instancia de OAuth2PasswordBearer se utiliza para proteger las rutas y asegurarse de que el cliente que hace la solicitud proporciona un token válido.

>>> tokenUrl es el nombre de la ruta que se utiliza para obtener un token de acceso. El valor de tokenUrl es "login". Esto significa que el cliente debe hacer una solicitud POST a la ruta "/login" para obtener un token de acceso.

>>> auto_error es un booleano que indica si FastAPI debe manejar automáticamente los errores de autenticación. El valor de auto_error es True. Esto significa que FastAPI manejará automáticamente los errores de autenticación y devolverá una respuesta de error si el cliente no proporciona un token de acceso válido.

>>> description es una cadena que proporciona una descripción de la autenticación. El valor de description es "Iniciar sesión para obtener un token de acceso". Esto significa que la descripción de la autenticación es "Iniciar sesión para obtener un token de acceso".

>>> scheme_name es una cadena que proporciona el nombre del esquema de autenticación. El valor de scheme_name es None. Esto significa que el nombre del esquema de autenticación es None.

>>> scopes es una lista de cadenas que proporciona los alcances de la autenticación. El valor de scopes es None. Esto significa que no hay alcances de autenticación.
"""
oauth2: OAuth2PasswordBearer = OAuth2PasswordBearer(
    tokenUrl="login",
    auto_error=True,
    description="Iniciar sesión para obtener un token de acceso",
    scheme_name=None,
    scopes=None,
)


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


# Base de datos de usuarios (simulada)
# users usuario
# db (database)
users_db: dict[str, dict[str, bool | str]] = {
    "danitrix": {
        "username": "danitrix",
        "full_name": "Daniel Perez",
        "email": "danitrix1312@gmail.com",
        "disabled": False,
        "password": "123456",
    },
    "danitrix2": {
        "username": "danitrix2",
        "full_name": "Daniel Perez 2",
        "email": "danitrix1312@gmail.com",
        "disabled": True,
        "password": "654321",
    },
}


def buscar_usuario(username: str) -> UserDB | None:
    if username in users_db:
        return User(**users_db[username])


def buscar_usuario_DB(username: str) -> UserDB | None:
    if username in users_db:
        return UserDB(**users_db[username])


"""
>>> Depends() es una función que se utiliza para declarar dependencias en las rutas. Al declarar una dependencia con Depends(), FastAPI ejecutará la función que se pasa a Depends() y usará el valor devuelto por esa función como valor de la dependencia.


"""


async def usuario_actual(token: str = Depends(dependency=oauth2, use_cache=True)):
    user: UserDB | None = buscar_usuario(username=token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="credenciales invalidas",
            headers={"WWW-Autenticate": "Bearer"},
        )
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario deshabilitado",
            headers={"X-Error": "El usuario esta deshabilitado"},
        )
    return user  # Asegúrarse de que esto no sea None


@app.post(path="/login")
async def login(
    formulario: OAuth2PasswordRequestForm = Depends(),
) -> dict[str, str] | None:
    user_db: dict[str, bool | str] | None = users_db.get(formulario.username)

    if not user_db:
        raise HTTPException(
            status_code=400,
            detail="Usuario no encontrado",
            headers={"Acceso-denegado": "usuario no encontrado"},
        )
    user: UserDB | None = buscar_usuario_DB(username=formulario.username)
    if not formulario.password == user.password:
        raise HTTPException(
            status_code=400,
            detail="Contraseña incorrecta",
            headers={"Acceso-denegado": "Contraseña incorrecta"},
        )
    """
    Retorna un diccionario con el token de acceso y el tipo de token. El token de acceso es el nombre de usuario del usuario. El tipo de token es "bearer". El token de acceso se utiliza para autenticar al usuario en las rutas protegidas. y el tipo de token es "bearer" que es un tipo de token de autenticacion que se usa para proteger las rutas de la api
    """
    return {"access_token": user.username, "token_type": "bearer"}


@app.get(path="/users/me")
async def me(user: User = Depends(dependency=usuario_actual)) -> User:
    return user
