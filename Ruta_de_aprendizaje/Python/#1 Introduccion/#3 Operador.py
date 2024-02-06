# Operadores Aritmeticos

# Operaciones con enteros
# Suma
print(3 + 4, end="\n")
# Resta
print(3 - 4, end="\n")
# Multiplicación
print(3 * 4, end="\n")
# División
print(3 / 4, end="\n")
# Módulo
print(10 % 3, end="\n")
# División entera
print(10 // 3, end="\n")
# Potencia el primer número es la base y el segundo el exponente
print(2**3, end="\n")
# Jerarquía de operaciones
print(2**3 + 3 - 7 / 1 // 4, end="\n")

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?", end="\n")
# str() convierte un número a cadena de texto
print("Hola " + str(5), end="\n")

# Operaciones mixtas
# En Python las operaciones se realizan de izquierda a derecha
"""
la multiplicación de cadenas de texto por un número entero
genera una nueva cadena de texto con el contenido repetido
En este caso "Hola " se repite 5 veces
"""
print("Hola " * 5, end="\n")

"""
En este caso "Hola " se repite 2 elevado a 3 veces que es 8
"""
print("Hola " * (2**3), end="\n")

flotante: float = 2.5 * 2
"""
En python no se puede multiplicar una cadena de texto por un número flotante
por eso se convierte a entero
En este caso "Hola " se repite 5 veces
"""
print("Hola " * int(flotante), end="\n")


# Operadores Comparativos

# Operaciones con enteros
"""
El operador de comparación devuelve un booleano
True si la comparación es cierta
False si la comparación es falsa
"""
# > significa mayor que
print(3 > 4, end="\n")  # False
# < significa menor que
print(3 < 4, end="\n")  # True
# >= significa mayor o igual que
print(3 >= 4, end="\n")  # False
# <= significa menor o igual que
print(4 <= 4, end="\n")  # True
# == significa igual que
print(3 == 4, end="\n")  # False
# != significa distinto que
print(3 != 4, end="\n")  # True

# Operaciones con cadenas de texto
"""
En python se pueden comparar cadenas de texto
por orden alfabético por ASCII 
"""

print("Hola" > "Python", end="\n")  # False
print("Hola" < "Python", end="\n")  # True
print("aaaa" >= "abaa", end="\n")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"), end="\n")  # Cuenta caracteres
print("Hola" <= "Python", end="\n")  # False
print("Hola" == "Hola", end="\n")  # True
print("Hola" != "Python", end="\n")  # True

# Operadores Lógicos

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
"""
Los operadores lógicos devuelven un booleano
>>> Los operadores lógicos son and, or, not
>>> and significa y
>>> or significa o
>>> not significa no o negación
"""

# Al usar el operador and si una de las comparaciones es falsa devuelve False
print(3 > 4 and "Hola" > "Python", end="\n")
# Al usar el operador or si una de las comparaciones es verdadera devuelve True
print(3 > 4 or "Hola" > "Python", end="\n")
print(3 < 4 and "Hola" < "Python", end="\n")
print(3 < 4 or "Hola" > "Python", end="\n")
print(3 < 4 or ("Hola" > "Python" and 4 == 4), end="\n")
# Al usar el operador not niega el resultado de la comparación y devuelve el contrario
# True se convierte en False y False se convierte en True
print(not (3 > 4), end="\n")
