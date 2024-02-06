"""
#03
ESTRUCTURAS DE DATOS
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
"""

import os

# Estructura de datos
# Lista
lista: list[int] = [1, 2, 3, 4, 5]
print(lista)

# Tupla
tupla: tuple[int, str, bool] = (1, "Hola", True)
print(tupla)

# Diccionario
diccionario: dict[int, str] = {1: "Hola", 2: "Mundo"}
print(diccionario)

# Conjunto
conjunto: set[int] = {1, 2, 3, 4, 5}
print(conjunto)

# Operaciones de inserción, borrado, actualización y ordenación.
# Lista
# Inserción
lista.append(6)
# Borrado
lista.pop()
# Actualización
lista[0] = 0
# Ordenación
lista.sort()

# las tuplas no se pueden modificar
# Diccionario
# Inserción
diccionario[3] = "!"
# Borrado
diccionario.pop(2)
# Actualización
diccionario[1] = "Adios"

# Conjunto
# Inserción
conjunto.add(6)
# Borrado
conjunto.pop()
# Actualización
conjunto.add(0)


# Ejericio Agenda de contactos

lista_contactos: list[str] = list()
lista_numeros: list[int] = list()
while True:
    str(input("Presione una tecla para continuar..."))
    while True:
        os.system(command="clear" if os.name == "posix" else "cls")
        print(
            """
        Bienvenido a la agenda de contactos
        1. Buscar contacto
        2. Insertar contacto
        3. Actualizar contacto
        4. Eliminar contacto
        5. Salir
        """,
            end="\n",
        )
        opcion: str = str(input("Ingrese una opción: "))
        if (
            opcion == "1"
            or opcion == "2"
            or opcion == "3"
            or opcion == "4"
            or opcion == "5"
        ):
            os.system(command="clear" if os.name == "posix" else "cls")
            break
        else:
            print("Opción inválida", end="\n")
            str(input("Presione una tecla para continuar..."))
            continue

    match opcion:
        case "1":
            if len(lista_contactos) == 0:
                print("No hay contactos", end="\n")
                continue
            print("Buscar contacto")
            buscar_contacto: str = str(
                input("Ingrese el nombre del contacto a buscar: ")
            ).capitalize()
            if buscar_contacto in lista_contactos:
                indice: int = lista_contactos.index(buscar_contacto)
                print(f"El contacto {lista_contactos[indice]} existe", end="\n")
                print(f"Su número es {lista_numeros[indice]}", end="\n")
            else:
                print(f"El contacto {buscar_contacto} no existe", end="\n")
            continue
        case "2":
            print("Insertar contacto", end="\n")
            añadir_nombre_contacto: str = str(input("Ingrese el nombre: ")).capitalize()
            while True:
                try:
                    añadir_numero_contacto: int = int(input("Ingrese el número: "))
                    if len(str(añadir_numero_contacto)) == 11:
                        lista_contactos.append(añadir_nombre_contacto)
                        lista_numeros.append(añadir_numero_contacto)
                        break
                    else:
                        print("El número debe tener 11 dígitos", end="\n")
                        continue
                except ValueError:
                    print("El número debe ser un entero", end="\n")
                    continue
        case "3":
            if len(lista_contactos) == 0:
                print("No hay contactos", end="\n")
                continue
            print("Actualizar contacto", end="\n")
            actualizar_contacto: str = str(
                input("Ingrese el nombre que quiere actualizar: ")
            ).capitalize()
            if actualizar_contacto in lista_contactos:
                indice: int = lista_contactos.index(actualizar_contacto)
                nuevo_nombre: str = str(input("Ingrese el nuevo nombre: ")).capitalize()
                nuevo_numero: int = int(input("Ingrese el nuevo número: "))
                lista_contactos[indice] = nuevo_nombre
                lista_numeros[indice] = nuevo_numero
            else:
                print(f"El contacto {actualizar_contacto} no existe", end="\n")
            continue

        case "4":
            if len(lista_contactos) == 0:
                print("No hay contactos", end="\n")
                continue
            print("Eliminar contacto")
            contacto: str = str(
                input("Ingrese el nombre del contacto a eliminar: ")
            ).capitalize()
            eliminar_contacto: str = str(
                input("Ingrese el nombre que quiere eliminar: ")
            ).capitalize()
            if eliminar_contacto in lista_contactos:
                lista_contactos.remove(eliminar_contacto)
            else:
                print(f"El contacto {eliminar_contacto} no existe", end="\n")
            continue
        case "5":
            print("Salir", end="")
            exit(code=0)
