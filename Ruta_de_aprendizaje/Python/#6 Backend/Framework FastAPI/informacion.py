""" 
El backend es la parte del software que no se ve, es la parte que se encarga de la lógica de la aplicación. También se le conoce como el servidor, ya que es el que se encarga de procesar la información y enviarla al cliente. 


El frontend es la parte del software que se ve, es la parte que se encarga de la interfaz de usuario. También se le conoce como el cliente, ya que es el que se encarga de enviar la información al servidor y mostrarla al usuario.


Framework: Es un conjunto de herramientas que nos ayudan a desarrollar aplicaciones de una manera más rápida y sencilla. Existen frameworks para frontend y para backend.

FastAPI: Es un framework para backend que nos permite crear APIs de una manera muy rápida y sencilla. FastAPI está escrito en Python y utiliza el tipado estático para mejorar el autocompletado y la detección de errores. FastAPI utiliza Pydantic para validar los datos que recibe y devuelve. Es un excelente framework para crear APIs REST. Tambien su ruta de aprendizaje es muy sencilla y rapida de aprender.

Pydantic: Es una librería que nos permite validar los datos que recibe y devuelve nuestra API. Pydantic utiliza el tipado estático para mejorar el autocompletado y la detección de errores. Pydantic es muy fácil de utilizar y nos permite crear modelos de datos de una manera muy sencilla.


API: Es un conjunto de funciones que nos permiten comunicarnos con un software. API significa Application Programming Interface. En español significa Interfaz de Programación de Aplicaciones. Una API nos permite comunicarnos con un software de una manera muy sencilla. Una API nos permite enviar y recibir información de un software. Una API nos permite crear aplicaciones que se comuniquen con un software. Una API nos permite crear aplicaciones que se comuniquen entre sí.

para instalar fastapi y uvicorn se debe de ejecutar el siguiente comando en la terminal de visual studio code: pip install fastapi[all]
"""


# Tema: Type Hints en Python que en español significa "Sugerencias de tipo"

string: str = "Mi String variable"
print(string)
print(type(string), end="\n")

string: int = 5
print(string)
print(type(string), end="\n")

tipo_variable: str = "Mi tipado String variable"
# Al referenciar el tipo de dato el intelisense de python nos brinda metodos y atributos que podemos utilizar con el tipo de dato referenciado en este caso string o str
print(tipo_variable, end="\n")
print(type(tipo_variable), end="\n")

tipo_variable: int = 5
print(tipo_variable, end="\n")
print(type(tipo_variable), end="\n")
