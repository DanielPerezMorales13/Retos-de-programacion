**Profundizando en la terminal y comandos avanzados**

**`Indice`**

- [**_Comandos avanzados_**](#comandos-avanzados)
- [**_Enlaces Simbolicos en directorios_**](#enlaces-simbolicos-en-directorios)
- [**_Permisos en directorios en Linux_**](#permisos-en-directorios-en-linux)
- [**_Redirecciones y tuberías en Linux_**](#redirecciones-y-tuberías-en-linux)

---

# **_Comandos avanzados_**

`find`

_El comando find se utiliza para buscar ficheros y directorios en el sistema de ficheros._

```bash
find /ruta/a/buscar -name "patrón"
```

El comando `find` en Linux es una herramienta poderosa para buscar ficheros y directorios. Aunque `find` no soporta directamente las expresiones regulares completas, puedes usar una funcionalidad similar con los comodines y la opción `-regex`. Aquí tienes algunos ejemplos:

-. **Buscar todos los ficheros `.py` en el directorio actual y en los subdirectorios**:

```bash
find ./ -name "*.py"
```

-. **Buscar todos los ficheros que comienzan con `file` en el directorio actual y en los subdirectorios**:

```bash
find ./ -name "file*"
```

-. **Usar `-regex` para buscar ficheros que coincidan con una expresión regular**. Por ejemplo, para buscar todos los ficheros `.py` o `.csv`:

```bash
find ./ -regex ".*\.\(py\|csv\)$"
```

-. **Buscar todos los ficheros que no coincidan con una expresión regular**. Por ejemplo, para buscar todos los ficheros que no son `.py` o `.csv`:

```bash
find ./ -not -regex ".*\.\(py\|csv\)$"
```

-. **Buscar todos los directorios que coincidan con una expresión regular**.

- _En el comando `find . -type d -name "dir_"`, las opciones `-type`y`-d` se utilizan para especificar el tipo de fichero que estás buscando.\*

- `-type`: Esta opción se utiliza para especificar el tipo de fichero que estás buscando. Puedes buscar varios tipos de ficheros, incluyendo ficheros regulares (`f`), directorios (`d`), enlaces simbólicos (`l`), y otros.

- `d`: Este es el argumento que se pasa a la opción `-type` para especificar que estás buscando directorios. Por lo tanto, `-type d` significa "buscar directorios".

- _Por lo tanto, el comando `find . -type d -name "dir_"` buscará todos los directorios cuyo nombre comienza con "dir" en el directorio actual y en todos sus subdirectorios.\*

```bash
find ./ -type d -name "dir*"
```

```bash
`man find`
```

- _`grep`_

_El comando grep se utiliza para buscar patrones de texto en ficheros._

```bash
grep "patrón" fichero
```

- _grep con Expresiones Regulares_

  - ```bash
    grep -E "expresión_regular" fichero
    ```

  - _`-E` y `--extended-regexp`_

  - _`-E`: Esta opción se utiliza con el comando `grep` y permite interpretar el patrón de búsqueda como una expresión regular extendida._

  - _`--extended-regexp`: Forma no abreviada de `-E`._

  - _Por ejemplo, para buscar una expresión regular extendida con `grep`, puedes usar:_

  - ```bash
    grep -E "patrón_de_expresión_regular" fichero
    ```

  - _Lo cual es equivalente a:_

  - ```bash
    grep --extended-regexp "patrón_de_expresión_regular" fichero
    ```

  - > [!IMPORTANT]
  - > _Cuando usas la opción -E con grep, estás indicando que deseas que grep interprete la expresión regular como una expresión regular extendida, lo que significa que no necesitas escapar los caracteres especiales como {} para que se interpreten correctamente como cuantificadores._

- _grep sin Expresiones Regulares_

  - ```bash
     grep -F "cadena_de_texto" fichero
    ```

  - _`-F` y `--fixed-strings`_

  - _`-F`: Esta opción se utiliza con el comando `grep` y especifica que el patrón de búsqueda es una cadena de texto literal, no una expresión regular._

  - `--fixed-strings`: Forma no abreviada de `-F`.

  - _Por ejemplo, para buscar una cadena de texto literal con `grep`, puedes usar:_

  - ```bash
     grep -F "cadena_de_texto" fichero
    ```

  - _Lo cual es equivalente a:_

  - ```bash
     grep --fixed-strings "cadena_de_texto" fichero
    ```

- **Instalación de tree**

_tree es una herramienta que muestra la estructura de directorios como un árbol._

```bash
sudo apt-get update
```

```bash
sudo apt-get install tree
```

- _Copiar directorios con el mismo nombre y sin el mismo nombre_

Para copiar un directorio manteniendo el mismo nombre en el destino, puedes usar el comando `cp` con la opción `-r` `--recursive` (para copiar recursivamente):

```bash
cp -r directorio_origen directorio_destino
```

```bash
cp --recursive directorio_origen directorio_destino
```

_Si deseas copiar un directorio pero renombrarlo en el destino, simplemente especifica un nuevo nombre para el directorio de destino:_

```bash
cp -r directorio_origen nuevo_nombre_directorio_destino
```

```bash
cp --recursive directorio_origen nuevo_nombre_directorio_destino
```

Esto copiará el contenido del directorio de origen en un nuevo directorio con el nombre especificado en el destino.

_Las expresiones regulares son patrones utilizados para buscar y coincidir con cadenas de texto en un fichero o en la salida de un comando en Linux. Aquí tienes algunos ejemplos de expresiones regulares que puedes utilizar con el comando `grep`:_

1. **Coincidir una palabra específica:**

   ```bash
   grep "palabra" fichero.py
   ```

2. **Coincidir una palabra al principio de la línea:**

   ```bash
   grep "^palabra" fichero.py
   ```

3. **Coincidir una palabra al final de la línea:**

   ```bash
   grep "palabra$" fichero.py
   ```

4. **Coincidir una palabra al principio o al final de la línea:**

   1. ```bash
       grep "^PalabraInicio$\|^FinPalabra$" fichero.py
      ```

      - ```bash
        grep -E "^PalabraInicio$\|^FinPalabra$" fichero.py
        ```

      - ```bash
        grep --extended-regexp "^PalabraInicio$\|^FinPalabra$" fichero.py
        ```

   2. ```bash
       grep "^PalabraInicio\|^FinPalabra$" fichero.py
      ```

      - ```bash
        grep -E "^PalabraInicio\|^FinPalabra$" fichero.py
        ```

      - ```bash
        grep --extended-regexp "^PalabraInicio\|^FinPalabra$" fichero.py
        ```

   3. ```bash
      grep "PalabraInicio$\|^FinPalabra$" fichero.py
      ```

      - ```bash
        grep -E "PalabraInicio$\|^FinPalabra$" fichero.py
        ```

      - ```bash
        grep --extended-regexp "PalabraInicio$\|^FinPalabra$" fichero.py
        ```

   4. ```bash
      grep "^PalabraInicio\|FinPalabra$" fichero.py
      ```

      - ```bash
         grep -E "^PalabraInicio\|FinPalabra$" fichero.py
        ```

      - ```bash
        grep --extended-regexp "^PalabraInicio\|FinPalabra$" fichero.py
        ```

   5. ```bash
      grep "^PalabraInicio\|^FinPalabra" fichero.py
      ```

      - ```bash
        grep -E "^PalabraInicio\|^FinPalabra" fichero.py
        ```

      - ```bash
        grep --extended-regexp "^PalabraInicio\|^FinPalabra" fichero.py
        ```

   6. ```bash
      grep "PalabraInicio$\|FinPalabra$" fichero.py
      ```

      - ```bash
        grep -E "PalabraInicio$\|FinPalabra$" fichero.py
        ```

      - ```bash
        grep --extended-regexp "PalabraInicio$\|FinPalabra$" fichero.py
        ```

5. **Coincidir una palabra ignorando mayúsculas y minúsculas:**

   ```bash
   grep -i "palabra" fichero.py
   ```

   ```bash
   grep --ignore-case "palabra" fichero.py
   ```

6. **Coincidir una palabra precedida por un cierto número de caracteres:**

   ```bash
   grep -E ".{5}palabra" fichero.py
   ```

   ```bash
   grep --extended-regexp ".{5}palabra" fichero.py
   ```

   ```bash
   grep ".\{5\}palabra" fichero.py
   ```

7. **Coincidir una palabra seguida por un cierto número de caracteres:**

   ```bash
   grep -E "palabra.{5}" fichero.py
   ```

   ```bash
   grep --extended-regexp "palabra.{5}" fichero.py
   ```

   ```bash
   grep "palabra.\{5\}" fichero.py
   ```

8. **Coincidir una palabra con una longitud específica:**

   ```bash
   grep -E "^.{5}$" fichero.py
   ```

   ```bash
   grep --extended-regexp "^.{5}$" fichero.py
   ```

   ```bash
   grep "^.\{5\}$" fichero.py
   ```

9. **Coincidir una palabra que comience con ciertos caracteres:**

   ```bash
   grep -E "^prefix.*" fichero.py
   ```

   ```bash
   grep --extended-regexp "^prefix.*" fichero.py
   ```

   ```bash
   grep "^prefix.*" fichero.py
   ```

10. **Coincidir una palabra que termine con ciertos caracteres:**

    ```bash
    grep -E ".*suffix$" fichero.py
    ```

    ```bash
    grep --extended-regexp ".*suffix$" fichero.py
    ```

    ```bash
    grep ".*suffix$" fichero.py
    ```

_Explicacion de cada uno de los caracteres y construcciones en el contexto de las expresiones regulares:_

1. _`|`: El símbolo `|` se utiliza en expresiones regulares para denotar una "alternativa". Por ejemplo, la expresión regular `a|b` coincidirá con cualquier cadena que contenga la letra "a" o la letra "b"._

2. _`.`: El punto (`.`) se utiliza en expresiones regulares para representar cualquier carácter individual. Por ejemplo, la expresión regular `a.c` coincidirá con cualquier cadena que contenga una "a", seguida de cualquier carácter, seguida de una "c"._

3. _`_`: El asterisco (`_`) se utiliza en expresiones regulares como un "cuantificador", que significa "cero o más repeticiones del elemento anterior". Por ejemplo, la expresión regular `a_` coincidirá con cualquier cadena que contenga cero o más "a".\*

4. _`\`: La barra invertida (`\`) se utiliza en expresiones regulares para "escapar" caracteres especiales, permitiendo que se interpreten literalmente. Por ejemplo, `\.`, `\\`, y `\(` coincidirán literalmente con un punto, una barra invertida y un paréntesis de apertura, respectivamente._

5. _`{}`: Las llaves (`{}`) se utilizan en expresiones regulares para cuantificar la cantidad de repeticiones de un elemento anterior. Por ejemplo, la expresión regular `a{3}` coincidirá con exactamente tres "a" consecutivas._

6. _`^`: El acento circunflejo (`^`) se utiliza en expresiones regulares para anclar la coincidencia al principio de una línea. Por ejemplo, la expresión regular `^inicio` coincidirá con "inicio" solo si aparece al principio de una línea._

7. _`$`: El signo de dólar (`$`) se utiliza en expresiones regulares para anclar la coincidencia al final de una línea. Por ejemplo, la expresión regular `final$` coincidirá con "final" solo si aparece al final de una línea._

---

# **_Enlaces Simbolicos en directorios_**

---

# **_Permisos en directorios en Linux_**

> _En Linux, los permisos de los ficheros y directorios determinan quién puede leer, escribir o ejecutar ciertos ficheros o directorios._

- **\*Lectura (r)**: Permite abrir y leer un fichero o directorio.\*
- **\*Escritura (w)**: Permite modificar un fichero o directorio.\*
- **\*Ejecución (x)**: Permite ejecutar un fichero o acceder a un directorio.\*

- **Comandos que no se pueden ejecutar sin permisos**

> _Si no tienes los permisos adecuados para un fichero o directorio, hay ciertos comandos que no podrás ejecutar. Aquí hay algunos ejemplos:_

- _`cat`, `ls`, `less`, `more`: Estos comandos no se pueden ejecutar en un fichero si no tienes **permisos de lectura** para ese fichero._

  - _`less` y `more` son comandos de paginación en Unix y sistemas similares a Unix que se utilizan para ver el contenido de ficheros de texto en la terminal._

    - **less**: Este comando proporciona una interfaz para desplazarse hacia adelante y hacia atrás en el fichero de texto. También permite buscar texto dentro del fichero. A diferencia de otros comandos de visualización, `less` no tiene que leer todo el fichero antes de empezar a mostrarlo, lo que puede ser más rápido para ficheros grandes. El nombre `less` es un juego de palabras, ya que su funcionalidad es más (en inglés, "more") que la del comando `more`.

      - ```bash
        # Ver el contenido de un fichero con less
        less fichero.py
        ```

    - **more**: Este comando también muestra el contenido de ficheros de texto en la terminal, pero solo permite desplazarse hacia adelante en el fichero, no hacia atrás. Aunque `more` tiene menos funcionalidades que `less`, puede ser suficiente para visualizar ficheros de texto que solo requieren un desplazamiento hacia adelante.

    - ```bash
      # Ver el contenido de un fichero con more
      more fichero.py
      ```

    - **En ambos casos, puedes salir de la vista del fichero presionando `q`.**

_- `touch`: Estos comandos no se pueden usar para escribir en un fichero si no tienes **permisos de escritura** para ese fichero._

_- `cd`: No puedes cambiar a un directorio si no tienes **permisos de ejecución** para ese directorio._

_- `./`: No puedes ejecutar un fichero si no tienes **permisos de ejecución** para ese fichero._

---

# **_Redirecciones y tuberías en Linux_**

> _En Linux, las redirecciones y las tuberías son formas de manejar los flujos de datos entre programas y ficheros._

- **Standard Input (stdin), Standard Output (stdout), Standard Error (stderr)**

- **\*Standard Input (stdin)**: Es el flujo de datos que se envía a un programa. Por defecto, este es el teclado. Su descriptor de fichero es 0.\*

- **\*Standard Output (stdout)**: Es el flujo de datos que un programa envía cuando se ejecuta correctamente. Por defecto, este es la terminal. Su descriptor de fichero es 1.\*

- **\*Standard Error (stderr)**: Es el flujo de datos que un programa envía cuando encuentra un error. Por defecto, este también es la terminal. Su descriptor de fichero es 2.\*

- **Redirecciones**

> _Las redirecciones te permiten cambiar de dónde proviene el stdin o a dónde va el stdout o stderr._

- _`>`: Redirige el stdout a un fichero. Si el fichero ya existe, lo sobrescribe._

- _`<`: Toma el stdin de un fichero en lugar del teclado._

- _`2>`: Redirige el stderr a un fichero._

```bash
# Ejemplo de redirección de stdout
ls -l > output.py
```

```bash
# Ejemplo de redirección de stdin
sort < input.py
```

```bash
# Ejemplo de redirección de stderr
ls ./NoExiste 2> error.py
```

**_Tuberías (Pipes)_**

> _Las tuberías te permiten tomar el stdout de un programa y usarlo como stdin para otro programa._

- _`|`: Toma el stdout del comando a la izquierda y lo usa como stdin para el comando a la derecha._

```bash
# Ejemplo de tubería
ls -l | grep ".py"
```

**_Comandos_**

1. _El comando `tail` se utiliza para mostrar las últimas líneas de un fichero o de un flujo de entrada. La opción `--lines` o su forma abreviada `-n` se utiliza para especificar el número de líneas a mostrar._

   - ```bash
      ls -l | tail --lines=+2
     ```

     - _`ls -l | tail --lines=+2`: Este comando muestra todas las líneas del output de `ls -l` a partir de la línea 2. El `+` antes del número indica que `tail` debe empezar a mostrar las líneas a partir de la línea 2._

   - ```bash
      ls -l | tail --lines=-2
     ```

     - _`ls -l | tail --lines=-2`: Este comando muestra las últimas dos líneas del output de `ls -l`. El `-` antes del número indica que `tail` debe mostrar las últimas n líneas._

   - ```bash
      ls -l | tail --lines=-2
     ```

     - _`ls -l | tail --lines=2`: Este comando es equivalente al anterior. Si no se especifica un signo antes del número, `tail` asume que debe mostrar las últimas n líneas._

   - _La forma abreviada de `--lines` es `-n`._

     - `ls -l | tail -n +2`

       - ```bash
         ls -l | tail -n +2
         ```

     - `ls -l | tail -n -2`

       - ```bash
         ls -l | tail -n -2
         ```

     - `ls -l | tail -n 2`

       - ```bash
         ls -l | tail -n 2
         ```

2. _El comando `head` se utiliza para mostrar las primeras líneas de un fichero o de un flujo de entrada. La opción `--lines` o su forma abreviada `-n` se utiliza para especificar el número de líneas a mostrar._

   - ```bash
      ls -l | head --lines=+2
     ```

     - _`ls -l | head --lines=+2`: Este comando muestra las lineas establecidas en `--lines=` del output de `ls -l`. El `+` antes del número indica que `head` debe empezar a mostrar las líneas a partir de la línea 2._

   - ```bash
      ls -l | head --lines=-2
     ```

     - _`ls -l | head --lines=-2`: Este comando muestra todas las líneas del output de ls -l excepto el numero de lineas dados._

   - ```bash
      ls -l | head --lines=2
     ```

     - _`ls -l | head --lines=2`: Este comando muestra las lineas establecidas en `--lines=` del output de `ls -l`. Si no se especifica un signo antes del número, `head` asume que debe mostrar las primeras n líneas._

   - _La forma abreviada de `--lines` es `-n`._

     - `ls -l | head -n +2`

       - ```bash
         ls -l | head -n +2
         ```

     - `ls -l | head -n -2`

       - ```bash
         ls -l | head -n -2
         ```

     - `ls -l | head -n 2`

       - ```bash
         ls -l | head -n 2
         ```

3. _sed es un acrónimo de "stream editor" en inglés._

- _"Stream" se refiere a un flujo de datos._

- _"Editor" se refiere a un programa que permite modificar esos datos._

- _Por lo tanto, sed es un programa que permite modificar flujos de datos._

- _En español, sed podría traducirse como "editor de flujo"._

- _El comando `sed` es un editor de flujo que puede realizar transformaciones de texto._

```bash
sed "s/  */ /g"
```

- _`s`: Es el comando de sustitución. Le dice a `sed` que vas a reemplazar texto._

- `/ */ /`: Es el patrón de sustitución. El primer espacio entre las primeras dos barras / es el texto que quieres reemplazar. El espacio entre las últimas dos barras / es el texto por el que quieres reemplazarlo. El `*` significa "cero o más del carácter anterior", por lo que `*` coincide con uno o más espacios.\*

- _`g`: Es una bandera que le dice a `sed` que realice la sustitución globalmente en cada línea, en lugar de solo la primera coincidencia._

_Por lo tanto, sed `"s/ _/ /g"` reemplaza todas las secuencias de uno o más espacios en cada línea con un solo espacio.\*

1. **\*Sustitución**: El uso más común de `sed` es para la sustitución, utilizando el comando `s`.\*

   ```bash
   echo "Hello, world!" | sed 's/world/universe/'
   ```

   _Este comando reemplaza la primera ocurrencia de "world" por "universe" en cada línea._

2. **\*Sustitución global**: Puedes hacer que `sed` reemplace todas las ocurrencias en una línea (en lugar de solo la primera) añadiendo `g` al final del comando de sustitución.\*

   ```bash
   echo "Hello, world! Goodbye, world!" | sed 's/world/universe/g'
   ```

   _Este comando reemplaza todas las ocurrencias de "world" por "universe"._

3. **\*Borrado de líneas**: Puedes usar `sed` para borrar líneas que coincidan con un patrón específico utilizando el comando `d`.\*

   ```bash
   echo -e 'Hello, world!\nGoodbye, world!' | sed '/Goodbye/d'
   ```

   _Este comando borra todas las líneas que contienen "Goodbye"._

4. **\*Inserción y añadido de líneas**: `sed` puede insertar una nueva línea antes de un patrón con el comando `i` o después de un patrón con el comando `a`.\*

   ```bash
   echo -e 'Hello, world!\nGoodbye, world!' | sed '/Goodbye/i Farewell, universe!'
   ```

   _Este comando inserta "Farewell, universe!" antes de cada línea que contiene "Goodbye"._

- _En `sed`, las opciones `s`, `g`, `i`, y `d` tienen los siguientes significados:_

- _`s`: Es el comando de sustitución. Se utiliza para reemplazar un patrón de texto por otro. Por ejemplo, `s/foo/bar/` reemplaza la primera ocurrencia de "foo" por "bar" en cada línea._

- _`g`: Es una bandera que se utiliza con el comando de sustitución `s` para indicar que la sustitución debe ser global, es decir, que debe reemplazar todas las ocurrencias del patrón en cada línea, no solo la primera. Por ejemplo, `s/foo/bar/g` reemplaza todas las ocurrencias de "foo" por "bar" en cada línea._

- _`i`: Es el comando de inserción. Se utiliza para insertar texto antes de una línea que coincide con un patrón específico. Por ejemplo, `/foo/i bar` inserta "bar" antes de cada línea que contiene "foo"._

- _`d`: Es el comando de eliminación. Se utiliza para eliminar líneas que coinciden con un patrón específico. Por ejemplo, `/foo/d` elimina todas las líneas que contienen "foo"._

- _La opción `-e` en el comando `echo` permite el reconocimiento de los caracteres de escape precedidos por barras invertidas (`\`)._

_Los caracteres de escape son caracteres que invocan una acción alternativa al comportamiento normal._

- _`\n`: Nueva línea_
- _`\t`: Tabulación_
- _`\r`: Retorno de carro_
- _`\\`: Barra invertida_
- _`\b`: Retroceso_

- _Por ejemplo, si quieres imprimir dos líneas de texto, puedes usar `\n` para insertar un salto de línea:_

```bash
echo -e "Hello\nWorld"
```

_Esto imprimirá:_

```bash
Hello
World
```

- _Sin la opción `-e`, `echo` imprimirá literalmente la cadena `\n` en lugar de insertar un salto de línea._

- _El comando `cut` se utiliza para cortar secciones de cada línea de los ficheros. Las opciones `-d` y `-f` son necesarias para especificar el delimitador y los campos a cortar, respectivamente. Aquí está lo que cada opción significa:_

- _`-d " "`: Esta opción especifica el delimitador que `cut` utilizará para dividir cada línea. En este caso, el delimitador es un espacio._

```bash
echo "field1 field2 field3" | cut -d " " -f 1
```

_Este comando imprimirá "field1", que es el primer campo delimitado por espacios._

- _`-f 3`: Esta opción especifica los campos que `cut` mostrará. En este caso, `cut` mostrará el tercer campo._

```bash
echo "field1 field2 field3" | cut -d " " -f 3
```

_Este comando imprimirá "field3", que es el tercer campo delimitado por espacios._

_Por lo tanto, `cut -d " " -f 3` dividirá cada línea en campos delimitados por espacios y mostrará el tercer campo de cada línea._

- _`cut -d " " -f 3,6`: Este comando divide cada línea en campos delimitados por espacios y muestra el tercer y sexto campo de cada línea._

  ```bash
  echo "field1 field2 field3 field4 field5 field6" | cut -d " " -f 3,6
  ```

  _Este comando imprimirá "field3 field6"._

- _`cut -d " " -f 3-`: Este comando divide cada línea en campos delimitados por espacios y muestra todos los campos desde el tercero en adelante._

  ```bash
  echo "field1 field2 field3 field4 field5 field6" | cut -d " " -f 3-
  ```

  _Este comando imprimirá "field3 field4 field5 field6"._

- _Mostrar un rango de campos: Puedes usar `-f m-n` para mostrar todos los campos desde el m-ésimo hasta el n-ésimo._

  ```bash
  echo "field1 field2 field3 field4 field5 field6" | cut -d " " -f 3-5
  ```

  _Este comando imprimirá "field3 field4 field5"._

- _Mostrar un solo campo: Puedes usar `-f n` para mostrar solo el n-ésimo campo._

  ```bash
  echo "field1 field2 field3 field4 field5 field6" | cut -d " " -f 3
  ```

  _Este comando imprimirá "field3"._

- _Cambiar el delimitador: Puedes usar cualquier carácter como delimitador._

  ```bash
  echo "field1,field2,field3,field4,field5,field6" | cut -d "," -f 3
  ```

  _Este comando imprimirá "field3"._

1. Redirigir solo la salida estándar:

   _Script de Python simple que imprime un mensaje en la salida estándar:_

   ```python
   print("Este es un mensaje para la salida estándar")
   ```

   _Puedes redirigir la salida de este script a un fichero llamado `salida.txt` de la siguiente manera:_

   ```bash
   python3 script.py > salida.txt
   ```

   _Después de ejecutar este comando, `salida.txt` contendrá el mensaje "Este es un mensaje para la salida estándar"._

2. _Redirigir solo la salida de error estándar:_

   _Aquí tienes un script de Python simple que imprime un mensaje en la salida de error estándar:_

   ```python
   print("Standard Output")
   raise Exception("Standard Error")
   ```

   _Puedes redirigir la salida de error de este script a un fichero llamado `error.txt` de la siguiente manera:_

   ```bash
   python3 script.py 2> error.txt
   ```

   _Después de ejecutar este comando, `error.txt` contendrá el mensaje "Este es un mensaje para la salida de error estándar"._

3. _Redirigir la entrada estándar:_

   _Script de Python simple que lee una línea de la entrada estándar:_

   ```python
   print(input("name: "))
   ```

   _Si tienes un fichero, por ejemplo input.txt, que contiene cualquier tipo de texto o caracteres, puedes usar este fichero como entrada para tu script. No importa qué información contenga el fichero, siempre que sea texto, puedes redirigirlo como entrada estándar para tu script de la siguiente manera:_

   ```bash
   python3 script.py < input.txt
   ```

   _Después de ejecutar este comando, el script imprimirá "Este es un mensaje para la entrada estándar"._

- _El comando `python3 error.py 2> error.txt > salida.txt < input.txt` ejecuta el script `error.py` con `python3`, redirige la entrada estándar desde `input.txt`, redirige la salida estándar a `salida.txt` y redirige la salida de error estándar a `error.txt`._

_Aquí está lo que hace cada parte del comando:_

1. _`python3 error.py`: Ejecuta el script `error.py` con `python3`._

   _El script `error.py` podría verse así:_

   ```python
   print(input("Mensaje para la salida: "))
   raise Exception("Standard Error")
   ```

   _Este script primero imprime el resultado de la función `input()`, que lee una línea de la entrada estándar, y luego lanza una excepción, que se imprimirá en la salida de error estándar._

2. _`2> error.txt`: Redirige la salida de error estándar (file descriptor 2) a `error.txt`. Cualquier cosa que se escriba en la salida de error estándar por el script se guardará en `error.txt`._

   _Si ejecutas solo esta parte del comando, verás que la salida de error estándar se guarda en `error.txt`:_

   ```bash
   python3 error.py 2> error.txt
   ```

   _Después de ejecutar este comando, `error.txt` contendrá el mensaje de la excepción lanzada por `error.py`._

3. _`> salida.txt`: Redirige la salida estándar (file descriptor 1) a `salida.txt`. Cualquier cosa que se escriba en la salida estándar por el script se guardará en `salida.txt`._

   _Si ejecutas solo esta parte del comando, verás que la salida estándar se guarda en `salida.txt`:_

   ```bash
   python3 error.py > salida.txt
   ```

   _Después de ejecutar este comando, `salida.txt` contendrá el resultado de la función `input()` en `error.py`._

4. _`< input.txt`: Redirige la entrada estándar desde `input.txt`. Cualquier cosa que el script lea de la entrada estándar se leerá de `input.txt`._

   _Si `input.txt` contiene la línea "Hola, mundo", y ejecutas solo esta parte del comando, verás que `input.txt` se usa como entrada para `error.py`:_

   ```bash
   python3 error.py < input.txt
   ```

   _Después de ejecutar este comando, verás que `error.py` imprime "Hola, mundo"._

- _El operador `>>` en Bash se utiliza para redirigir la salida estándar o la salida de error estándar a un fichero, pero a diferencia de `>`, `>>` añade la salida al final del fichero en lugar de sobrescribirlo._

_Aquí tienes algunos ejemplos utilizando el script `error.py`:_

1. _Redirigir la salida estándar añadiendo al final de un fichero:_

   ```bash
   python3 error.py >> salida.txt
   ```

   _Este comando ejecutará `error.py` y añadirá la salida estándar al final de `salida.txt`._

2. _Redirigir la salida de error estándar añadiendo al final de un fichero:_

   ```bash
   python3 error.py 2>> error.txt
   ```

   _Este comando ejecutará `error.py` y añadirá la salida de error estándar al final de `error.txt`._

_El operador `<<` en Bash se utiliza para redirigir la entrada estándar desde un literal de aquí-documento. Un aquí-documento es una sección de un script de shell que se dirige como entrada a un comando._

_Aquí tienes un ejemplo de cómo puedes usar un aquí-documento con el script `error.py`._

- _Si quieres terminar la entrada y ejecutar el programa, debes escribir EOF en una línea por sí misma._

```bash
python3 error.py << EOF
> Este es un mensaje para la entrada estándar
> EOF
```

```bash
python3 error.py << EOF
> Este es un mensaje para la entrada estándar
> No tomara esta linea por que la de arriba tiene un enter al final
> EOF
```

- _Sí, puedes utilizar cualquier palabra o cadena para delimitar el inicio y el final de un "aquí-documento" en Bash. No tiene que ser necesariamente EOF. La cadena que elijas simplemente debe aparecer por sí misma en una línea para indicar el final de la entrada._

**Aquí tienes un ejemplo utilizando FIN en lugar de EOF:**

```bash
python3 error.py << FIN
> Este es un mensaje para la entrada estándar
> FIN
```

```bash
python3 error.py << FIN
> Este es un mensaje para la entrada estándar
> No tomara esta linea por que la de arriba tiene un enter al final
> FIN
```

- *Puedes mezclar tuberías y redirecciones en Bash. Aquí te dejo algunos ejemplos utilizando el script `error.py`:*

1. *Redirigir la salida estándar añadiendo al final de un archivo y utilizando una tubería:*

    ```bash
    python3 error.py | grep "mensaje" >> salida.txt
    ```

    *Este comando ejecutará `error.py`, pasará la salida estándar al comando `grep`, que buscará líneas que contengan "mensaje", y añadirá el resultado al final de `salida.txt`.*

2. *Redirigir la salida de error estándar añadiendo al final de un archivo y utilizando una tubería:*

    ```bash
    python3 NoExiste.py 2> error.txt
    ```

    ```bash
    python3 error.py 2>&1 | grep "error" >> error.txt
    ```

    *En Bash, `&1` es una referencia al descriptor de archivo de la salida estándar.*

    *Los descriptores de archivo son una forma de referirse a las entradas y salidas abiertas por un proceso. En Bash, `0`, `1` y `2` son descriptores de archivo especiales que representan la entrada estándar, la salida estándar y la salida de error estándar, respectivamente.*

    *Cuando ves `2>&1` en un comando Bash, significa "redirige la salida de error estándar (2) a la misma ubicación a la que se está redirigiendo la salida estándar (1)".*

    *El comando `command > file.txt 2>&1` redirige la salida estándar de `command` a `file.txt` y luego redirige la salida de error estándar al mismo lugar (es decir, también a `file.txt`). Como resultado, tanto la salida estándar como la salida de error estándar de `command` se escribirán en `file.txt`.*

*El operador `<<` en Bash se utiliza para redirigir la entrada estándar desde un literal de aquí-documento. Un aquí-documento es una sección de un script de shell que se dirige como entrada a un comando.*

*Puedes redirigir tanto la entrada como la salida al mismo tiempo en Bash. Aquí tienes un ejemplo utilizando un script de Python simple:*

*Script de Python simple que lee una línea de la entrada estándar y la imprime en la salida estándar:*

```python
print(input("Lista: "))
```

*Puedes redirigir la entrada de este script desde un archivo llamado `input.txt` y la salida a un archivo llamado `output.txt` de la siguiente manera:*

```bash
python3 script.py < input.txt > output.txt
```

*Este comando ejecutará `script.py`, usará `input.txt` como entrada estándar y guardará la salida estándar en `output.txt`.*

*En una tubería (pipeline) en Bash, la salida de cada comando se pasa automáticamente como entrada al siguiente comando. Por lo tanto, no puedes redirigir la entrada o la salida de los comandos individuales en medio de la tubería, ya que esto interferiría con el flujo de datos a través de la tubería.*

```bash
python3 programa.py < input.txt  | sed "s/  */ /g" | cut -d " " -f 1,9 | tail --lines=+2 >> output.txt
```

*La salida del comando `python3 programa.py < input.txt` se pasa como entrada al comando `sed "s/  */ /g"`. Luego, la salida de `sed` se pasa como entrada a `cut -d " " -f 1,9`. Finalmente, la salida de `cut` se pasa como entrada a `tail --lines=+2 >> output.txt`.*

*Si intentas redirigir la entrada del comando `cut -d " " -f 1,9` con `< input.txt`, Bash se confundirá porque no está claro si `cut` debería tomar su entrada de `input.txt` o de la salida del comando `sed`.*

*De manera similar, si intentas redirigir la salida del comando `sed "s/  */ /g"` con `> output.txt`, Bash se confundirá porque no está claro si la salida de `sed` debería ir a `output.txt` o al comando `cut`.*

*Por lo tanto, cuando estás utilizando tuberías en Bash, no puedes redirigir la entrada o la salida de los comandos individuales en medio de la tubería. Sin embargo, puedes redirigir la entrada al primer comando y la salida del último comando.*
