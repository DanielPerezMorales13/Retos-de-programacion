class Persona:
    def __init__(self: object, nombre: str, edad: int, nacionalidad: str) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.nacionalidad: str = nacionalidad

    def Hablar(self: object) -> str:
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años y soy {self.nacionalidad}"


class Artista:
    def __init__(self: object, habilidad: str) -> None:
        self.habilidad: str = habilidad

    def Mostrar_Habilidad(self: object) -> str:
        return f"Mi habilidad es {self.habilidad}"


class EmpleadoArtista(Persona, Artista):
    def __init__(
        self: object,
        nombre: str,
        edad: int,
        nacionalidad: str,
        habilidad: str,
        salario: float,
        empresa: str,
    ) -> None:
        # En este caso, la clase EmpleadoArtista hereda los atributos de las clases Persona y Artista.

        # pero no podemos usar super().__init__() tenemos que usar el nombre de la clase y pasar los atributos de las clases padre y pasarle el self.

        Persona.__init__(self=self, nombre=nombre, edad=edad, nacionalidad=nacionalidad)

        Artista.__init__(self=self, habilidad=habilidad)

        self.salario: float = salario

        self.empresa: str = empresa

    def presentarse_super(self: object) -> str:
        return f"{super().Mostrar_Habilidad()}"

    # al hacer super().Hablar() estamos accediendo al metodo Hablar de la clase padre no de la clase hija.

    def presentarse_self(self: object) -> str:
        return f"{self.Mostrar_Habilidad()}"

    # y cuando hacemos self.Mostrar_Habilidad() estamos accediendo al metodo Mostrar_Habilidad de la clase hija no de la clase padre.

    def Mostrar_Habilidad(self: object) -> str:
        return "No tengo habilidad"

    # si nosotros creamos un metodo con el mismo nombre de un metodo de una clase padre, el metodo de la clase hija va a tener prioridad.
    def Presentarse_One(self: object) -> str:
        return f"Hola, mi nombre es {self.nombre} y mi habilidad es {self.Mostrar_Habilidad()} y tengo {self.edad} años y soy {self.nacionalidad} y trabajo en {self.empresa} y gano {self.salario}"

    def Presentarse_Two(self: object) -> str:
        return f"Hola, mi nombre es {self.nombre} y {super().Mostrar_Habilidad()} y tengo {self.edad} años y soy {self.nacionalidad} y trabajo en {self.empresa} y gano {self.salario} dolares al mes"


Daniel = EmpleadoArtista(
    nombre="Daniel",
    edad=20,
    nacionalidad="Nicaraguense",
    habilidad="Cantar",
    salario=1000000,
    empresa="Google",
)

# print(Daniel.presentarse_super())
# print(Daniel.presentarse_self())
print(Daniel.Presentarse_Two())
