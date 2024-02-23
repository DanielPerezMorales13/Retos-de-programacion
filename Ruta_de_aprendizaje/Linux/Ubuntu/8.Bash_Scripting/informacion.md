# **_En Bash, puedes declarar una variable de la siguiente manera:_**

_En la consola o terminal:_

```bash
nombre="Daniel Perez"
echo $nombre
```

_En un fichero de script Bash:_

```bash
#!/bin/bash
nombre="Daniel Perez"
echo $nombre
```

- _En el primer ejemplo, simplemente estás declarando una variable en la línea de comandos. En el segundo ejemplo, estás creando un script Bash. La primera línea `#!/bin/bash` es necesaria para indicar que el script debe ejecutarse utilizando Bash. Luego, declaras tu variable y la imprimes._

- _En Bash, los espacios alrededor del operador `=` son significativos. Si pones un espacio antes o después del `=`, Bash interpretará la variable y el valor como dos comandos separados, lo que causará un error._

_Por ejemplo, si intentas hacer esto:_

```bash
nombre = "Daniel Perez"
```

- _Bash interpretará `nombre` como un comando y `="Daniel Perez"` como un argumento para ese comando, lo que probablemente no es lo que quieres._

- _Por lo tanto, siempre debes asegurarte de no tener espacios alrededor del `=` al asignar valores a las variables en Bash. Así es como debería verse:_

```bash
nombre="Daniel Perez"
```

_Para eliminar una variable en Bash, puedes usar el comando `unset`. Aquí te muestro cómo:_

```bash
unset nombre
echo $nombre
```

_Después de ejecutar el comando `unset`, la variable `nombre` ya no existirá, por lo que el comando `echo $nombre` no imprimirá nada._

_Para sumar números en Bash, puedes hacerlo de la siguiente manera:_

_En la consola o terminal:_

```bash
num1=5
```

```bash
num2=10
```

```bash
suma=$((num1 + num2))
```

```bash
echo $suma
```

_En un fichero de script Bash:_

```bash
#!/bin/bash
num1=5
```

```bash
num2=10
```

```bash
suma=$((num1 + num2))
```

```bash
echo $suma
```

> _En ambos casos, se declaran dos variables, `num1` y `num2`, y luego se suman utilizando la sintaxis `$((num1 + num2))`. El resultado se almacena en la variable `suma`, que luego se imprime con `echo`._

El comando `expr` en Linux es una abreviatura de la palabra inglesa "expression". Este comando se utiliza para evaluar expresiones y realizar operaciones como aritmética, comparaciones de cadenas y operaciones de bits.

En español, "expression" se traduce como "expresión". Por lo tanto, `expr` sería una abreviatura de "expresión" en inglés.

_Aquí tienes algunos ejemplos de cómo usar el comando `expr` en Linux:_

- _Operaciones aritméticas:_

_En la consola o terminal:_

```bash
# suma
expr 10 + 3
```

```bash
# Resta
expr 10 - 3
```

```bash
# Multiplicacion
expr 10 \* 5
```

```bash
# Division
expr 10 \/ 5
```

_En un fichero de script Bash:_

```bash
# Suma
echo $(expr 5 + 3)  # Imprime 8
```

```bash
# Resta
echo $(expr 10 - 3)  # Imprime 7
```

```bash
# Division
echo $(expr 10 \/ 2)  # Imprime 5
```

```bash
# **Multiplicacion**
echo $(expr 10 \* 3)  # Imprime 30
```

> _Recuerda que para la multiplicación y las operaciones de bits necesitas escapar los operadores con \ para evitar que sean interpretados por la shell._

_En Linux y en otros sistemas de tipo Unix, múltiples barras inclinadas (`/`) seguidas se tratan como una sola. Esto es parte de la especificación POSIX para rutas de ficheros._

_Por lo tanto, `~/Escritorio///////test` es equivalente a `~/Escritorio/test`. Ambos se refieren al mismo fichero o directorio._

_Esto puede ser útil en situaciones donde estás construyendo rutas de ficheros de manera dinámica, y no tienes que preocuparte si ya hay una barra inclinada al final de una parte de la ruta antes de agregar la siguiente parte._

El comando `tr` en Unix y Linux se utiliza para traducir o eliminar caracteres. Es un comando muy útil para manipular cadenas de texto en la línea de comandos. Aquí tienes algunos ejemplos de cómo puedes usarlo:

**Convertir minúsculas a mayúsculas:**

```bash
echo 'hola mundo' | tr 'a-z' 'A-Z'
```

_Este comando imprimirá 'HOLA MUNDO'._

**Eliminar caracteres:**

```bash
echo 'hola mundo' | tr -d 'o'
```

```bash
echo 'hola mundo' | tr --delete 'o'
```

_Este comando imprimirá 'hla mund'. Ha eliminado todas las ocurrencias de 'o'._

**Sustituir caracteres:**

```bash
echo 'hola mundo' | tr 'o' 'O'
```

_Este comando imprimirá 'hOla mundO'. Ha reemplazado todas las ocurrencias de 'o' por 'O'._

_Traducir espacios en blanco a tabulaciones:_

```bash
echo "hola mundo" | tr ' ' '\t'
```

**Squeeze: reemplaza cada secuencia de entrada de caracteres repetidos que están en SET1 con una sola aparición de ese carácter:**

```bash
echo "hoooola mundo" | tr -s 'o'
```

```bash
echo "hoooola mundo" | tr --squeeze-repeats 'o'
```

_Este comando imprimirá 'hola mundo'. Ha reemplazado todas las secuencias de 'o' repetidas por una sola 'o'._

**Complemento: `-c` o `-C` se usa para tomar el complemento de SET1:**

```bash
echo "hola mundo" | tr -c 'a-z' '*'
```

```bash
echo "hola mundo" | tr -C 'a-z' '*'
```

```bash
echo "hola mundo" | tr --complement 'a-z' '*'
```

*Este comando imprimirá `'**** ****'`. Ha reemplazado todos los caracteres que no son letras minúsculas por '*'.*

*El comando `tr` en Unix y Linux es una utilidad de línea de comandos para traducir o eliminar caracteres. Sin embargo, `tr` no soporta expresiones regulares completas. En su lugar, `tr` opera en listas de caracteres.*

*Por ejemplo, puedes usar `tr` para cambiar todas las letras minúsculas a mayúsculas:*

```bash
echo 'hola mundo' | tr 'a-z' 'A-Z'
```

O para eliminar todos los dígitos de una cadena:

```bash
echo 'hola123' | tr -d '0-9'
```

```bash
echo 'hola123' | tr --delete '0-9'
```

> _Bash es principalmente un lenguaje de scripting de comando que sigue el paradigma de programación imperativa. En este paradigma, los comandos se ejecutan en secuencia, y el estado del programa se modifica a través de la asignación de variables y la ejecución de comandos._

**Aquí están los paradigmas que Bash soporta:**

1. **Imperativo**: *Bash sigue un estilo de programación imperativo donde se da una serie de comandos para cambiar su estado.*

2. **Procedimental**: *Bash permite la definición de funciones, lo que permite la reutilización de código y la estructuración de scripts de manera más modular.*

3.**Comando**: *Bash es un lenguaje de comandos, lo que significa que su principal propósito es ejecutar comandos y manipular su salida.*

- *`#!/bin/bash` es una línea especial que se conoce como shebang o hashbang. Esta línea es la primera en los scripts de Bash y determina el intérprete que se utilizará para ejecutar el script.*

*En este caso, `#!/bin/bash` indica que el script debe ser ejecutado usando Bash, que es un shell de línea de comandos en sistemas Unix y Linux.*

- *Cuando un script con un shebang se ejecuta como un programa (por ejemplo, `./myscript.sh`), el sistema operativo utiliza la ruta especificada después del `#!` para encontrar el intérprete y lo ejecuta pasando el camino del script como argumento.*

- *`$1`: En Bash, `$1` se refiere al primer argumento que se pasa a tu script. Por ejemplo, si ejecutas tu script como `./script.sh miDirectorio`, entonces dentro de tu script, `$1` será `18`.*

*Se utiliza dentro de `[ ]` o `[[ ]]`.*

- *`-eq`: igual a*

- *`-ne`: no igual a*

- *`-gt`: mayor que*

- *`-ge`: mayor o igual a*

- *`-lt`: menor que*

- *`-le`: menor o igual a*

Claro, aquí tienes un ejemplo de cada uno de estos operadores de comparación numérica en Bash:

```bash
# -eq (igual a)
if [ "$1" -eq 10 ]; then
  echo "El primer argumento es igual a 10"
fi
```

```bash
# -eq (igual a)
if [ "$1" -eq 10 ]
then
  echo "El primer argumento es igual a 10"
fi
```

```bash
# -ne (no igual a)
if [ "$1" -ne 10 ]; then
  echo "El primer argumento no es igual a 10"
fi
```

```bash
# -ne (no igual a)
if [ "$1" -ne 10 ]
then
  echo "El primer argumento no es igual a 10"
fi
```

```bash
# -gt (mayor que)
if [ "$1" -gt 10 ]; then
  echo "El primer argumento es mayor que 10"
fi
```

```bash
# -gt (mayor que)
if [ "$1" -gt 10 ]
then
  echo "El primer argumento es mayor que 10"
fi
```

```bash
# -ge (mayor o igual a)
if [ "$1" -ge 10 ]; then
  echo "El primer argumento es mayor o igual a 10"
fi
```

```bash
# -ge (mayor o igual a)
if [ "$1" -ge 10 ]
then
  echo "El primer argumento es mayor o igual a 10"
fi
```

```bash
# -lt (menor que)
if [ "$1" -lt 10 ]; then
  echo "El primer argumento es menor que 10"
fi
```

```bash
# -lt (menor que)
if [ "$1" -lt 10 ]
then
  echo "El primer argumento es menor que 10"
fi
```

```bash
# -le (menor o igual a)
if [ "$1" -le 10 ]; then
  echo "El primer argumento es menor o igual a 10"
fi
```

```bash
# -le (menor o igual a)
if [ "$1" -le 10 ]
then
  echo "El primer argumento es menor o igual a 10"
fi
```

*Estos scripts toman un argumento (`$1`) cuando se ejecutan y lo comparan con el número 10 utilizando diferentes operadores de comparación. Por ejemplo, puedes ejecutar uno de estos scripts con un argumento así: `./script.sh 15`.*

*Esto imprimirá "El primer argumento es igual a 10" si el primer argumento que pasas al script es 10.*

*Recuerda que estos operadores son para comparar números. Si estás comparando cadenas, debes usar `=`, `!=`, `<`, `>`, etc., en lugar de `-eq`, `-ne`, `-lt`, `-gt`, etc.*

*Por ejemplo, si tienes un script llamado `script.sh` con `#!/bin/bash` en la primera línea, cuando ejecutas `./script.sh`, el sistema operativo ejecuta algo como `/bin/bash ./script.sh` internamente.*

- *`[]`: En Bash, `[]` se usa para pruebas condicionales. Por ejemplo, `-d $1` comprueba si `$1` es un directorio, y `-f $name` comprueba si `$name` es un fichero regular.*

- *En Bash, tanto `[]` como `[[]]` se pueden usar para pruebas condicionales con números y cadenas. La diferencia principal entre los dos es que `[[]]` es una característica más nueva que proporciona más funcionalidades y es menos propensa a errores de sintaxis.*

*Para las pruebas numéricas, puedes usar operadores como `-eq`, `-ne`, `-lt`, `-le`, `-gt`, `-ge` dentro de `[]` o `[[]]`.*

*Para las pruebas de cadenas, puedes usar operadores como `=`, `!=`, `<`, `>`, `-n` (cadena no vacía), `-z` (cadena vacía) dentro de `[]` o `[[]]`.*

*El operador `-a` se usa para la conjunción lógica (AND) y `-o` para la disyunción lógica (OR) dentro de `[]`. Por ejemplo:*

```bash
if [ $1 -gt 10 -a $1 -lt 20 ]; then
  echo "El número está entre 10 y 20"
fi
```

```bash
if [ $1 -gt 10 -a $1 -lt 20 ]
then
  echo "El número está entre 10 y 20"
fi
```

Sin embargo, dentro de `[[]]`, debes usar `&&` para AND y `||` para OR:

```bash
if [[ $1 -gt 10 && $1 -lt 20 ]]; then
  echo "El número está entre 10 y 20"
fi
```

```bash
if [[ $1 -gt 10 && $1 -lt 20 ]]
then
  echo "El número está entre 10 y 20"
fi
```

*En general, es recomendable usar `[[]]` en lugar de `[]` en los scripts de Bash debido a su mayor flexibilidad y seguridad.*

*Ejemplos de `if`, `elif`, `else`, `for`, `foreach` (que en Bash se hace con `for`) y `while` en Bash, junto con comentarios explicativos*

- **Ejemplo de if, elif, else**

```bash
if [ "$1" -gt 10 ]; then
  echo "El argumento es mayor que 10"
elif [ "$1" -eq 10 ]; then
  echo "El argumento es igual a 10"
else
  echo "El argumento es menor que 10"
fi
```

```bash
if [ "$1" -gt 10 ]
then
  echo "El argumento es mayor que 10"
elif [ "$1" -eq 10 ]
then
  echo "El argumento es igual a 10"
else
  echo "El argumento es menor que 10"
fi
```

*Este script toma un argumento (`$1`) y verifica si es mayor que, igual a, o menor que 10.*

- **Ejemplo de for**

```bash
for i in 1 2 3 4 5; do
  echo "Número: $i"
done
```

```bash
for i in 1 2 3 4 5
do
  echo "Número: $i"
done
```

*Este script imprime los números del 1 al 5. `for` itera sobre los elementos de la lista (1 2 3 4 5), y para cada iteración, la variable `i` toma el valor del elemento actual.*

- **Ejemplo de foreach (usando for en Bash)**

```bash
for i in $(ls); do
  echo "fichero: $i"
done
```

```bash
for i in $(ls) 
do
  echo "fichero: $i"
done
```

```bash
for i in `ls`; do
  echo "fichero: $i"
done
```

```bash
for i in `ls`
do
  echo "fichero: $i"
done
```

*Este script imprime los nombres de todos los ficheros en el directorio actual. `for` itera sobre la salida del comando `ls`, y para cada iteración, la variable `i` toma el valor del nombre del fichero actual.*

- **Ejemplo de while**

```bash
i=1
while [ $i -le 5 ]; do
  echo "Número: $i"
  ((i++))
done
```

```bash
i=1
while [ $i -le 5 ]
do
  echo "Número: $i"
  ((i++))
done
```

*Este script imprime los números del 1 al 5. El bucle `while` continúa mientras la condición `[ $i -le 5 ]` sea verdadera. Dentro del bucle, se incrementa el valor de `i` en cada iteración con `((i++))`.*

- *`then` y `fi`: Estos son parte de la sintaxis de la declaración `if` en Bash. `then` indica el comienzo del bloque de código que se ejecutará si la condición de la declaración `if` es verdadera, y `fi` indica el final de este bloque.*

- *`do` y `done`: Estos son parte de la sintaxis del bucle `for` en Bash. `do` indica el comienzo del bloque de código que se ejecutará para cada iteración del bucle, y `done` indica el final de este bloque.*

- *`-f`: Cuando se usa con `[ ]` o `[[ ]]`, `-f` comprueba si un fichero existe y es un fichero regular.*

- *`-n` y `-e`: Estas son opciones para el comando `echo`. `-n` evita que `echo` imprima una nueva línea al final de la salida, y `-e` permite la interpretación de caracteres de escape como `\n` para una nueva línea.*

- *`(( ))`: En Bash, `(( ))` se usa para la aritmética de enteros. Por ejemplo, `(( total += $bytes ))` suma el valor de `$bytes` a `total`.*

- *`` `ls $1` ``: Esto ejecuta el comando `ls $1` y sustituye `` `ls $1` `` en el script por su salida. Esto se llama sustitución de comandos. En tu script, `ls $1` lista los ficheros en el directorio especificado por `$1`.*

- *En Bash, `$#` es una variable especial que contiene el número de argumentos que se pasaron al script o a la función.*

  - *Por ejemplo, si ejecutas tu script como `./script.sh arg1 arg2 arg3`, entonces dentro de tu script, `$#` será `3` porque pasaste tres argumentos al script.*

  - *Esto puede ser útil si necesitas realizar diferentes acciones dependiendo del número de argumentos, o si necesitas verificar que se ha proporcionado el número correcto de argumentos.*

> [!IMPORTANT]
> *Bash no tiene un tipado fuerte como otros lenguajes de programación como Python, y no soporta estructuras de datos complejas como listas, diccionarios o tuplas de la misma manera. Sin embargo, Bash tiene arrays y puedes iterar sobre un rango de números usando un bucle `for`. Aquí te dejo algunos ejemplos:*

**Rango en un bucle for:**

```bash
for i in {1..5}; do
  echo "Número: $i"
done
```

```bash
for i in {1..5} 
do
  echo "Número: $i"
done
```

*Esto imprimirá los números del 1 al 5.*

**Array:**

```bash
array=("elemento1" "elemento2" "elemento3")
for i in "${array[@]}"; do
  echo "Elemento: $i"
done
```

```bash
array=("elemento1" "elemento2" "elemento3")
for i in "${array[@]}"
do
  echo "Elemento: $i"
done
```

*En Bash, puedes acceder a un elemento específico de un array utilizando su índice. Los índices en Bash comienzan en 0. Aquí te dejo un ejemplo de cómo puedes hacerlo:*

```bash
array=("elemento1" "elemento2" "elemento3")
```

```bash
# Acceder al primer elemento (índice 0)
echo "Primer elemento: ${array[0]}"
```

```bash
# Acceder al segundo elemento (índice 1)
echo "Segundo elemento: ${array[1]}"
```

```bash
# Acceder al tercer elemento (índice 2)
echo "Tercer elemento: ${array[2]}"
```

*Si quieres iterar sobre los elementos del array junto con sus índices, puedes hacerlo de la siguiente manera:*

```bash
array=("elemento1" "elemento2" "elemento3")
for index in "${!array[@]}"; do
  echo "Elemento en el índice $index: ${array[$index]}"
done
```

*En Bash, puedes crear una lista (array) de números o cadenas de la siguiente manera:*

**Array de números:**

```bash
numeros=(1 2 3 4 5)
for num in "${numeros[@]}"; do
  echo "Número: $num"
done
```

```bash
numeros=(1 2 3 4 5)
for num in "${numeros[@]}"
do
  echo "Número: $num"
done
```

*Esto creará un array con los números del 1 al 5 y luego imprimirá cada número.*

*Si quieres crear un array que contenga tanto números como cadenas, puedes hacerlo de la siguiente manera:*

**Array de números y cadenas:**

```bash
mezcla=(1 "dos" 3 "cuatro" 5)
for elem in "${mezcla[@]}"; do
  echo "Elemento: $elem"
done
```

```bash
mezcla=(1 "dos" 3 "cuatro" 5)
for elem in "${mezcla[@]}"
do
  echo "Elemento: $elem"
done
```

*Esto creará un array con una mezcla de números y cadenas y luego imprimirá cada elemento.*

- *En Bash, `@` y `!` tienen significados especiales cuando se usan con arrays:*

- *`${array[@]}`: Esto se usa para acceder a todos los elementos de un array. Por ejemplo, si tienes un array llamado `array`, puedes usar `${array[@]}` para obtener todos sus elementos.*

- *`${!array[@]}`: Esto se usa para obtener todos los índices de un array. Por ejemplo, si tienes un array llamado `array`, puedes usar `${!array[@]}` para obtener todos sus índices.*

*Aquí tienes un ejemplo de cómo puedes usar ambos en un bucle `for` para imprimir los índices y los elementos de un array:*

```bash
array=("elemento1" "elemento2" "elemento3")
for index in "${!array[@]}"; do
  echo "Índice: $index"
  echo "Elemento: ${array[$index]}"
done
```

```bash
array=("elemento1" "elemento2" "elemento3")
for index in "${!array[@]}"
do
  echo "Índice: $index"
  echo "Elemento: ${array[$index]}"
done
```

*Esto imprimirá el índice y el elemento correspondiente para cada elemento en el array.*

*Si intentas imprimir un array en Bash utilizando `echo $array` o `echo ${array}`, sólo obtendrás el primer elemento del array. Esto se debe a que, en Bash, referirse a un array sin un índice es equivalente a referirse al elemento en el índice 0.*

*Aquí tienes un ejemplo:*

```bash
array=("elemento1" "elemento2" "elemento3")
echo $array  # Imprime: elemento1
```

*Si quieres imprimir todos los elementos de un array, debes usar `${array[@]}` o `${array[*]}`:*

```bash
array=("elemento1" "elemento2" "elemento3")
echo ${array[@]}  # Imprime: elemento1 elemento2 elemento3
```

```bash
array=("elemento1" "elemento2" "elemento3")
echo ${array[*]}  # Imprime: elemento1 elemento2 elemento3
```

*Si quieres imprimir los elementos de un array cada uno en una línea separada, puedes usar un bucle `for`:*

```bash
array=("elemento1" "elemento2" "elemento3")
for elem in "${array[@]}"; do
  echo $elem
done
```

```bash
array=("elemento1" "elemento2" "elemento3")
for elem in "${array[@]}"
do
  echo $elem
done
```

*Esto imprimirá cada elemento del array en su propia línea.*

*En Bash puedes usar `-1` para acceder al último elemento de un array, pero esto sólo funciona en Bash 4.3 y versiones posteriores. Aquí tienes un ejemplo:*

```bash
array=("elemento1" "elemento2" "elemento3")
echo ${array[-1]}  # Imprime: elemento3
```

*Si estás utilizando una versión de Bash anterior a la 4.3, puedes obtener el último elemento de un array utilizando la longitud del array:*

```bash
array=("elemento1" "elemento2" "elemento3")
last_index=$(( ${#array[@]} - 1 ))
echo ${array[$last_index]}  # Imprime: elemento3
```

*La línea `last_index=$(( ${#array[@]} - 1 ))` en Bash está calculando el índice del último elemento de un array. Aquí está lo que hace cada parte:*

- *`last_index=`: Esto asigna el valor de la expresión a la derecha a la variable `last_index`.*

- *`$(( ... ))`: Esto es una construcción de Bash que permite la evaluación de una expresión aritmética. Todo lo que está dentro de `$(( ... ))` se evalúa como una expresión aritmética.*

- *`${#array[@]}`: Esto es una construcción de Bash que obtiene la longitud de un array. `array` es el nombre del array, `@` significa "todos los elementos del array", y `#` antes de un nombre de variable significa "la longitud de". Entonces, `${#array[@]}` significa "la longitud del array".*

- *`- 1`: Esto es una operación aritmética que resta 1 del valor a su izquierda. En este caso, está restando 1 de la longitud del array.*

*Por lo tanto, `last_index=$(( ${#array[@]} - 1 ))` calcula el índice del último elemento del array y asigna ese valor a la variable `last_index`.*

> [!NOTE]
> *Bash no soporta diccionarios hasta la versión 4. Si estás usando Bash 4 o superior, puedes crear y usar diccionarios de la siguiente manera:*

**Diccionario:**

```bash
declare -A diccionario
diccionario=([clave1]="valor1" [clave2]="valor2")
for clave in "${!diccionario[@]}"; do
  echo "Clave: $clave"
  echo "Valor: ${diccionario[$clave]}"
done
```

```bash
declare -A diccionario
diccionario=([clave1]="valor1" [clave2]="valor2")
for clave in "${!diccionario[@]}"
do
  echo "Clave: $clave"
  echo "Valor: ${diccionario[$clave]}"
done
```

*Esto creará un diccionario con dos pares clave-valor y luego imprimirá cada clave y su valor correspondiente.*

- *`declare -A` en Bash se utiliza para declarar una variable como un array asociativo (también conocido como diccionario o mapa hash). Los arrays asociativos son arrays que utilizan cadenas como índices en lugar de números.*

*Aquí tienes un ejemplo de cómo puedes declarar y utilizar un array asociativo en Bash:*

```bash
declare -A animales
animales=(["gato"]="miau" ["perro"]="guau" ["vaca"]="muu")

echo "El gato dice ${animales[gato]}"
echo "El perro dice ${animales[perro]}"
echo "La vaca dice ${animales[vaca]}"
```

*En este ejemplo, `animales` es un array asociativo que mapea nombres de animales a los sonidos que hacen. Puedes acceder a los valores en el array utilizando las claves entre corchetes, como `${animales[gato]}`.*

> *Recuerda que Bash es un lenguaje de scripting orientado a la manipulación de texto y la ejecución de comandos, por lo que no tiene muchas de las características de los lenguajes de programación de propósito general. Si necesitas trabajar con estructuras de datos más complejas, podrías considerar usar un lenguaje como Python en su lugar.*

- *En un script de Bash, `$0` es una variable especial que representa el nombre del script que se está ejecutando.*

*Por ejemplo, si tienes un script llamado `myscript.sh` y lo ejecutas con el comando `./myscript.sh`, dentro del script, `$0` será `./myscript.sh`.*

- *Esto puede ser útil en situaciones donde necesitas mostrar mensajes de error o ayuda que incluyan el nombre del script. Por ejemplo:*

```bash
#!/bin/bash
echo "Este es el script $0"
```

*Cuando ejecutes este script, imprimirá "Este es el script ./myscript.sh" (o cualquier que sea el nombre del script).*

```bash
cadena="S"
if [[ $cadena == [sS] ]]; then
    echo "La cadena contiene (S) os (s) "
fi
```

```bash
cadena="S"
if [[ $cadena == [sS] ]]
then
    echo "La cadena contiene (S) os (s) "
fi
```

- *La expresión `[[ $cadena == [sS] ]]` en Bash es una condición que verifica si la variable `cadena` es igual a "s" o "S". Los corchetes dobles `[[ ]]` se utilizan en Bash para pruebas condicionales avanzadas, incluyendo la comparación de cadenas y patrones.*

  - *La expresión `[sS]` es un patrón que coincide con cualquier carácter que sea "s" o "S". Por lo tanto, `[[ $cadena == [sS] ]]` es verdadero si `cadena` es "s" o "S".*

  - *No puedes usar `[ $cadena == [sS] ]` para lograr lo mismo. Los corchetes simples `[ ]` en Bash son una versión más antigua de las pruebas condicionales y no soportan la comparación de patrones. Si intentas usar `[ $cadena == [sS] ]`, Bash interpretará `[sS]` literalmente como la cadena "[sS]", no como un patrón que coincide con "s" o "S".*

- *Comprobar si una cadena comienza con una letra específica:*

```bash
cadena="Hola mundo"
if [[ $cadena == H* ]]; then
    echo "La cadena comienza con H"
fi
```

```bash
cadena="Hola mundo"
if [[ $cadena == H* ]]
then
    echo "La cadena comienza con H"
fi
```

- *Comprobar si una cadena termina con una letra específica:*

```bash
cadena="Hola mundo"
if [[ $cadena == *o ]]; then
    echo "La cadena termina con o"
fi
```

```bash
cadena="Hola mundo"
if [[ $cadena == *o ]]
then
    echo "La cadena termina con o"
fi
```

- *Comprobar si una cadena contiene solo dígitos:*

```bash
cadena="12345"
if [[ $cadena =~ ^[0-9]+$ ]]; then
    echo "La cadena contiene solo dígitos"
fi
```

```bash
cadena="12345"
if [[ $cadena =~ ^[0-9]+$ ]]
then
    echo "La cadena contiene solo dígitos"
fi
```

- *Comprobar si una cadena contiene solo letras mayúsculas:*

```bash
cadena="HOLA"
if [[ $cadena =~ ^[A-Z]+$ ]]; then
    echo "La cadena contiene solo letras mayúsculas"
fi
```

```bash
cadena="HOLA"
if [[ $cadena =~ ^[A-Z]+$ ]]
then
    echo "La cadena contiene solo letras mayúsculas"
fi
```

- *Comprobar si una cadena contiene solo letras minúsculas:*

```bash
cadena="hola"
if [[ $cadena =~ ^[a-z]+$ ]]; then
    echo "La cadena contiene solo letras minúsculas"
fi
```

```bash
cadena="hola"
if [[ $cadena =~ ^[a-z]+$ ]]
then
    echo "La cadena contiene solo letras minúsculas"
fi
```

- *Comprobar si una cadena contiene una letra:*

```bash
cadena="hola"
if [[ $cadena =~ o ]]; then
    echo "La cadena contiene la letra o"
fi
```

```bash
cadena="hola"
if [[ $cadena =~ o ]]
then
    echo "La cadena contiene la letra o"
fi
```

- **Explicación de cada expresión regular utilizada en los ejemplos:**

1. *La expresión regular en este fragmento de código Bash es `[sS]`. Esta es una clase de caracteres que coincide con cualquier carácter que esté dentro de los corchetes. En este caso, los caracteres son "s" y "S", por lo que `[sS]` coincide con cualquier cadena que sea "s" o "S".*

   - *El código completo verifica si la variable `cadena` es igual a "s" o "S". Si es así, imprime "La cadena contiene (S) o (s)".*

2. *`H*`: Este patrón coincide con cualquier cadena que comienza con "H". El asterisco (`*`) significa "cero o más de lo que precede", por lo que `H*` coincide con "H" seguido de cualquier número de cualquier carácter.*

3. *`*o`: Este patrón coincide con cualquier cadena que termina con "o". De nuevo, el asterisco significa "cero o más de lo que precede", por lo que `*o` coincide con cualquier número de cualquier carácter seguido de "o".*

4. `^[0-9]+$`: Este es un patrón más complejo que utiliza varias partes:
   - *`^` es el inicio de la cadena.*

   - *`[0-9]` es un conjunto de caracteres que coincide con cualquier dígito del 0 al 9.*

   - *`+` significa "uno o más de lo que precede", por lo que `[0-9]+` coincide con uno o más dígitos.*

   - *`$` es el final de la cadena.
   Por lo tanto, `^[0-9]+$` coincide con cualquier cadena que consista únicamente en uno o más dígitos.*

5. *`^[A-Z]+$`: Este patrón es similar al anterior, pero en lugar de dígitos, coincide con letras mayúsculas. `[A-Z]` es un conjunto de caracteres que coincide con cualquier letra mayúscula de la A a la Z.*

6. *`^[a-z]+$`: Este patrón también es similar a los anteriores, pero coincide con letras minúsculas. `[a-z]` es un conjunto de caracteres que coincide con cualquier letra minúscula de la a a la z.*

**`~=` es el operador de coincidencia de patrones en Bash. Se utiliza para comparar una cadena con una expresión regular.**

  *`== *o` y `=~ *o` no son lo mismo en Bash.*

  *`== *o` es una comparación de patrones. Comprueba si la cadena a la izquierda del `==` termina con "o". El asterisco (`*`) aquí actúa como un comodín que puede representar cualquier número de cualquier carácter.*

  *`=~ o*` es una comparación de expresiones regulares. `o*` es una expresión regular válida que coincide con cero o más ocurrencias de "o". En las expresiones regulares, el asterisco (`*`) significa "cero o más de lo que precede". Si quieres comprobar si una cadena contiene "o" una o más veces, podrías usar `=~ o+`.

  **El operador `=~` en Bash permite el uso de varias expresiones regulares, incluyendo:**

   *`^` para el inicio de la cadena.*

   *`$` para el final de la cadena.*

   *`.` para cualquier carácter.*

   *`*` para cero o más de lo que precede.*

   *`+` para uno o más de lo que precede.*

   *`?` para cero o uno de lo que precede.*

   *`[abc]` para cualquier carácter que sea "a", "b" o "c".*

   *`[a-z]` para cualquier carácter que sea una letra minúscula.*

   *`[A-Z]` para cualquier carácter que sea una letra mayúscula.*

   *`[0-9]` para cualquier carácter que sea un dígito.*

   *`(abc|def)` para cualquier cadena que sea "abc" o "def".*

   *`\` para escapar el carácter que sigue, por ejemplo, para buscar literalmente un punto, se usaría `\.`.*

> [!NOTE]
> *La sintaxis correcta para usar el operador `=~` en Bash es sin comillas alrededor de la expresión regular. Si pones comillas alrededor de la expresión regular, Bash la tratará como una cadena literal en lugar de una expresión regular.*

**Recuerda que las expresiones regulares son sensibles a mayúsculas y minúsculas, por lo que debes tener cuidado con eso al escribir tus patrones.**
