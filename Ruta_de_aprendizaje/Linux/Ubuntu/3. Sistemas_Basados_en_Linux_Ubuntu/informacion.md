_Sistemas basados en Linux Ubuntu_

**Indice**

- [**_Usuarios en linux_**](#usuarios-en-linux)
- [**_Configurando GRUB en Ubuntu_**](#configurando-grub-en-ubuntu)
- [**_Atajo Linux!!_**](#atajo-linux)
- [**_Gestores de paquetes en Linux Ubuntu_**](#gestores-de-paquetes-en-linux-ubuntu)
- [**_Cambiar el tema de la terminal en Ubuntu_**](#cambiar-el-tema-de-la-terminal-en-ubuntu)
- [**_Permisos en linux_**](#permisos-en-linux)

---

# **_Usuarios en linux_**

_El comando sudo su root en Linux se utiliza para cambiar al usuario root._

**sudo** _es un acrónimo de "SuperUser DO" en inglés. En español, podría interpretarse como "Hacer como SuperUsuario". Este comando permite a los usuarios ejecutar programas con los privilegios de seguridad de otro usuario (por defecto, el usuario root)._

**su** _significa "Substitute User" en inglés, que en español se traduce como "Sustituir Usuario". Este comando se utiliza para cambiar al usuario root o a cualquier otro usuario._

_root es el nombre del usuario superusuario en sistemas Unix y Linux. El usuario root tiene todos los privilegios y puede hacer cualquier cosa en el sistema._

1. ```bash
    sudo su root
   ```

1. ```bash
    sudo su
   ```

   - _Después de ejecutar este comando, se te pedirá que introduzcas tu contraseña. Una vez que la introduzcas correctamente, tu prompt cambiará para indicar que ahora estás operando como el usuario root.**`sudo su root && sudo su es lo mismo`**_

---

# **_Configurando GRUB en Ubuntu_**

_GRUB es el acrónimo de "GRand Unified Bootloader". En español, se podría traducir como "Cargador de Arranque Unificado Grande". Es un gestor de arranque múltiple, lo que significa que permite seleccionar entre diferentes sistemas operativos durante el arranque del equipo._

_GRUB es muy flexible y potente, ya que puede cargar una amplia variedad de sistemas operativos y también puede cargar una gran cantidad de formatos de fichero de kernel._

_Por ejemplo, si tienes instalados Linux y Windows en la misma máquina, GRUB te permitirá elegir cuál de ellos quieres arrancar cuando enciendas tu computadora._

> **Para editar el fichero de configuracion de grup**

1. _Para ver el contenido del fichero_

   1. ```bash
      cat /etc/default/grub
      ```

   2. ![img-grup#1](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-grub/img-grup%231.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-grub/img-grup%231.png?raw=true")

2. _Para editarlo_

   1. ```bash
      sudo nano /etc/default/grup
      ```

   2. ![img-grup#2](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-grub/img-grup%232.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-grub/img-grup%232.png?raw=true")

   3. ```bash
      sudo update-grub
      ```

      - > _Luego de editar el fichero debes ejecutar sudo update-grub y reiniciar el sistema operativo para aplicar los cambios._

   4. _El fichero real de la configuracion del grub se encuentra en esta ruta **`/bootgrub/grub.cfg`**.Este fichero es la configuración principal de GRUB, el gestor de arranque._

      1. ```bash
          sudo nano /boot/grub/grub.cfg
         ```

      2. ```bash
          cat /boot/grub/grub.cfg
         ```

   - con cat`/bootgrub/grub.cfg` Este comando mostrará el contenido del fichero grub.cfg, que incluye las entradas del menú de arranque, las opciones de arranque y otros ajustes de GRUB. Este fichero normalmente no se edita directamente, sino que se genera a partir de otros ficheros de configuración mediante el comando update-grub.

   - La extensión .cfg se utiliza generalmente para ficheros de configuración. Estos ficheros contienen los ajustes para programas y aplicaciones. En este caso, grub.cfg contiene la configuración para el gestor de arranque GRUB.

3. ![img-grup#3](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-grub/img-grup%233.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-grub/img-grup%233.png?raw=true")

   1. _La línea GRUB_DEFAULT=0 es una configuración en el fichero de configuración de GRUB, que normalmente se encuentra en /etc/default/grub en sistemas Linux._

      - _GRUB_DEFAULT controla qué entrada del menú de GRUB se selecciona por defecto cuando el sistema arranca. Las entradas del menú se cuentan desde 0, por lo que GRUB_DEFAULT=0 significa que se seleccionará la primera entrada del menú._

      - _Por ejemplo, si tu menú de GRUB tiene las siguientes entradas:_

        - **Ubuntu**
        - **Advanced options for Ubuntu**
        - **Windows Boot Manager**

      - > _Entonces GRUB_DEFAULT=0 seleccionará "Ubuntu" por defecto._

4. ![img-grup#4](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-grub/img-grup%234.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-grub/img-grup%234.png?raw=true")

   1. _La línea GRUB_TIMEOUT=10 es una configuración en el fichero de configuración de GRUB, que normalmente se encuentra en /etc/default/grub en sistemas Linux._

      - _GRUB_TIMEOUT controla cuánto tiempo (en segundos) GRUB espera antes de arrancar automáticamente la entrada del menú por defecto. En este caso, GRUB_TIMEOUT=10 significa que GRUB esperará 10 segundos antes de arrancar la entrada por defecto._

      - _Si durante ese tiempo seleccionas manualmente otra entrada del menú, GRUB arrancará esa entrada en lugar de la entrada por defecto._

---

# **_Atajo Linux!!_**

> _!! es un evento de diseño en la línea de comandos de Bash que se refiere al último comando ejecutado._

**ejemplo:**

1. _El primer comando que ejecutaste fue este_

   - ```bash
     update-grub
     ```

   - ```bash
     sudo !!
     ```

   - _Por lo tanto, si el último comando que ejecutaste fue update-grub (o update-grup como mencionaste, aunque el comando correcto para actualizar la configuración de GRUB es update-grub), entonces sudo !! ejecutará sudo update-grub._

   - _En este ejemplo, el primer comando intentará ejecutar update-grub sin privilegios de superusuario, lo que probablemente fallará si requiere privilegios de superusuario. Luego, sudo !! ejecutará sudo update-grub, que ejecutará update-grub con privilegios de superusuario._

2. _Otro ejemplo_

   1. ![img-grup#5](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-grub/img-grup%235.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-grub/img-grup%235.png?raw=true")

---

# **_Gestores de paquetes en Linux Ubuntu_**

> _Los gestores de paquetes más comunes en Ubuntu son APT,Snap y dpkg._

1. _**APT** (Advanced Package Tool): Herramienta Avanzada de Paquetes. Es una interfaz de línea de comandos para la gestión de paquetes en Ubuntu y otras distribuciones basadas en Debian. APT simplifica el proceso de instalación, actualización y eliminación de software._

2. _**dpkg (Debian Package)**: Paquete Debian. Es el sistema de gestión de paquetes de bajo nivel en Debian y sus derivados, incluyendo Ubuntu. dpkg se utiliza para instalar, eliminar y proporcionar información sobre los paquetes .deb._

3. _**Snap**: Snap es un sistema de gestión de paquetes desarrollado por Canonical, los creadores de Ubuntu. Los paquetes Snap son autocontenidos, lo que significa que incluyen todas las dependencias necesarias para que la aplicación funcione, lo que facilita su instalación y actualización. "Snap" no es un acrónimo, por lo que no tiene una traducción directa ni un significado más allá de ser el nombre del sistema de gestión de paquetes._

> _El comando apt list en Ubuntu y otras distribuciones basadas en Debian se utiliza para listar los paquetes disponibles en los repositorios de software configurados en el sistema._

1. ```bash
   apt list
   ```

   1. ```bash
      apt list --installed
      ```

      1. > _apt list --installed: Lista todos los paquetes instalados en el sistema._

   2. ```bash
      apt list --upgradable
      ```

      1. > _apt list --upgradable: Lista todos los paquetes instalados que pueden ser actualizados._

   3. ```bash
      apt list --all-versions
      ```

      1. > _apt list --all-versions: Lista todas las versiones disponibles de todos los paquetes._

   4. ```bash
      apt list <nombre_del_paquete>
      ```

      1. > _apt list nombre_del_paquete: Muestra el estado del paquete especificado._

> _Los comandos sudo apt-get update y sudo apt-get upgrade son comandos fundamentales en Ubuntu y otras distribuciones basadas en Debian para mantener el sistema actualizado._

1. **sudo apt-get update**: _Este comando descarga la lista de paquetes desde los repositorios y "actualiza" la lista de paquetes disponibles y sus versiones, pero no instala ni actualiza ningún paquete._

   1. ```bash
      sudo apt-get update
      ```

**sudo apt-get upgrade**: _Este comando instala las versiones más recientes de todos los paquetes actualmente instalados en el sistema a partir de las listas de paquetes recuperadas con apt-get update._

1. ```bash
   sudo apt-get upgrade
   ```

> _Añadir un repositorio_

_Para añadir un repositorio, utilizamos el comando `add-apt-repository`. Aquí está la descomposición del comando:_

- _`sudo`: Ejecuta el comando como superusuario._
- _`add-apt-repository`: Añade un repositorio a la lista de fuentes de paquetes de APT._
- _`ppa:user/repo`: El repositorio que quieres añadir. PPA significa Personal Package Archive que es su traduccion es fichero de Paquetes Personal._

**_Ejemplo_**

```bash
sudo add-apt-repository ppa:mmstick76/alacritty
```

> _Para instalar un paquete, utilizamos el comando `sudo apt-get install`_

```bash
sudo apt-get install alacritty
```

```bash
sudo apt-get install ./package.deb
```

> _Para instalar un paquete con Snap, utilizamos el comando `snap install`. Por ejemplo, para instalar Alacritty:_

```bash
sudo snap install --classic code
```

> _Instalación de paquetes con dpkg_

_Para instalar un paquete .deb con dpkg, utilizamos el comando dpkg -i. Por ejemplo, para instalar un paquete llamado package.deb:_

```bash
sudo dpkg -i package.deb
```

_Cuando se usa con dpkg, el comando `-i` o `--install` indica que se debe instalar un paquete. En este caso, package.deb es el paquete que se va a instalar._

---

# **_Cambiar el tema de la terminal en Ubuntu_**

1. _Abre la terminal._

   1. Crea un fichero one-dark.sh

      1. ```bash
         touch ./one-dark.sh
         ```

      2. ```bash
          nano one-dark.sh
         ```

      3. Colocar esto en el fichero one-dark.s

         1. ```bash
            #!/usr/bin/env bash
            # ONE DARK
            # --- ----
            # Gnome Terminal color scheme install script
            # Based on:
            #   https://github.com/chriskempson/base16-gnome-terminal/

            [[ -z "$PROFILE_NAME" ]] && PROFILE_NAME="One Dark"
            [[ -z "$PROFILE_SLUG" ]] && PROFILE_SLUG="one-dark"
            [[ -z "$DCONF" ]] && DCONF=dconf
            [[ -z "$UUIDGEN" ]] && UUIDGEN=uuidgen

            dset() {
               local key="$1"; shift
               local val="$1"; shift

               if [[ "$type" == "string" ]]; then
                  val="'$val'"
               fi

               "$DCONF" write "$PROFILE_KEY/$key" "$val"
            }

            # because dconf still doesn't have "append"
            dlist_append() {
               local key="$1"; shift
               local val="$1"; shift

               local entries="$(
                  {
                        "$DCONF" read "$key" | tr -d '[]' | tr , "\n" | fgrep -v "$val"
                        echo "'$val'"
                  } | head -c-1 | tr "\n" ,
               )"

               "$DCONF" write "$key" "[$entries]"
            }

            # Newest versions of gnome-terminal use dconf
            if which "$DCONF" > /dev/null 2>&1; then
               [[ -z "$BASE_KEY_NEW" ]] && BASE_KEY_NEW=/org/gnome/terminal/legacy/profiles:

               if [[ -n "`$DCONF list $BASE_KEY_NEW/`" ]]; then
                  if which "$UUIDGEN" > /dev/null 2>&1; then
                        PROFILE_SLUG=`uuidgen`
                  fi

                  if [[ -n "`$DCONF read $BASE_KEY_NEW/default`" ]]; then
                        DEFAULT_SLUG=`$DCONF read $BASE_KEY_NEW/default | tr -d \'`
                  else
                        DEFAULT_SLUG=`$DCONF list $BASE_KEY_NEW/ | grep '^:' | head -n1 | tr -d :/`
                  fi

                  DEFAULT_KEY="$BASE_KEY_NEW/:$DEFAULT_SLUG"
                  PROFILE_KEY="$BASE_KEY_NEW/:$PROFILE_SLUG"

                  # copy existing settings from default profile
                  $DCONF dump "$DEFAULT_KEY/" | $DCONF load "$PROFILE_KEY/"

                  # add new copy to list of profiles
                  dlist_append $BASE_KEY_NEW/list "$PROFILE_SLUG"

                  # update profile values with theme options
                  dset visible-name "'$PROFILE_NAME'"
                  dset palette "['#000000', '#e06c75', '#98c379', '#d19a66', '#61afef', '#c678dd', '#56b6c2', '#abb2bf', '#5c6370', '#e06c75', '#98c379', '#d19a66', '#61afef', '#c678dd', '#56b6c2', '#ffffff']"
                  dset background-color "'#282c34'"
                  dset foreground-color "'#abb2bf'"
                  dset bold-color "'#ABB2BF'"
                  dset bold-color-same-as-fg "true"
                  dset use-theme-colors "false"
                  dset use-theme-background "false"

                  unset PROFILE_NAME
                  unset PROFILE_SLUG
                  unset DCONF
                  unset UUIDGEN
                  exit 0
               fi
            fi

            # Fallback for Gnome 2 and early Gnome 3
            [[ -z "$GCONFTOOL" ]] && GCONFTOOL=gconftool
            [[ -z "$BASE_KEY" ]] && BASE_KEY=/apps/gnome-terminal/profiles

            PROFILE_KEY="$BASE_KEY/$PROFILE_SLUG"

            gset() {
               local type="$1"; shift
               local key="$1"; shift
               local val="$1"; shift

               "$GCONFTOOL" --set --type "$type" "$PROFILE_KEY/$key" -- "$val"
            }

            # Because gconftool doesn't have "append"
            glist_append() {
               local type="$1"; shift
               local key="$1"; shift
               local val="$1"; shift

               local entries="$(
                  {
                        "$GCONFTOOL" --get "$key" | tr -d '[]' | tr , "\n" | grep -f -v "$val"
                        echo "$val"
                  } | head -c-1 | tr "\n" ,
               )"

               "$GCONFTOOL" --set --type list --list-type $type "$key" "[$entries]"
            }

            # Append profile to the profile list
            glist_append string /apps/gnome-terminal/global/profile_list "$PROFILE_SLUG"

            gset string visible_name "$PROFILE_NAME"
            gset string palette "#000000:#e06c75:#98c379:#d19a66:#61afef:#c678dd:#56b6c2:#abb2bf:#5c6370:#e06c75:#98c379:#d19a66:#61afef:#c678dd:#56b6c2:#ffffff"
            gset string background_color "#282c34"
            gset string foreground_color "#abb2bf"
            gset string bold_color "#abb2bf"
            gset bool   bold_color_same_as_fg "true"
            gset bool   use_theme_colors "false"
            gset bool   use_theme_background "false"

            unset PROFILE_NAME
            unset PROFILE_SLUG
            unset DCONF
            unset UUIDGEN
            ```

2. _Se nos creara un perfil lo seleccionamos y le damos como predeterminado_

   1. ![theme-terminal#1](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-tema-terminal/theme-terminal%231.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-tema-terminal/theme-terminal%231.png?raw=true")
   2. ![theme-terminal#2](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-tema-terminal/theme-terminal%232.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-tema-terminal/theme-terminal%232.png?raw=true")

3. _Configurando fuente, transparencia, tamaño_

   1. ![theme-terminal#3](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-tema-terminal/theme-terminal%233.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-tema-terminal/theme-terminal%233.png?raw=true")
   2. ![theme-terminal#4](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-tema-terminal/theme-terminal%234.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-tema-terminal/theme-terminal%234.png?raw=true")

> _Instalación de curl en Ubuntu_

_curl es una herramienta de línea de comandos que permite transferir datos desde o hacia un servidor. Soporta una multitud de protocolos, incluyendo HTTP, HTTPS, FTP y SFTP. Es muy útil para descargar ficheros, probar APIs y mucho más._

_Para instalar curl en Ubuntu, puedes usar el comando `apt-get install` de la siguiente manera:_

```bash
sudo apt-get install curl
```

---

# **_Permisos en linux_**

> _En linux existen diferentes tipos de permisos para los ficheros y directorios, estos son: **lectura**, **escritura** y **ejecución**. Los tres primeros son para el usuario, los otros tres permisos son para grupos y los ultimos tres permisos son para otros usuario_

1. _**Lectura**: Permite ver el contenido del fichero o directorio._

2. _**Escritura**: Permite modificar el contenido del fichero o directorio._

3. _**Ejecución**: Permite ejecutar el fichero o acceder al directorio._

4. _**Orden**: El primero es lectura, el segundo escritura el ultimo. `---------` significa que el archivo o directorio no tiene ningún permiso establecido para el propietario, el grupo y otros usuarios._

> para ver los permisos de un fichero o directorio, utilizamos el comando `ls -l`.

1. _Si es un fichero, el primer carácter será una -._

   1. ```bash
      ls -l fichero.py
      ```

   2. **Output**: `-rw-rw-r-- 1 daniel daniel    0 feb  1 16:04 fichero.py`

      1. `-rw-rw-r--`: _Estos son los permisos del archivo. Se dividen en cuatro partes:_

      2. _El primer carácter `-` indica el tipo de archivo. Un `-` significa que es un archivo regular. Algunos otros valores posibles incluyen `d` para directorios y `l` para enlaces simbólicos._

      3. _Los siguientes tres caracteres `rw-` representan los permisos del propietario del archivo. En este caso, el propietario tiene permisos de lectura `(r)` y escritura `(w)`._

      4. _Los siguientes tres caracteres `rw-` representan los permisos del grupo del archivo. Al igual que el propietario, el grupo tiene permisos de lectura `(r)` y escritura `(w)`._

      5. _Los últimos tres caracteres `r--` representan los permisos de todos los demás usuarios. En este caso, otros usuarios solo tienen permisos de lectura `(r)`._

      6. _`1`: Este es el número de enlaces al archivo. Un archivo regular tendrá al menos 1._

      7. _`daniel`: El primer daniel es el propietario del archivo._

      8. _`daniel`: El segundo daniel es el grupo del archivo._

      9. _`0`: Este es el tamaño del archivo en bytes._

      10. _`feb 1 16:04`: Esta es la fecha y hora de la última modificación del archivo._

      11. _`fichero.py`: Este es el nombre del archivo._

2. _Si es un directorio, el primer carácter será una d._

   1. ```bash
      ls -l fichero.py
      ```

      1. _Output: `drwxrwxr-x`: Estos son los permisos del directorio. Se dividen en cuatro partes:_

         1. _El primer carácter d indica el tipo. Un d significa que es un directorio._

         2. _Los siguientes tres caracteres rwx representan los permisos del grupo del directorio. Al igual que el propietario, el grupo tiene permisos de lectura `(r)`, escritura `(w)` y ejecución `(x)`._

         3. _Los últimos tres caracteres r-x representan los permisos de todos los demás usuarios. En este caso, otros usuarios tienen permisos de lectura `(r)` y ejecución `(x)`, pero no de escritura._

         4. _`2`: Este es el número de enlaces al directorio. Para los directorios, este número es el número de subdirectorios + 2 (uno por el directorio mismo y otro por su directorio padre)._

         5. _`daniel`: El primer daniel es el propietario del directorio._

         6. _`daniel`: El segundo daniel es el grupo del directorio._

         7. _`4096:` Este es el tamaño del directorio en bytes. Este número representa el tamaño del espacio en disco que se utiliza para almacenar las metainformaciones del directorio, pero no el tamaño de los archivos dentro del directorio._

         8. _`feb 1 16:04`: Esta es la fecha y hora de la última modificación del directorio._

         9. _`directorio`: Este es el nombre del directorio._

> _En la primera posición, un guion `-` indica que el elemento es un archivo regular. Otros posibles valores en esta posición incluyen `d` para directorios, `l` para enlaces simbólicos, `s` para sockets, `p` para pipes, `c` para archivos de caracteres especiales y `b` para archivos de bloques especiales._

1. > _un guion `-` indica la ausencia de un permiso. Los permisos se representan con las letras `r` para lectura, `w` para escritura y `x` para ejecución. Si uno de estos permisos no está presente, se representa con un guion `-`._

2. _Si es un enlace simbólico, el primer carácter será una l._

3. _Si es un fichero regular, el primer carácter será un guion._

4. > _Para cambiar los permisos de un fichero o directorio, utilizamos el comando `chmod`._

> _`chmod [opciones] modo archivo`_

-._`u` (usuario), `g` (grupo), `o` (otros), `a` (todos): especifica a quién se aplicarán los cambios._

-._`+` (añadir permisos), `-` (quitar permisos), `=` (establecer permisos): especifica qué acción se realizará._

-._`r` (lectura), `w` (escritura), `x` (ejecución): especifica qué permisos se cambiarán._

-._Añadir permisos al usuario_

1. ```bash
   chmod u+w fichero.py
   ```

2. ```bash
   chmod u+r fichero.py
   ```

3. ```bash
   chmod u+x fichero.py
   ```

-. _Añadir permisos al grupo_

1. ```bash
   chmod g+w fichero.py
   ```

2. ```bash
   chmod g+r fichero.py
   ```

3. ```bash
   chmod g+x fichero.py
   ```

-. _Añadir permisos a otros usarios_

1. ```bash
   chmod o+w fichero.py
   ```

2. ```bash
   chmod o+r fichero.py
   ```

3. ```bash
   chmod o+x fichero.py
   ```

-. _Quitar permisos al usuario_

1. ```bash
   chmod u-w fichero.py
   ```

2. ```bash
   chmod u-r fichero.py
   ```

3. ```bash
   chmod u-x fichero.py
   ```

-. _Quitar permisos al grupo_

1. ```bash
   chmod g-w fichero.py
   ```

2. ```bash
   chmod g-r fichero.py
   ```

3. ```bash
   chmod g-x fichero.py
   ```

-. _Quitar permisos a otros usarios_

1. ```bash
   chmod o-w fichero.py
   ```

2. ```bash
   chmod o-r fichero.py
   ```

3. ```bash
   chmod o-x fichero.py
   ```

-. _Añadir multiples permisos separando por coma_

1. ```bash
   chmod u+x,g+r,o+w fichero.py
   ```

2. ```bash
   chmod u-x,g-r,o-w fichero.py
   ```

3. ```bash
   chmod u-x,g+r,g+x fichero.py
   ```

-. \*Establecer permisos de lectura y escritura y ejecucion para todos los usuarios en el archivo fichero.py **a: Esto significa "todos", que incluye al usuario propietario, al grupo y a otros usuarios.**

1. ```bash
   chmod a=rwx fichero.py
   ```

2. ```bash
   chmod a=rw fichero.py
   ```

3. ```bash
   chmod a=r fichero.py
   ```

> _Los permisos en Linux se pueden representar en forma binaria, pero la representación binaria se convierte a decimal para su uso con el comando chmod._

1. _`r (lectura)` se representa como `4` en decimal, `100` en binario._

2. _`w (escritura)` se representa como `2` en decimal, `010` en binario._

3. _`x (ejecución)` se representa como `1` en decimal, `001` en binario._

> _Por lo tanto, si quieres dar permisos de lectura, escritura y ejecución al propietario `(rwx)`, y solo lectura al grupo y a otros `(r--)`_

1. ```bash
   chmod 744 fichero.py
   ```

> _En este caso, `7` `(4+2+1)` en decimal representa `rwx` en binario para el propietario, y `4` en decimal representa `r--` en binario para el grupo y otros. `-rwxr--r-- 1 daniel daniel    0 feb  1 16:04 fichero.py`_

1. `000` es igual a `---` (ningún permiso)
2. `001` es igual a `--x` (permiso de ejecución)
3. `010` es igual a `-w-` (permiso de escritura)
4. `011` es igual a `-wx` (permisos de escritura y ejecución)
5. `100` es igual a `r--` (permiso de lectura)
6. `101` es igual a `r-x` (permisos de lectura y ejecución)
7. `110` es igual a `rw-` (permisos de lectura y escritura)
8. `111` es igual a `rwx` (permisos de lectura, escritura y ejecución)

| Decimal | Binario |
| ------- | ------- |
| 0       | 0000    |
| 1       | 0001    |
| 2       | 0010    |
| 3       | 0011    |
| 4       | 0100    |
| 5       | 0101    |
| 6       | 0110    |
| 7       | 0111    |
| 8       | 1000    |
| 9       | 1001    |
| 10      | 1010    |
| 11      | 1011    |
| 12      | 1100    |
| 13      | 1101    |
| 14      | 1110    |
| 15      | 1111    |

- Los siguientes tres caracteres `---` representan los permisos del grupo del archivo. Al igual que el propietario, el grupo no tiene permisos de lectura, escritura ni ejecución.

- Los últimos tres caracteres `---` representan los permisos de todos los demás usuarios. En este caso, otros usuarios tampoco tienen permisos de lectura, escritura ni ejecución.

Por lo tanto, un archivo con permisos `---------` no sería accesible para ninguna operación de lectura, escritura o ejecución.

> _Un **enlace duro** es esencialmente un nombre adicional para un archivo existente en los sistemas de archivos de Unix y Linux. Todos los enlaces duros a un archivo realmente se refieren al mismo archivo, y es posible tener varios enlaces duros a un solo archivo._ > _Un **enlace simbólico** (también conocido como symlink o soft link) es un tipo especial de archivo que sirve como referencia a otro archivo o directorio._

**Conceptos y usos:**

- _Los enlaces duros son útiles cuando quieres tener acceso rápido a un archivo que está en un directorio diferente sin tener que navegar a ese directorio._

- _Los enlaces simbólicos son útiles cuando quieres crear un enlace a un directorio (los enlaces duros a directorios no están permitidos en Linux) o cuando quieres crear un enlace a un archivo que está en otro sistema de archivos._

**Para crear un enlace duro:**

```bash
ln archivo_origen enlace_duro
```

```bash
ln fichero.py enlace_duro.py
```

**Para crear un enlace simbólico:**

```bash
ln -s archivo_origen enlace_simbolico
```

`-s, --symbolic              crea enlaces simbólicos en vez de enlaces duros`

```bash
ln -s fichero.py enlace_simbolico.py
```

**output**: `lrwxrwxrwx 1 daniel daniel 20 feb  2 13:03 enlace_simbolico.py -> ./carpeta/fichero.py`

_`l` significa que es un enlace simbólico._

_`enlace_simbolico.py`: Este es el nombre del enlace simbólico._

_`->`: Este símbolo indica que el archivo es un enlace simbólico que apunta a otro archivo._

_`./carpeta/fichero.py`: Este es el archivo al que apunta el enlace simbólico. En este caso, el enlace simbólico enlace_simbolico.py apunta al archivo fichero.py en el directorio carpeta_

**Ejemplo en código:**

Supongamos que tienes un archivo llamado `fichero.py` y quieres crear un enlace duro llamado `enlace_duro` y un enlace simbólico llamado `enlace_simbolico`.

Para el enlace duro, usarías:

```bash
ln fichero.py enlace_duro
```

Para el enlace simbólico, usarías:

```bash
ln -s fichero.py enlace_simbolico
```

Después de ejecutar estos comandos, tanto `enlace_duro` como `enlace_simbolico` apuntarán a `fichero1.py`. Sin embargo, si `fichero1.py` se mueve o se elimina, `enlace_duro` seguirá apuntando al contenido del archivo original, mientras que `enlace_simbolico` se romperá y no apuntará a nada.

**un enlace simbólico es similar a un acceso directo en Windows. Apunta a la ubicación de un archivo o directorio real en el sistema de archivos.**

**_Utilidades de Enlaces duros y simbolicos_**

> _Los enlaces simbólicos y duros son útiles para hacer que un archivo o directorio esté disponible en múltiples ubicaciones sin duplicar el contenido real._

**Enlaces duros:**

1. **Backup de archivos**: _Los enlaces duros pueden ser útiles para hacer copias de seguridad de archivos. Si creas un enlace duro a un archivo y luego modificas el archivo, el enlace duro reflejará los cambios, ya que ambos apuntan a los mismos datos._

**Enlaces simbólicos:**

1. **Versionado de software**: _Los enlaces simbólicos son comúnmente utilizados para cambiar fácilmente entre diferentes versiones de un programa. Por ejemplo, podrías tener `programa-1.0` y `programa-1.1` en tu sistema, con un enlace simbólico llamado `programa` que apunta a la versión que deseas usar. Cuando quieras cambiar de versión, simplemente cambias a qué versión apunta el enlace simbólico._

2. **Crear accesos rápidos**: _Los enlaces simbólicos pueden actuar como accesos rápidos a archivos o directorios que se utilizan con frecuencia. Por ejemplo, podrías tener un enlace simbólico a un directorio de logs o a un archivo de configuración en tu directorio de inicio para un acceso rápido._

> _Recuerda que los enlaces duros no pueden referirse a directorios ni pueden cruzar sistemas de archivos, mientras que los enlaces simbólicos pueden hacer ambas cosas._
