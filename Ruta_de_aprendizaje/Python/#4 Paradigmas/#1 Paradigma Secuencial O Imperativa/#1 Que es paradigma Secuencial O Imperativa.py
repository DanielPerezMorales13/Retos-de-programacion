"""
El paradigma secuencial o imperativo es el paradigma de programación más antiguo y más utilizado.
En este paradigma, el programador escribe instrucciones que describen los pasos que el programa debe seguir para alcanzar un estado deseado.
El programa se ejecuta siguiendo exactamente los pasos descritos.
"""

# Ejemplo de paradigma secuencial o imperativo

# El juego de la serpiente snake

import os
import random

import readchar

# * Constantes que se usaran para el tamaño del mapa
ALTO: int = 15
ANCHO: int = 20
POS_X: int = 0
POS_Y: int = 1
TECHO: str = "-" * (3 * ANCHO + 2)
tamaño_cola: int = 0
cola: list[list[int]] = list()
mi_posicion: list[int] = [random.randint(0, ANCHO - 1), random.randint(0, ALTO - 1)]
comida: list[list[int]] = list()
while True:
    if mi_posicion in cola:
        exit(code="Haz chocado con tu cola")
    while len(comida) <= 10:
        posicion_comida: list[int] = [
            random.randint(a=0, b=ANCHO - 1),
            random.randint(a=0, b=ALTO - 1),
        ]
        if posicion_comida not in comida and posicion_comida != mi_posicion:
            comida.append(posicion_comida)
        else:
            continue
    os.system(command="cls" if os.name == "nt" else "clear")
    print(TECHO, end="\n")
    for cordenada_y in range(0, ALTO, 1):
        print("|", end="")
        for cordenada_x in range(0, ANCHO, 1):
            caracter: str = "   "
            for alimento in comida:
                if alimento[POS_Y] == cordenada_y and alimento[POS_X] == cordenada_x:
                    caracter = " * "
            for la_cola in cola:
                if la_cola[POS_Y] == cordenada_y and la_cola[POS_X] == cordenada_x:
                    caracter = " @ "
            if mi_posicion[POS_Y] == cordenada_y and mi_posicion[POS_X] == cordenada_x:
                caracter = " @ "
                if mi_posicion in comida:
                    comida.remove(mi_posicion)
                    tamaño_cola += 1
            print(f"{caracter}", end="")
        else:
            print("|", end="\n")
    else:
        print(TECHO, end="\n")
        print(f"comida {tamaño_cola}")
    movimiento: str = readchar.readchar().lower()
    if movimiento == "w":
        cola.insert(0, mi_posicion.copy())
        cola = cola[:tamaño_cola]
        mi_posicion[POS_Y] -= 1
        if mi_posicion[POS_Y] == -1:
            mi_posicion[POS_Y] = 14
    elif movimiento == "s":
        cola.insert(0, mi_posicion.copy())
        cola = cola[:tamaño_cola]
        mi_posicion[POS_Y] += 1
        if mi_posicion[POS_Y] == 15:
            mi_posicion[POS_Y] = 0
    elif movimiento == "a":
        cola.insert(0, mi_posicion.copy())
        cola = cola[:tamaño_cola]
        mi_posicion[POS_X] -= 1
        if mi_posicion[POS_X] == -1:
            mi_posicion[POS_X] = 19
    elif movimiento == "d":
        cola.insert(0, mi_posicion.copy())
        cola = cola[:tamaño_cola]
        mi_posicion[POS_X] += 1
        if mi_posicion[POS_X] == 20:
            mi_posicion[POS_X] = 0
    elif movimiento == "q":
        exit(code="Haz salido del juego")
