**Profundizando en la terminal y comandos avanzados**

**`Indice`**

- [**_Comandos avanzados_**](#comandos-avanzados)
- [***Enlaces Simbolicos en directorios***](#enlaces-simbolicos-en-directorios)
- [***Permisos en directorios en Linux***](#permisos-en-directorios-en-linux)
- [***Redirecciones y tuberías en Linux***](#redirecciones-y-tuberías-en-linux)

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

- *En el comando `find . -type d -name "dir*"`, las opciones `-type` y `-d` se utilizan para especificar el tipo de fichero que estás buscando.*

- `-type`: Esta opción se utiliza para especificar el tipo de fichero que estás buscando. Puedes buscar varios tipos de ficheros, incluyendo ficheros regulares (`f`), directorios (`d`), enlaces simbólicos (`l`), y otros.

- `d`: Este es el argumento que se pasa a la opción `-type` para especificar que estás buscando directorios. Por lo tanto, `-type d` significa "buscar directorios".

- *Por lo tanto, el comando `find . -type d -name "dir*"` buscará todos los directorios cuyo nombre comienza con "dir" en el directorio actual y en todos sus subdirectorios.*

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
  - > *Cuando usas la opción -E con grep, estás indicando que deseas que grep interprete la expresión regular como una expresión regular extendida, lo que significa que no necesitas escapar los caracteres especiales como {} para que se interpreten correctamente como cuantificadores.*

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

# ***Enlaces Simbolicos en directorios***

---

# ***Permisos en directorios en Linux***

> *En Linux, los permisos de los ficheros y directorios determinan quién puede leer, escribir o ejecutar ciertos ficheros o directorios.*

- ***Lectura (r)**: Permite abrir y leer un fichero o directorio.*
- ***Escritura (w)**: Permite modificar un fichero o directorio.*
- ***Ejecución (x)**: Permite ejecutar un fichero o acceder a un directorio.*

- **Comandos que no se pueden ejecutar sin permisos**

> *Si no tienes los permisos adecuados para un fichero o directorio, hay ciertos comandos que no podrás ejecutar. Aquí hay algunos ejemplos:*

- *`cat`, `ls`, `less`, `more`: Estos comandos no se pueden ejecutar en un fichero si no tienes **permisos de lectura** para ese fichero.*
  
  - *`less` y `more` son comandos de paginación en Unix y sistemas similares a Unix que se utilizan para ver el contenido de ficheros de texto en la terminal.*

    - **less**: Este comando proporciona una interfaz para desplazarse hacia adelante y hacia atrás en el archivo de texto. También permite buscar texto dentro del archivo. A diferencia de otros comandos de visualización, `less` no tiene que leer todo el archivo antes de empezar a mostrarlo, lo que puede ser más rápido para ficheros grandes. El nombre `less` es un juego de palabras, ya que su funcionalidad es más (en inglés, "more") que la del comando `more`.

      - ```bash
        # Ver el contenido de un archivo con less
        less fichero.py
        ```

    - **more**: Este comando también muestra el contenido de ficheros de texto en la terminal, pero solo permite desplazarse hacia adelante en el archivo, no hacia atrás. Aunque `more` tiene menos funcionalidades que `less`, puede ser suficiente para visualizar ficheros de texto que solo requieren un desplazamiento hacia adelante.

    - ```bash
      # Ver el contenido de un archivo con more
      more fichero.py
      ```

    - **En ambos casos, puedes salir de la vista del archivo presionando `q`.**

*- `touch`: Estos comandos no se pueden usar para escribir en un fichero si no tienes **permisos de escritura** para ese fichero.*

*- `cd`: No puedes cambiar a un directorio si no tienes **permisos de ejecución** para ese directorio.*

*- `./`: No puedes ejecutar un fichero si no tienes **permisos de ejecución** para ese fichero.*

---

# ***Redirecciones y tuberías en Linux***

> *En Linux, las redirecciones y las tuberías son formas de manejar los flujos de datos entre programas y ficheros.*

- **Standard Input (stdin), Standard Output (stdout), Standard Error (stderr)**

- ***Standard Input (stdin)**: Es el flujo de datos que se envía a un programa. Por defecto, este es el teclado. Su descriptor de archivo es 0.*

- ***Standard Output (stdout)**: Es el flujo de datos que un programa envía cuando se ejecuta correctamente. Por defecto, este es la terminal. Su descriptor de archivo es 1.*

- ***Standard Error (stderr)**: Es el flujo de datos que un programa envía cuando encuentra un error. Por defecto, este también es la terminal. Su descriptor de archivo es 2.*

- **Redirecciones**

> *Las redirecciones te permiten cambiar de dónde proviene el stdin o a dónde va el stdout o stderr.*

- *`>`: Redirige el stdout a un archivo. Si el archivo ya existe, lo sobrescribe.*

- *`<`: Toma el stdin de un archivo en lugar del teclado.*

- *`2>`: Redirige el stderr a un archivo.*

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

***Tuberías (Pipes)***

> *Las tuberías te permiten tomar el stdout de un programa y usarlo como stdin para otro programa.*

- *`|`: Toma el stdout del comando a la izquierda y lo usa como stdin para el comando a la derecha.*

```bash
# Ejemplo de tubería
ls -l | grep ".py"
```

***Comandos***

1. *El comando `tail` se utiliza para mostrar las últimas líneas de un archivo o de un flujo de entrada. La opción `--lines` o su forma abreviada `-n` se utiliza para especificar el número de líneas a mostrar.*

     - ```bash
        ls -l | tail --lines=+2
       ```

       - *`ls -l | tail --lines=+2`: Este comando muestra todas las líneas del output de `ls -l` a partir de la línea 2. El `+` antes del número indica que `tail` debe empezar a mostrar las líneas a partir de la línea 2.*

     - ```bash
        ls -l | tail --lines=-2
       ```

        - *`ls -l | tail --lines=-2`: Este comando muestra las últimas dos líneas del output de `ls -l`. El `-` antes del número indica que `tail` debe mostrar las últimas n líneas.*

     - ```bash
        ls -l | tail --lines=-2
       ```

        - *`ls -l | tail --lines=2`: Este comando es equivalente al anterior. Si no se especifica un signo antes del número, `tail` asume que debe mostrar las últimas n líneas.*

     - *La forma abreviada de `--lines` es `-n`.*

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

2. *El comando `head` se utiliza para mostrar las primeras líneas de un archivo o de un flujo de entrada. La opción `--lines` o su forma abreviada `-n` se utiliza para especificar el número de líneas a mostrar.*

     - ```bash
        ls -l | head --lines=+2
       ```

       - *`ls -l | head --lines=+2`: Este comando muestra las lineas establecidas en `--lines=` del output de `ls -l`. El `+` antes del número indica que `head` debe empezar a mostrar las líneas a partir de la línea 2.*

     - ```bash
        ls -l | head --lines=-2
       ```

        - *`ls -l | head --lines=-2`: Este comando muestra todas las líneas del output de ls -l excepto el numero de lineas dados.*

     - ```bash
        ls -l | head --lines=2
       ```

        - *`ls -l | head --lines=2`: Este comando muestra las lineas establecidas en `--lines=` del output de `ls -l`. Si no se especifica un signo antes del número, `head` asume que debe mostrar las primeras n líneas.*

     - *La forma abreviada de `--lines` es `-n`.*

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

3. *sed es un acrónimo de "stream editor" en inglés.*

- *"Stream" se refiere a un flujo de datos.*

- *"Editor" se refiere a un programa que permite modificar esos datos.*

- *Por lo tanto, sed es un programa que permite modificar flujos de datos.*

- *En español, sed podría traducirse como "editor de flujo".*

- *El comando `sed` es un editor de flujo que puede realizar transformaciones de texto.*

```bash
sed "s/  */ /g"
```

- *`s`: Es el comando de sustitución. Le dice a `sed` que vas a reemplazar texto.*

- *`/  */ /`: Es el patrón de sustitución. El primer espacio entre las primeras dos barras `/` es el texto que quieres reemplazar. El espacio entre las últimas dos barras `/` es el texto por el que quieres reemplazarlo. El `*` significa "cero o más del carácter anterior", por lo que `  *` coincide con uno o más espacios.*

- *`g`: Es una bandera que le dice a `sed` que realice la sustitución globalmente en cada línea, en lugar de solo la primera coincidencia.*

*Por lo tanto, `sed "s/  */ /g"` reemplaza todas las secuencias de uno o más espacios en cada línea con un solo espacio.*
