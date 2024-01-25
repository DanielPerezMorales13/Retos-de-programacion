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

        Persona.__init__(self, nombre, edad, nacionalidad)

        Artista.__init__(self, habilidad)

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


Daniel: object = EmpleadoArtista(
    nombre="Daniel",
    edad=20,
    nacionalidad="Nicaraguense",
    habilidad="Cantar",
    salario=1000000,
    empresa="Google",
)

Danna: object = Artista(habilidad="Programar")

# Para saber si una clase es subclase de otra, podemos usar la funcion issubclass() y pasarle como primer argumento la clase que queremos saber si es subclase de otra y como segundo argumento la clase de la cual queremos saber si es subclase.
"""

>>> herencia = issubclass(clase, clase_de_la_cual_queremos_saber_si_es_subclase)

el valor que nos va a retornar es un booleano, True si es subclase y False si no lo es.
"""

herencia: bool = issubclass(EmpleadoArtista, Persona)
print(
    f"¿Es EmpleadoArtista subclase de Persona?: {'Si' if (herencia == True) else 'No'}"
)

herencia: bool = issubclass(Artista, Persona)
print(f"¿Es Artista subclase de Persona?: {'Si' if (herencia == True) else 'No'}")

# para saber si un objeto es una instancia de una clase, podemos usar la funcion isinstance() y pasarle como primer argumento el objeto que queremos saber si es instancia de una clase y como segundo argumento la clase de la cual queremos saber si es instancia.

"""
ejemplo:
instancia = isinstance(objeto, clase_de_la_cual_queremos_saber_si_es_instancia)
"""

instancia: bool = isinstance(Daniel, EmpleadoArtista)
print(
    f"¿Es Daniel una instancia de EmpleadoArtista?: {'Si' if (instancia == True) else 'No'}"
)
# la razon por la cual Daniel es una instancia de EmpleadoArtista es porque Daniel es un objeto de la clase EmpleadoArtista.

instancia: bool = isinstance(Daniel, Artista)
print(f"¿Es Daniel una instancia de Artista?: {'Si' if (instancia == True) else 'No'}")
# la razon por la cual Daniel es una instancia de Artista es porque la clase EmpleadoArtista hereda los atributos de la clase Artista.

instancia: bool = isinstance(Daniel, Persona)
print(f"¿Es Daniel una instancia de Persona?: {'Si' if (instancia == True) else 'No'}")
# la razon por la cual Daniel es una instancia de Persona es porque la clase EmpleadoArtista hereda los atributos de la clase Persona.

instancia: bool = isinstance(Danna, EmpleadoArtista)
print(
    f"¿Es Danna una instancia de EmpleadoArtista?: {'Si' if (instancia == True) else 'No'}"
)
# la razon por la cual Danna no es una instancia de EmpleadoArtista es porque Danna es un objeto de la clase Artista y la clase Artista no hereda los atributos de la clase EmpleadoArtista.

instancia: bool = isinstance(Danna, Persona)
print(f"¿Es Danna una instancia de Persona?: {'Si' if (instancia == True) else 'No'}")

instancia: bool = isinstance(Danna, Artista)
print(f"¿Es Danna una instancia de Artista?: {'Si' if (instancia == True) else 'No'}")
