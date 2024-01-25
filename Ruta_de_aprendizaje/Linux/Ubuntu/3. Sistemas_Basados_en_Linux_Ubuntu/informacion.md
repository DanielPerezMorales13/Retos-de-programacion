_Sistemas basados en Linux Ubuntu_

**Indice**

- [**_Usuarios en linux_**](#usuarios-en-linux)
- [**_Configurando GRUB en Ubuntu_**](#configurando-grub-en-ubuntu)
- [**_Atajo Linux!!_**](#atajo-linux)
- [_Gestores de paquetes en Linux Ubuntu_](#gestores-de-paquetes-en-linux-ubuntu)
- [_Cambiar el tema de la terminal en Ubuntu_](#cambiar-el-tema-de-la-terminal-en-ubuntu)

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

_GRUB es muy flexible y potente, ya que puede cargar una amplia variedad de sistemas operativos y también puede cargar una gran cantidad de formatos de archivo de kernel._

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

   4. _El fichero real de la configuracion del grub se encuentra en esta ruta **`/bootgrub/grub.cfg`**.Este archivo es la configuración principal de GRUB, el gestor de arranque._

      1. ```bash
          sudo nano /boot/grub/grub.cfg
         ```

      2. ```bash
          cat /boot/grub/grub.cfg
         ```

   - con cat`/bootgrub/grub.cfg` Este comando mostrará el contenido del archivo grub.cfg, que incluye las entradas del menú de arranque, las opciones de arranque y otros ajustes de GRUB. Este archivo normalmente no se edita directamente, sino que se genera a partir de otros archivos de configuración mediante el comando update-grub.

   - La extensión .cfg se utiliza generalmente para archivos de configuración. Estos archivos contienen los ajustes para programas y aplicaciones. En este caso, grub.cfg contiene la configuración para el gestor de arranque GRUB.

3. ![img-grup#3](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-grub/img-grup%233.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-grub/img-grup%233.png?raw=true")

   1. _La línea GRUB_DEFAULT=0 es una configuración en el archivo de configuración de GRUB, que normalmente se encuentra en /etc/default/grub en sistemas Linux._

      - _GRUB_DEFAULT controla qué entrada del menú de GRUB se selecciona por defecto cuando el sistema arranca. Las entradas del menú se cuentan desde 0, por lo que GRUB_DEFAULT=0 significa que se seleccionará la primera entrada del menú._

      - _Por ejemplo, si tu menú de GRUB tiene las siguientes entradas:_

        - **Ubuntu**
        - **Advanced options for Ubuntu**
        - **Windows Boot Manager**

      - > _Entonces GRUB_DEFAULT=0 seleccionará "Ubuntu" por defecto._

4. ![img-grup#4](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-grub/img-grup%234.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/img-grub/img-grup%234.png?raw=true")

   1. _La línea GRUB_TIMEOUT=10 es una configuración en el archivo de configuración de GRUB, que normalmente se encuentra en /etc/default/grub en sistemas Linux._

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

# _Gestores de paquetes en Linux Ubuntu_

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
- _`ppa:user/repo`: El repositorio que quieres añadir. PPA significa Personal Package Archive que es su traduccion es Archivo de Paquetes Personal._

**Ejemplo**

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

# _Cambiar el tema de la terminal en Ubuntu_

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

   1. [theme-terminal#1]("")
   2. [theme-terminal#2]("")

3. _Configurando fuente, transparencia, tamaño_

   1. [theme-terminal#3]("")
   2. [theme-terminal#4]("")
