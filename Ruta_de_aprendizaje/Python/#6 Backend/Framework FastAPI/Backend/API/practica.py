from pymongo import MongoClient

"""
>>> NOSQl
# Si eres bueno en algo nunca lo haras gratis.13
>>> N:Not
>>> O:Only
>>> S:SQL
>>> Q:Query
>>> L:Language
"""

# Crea una conexión al cliente con tu instancia de MongoDB
client = MongoClient(
    host="localhost",
    port=27017,
    document_class=dict,
    tz_aware=False,
    connect=True,
)

# Accede a la base de datos 'mydatabase'
db = client["local"]

# Accede a la colección 'mycollection'
# collection = db["users"]

# Inserta un documento en la colección 'mycollection'
# collection.insert_one({"nombre": "daniel"})

"""
El método insert_one() de PyMongo se utiliza para insertar un documento en una colección.
document: Este es el documento que deseas insertar en la colección. No tiene un valor predeterminado ya que debes proporcionar el documento a insertar.

bypass_document_validation: Si es True, permite insertar documentos que no pasan la validación de esquema. Por defecto, es False.

session: Opcional, instancia de la clase ClientSession que se utiliza en caso de que la operación forme parte de una transacción multi-documento. Por defecto, es None.
"""
id = db.carpeta.insert_one(
    bypass_document_validation=False,
    comment=None,
    document={"nombre": "daniel"},
    session=None,
).inserted_id  # {"nombre": "daniel"}

"""
db.list_collection_names(
        comment=None,
        session=None,
        filter="carpeta",
    )
"""
print(db.carpeta.find_one({"_id": id}))
