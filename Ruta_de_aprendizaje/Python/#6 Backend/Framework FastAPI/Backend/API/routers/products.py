from fastapi import APIRouter

# El parametro prefix es opcional, pero si se usa, se le puede pasar una cadena que se agregará al principio de todas las rutas definidas en la instancia de APIRouter.


# El parametro tags es opcional, pero si se usa, se le puede pasar una lista de cadenas que se usarán como etiquetas para la documentación de la API. Las etiquetas se mostrarán en la documentación de la API en la interfaz de usuario de Swagger y ReDoc.

# El parametro responses es opcional, pero si se usa, se le puede pasar un diccionario que se usará para definir respuestas predeterminadas para todas las rutas definidas en la instancia de APIRouter. Las respuestas predeterminadas se mostrarán en la documentación de la API en la interfaz de usuario de Swagger y ReDoc.
router: APIRouter = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"mensaje": "No se encontro el recurso"}},
)
products_list: list[str] = [
    "Product 1",
    "Product 2",
    "Product 3",
    "Product 4",
    "Product 5",
]


# * ya no es necesario pasar el parametro path, ya que se esta usando la instancia de la clase APIRouter con el parametro prefix que se le paso al inicializar la instancia de la clase APIRouter que se asigno a la variable router y se le paso la ruta /products
# @router.get(path="/products")
@router.get(path="/")
async def products() -> list[str]:
    return [
        "Product 1",
        "Product 2",
        "Product 3",
        "Product 4",
        "Product 5",
    ]


# * ya no es necesario pasar el parametro path, ya que se esta usando la instancia de la clase APIRouter con el parametro prefix que se le paso al inicializar la instancia de la clase APIRouter que se asigno a la variable router y se le paso la ruta /products
# @router.get(path="/products/{identificador}")
@router.get(path="/{identificador}")
async def products(identificador: int) -> str:
    return products_list[identificador]
