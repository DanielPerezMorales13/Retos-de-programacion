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
        ls
       ```

   - _Este comando se utiliza para listar los archivos y directorios en el directorio actual_
   - **Traduccion:** _"List", lista_

7. _mkdir_

    1. ```bash
        mkdir <nombre directorio>
       ```

   - _Este comando se utiliza para crear un nuevo directorio. Toma como parámetro el nombre del directorio que se desea crear_
   - **Traduccion:** _Make Directory, Crear Directorio_

8. _rmdir_

    1. ```bash
        rmdir <nombre directorio>
       ```

   - _Este comando se utiliza para eliminar un directorio vacío. Toma como parámetro el nombre del directorio que se desea eliminar_
     - _**Nota:** rmdir sólo eliminará un directorio si está vacío_
   - **Traduccion:** _Remove Directory,Eliminar Directorio_

<!--

 * *  * *  * *

 * *  * *  * *

 -->
