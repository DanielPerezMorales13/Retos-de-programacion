class Celular:
    def __init__(self: object, marca: str, modelo: str, camara: str) -> None:
        self.marca: str = marca
        self.modelo: str = modelo
        self.camara: str = camara

    # metodos son acciones que puede realizar un objeto de la clase, por ejemplo, un celular puede llamar, colgar, etc. si esta dentro de una clase, se le llama metodo, si esta fuera de una clase, se le llama funcion.

    # le pasamos self como parametro, porque self hace referencia al objeto que se esta creando, es decir, self es el objeto que se esta creando, y se le asigna los valores que se le pasan al crear el objeto.

    def llamar(self: object) -> None:
        print(f"Llamando desde un {self.marca} {self.modelo}")

    def colgar(self: object) -> None:
        print(f"Colgando {self.marca} {self.modelo}")


celular1: object = Celular(marca="Xiaomi", modelo="Redmi Note 9", camara="64MP")

celular2: object = Celular(marca="Samsung", modelo="Galaxy A51", camara="48MP")

celular1.llamar()
celular1.colgar()

celular2.llamar()
celular2.colgar()
