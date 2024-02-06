# Tema: Modulos
# Modules

"""
los módulos son ficheros de python que contienen funciones, variables y clases que pueden ser importadas desde otros ficheros de python para ser usadas en el fichero que lo importa
"""

"""
Estructura de un modulo

>>> from es para importar un modulo 
>>> import es para importar un modulo y se puede usar para importar un modulo especifico de un paquete
>>> as es para renombrar un modulo el cual se puede usar para evitar conflictos de nombres de modulos
"""
import math

# Modulo de python 
from math import pi as PI_VALUE


import modulo

# Modulo propio
from modulo import imprimirValor, sumarValores

# Modulo propio dentro de un paquete o carpeta o directorio
from imports.module import modulo_propio 

# importamos sin usar el from para importar un modulo especifico de un paquete o carpeta o directorio. 
import imports.module.modulo_propio

# Usamos el as para renombrar el modulo porque si no lo renombramos tendremos que usar el nombre completo del modulo para usarlo y eso no es muy practico
import imports.module.modulo_propio as modulo_propio

# Importamos una funcion especifica de un modulo propio dentro de un paquete o carpeta o directorio
from imports.module.modulo_propio import idValor
from imports.module.modulo_propio import idValor as idValorModuloPropio

from imports.module.functions import modulo_funciones
from imports.module.functions import modulo_funciones as modulo_funciones_renombrado
import imports.module.functions.modulo_funciones
import imports.module.functions.modulo_funciones as ModuloFunciones
from imports.module.functions.modulo_funciones import TipoDato
from imports.module.functions.modulo_funciones import TipoDato as TipoDatoModuloFunciones




modulo.sumarValores(numeroUno=5, numeroDos=3, numeroTres=1)
modulo.imprimirValor(valor="Hola Python!")

modulo.sumarValores(numeroUno=5, numeroDos=3.2, numeroTres=11)
imprimirValor(valor="Rust")

# El metodo pi() del modulo math nos retorna el valor de pi
print(math.pi, end="\n")
# El metodo pow() del modulo math nos retorna el valor de 2 elevado a 8
print(math.pow(2, 8), end="\n")


print(PI_VALUE, end="\n")

edad: int = 18
# manera de importar un modulo propio dentro de un paquete o carpeta o directorio.

print(idValor(valor=edad), end="\n")
print(idValorModuloPropio(valor=edad), end="\n")

print(modulo_funciones.TipoDato(dato=edad), end="\n")
print(imports.module.functions.modulo_funciones.TipoDato(dato=edad), end="\n")
print(TipoDatoModuloFunciones(dato=edad), end="\n") 



# Cuando importamos un modulo propio y ejecutamos el fichero que lo  esta importando se crea un carpeta __pycache__ la cual contiene un fichero .pyc el cual es un fichero compilado del modulo que importamos