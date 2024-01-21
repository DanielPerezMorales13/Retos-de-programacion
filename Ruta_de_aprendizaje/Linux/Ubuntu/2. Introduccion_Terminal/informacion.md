**_Introduccion ala terminal_**

**Indice**

- [**_Primeros Comandos_**](#primeros-comandos)

---

# **_Primeros Comandos_**

> **Conceptos importantes sobre linux**

1. *Directorio: En programacion un directorio es una carpeta*
2. *Fichero: En programacion un fichero es una archivo con o sin extensio*

   1. **Ejemplo:**

      1. ```bash
         script.py
         ```

      2. *script es el nombre del fichero y lo que esta luego del punto es la extension del fichero*

3. _**.** : Representa el directorio actual._
4. _**~**: Representa el directorio home del usuario actual._

   1. _Por ejemplo, si tu nombre de usuario es daniel, ~ generalmente se traduciría a /home/daniel._
5. ***..**: Representa el directorio padre del directorio actual. Entonces, si estás en /home/daniel/Escritorio/carpeta y ejecutas cd .., te moverías al directorio /home/daniel/Escritorio.*

   1. ***Ejemplo:** ../descargas: Esto te movería al directorio descargas que se encuentra en el mismo nivel que tu directorio actual. Entonces, si estás en /home/daniel/Escritorio/carpeta y ejecutas*

      1. ```bash
         cd ../descargas 
         ```

      2. *Te moverías al directorio /home/daniel/Escritorio/descargas.*

> _**Comandos**_

1. _<kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>t</kbd>_

   - _Abre una nueva ventana de terminal_

2. *whoami*

   1. ```bash
        whoami
       ```

    - *imprimir el nombre de usuario del usuario actual*
    - **Traduccion:** *whoami ,quién soy yo?*
3. *pwd*

    1. ```bash
        pwd
       ```

    - *muestra la ruta completa del directorio en el que te encuentras actualmente*
    - Traduccion: _"Print Working Directory", que se traduce al español como "Imprimir el Directorio de Trabajo_

4. *clear*

   1. ```bash
        clear
       ```

    - *limpiar la pantalla de la termina*
    - **Traduccion:** *clear, limpiar*

   2. *Otra manera de hacerlo*

      1. <kbd>Ctrl</kbd> + <kbd>l</kbd> 

5. _cd <directorio>_

   1. ```bash
        cd <directorio>
      ```

   - _Este comando se utiliza para cambiar el directorio de trabajo actual a otro directorio y toma como parametro el nombre del directorio_
     - _Entonces, cd . simplemente te mantendría en el mismo directorio._
   - **Traduccion:** _Change Directory, Cambiar - Directorio_

6. _ls_

    1. ```bash
        ls ./
       ```

    2. ```bash
        ls ./Escritorio/
       ```

    3. ```bash
        ls ../
        ```

    4. ```bash
        ls ../carpeta/
        ```

   - _Este comando se utiliza para listar los archivos y directorios en el directorio actual. **Tambien se le puede pasar rutas relativas como absoluta**_
   - **Traduccion:** _"List", lista_

7. _mkdir_

    1. ```bash
        mkdir directorio/
       ```

    2. ```bash
        mkdir ./Escritorio/carpeta/
       ```

    3. ```bash
        mkdir ../carpeta/
        ```

    4. ```bash
        mkdir directorio/ otro/
       ```

    5. ```bash
        mkdir ./Escritorio/carpeta ./Escritorio/otro/
       ```

    6. ```bash
        mkdir ../carpeta/ ../otro/
        ```

    7. ```bash
        mkdir ./"nuevo directorio"/
        ```

    8. ```bash
        mkdir ./nuevo\ directorio/
        ```

   - _Este comando se utiliza para crear un nuevo directorio. Toma como parámetro el nombre del directorio que se desea crear. **Tambien se le puede pasar rutas relativas como absoluta**_
   - **Traduccion:** _Make Directory, Crear Directorio_

8. _rmdir_

    1. ```bash
        rmdir directorio/
       ```

    2. ```bash
        rmdir ./Escritorio/carpeta/
       ```

    3. ```bash
        rmdir ../carpeta/
        ```

    4. ```bash
        rmdir directorio/ otro/
       ```

    5. ```bash
        rmdir ./Escritorio/carpeta/ ./Escritorio/otro/
       ```

    6. ```bash
        rmdir ../carpeta/ ../otro/
        ```

    7. ```bash
        rmdir ./"nuevo directorio"/
        ```

    8. ```bash
        rmdir ./nuevo\ directorio/
        ```

   - _Este comando se utiliza para eliminar un directorio vacío. Toma como parámetro el nombre del directorio que se desea eliminar. **Tambien se le puede pasar rutas relativas como absoluta**_

     - _**Nota:** rmdir sólo eliminará un directorio si está vacío_

     - **Se pueden pasar mas de un parametro**
   - **Traduccion:** _Remove Directory,Eliminar Directorio_

9. *touch*

   1. ```bash
      touch fichero.txt
      ```

   2. ```bash
        touch ./Escritorio/carpeta/fichero.txt
       ```

   3. ```bash
        touch ../carpeta/fichero.txt
        ```

   4. ```bash
      touch fichero.txt fichero2.txt
      ```

   5. ```bash
        touch ./Escritorio/carpeta/fichero.txt ./Escritorio/carpeta/fichero2.txt
       ```

   6. ```bash
        touch ../carpeta/fichero.txt ../carpeta/copia.txt
        ```

   7. ```bash
        touch ./"mi primer programa.py"
        ```

   8. ```bash
        touch ./"mi primer programa".py
        ```

   9. ```bash
        touch ./mi\ primer\ programa.py
        ```

   - *El comando touch en Linux se utiliza para cambiar las marcas de tiempo de acceso y modificación de un archivo. También se puede utilizar para crear un nuevo archivo si el archivo especificado no existe. **Tambien se le puede pasar rutas relativas como absoluta***

      - **Se pueden pasar mas de un parametro**

10. *rm*

      1. ```bash
         rm fichero.txt
         ```

      2. ```bash
         rm ./Escritorio/carpeta/fichero.txt
         ```

      3. ```bash
         rm ../carpeta/fichero.txt
         ```

      4. ```bash
         rm fichero.txt copia.txt
         ```

      5. ```bash
         rm ./Escritorio/carpeta/fichero.txt ./Escritorio/carpeta/copia.txt
         ```

      6. ```bash
         rm ../carpeta/fichero.txt ../carpeta/copia.txt
         ```

      7. ```bash
         rm ./"mi primer programa.py"
         ```

      8. ```bash
         rm ./"mi primer programa".py
         ```

      9. ```bash
         rm ./mi\ primer\ programa.py
         ```

      - *El comando rm en Linux se utiliza para eliminar archivos y directorios. **Tambien se le puede pasar rutas relativas como absoluta***
        - **Se pueden pasar mas de un parametro**

        - *Este comando eliminará el archivo llamado fichero.txt del directorio actual. Ten en cuenta que este comando no moverá el archivo a la papelera de reciclaje, sino que lo eliminará permanentemente. Por lo tanto, debes tener cuidado al usarlo.*

      - **Traduccion**: Las siglas rm provienen del inglés y significan "remove", que en español se traduce como "eliminar".

11. *cp*

      1. ```bash
         cp fichero.txt ./copia.txt
         ```

      2. ```bash
         cp ./Escritorio/carpeta/fichero.txt ./Escritorio/carpeta/copia.txt
         ```

      3. ```bash
         cp ../carpeta/fichero.txt ../carpeta/copia.txt
         ```

      - *Se utilizan para copiar ficheros.*
        - *Si la el fichero ya existe, será sobrescrito.*

      - **Traduccion:** *cp proviene de las siglas en inglés "copy", que significa "copiar".*

12. *mv*

    1. ```bash
         mv fichero.txt ./copia.txt
        ```

    2. ```bash
         mv ./Escritorio/carpeta/fichero.txt ./Escritorio/carpeta/copia.txt
       ```

    3. ```bash
         mv ../carpeta/fichero.txt ../carpeta/copia.txt
       ```  

    - *Este comando mover el fichero a otra ubicacion si ya existe, será sobrescrito.*

      - *Además, mv también se puede utilizar para renombrar archivos.*
    - **Traduccion:** *mv proviene de las siglas en inglés "move", que significa "mover".*

13. *echo*

    1. ```bash
       echo "Este mensaje se imprimira en la terminal"
       ```

    2. ```bash
        echo $HOME
        ```

     - *El comando echo en Linux se utiliza para mostrar una línea de texto u otras variables de entorno en la terminal.*

     - **Traduccion:** *echo es una palabra en inglés que significa "eco", en el sentido de repetir lo que se le da.*

14. *cat*

      1. ```bash
         cat ./fichero.txt
         ```

      2. ```bash
         cat ./fichero.txt ./fichero2.txt
         ```

      3. ```bash
         cat ./fichero.txt > ./fichero2.txt
         ```

      4. ```bash
         cat ./Escritorio/carpeta/fichero.txt
         ```

      5. ```bash
         cat ./Escritorio/carpeta/fichero.txt ./Escritorio/carpeta/fichero2.txt
         ```

      6. ```bash
         cat ./Escritorio/carpeta/fichero.txt > ./Escritorio/carpeta/fichero2.txt
         ```

      7. ```bash
         cat ../carpeta/fichero.txt
         ```

      8. ```bash
         cat ../carpeta/fichero.txt ../carpeta/fichero2.txt
         ```

      9. ```bash
          cat ../carpeta/fichero.txt > ../carpeta/fichero2.txt
         ```

      10. ```bash
          cat ./fichero.txt ./fichero2.txt > fichero3.txt
          ```

     - *El comando cat en Linux se utiliza para concatenar y mostrar archivos.*

       - *Este comando concatenará el contenido de **fichero.txt** y **fichero2.txt**, y el resultado se guardará en **archivo3.txt**. **Si fichero3.txt ya existe, será sobrescrito si no sera se creara el archivo.***

       - *El símbolo > en Linux se utiliza para redirigir la salida de un comando a un fichero.*

       - **Se pueden pasar mas de un parametro**

     - **Traduccion:** *cat es una abreviatura de la palabra en inglés "concatenate", que significa "concatenar".*

15. *man `<command>`*

       1. ```bash
          man ls
          ```

      - *El comandos man en Linux se utiliza para obtener ayuda sobre un comando toma como parametro el comando.*

      - **Traduccion:** *man es un acrónimo de "manual", y man <comando> muestra la página del manual para el <comando>. Las páginas del manual contienen una descripción detallada del comando, sus opciones y su uso.*

16. *nano `<fichero>`*

      1. ```bash
         nano fichero.txt
         ```

      - *nano es un editor de texto en la línea de comandos de Linux. nano archivo.txt abrirá el archivo archivo.txt en el editor nano.*

17. *grep `palabra <fichero>`*

    1. ```bash
         grep lista fichero.txt
         ```

    - *El comando grep en Linux se utiliza para buscar texto en archivos.*

      - *El comando grep lista fichero.txt buscará la palabra "lista" en el archivo fichero.txt y mostrará las líneas que contienen esa palabra.*

    - **Traduccion:** *grep es un acrónimo de "Global Regular Expression Print", Impresión global de expresiones regulares.*

18. *comando con opciones*

     - > *Las opciones en Linux, también conocidas como flags o switches, son argumentos que se utilizan para modificar el comportamiento de un comando. Generalmente se añaden después del nombre del comando y antes de cualquier otro argumento.*
       - > *Las opciones suelen comenzar con un guion - o dos guiones --. Las opciones que comienzan con un solo guion suelen ser abreviaturas de una sola letra, mientras que las opciones que comienzan con dos guiones suelen ser palabras completas.*

     1. ```bash
          <command> --help
          ```

           1. ```bash
               ls --help
               ```

               - *Este comando mostrará la ayuda para el comando*

     2. ```bash
          rm -r ./carpeta
          ```

     3. ```bash
          rm -r -i ./carpeta
          ```

     4. ```bash
          rm -ri ./carpeta
          ```

     5. ```bash
          rm -ir ./carpeta
          ```

     6. ```bash
          rm --recursive ./carpeta 
          ```

     7. ```bash
          rm --recursive --interactive ./carpeta
          ```

     8. ```bash
          rm --interactive --recursive ./carpeta
          ```

     9. ```bash
          rm --recursive -i ./carpeta
          ```

     10. ```bash
          rm -i --recursive ./carpeta
          ```

     11. ```bash
          rm -r --interactive ./carpeta
          ```

     12. ```bash
          rm --interactive -r ./carpeta
          ```
