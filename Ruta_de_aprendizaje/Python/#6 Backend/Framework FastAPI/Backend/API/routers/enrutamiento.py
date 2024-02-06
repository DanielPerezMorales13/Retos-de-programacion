"""
El enrutamiento es el proceso de determinar cómo una aplicación responde a una solicitud de un cliente a un punto final en particular, que es una URI (o ruta) y un método HTTP específico (GET, POST, etc.).


En fastapi, el enrutamiento se define inicializando una instancia de la clase APIRouter y luego definiendo rutas en esa instancia. 

Importamos la clase APIRouter de fastapi y luego inicializamos una instancia de esa clase y la asignamos a una variable llamada router. Luego, definimos rutas en esa instancia con el decorador router.get().

Esto sirve para separar las rutas en diferentes archivos y luego incluirlas en la aplicación principal.
"""