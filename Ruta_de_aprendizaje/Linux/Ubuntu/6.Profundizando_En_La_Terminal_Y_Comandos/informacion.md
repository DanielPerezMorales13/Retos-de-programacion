**Profundizando en la terminal y comandos avanzados**

**`Indice`**

- [**_Comandos avanzados_**](#comandos-avanzados)

---

# **_Comandos avanzados_**

`find`

_El comando find se utiliza para buscar ficheros y directorios en el sistema de ficheros._

```bash
find /ruta/a/buscar -name "patrón"
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
sudo apt update
```

```bash
sudo apt install tree
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
   grep "palabra" fichero.txt
   ```

2. **Coincidir una palabra al principio de la línea:**

   ```bash
   grep "^palabra" fichero.txt
   ```

3. **Coincidir una palabra al final de la línea:**

   ```bash
   grep "palabra$" fichero.txt
   ```

4. **Coincidir una palabra al principio o al final de la línea:**

   1. ```bash
       grep "^PalabraInicio$\|^FinPalabra$" fichero.txt
      ```

        - ```bash
          grep -E "^PalabraInicio$\|^FinPalabra$" fichero.txt
          ```

        - ```bash
          grep --extended-regexp "^PalabraInicio$\|^FinPalabra$" fichero.txt
          ```

   2. ```bash
       grep "^PalabraInicio\|^FinPalabra$" fichero.txt
      ```

      - ```bash
        grep -E "^PalabraInicio\|^FinPalabra$" fichero.txt
        ```

      - ```bash
        grep --extended-regexp "^PalabraInicio\|^FinPalabra$" fichero.txt
        ```

   3. ```bash
      grep "PalabraInicio$\|^FinPalabra$" fichero.txt
      ```

        - ```bash
          grep -E "PalabraInicio$\|^FinPalabra$" fichero.txt
          ```

        - ```bash
          grep --extended-regexp "PalabraInicio$\|^FinPalabra$" fichero.txt
          ```

   4. ```bash
      grep "^PalabraInicio\|FinPalabra$" fichero.txt
      ```

        - ```bash
           grep -E "^PalabraInicio\|FinPalabra$" fichero.txt
          ```

        - ```bash
          grep --extended-regexp "^PalabraInicio\|FinPalabra$" fichero.txt
          ```

   5. ```bash
       grep "^PalabraInicio\|^FinPalabra" fichero.txt
        ```

       - ```bash
         grep -E "^PalabraInicio\|^FinPalabra" fichero.txt
         ```

       - ```bash
         grep --extended-regexp "^PalabraInicio\|^FinPalabra" fichero.txt
         ```

   6. ```bash
      grep "PalabraInicio$\|FinPalabra$" fichero.txt
      ```

       - ```bash
         grep -E "PalabraInicio$\|FinPalabra$" fichero.txt
         ```

       - ```bash
         grep --extended-regexp "PalabraInicio$\|FinPalabra$" fichero.txt
         ```

5. **Coincidir una palabra ignorando mayúsculas y minúsculas:**

   ```bash
   grep -i "palabra" fichero.txt
   ```

   ```bash
   grep --ignore-case "palabra" fichero.txt
   ```

6. **Coincidir una palabra precedida por un cierto número de caracteres:**

   ```bash
   grep -E ".{5}palabra" fichero.txt
   ```

   ```bash
   grep --extended-regexp ".{5}palabra" fichero.txt
   ```

   ```bash
   grep ".\{5\}palabra" fichero.txt
   ```

7. **Coincidir una palabra seguida por un cierto número de caracteres:**

    ```bash
   grep -E "palabra.{5}" fichero.txt
   ```

   ```bash
   grep --extended-regexp "palabra.{5}" fichero.txt
   ```

   ```bash
   grep "palabra.\{5\}" fichero.txt
   ```

8. **Coincidir una palabra con una longitud específica:**

   ```bash
   grep -E "^.{5}$" fichero.txt
   ```

   ```bash
   grep --extended-regexp "^.{5}$" fichero.txt
   ```

   ```bash
   grep "^.\{5\}$" fichero.txt
   ```

9. **Coincidir una palabra que comience con ciertos caracteres:**

   ```bash
   grep -E "^prefix.*" fichero.txt
   ```

    ```bash
    grep --extended-regexp "^prefix.*" fichero.txt
    ```

   ```bash
   grep "^prefix.*" fichero.txt
   ```

10. **Coincidir una palabra que termine con ciertos caracteres:**

    ```bash
    grep -E ".*suffix$" fichero.txt
    ```

    ```bash
    grep --extended-regexp ".*suffix$" fichero.txt
    ```

    ```bash
    grep ".*suffix$" fichero.txt
    ```

_Explicacion de cada uno de los caracteres y construcciones en el contexto de las expresiones regulares:_

1. _`|`: El símbolo `|` se utiliza en expresiones regulares para denotar una "alternativa". Por ejemplo, la expresión regular `a|b` coincidirá con cualquier cadena que contenga la letra "a" o la letra "b"._

2. _`.`: El punto (`.`) se utiliza en expresiones regulares para representar cualquier carácter individual. Por ejemplo, la expresión regular `a.c` coincidirá con cualquier cadena que contenga una "a", seguida de cualquier carácter, seguida de una "c"._

3. _`_`: El asterisco (`_`) se utiliza en expresiones regulares como un "cuantificador", que significa "cero o más repeticiones del elemento anterior". Por ejemplo, la expresión regular `a_` coincidirá con cualquier cadena que contenga cero o más "a".\*

4. _`\`: La barra invertida (`\`) se utiliza en expresiones regulares para "escapar" caracteres especiales, permitiendo que se interpreten literalmente. Por ejemplo, `\.`, `\\`, y `\(` coincidirán literalmente con un punto, una barra invertida y un paréntesis de apertura, respectivamente._

5. _`{}`: Las llaves (`{}`) se utilizan en expresiones regulares para cuantificar la cantidad de repeticiones de un elemento anterior. Por ejemplo, la expresión regular `a{3}` coincidirá con exactamente tres "a" consecutivas._

6. _`^`: El acento circunflejo (`^`) se utiliza en expresiones regulares para anclar la coincidencia al principio de una línea. Por ejemplo, la expresión regular `^inicio` coincidirá con "inicio" solo si aparece al principio de una línea._

7. _`$`: El signo de dólar (`$`) se utiliza en expresiones regulares para anclar la coincidencia al final de una línea. Por ejemplo, la expresión regular `final$` coincidirá con "final" solo si aparece al final de una línea._
