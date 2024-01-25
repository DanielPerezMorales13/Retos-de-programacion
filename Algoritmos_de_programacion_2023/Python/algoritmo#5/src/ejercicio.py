"""
# 5
ÁREA DE UN POLÍGONO
/*

* Crea una única función (importante que sólo sea una) que sea capaz
* de calcular y retornar el área de un polígono.
* - La función recibirá por parámetro sólo UN polígono a la vez.
* - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
* - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""

import os

"""
Área de un triángulo:
La fórmula general es Área = (base * altura) / 2.

Área de un cuadrado:
La fórmula es Área = lado * lado.

Área de un rectángulo:
La fórmula es Área = longitud * ancho.
"""


def borrar() -> None:
    os.system(command="cls" if os.name == "nt" else "clear")


def main(
    poligono: str,
    base: float = 0,
    altura: float = 0,
    lado: float = 0,
    longitud: float = 0,
    ancho: float = 0,
) -> str:
    match poligono:
        case "1":
            # triangulo
            area: float = base * altura / 2
            return "El area del triangulo es: {variable} metros".format(
                variable=float(area)
            )

        case "2":
            # cuadrado
            area: float = lado * lado
            return "El area del cuadrado es: {variable} metros".format(
                variable=float(area)
            )

        case "3":
            # rectangulo
            area: float = longitud * ancho
            return "El area del rectangulo es: {variable} metros".format(
                variable=float(area)
            )


if __name__ == "__main__":
    while True:
        borrar()
        print(
            """
1. Triangulo
2. Cuadrado
3. Rectangulo

Selecciona el poligono que deseas calcular su area (1, 2, 3)

""",
            end="",
        )
        input_usuario: str = str(input("Seleccione el nombre del poligono: ")).lower()
        match input_usuario:
            case "1":
                while True:
                    try:
                        base_float: float = float(
                            input("Ingrese la base del triangulo: ")
                        )
                        altura_float: float = float(
                            input("Ingrese la altura del triangulo: ")
                        )
                        break
                    except ValueError:
                        print("Ingrese un numero valido")
                        continue
                print(main(poligono=input_usuario, base=base_float, altura=10))

            case "2":
                while True:
                    try:
                        lado_float: float = float(
                            input("Ingrese el lado del cuadrado: ")
                        )
                        break
                    except ValueError:
                        print("Ingrese un numero valido")
                        continue
                print(main(poligono=input_usuario, lado=lado_float))
            case "3":
                while True:
                    try:
                        longitud_float: float = float(
                            input("Ingrese la longitud del rectangulo: ")
                        )
                        ancho_float: float = float(
                            input("Ingrese el ancho del rectangulo: ")
                        )
                        break
                    except ValueError:
                        print("Ingrese un numero valido")
                        continue
                print(
                    main(
                        poligono=input_usuario,
                        longitud=longitud_float,
                        ancho=ancho_float,
                    )
                )
            case _:
                continue
        break
