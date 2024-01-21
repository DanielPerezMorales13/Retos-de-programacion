```python
# Ejemplo python
"""
>>> Ejemplo
"""
import os

def borrar() -> None: os.system(command="cls" if os.name == "nt" else "clear")

class Autor():
    def __init__(self: object) -> None:
        self.__nombre: str = "Daniel Perez"
        self.__edad: int = 18
        self.__nacionalidad: str = "Nicaraguense"
        self.__habilidad: str "Programar"

    @property
    def habilidad(self: object) -> str:
        return self.__habilidad

    @habilidad.setter
    def habilidad(self: object, nueva_habilidad: str) -> None:
        self.__habilidad: str = nueva_habilidad

    @habilidad.deleter
    def habilidad(self: object) -> None:
        del self.__habilidad

if __name__ == "__main__":
    borrar()
    Danitrix: object = Autor()
    Danitrix.habilidad: str = "Musico"
    print(Danitrix.habilidad)
```

```Java
// Ejemplo Java
Package Carpeta.Mardown;
public class Ejemplo
{
    public Ejemplo()
    {

    }
    public static void main(String[] args)
    {
        System.out.println("Hola esto es un ejemplo");
    }
}
```

```Javascript
// Ejemplo Javascript
console.log("Ejemplo javascript");
```

```Typescript
// Ejemplo Typescript
console.log("Ejemplo Typescript");
```

```C
/* Ejemplo en c*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define NUMERO 13


int main(int argc, char *argv[]) {
    printf("Hola Mundo\n");

    printf("Número de argumentos: %d\n", argc);
    for(short int i = 0; i < argc; i++) {
        printf("Argumento %d: %s\n", i, argv[i]);
    }

    return 0;
}
```