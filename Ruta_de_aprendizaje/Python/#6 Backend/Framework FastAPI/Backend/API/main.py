# importacion fastapi
from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles

from routers import products, users

# Esta es la forma de crear una instancia de la clase FastAPI y asignarla a una variable llamada app
app: FastAPI = FastAPI()

# Routers
"""
El metodo include_router() se usa para incluir una instancia de la clase APIRouter en la aplicación principal.

El parametro router sirve para incluir una instancia de la clase APIRouter en la aplicación principal.
"""
app.include_router(router=products.router)
app.include_router(router=users.router)


"""
>>> El metodo mount() se usa para incluir un directorio de recursos estaticos en la aplicación principal.  Los recursos estaticos son archivos que no cambian, como por ejemplo, imagenes, videos, hojas de estilo, scripts, etc. Los recursos estaticos se almacenan en un directorio llamado static.

>>> los parametros path y app son obligatorios, pero los parametros check_dir, html y packages son opcionales.

>>> path: Es la ruta de la url que se usará para acceder a los recursos estaticos. Por defecto, la ruta de la url es /static.

>>> app: Es la instancia de la clase StaticFiles que creamos con el directorio de recursos estaticos.

>>> check_dir: Es un parametro opcional que se usa para indicarle a FastAPI que verifique si el directorio de recursos estaticos existe. Por defecto, el valor de check_dir es True.

>>> html: Es un parametro opcional que se usa para indicarle a FastAPI que permita que se sirvan archivos HTML. Por defecto, el valor de html es False.

>>> packages: Es un parametro opcional que se usa para indicarle a FastAPI que permita que se sirvan archivos de paquetes de Python. Por defecto, el valor de packages es None.

>>> name: Es un parametro opcional que se usa para indicarle a FastAPI que le asigne un nombre a la ruta de la url. Por defecto, el valor de name es static.
"""
app.mount(
    path="/static",
    app=StaticFiles(directory="static", check_dir=True, html=False, packages=None),
    name="static",
)


"""
Los nombres de las cookies deben cumplir con ciertas reglas. En particular, no pueden contener espacios en blanco, comas, puntos y comas, ni muchos otros caracteres especiales.
"""


@app.post("/cookie")
async def crear_cookie(response: Response) -> dict[str, str]:
    # el metodo set_cookie() se usa para crear una cookie en el navegador del cliente. El metodo set_cookie() recibe los siguientes parametros:
    """
    key: Es el nombre de la cookie.
    value: Es el valor de la cookie.
    """
    response.set_cookie(
        key="Cookie_Usuario",
        value="cookie_de_daniel_perez",
    )
    return {"message": "cookie creada"}


"""
Los headers son la parte superior de una solicitud o respuesta HTTP. 

los headers son metadatos que se utilizan para enviar información adicional sobre una solicitud o respuesta HTTP. Los headers se utilizan para enviar información sobre el tipo de contenido que se está enviando, la longitud del contenido que se está enviando, la codificación del contenido que se está enviando, la fecha en que se envió el contenido, etc.
"""


@app.get("/headers/")
async def obtener_headers(response: Response) -> dict[str, str]:
    response.headers["Cabecera-prueba"]: str = "Cabecera de Daniel"
    return {"message": "Hola FastAPI con headers"}


"""
>>> Podemos crear una ruta con el decorador app.get() y pasarle como argumento la ruta que queremos que responda a esa petición

/ Es la ruta raíz de nuestra aplicación. Es decir, es la ruta principal de nuestra aplicación. Cuando un usuario ingrese a la ruta raíz de nuestra aplicación, se ejecutará la función que le pasemos como argumento al decorador app.get().

/url Es una ruta secundaria de nuestra aplicación. Es decir, es una ruta que no es la ruta principal de nuestra aplicación. Cuando un usuario ingrese a la ruta secundaria de nuestra aplicación, se ejecutará la función que le pasemos como argumento al decorador app.get().


>>> Las funciones async asíncronas nos permiten ejecutar código de manera asíncrona. Esto significa que podemos ejecutar varias funciones al mismo tiempo. Esto es muy útil cuando tenemos que realizar tareas que consumen mucho tiempo, como por ejemplo, realizar una petición a una API externa. Mientras se realiza la petición a la API externa, podemos ejecutar otras funciones. Cuando la petición a la API externa termine, podemos continuar ejecutando el código de la función asíncrona. Esto nos permite crear aplicaciones que respondan de manera más rápida.

Las funciones asíncronas se crean con la palabra clave async. Las funciones asíncronas se ejecutan con la palabra clave await. Las funciones asíncronas nos permiten ejecutar código de manera asíncrona.
"""


@app.get(path="/")
async def root() -> dict[str, str]:
    return {"mensaje": "Hola FastAPI"}


@app.get(path="/url")
async def root() -> dict[str, str]:
    return {"link": "https://github.com/Danitrix13/Retos-de-programacion"}


# Hemos hecho 2 peticiónes a nuestro servidor local. La primera petición fue a la ruta raíz de nuestra aplicación. La segunda petición fue a una ruta secundaria de nuestra aplicación. Cuando hacemos una petición a una ruta de nuestra aplicación, se ejecuta la función que le pasamos como argumento al decorador app.get() de esa ruta. La ruta seria la url que se muestra en la terminal, en este caso Esto http://127.0.0.1:8000/

# son peticiones get, es decir, son peticiones que se hacen con el método GET. El método GET es el método por defecto de las peticiones HTTP. Cuando hacemos una petición a una ruta de nuestra aplicación, se ejecuta la función que le pasamos como argumento al decorador app.get() de esa ruta. La ruta es Esto http://127.0.0.1:8000/url

# Documentación con Swagger UI http://127.0.0.1:8000/docs#/ es la ruta de la documentación de nuestra aplicación. Cuando ejecutamos el servidor de desarrollo de FastAPI, podemos acceder a la documentación de nuestra aplicación en la ruta.

# Documentación con ReDoc http://127.0.0.1:8000/redoc es otra ruta de la documentación de nuestra aplicación. Cuando ejecutamos el servidor de desarrollo de FastAPI, podemos acceder a la documentación de nuestra aplicación en la ruta.

"""
Si el servidor retorna un código de estado que empieza por el 1, significa que la petición se está procesando. 

Si el servidor retorna un código de estado que empieza por el 2, significa que la petición se ha procesado correctamente. 

Si el servidor retorna un código de estado que empieza por el 3, significa que la petición se ha redirigido. 

Si el servidor retorna un código de estado que empieza por el 4, significa que la petición no se ha podido procesar porque el cliente no tiene permiso para acceder a la ruta. 

Si el servidor retorna un código de estado que empieza por el 5, significa que la petición no se ha podido procesar porque ha ocurrido un error en el servidor.
"""

"""
Para levantar el servidor de desarrollo de FastAPI, tenemos que ejecutar el siguiente comando en la terminal:

Iniciar servidor de desarrollo de FastAPI
>>> uvicorn users:app --reload --port 8000 --host 127.0.0.1

Detener servidor de desarrollo de FastAPI
>>> Ctrl + C

Esto http://127.0.0.1:8000/ es un localhost, es decir, un servidor local. Cuando ejecutamos el servidor de desarrollo de FastAPI, estamos ejecutando un servidor local. El servidor de desarrollo de FastAPI se ejecuta en el puerto 8000. El puerto 8000 es el puerto por defecto para los servidores de desarrollo de FastAPI.

uvicorn: Es el servidor de desarrollo de FastAPI.
main: Es el nombre del ficheros principal de nuestra aplicación. Se recomienda que el ficheros principal de nuestra aplicación se llame main.py.

app: Es la instancia de la clase FastAPI que creamos en el ficheros main.py.

--reload: Es un parámetro que le pasamos a uvicorn para que reinicie el servidor cada vez que guardemos un cambio en nuestro código.

--port: Es un parámetro que le pasamos a uvicorn para indicarle en qué puerto queremos que se ejecute nuestro servidor de desarrollo. Por defecto, el servidor de desarrollo de FastAPI se ejecuta en el puerto 8000. Si queremos que se ejecute en otro puerto, tenemos que pasarle el parámetro --port seguido del número de puerto que queremos utilizar. 

--host: Es un parámetro que le pasamos a uvicorn para indicarle en qué host queremos que se ejecute nuestro servidor de desarrollo. Por defecto, el servidor de desarrollo de FastAPI se ejecuta en el host

Los puertos son números que se utilizan para identificar los programas que se ejecutan en un servidor. Cada programa que se ejecuta en un servidor tiene un puerto diferente. 

>>> Un localhost es un servidor local. Es decir, es un servidor que se ejecuta en nuestra computadora. Cuando ejecutamos el servidor de desarrollo de FastAPI, estamos ejecutando un servidor local.

Los puertos mas comunes son:

- 80: Es el puerto por defecto para los servidores web.

- 443: Es el puerto por defecto para los servidores web que utilizan HTTPS.

- 22: Es el puerto por defecto para los servidores SSH.

- 21: Es el puerto por defecto para los servidores FTP.

- 25: Es el puerto por defecto para los servidores SMTP.

- 110: Es el puerto por defecto para los servidores POP3.

- 143: Es el puerto por defecto para los servidores IMAP.

- 3306: Es el puerto por defecto para los servidores MySQL.

- 5432: Es el puerto por defecto para los servidores PostgreSQL.

- 27017: Es el puerto por defecto para los servidores MongoDB.

- 6379: Es el puerto por defecto para los servidores Redis.

- 8080: Es el puerto por defecto para los servidores que utilizan un proxy inverso.

- 8000: Es el puerto por defecto para los servidores de desarrollo de FastAPI.

- 8888: Es el puerto por defecto para los servidores de Jupyter Notebook.

Los puertos van de 0 a 65535. 
>>> Los puertos del 0 al 1023 son los puertos reservados. 
>>> Los puertos del 1024 al 49151 son los puertos registrados.
>>> Los puertos del 49152 al 65535 son los puertos dinámicos o privados.
"""

"""
>>> Operaciones get: Las operaciones get son operaciones que se utilizan para obtener datos. Las operaciones get se utilizan para obtener datos de una base de datos, para obtener datos de una API externa, para obtener datos de un ficheros, etc.

>>> Operaciones post: Las operaciones post son operaciones que se utilizan para crear datos. Las operaciones post se utilizan para crear datos en una base de datos, para crear datos en una API externa, para crear datos en un ficheros, etc.

>>> Operaciones put: Las operaciones put son operaciones que se utilizan para actualizar datos. Las operaciones put se utilizan para actualizar datos en una base de datos, para actualizar datos en una API externa, para actualizar datos en un ficheros, etc.

>>> Operaciones delete: Las operaciones delete son operaciones que se utilizan para eliminar datos. Las operaciones delete se utilizan para eliminar datos en una base de datos, para eliminar datos en una API externa, para eliminar datos en un ficheros, etc.

>>> Operaciones patch: Las operaciones patch son operaciones que se utilizan para actualizar datos. Las operaciones patch se utilizan para actualizar datos en una base de datos, para actualizar datos en una API externa, para actualizar datos en un ficheros, etc. La diferencia entre las operaciones put y las operaciones patch es que las operaciones put actualizan todos los datos de un recurso y las operaciones patch actualizan solo algunos datos de un recurso.

>>> Operaciones options: Las operaciones options son operaciones que se utilizan para obtener información sobre una ruta. Las operaciones options se utilizan para obtener información sobre una ruta de una API externa, para obtener información sobre una ruta de un servidor web, etc.

>>> Operaciones head: Las operaciones head son operaciones que se utilizan para obtener información sobre una ruta. Las operaciones head se utilizan para obtener información sobre una ruta de una API externa, para obtener información sobre una ruta de un servidor web, etc. La diferencia entre las operaciones options y las operaciones head es que las operaciones options devuelven información sobre una ruta y las operaciones head devuelven información sobre una ruta sin el cuerpo de la respuesta.

>>> Operaciones trace: Las operaciones trace son operaciones que se utilizan para obtener información sobre una ruta. Las operaciones trace se utilizan para obtener información sobre una ruta de una API externa, para obtener información sobre una ruta de un servidor web, etc.

"""

"""
>>> Hoy en dia existen aplicaciones para hacer peticiones a una API, como por ejemplo, Postman y  la extension de Vscode Thunder Client. 
Estas aplicaciones nos permiten hacer peticiones a una API y ver la respuesta de la API. Estas aplicaciones son muy útiles para probar una API.

Pero tambien podemos hacer peticiones a una API desde la terminal con el comando curl. 

>>> El comando curl nos permite hacer peticiones a una API y ver la respuesta de la API. El comando curl es muy útil para probar una API.

>>> Pero tambien podemos hacer peticiones programaticamente con Python. Con la libreria requests podemos hacer peticiones a una API y ver la respuesta de la API. La libreria requests es muy útil para probar una API.
"""


"""
>>> Recurso estaticos son archivos que no cambian, como por ejemplo, imagenes, videos, hojas de estilo, scripts, etc. Los recursos estaticos se almacenan en un directorio llamado static.
"""
