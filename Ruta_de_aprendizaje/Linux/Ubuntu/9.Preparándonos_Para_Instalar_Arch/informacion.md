**_Cómo personalizar el prompt de tu terminal y trabajar con variables de entorno_**

- [**_Personalizar el prompt de tu terminal_**](#personalizar-el-prompt-de-tu-terminal)
- [**_Variables de entorno_**](#variables-de-entorno)
- [**_Crear un comando temporal_**](#crear-un-comando-temporal)
- [**_Crear un comando global_**](#crear-un-comando-global)
- [**_/etc/host_**](#etchost)
- [**_Operadores `&&` y `||`_**](#operadores--y-)

---

# **_Personalizar el prompt de tu terminal_**

> _El prompt de tu terminal se puede personalizar editando la variable de entorno `PS1` en Bash. Puedes generar un prompt personalizado utilizando herramientas en línea como [**Bash Prompt Generator**](https://bash-prompt-generator.org/ "https://bash-prompt-generator.org/")._

_Para personalizar tu prompt, sigue estos pasos:_

1. _Ve a [**Bash Prompt Generator**](https://bash-prompt-generator.org/ "https://bash-prompt-generator.org/")._

2. _Personaliza tu prompt utilizando las opciones disponibles._

3. _Copia el código generado._

4. _Abre tu fichero `~/.bashrc` con un editor de texto. Por ejemplo, puedes usar `nano ~/.bashrc` en la terminal._

5. _Pega el código al final del fichero._

6. _Guarda y cierra el fichero._

7. _Reinicia tu terminal o ejecuta `source ~/.bashrc` para que los cambios surtan efecto._

---

# **_Variables de entorno_**

_Las variables de entorno son valores que se pueden utilizar en los procesos de tu sistema operativo. Pueden contener información sobre el sistema, las preferencias del usuario, los detalles de la conexión, etc._

_Las variables de entorno se almacenan en `/etc/environment` y en varios otros ficheros de configuración del sistema y del usuario, como `~/.bashrc` y `~/.bash_profile`._

# **_Crear un comando temporal_**

_Puedes crear un comando temporal en la terminal definiendo una función. Por ejemplo:_

```bash
mi_comando() {
    echo "Este es mi comando temporal"
}
```

_Este comando estará disponible en la sesión de terminal actual, pero desaparecerá una vez que cierres la terminal._

- _`PATH="$PATH:/home/Directorio/comando."`: Este comando añade `/home/Directorio/comando.` al final de la variable de entorno `PATH`. Esto significa que el sistema también buscará programas en `/home/Directorio/comando.` cuando escribas un comando en la terminal. El carácter : se utiliza como separador entre diferentes rutas en la variable PATH._

  - _Cuando escribes un comando en la terminal, el sistema busca el programa correspondiente en los directorios listados en la variable PATH. Los diferentes directorios en PATH están separados por :._

- _No es necesario poner `.sh` al final del nombre del directorio porque `PATH` debe contener directorios, no ficheros individuales. Cuando escribes un comando, el sistema busca un fichero ejecutable con ese nombre en los directorios listados en `PATH`._

- _Cuando ejecutas un comando en la terminal, se crea en la sesión actual de la terminal. Una sesión de terminal dura solo mientras la terminal está abierta. Cuando cierras la terminal, la sesión termina y todos los comandos, variables y procesos que se crearon en esa sesión se pierden._

> [!NOTE]
> _Cuando creas un script de shell, por defecto, puede que no tenga el permiso de ejecución. Esto significa que aunque el fichero contenga código que puede ser ejecutado, el sistema no lo tratará como un programa ejecutable hasta que le des permiso para hacerlo._

---

# **_Crear un comando global_**

> _Para crear un comando que esté disponible en todas las sesiones de terminal, puedes agregar la definición de la función a tu fichero `~/.bashrc`. Por ejemplo:_

```bash
echo 'mi_comando() { echo "Este es mi comando global"; }' >> ~/.bashrc
```

_Después de agregar esta línea, necesitarás reiniciar tu terminal o ejecutar `source ~/.bashrc` para que los cambios surtan efecto._

_El comando `source` en Bash se utiliza para cargar cualquier función o variable en el shell actual. Cuando ejecutas un script, se crea un nuevo shell, se ejecutan los comandos en ese shell y luego se cierra el shell. Pero si quieres que las variables y funciones definidas en el script estén disponibles en el shell actual, necesitas `source` el script._

_Por ejemplo, si tienes un script `myscript.sh` que define una variable:_

```bash
# myscript.sh
MY_VARIABLE="Hello, world!"
```

_Si ejecutas el script normalmente con `./myscript.sh`, la variable `MY_VARIABLE` no estará disponible en el shell actual. Pero si `source` el script con `source myscript.sh`, entonces `MY_VARIABLE` estará disponible._

_Esto es especialmente útil para scripts que definen variables de entorno, funciones, alias, etc., que quieres que estén disponibles en tu shell actual. Por ejemplo, a menudo se utiliza `source` para cargar variables de entorno desde un fichero `.env` o para actualizar el shell actual después de modificar ficheros de configuración como `~/.bashrc` o `~/.bash_profile`._

- `$PATH`: Es una variable de entorno que el sistema operativo utiliza para buscar programas. Cuando escribes un comando en la terminal, el sistema busca el programa en los directorios listados en `PATH`.

- `$USER`: Es una variable de entorno que contiene el nombre del usuario actual.

- `$PWD`: Es una variable de entorno que contiene el directorio de trabajo actual.

- _Si quieres que un comando esté disponible incluso después de cerrar la terminal, necesitas agregar la definición del comando a un fichero de configuración de shell que se lee cada vez que se inicia una nueva sesión de terminal. Para Bash, los ficheros de configuración comunes son `~/.bashrc` y `~/.bash_profile`._

_Por ejemplo, si agregas la definición de un comando a tu fichero `~/.bashrc`:_

```bash
echo 'mi_comando() { echo "Este es mi comando"; }' >> ~/.bashrc
```

- _Y luego ejecutas `source ~/.bashrc` para cargar las nuevas definiciones en tu sesión actual, el comando `mi_comando` estará disponible en todas las nuevas sesiones de terminal._

_En cuanto a `/w` y `/W` en el fichero `.bashrc`, son secuencias de escape que se utilizan en la variable `PS1` para personalizar el prompt de la terminal:_

- _`\w` se expande al directorio de trabajo actual, con el nombre de ruta completo._

- _`\W` se expande al nombre base del directorio de trabajo actual, es decir, solo el último componente de la ruta._

_Por ejemplo, si estás en el directorio `/home/usuario/proyectos`, `\w` se expandirá a `/home/usuario/proyectos` y `\W` se expandirá a `proyectos`._

_Aquí hay un ejemplo de cómo podrías usar `\w` y `\W` en tu fichero `.bashrc` para personalizar tu prompt:_

```bash
PS1="\u@\h:\w\$ "  # El prompt será "usuario@host:/ruta/completa$ "
```

```bash
PS1="\u@\h:\W\$ "  # El prompt será "usuario@host:directorio$ "
```

_Después de agregar estas líneas a tu `.bashrc`, necesitarás ejecutar `source ~/.bashrc` para que los cambios surtan efecto._

**El fichero `.bashrc` se encuentra generalmente en el directorio de inicio del usuario. En un sistema Unix-like, puedes acceder a él con la ruta `~/.bashrc` o `/home/username/.bashrc`, donde `username` es tu nombre de usuario.**

# **_/etc/host_**

_Para editar tu hostname en Linux, puedes usar el comando `hostnamectl`. Aquí hay un ejemplo de cómo cambiar tu hostname a "mi-nuevo-host":_

```bash
sudo hostnamectl set-hostname mi-nuevo-host
```

> [!NOTE]
> **Después de ejecutar este comando, necesitarás reiniciar tu sistema para que los cambios surtan efecto.**

```bash
127.0.0.1       localhost
127.0.1.1       daniel-B550-GAMING-X

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

_El fichero `/etc/hosts` es un fichero de configuración del sistema operativo que mapea los nombres de host a las direcciones IP. Es una de las varias formas en que un sistema puede resolver los nombres de host._

_En tu fichero `/etc/hosts`, tienes varias entradas:_

- _`127.0.0.1 localhost`: Esta línea mapea el nombre de host `localhost` a la dirección IP `127.0.0.1`, que es la dirección IP de loopback. Esto significa que `localhost` siempre se referirá a tu propia máquina._

- _`127.0.1.1 daniel-B550-GAMING-X`: Esta línea mapea el nombre de host `daniel-B550-GAMING-X` a la dirección IP `127.0.1.1`. Esto es común en los sistemas Debian y Ubuntu, donde el nombre de host del sistema se mapea a esta dirección IP en lugar de la dirección IP real del sistema._

- _Las líneas que comienzan con `::1` y `fe00::0` son similares, pero para IPv6 en lugar de IPv4._

_Si quieres agregar un nuevo mapeo de nombre de host a dirección IP, puedes agregar una nueva línea a este fichero. Por ejemplo, si quieres que `mi-servidor` se resuelva a la dirección IP `192.168.1.100`, podrías agregar esta línea:_

```bash
192.168.1.100 mi-servidor
```

- _Después de hacer cambios en `/etc/hosts`, no necesitas reiniciar ni recargar ningún servicio. Los cambios surtirán efecto inmediatamente._

# **_Operadores `&&` y `||`_**

> _Los operadores `&&` y `||` en Bash se utilizan para combinar comandos basándose en si el comando anterior tuvo éxito o no._

```bash
mkdir dir && touch fichero.sh
```

```bash
mkdir dir || touch fichero.sh
```

- _`&&` ejecuta el segundo comando solo si el primer comando tuvo éxito. En tu ejemplo, `touch fichero.sh` solo se ejecutará si `mkdir dir` tiene éxito._

- _`||` ejecuta el segundo comando solo si el primer comando falla. En tu ejemplo, `touch fichero.sh` solo se ejecutará si `mkdir dir` falla._

_Aquí tienes un ejemplo que muestra la diferencia:_

```bash
# Crear un directorio que ya existe, por lo que fallará
mkdir ~/Documents && echo "El directorio se creó con éxito" || echo "El directorio ya existe"
```

- _En este caso, `mkdir ~/Documents` fallará si el directorio `~/Documents` ya existe. Como resultado, `echo "El directorio se creó con éxito"` no se ejecutará, pero `echo "El directorio ya existe"` sí se ejecutará._

**Para crear un alias, puedes usar el comando `alias`. Aquí tienes un ejemplo:**

```bash
alias mi_comando='echo Hola, mundo!'
```

> _Después de ejecutar este comando, puedes escribir `mi_comando` en la terminal para ejecutar `echo Hola, mundo!`. Este alias solo durará hasta que cierres la terminal. Si quieres que el alias sea permanente, puedes agregar el comando `alias` a tu fichero `~/.bashrc`._

_El comando `cd -` en Bash te lleva al directorio en el que estabas antes del directorio actual. Es una forma rápida de cambiar entre dos directorios._

_Por ejemplo, si estás en el directorio `/home/usuario` y luego cambias al directorio `/etc`, puedes usar `cd -` para volver a `/home/usuario`._

_Aquí tienes un ejemplo de cómo se usaría:_

```bash
cd /etc
```

```bash
cd -
```

_Después de ejecutar estos comandos, te encontrarás de nuevo en el directorio en el que estabas antes de cambiar a `/etc`._

*Para formatear una unidad USB en Ubuntu, puedes seguir estos pasos utilizando la utilidad de discos:*

1. *Inserta tu unidad USB en tu computadora.*

2. *Abre la aplicación "Discos" desde el menú de aplicaciones.*

3. *En la lista de dispositivos de almacenamiento en el lado izquierdo, selecciona tu unidad USB.*

4. *Selecciona la partición que deseas formatear en el diagrama de particiones. Normalmente, una unidad USB tiene una sola partición.*

5. *Haz clic en el botón de "Menú" (los dos engranajes) debajo del diagrama de particiones y selecciona "Format Partition...".*

6. *En el cuadro de diálogo que aparece, puedes elegir el tipo de sistema de ficheros y darle un nombre a la partición. Para la mayoría de los usos, puedes seleccionar "Compatible with all systems (FAT)" como el tipo de sistema de ficheros.*

7. *Haz clic en "Format..." para formatear la partición. Ten en cuenta que esto borrará todos los datos en la partición, así que asegúrate de tener una copia de seguridad de cualquier dato importante.*

*Después de seguir estos pasos, tu unidad USB estará formateada y lista para usar.*

- *Para formatear un disco usando `mkfs` en Linux, primero necesitas conocer el nombre del dispositivo que deseas formatear. Puedes usar el comando `lsblk` o `fdisk -l`,`-l` es una abreviatura de `--list`para listar tus dispositivos de almacenamiento.*

```bash
fdisk -l
```

```bash
fdisk --list
```

*Una vez que sepas cuál es tu dispositivo, puedes usar `mkfs` para formatearlo. Por ejemplo, si tu dispositivo es `/dev/sdb`, puedes formatearlo a ext4 con el siguiente comando:*

```bash
sudo mkfs.ext4 /dev/sdb
```

- **ext4** *es la abreviatura de "fourth extended filesystem", o "cuarto sistema de ficheros extendido" en español. Es un sistema de ficheros de tipo journaling para Linux, y es la evolución de los anteriores sistemas de ficheros ext2 y ext3.*

  - *Un sistema de ficheros define cómo se almacenan y organizan los datos en un dispositivo de almacenamiento. ext4 es uno de los sistemas de ficheros más comúnmente utilizados en Linux debido a sus características, que incluyen soporte para grandes tamaños de fichero y sistema de ficheros, journaling para mejorar la fiabilidad, y varias mejoras de rendimiento sobre sus predecesores.*

  - *Cuando formateas un disco o una partición con ext4, estás preparando ese disco o partición para almacenar datos de acuerdo con las reglas y estructuras definidas por el sistema de ficheros ext4.*

> [!WARNING]
> **¡Cuidado!** *Este comando borrará todos los datos en `/dev/sdb`. Asegúrate de que estás formateando el dispositivo correcto y de que has hecho una copia de seguridad de todos los datos importantes.*

*Después de ejecutar este comando, tu dispositivo estará formateado con el sistema de ficheros ext4 y estará listo para ser montado y utilizado.*

> [!NOTE]
> *Nota: Reemplaza `/dev/sdb` con el nombre de tu dispositivo.*

- *La opción `-l` con `fdisk`, es decir, `fdisk -l` o `fdisk --fs`, se utiliza para listar todas las particiones de disco en el sistema. Muestra información detallada sobre las particiones, incluyendo el dispositivo, el tipo de partición, el tamaño y más.*

- *Por otro lado, `lsblk` es otro comando en sistemas Linux que también lista información sobre todos los bloques de dispositivos, que incluyen dispositivos de disco y sus particiones. `lsblk` muestra la información en un formato de árbol por defecto, lo que puede ser más fácil de leer si tienes muchos dispositivos y particiones.*

*Aquí tienes un ejemplo de cómo se usaría `lsblk`:*

```bash
lsblk
```

*Esto listará todos tus dispositivos de bloque y sus particiones en un formato de árbol. Si quieres más detalles, puedes usar la opción `-f` o `--fs`:*

```bash
lsblk -f
```

```bash
lsblk --fs
```

*Esto mostrará información adicional, como el sistema de ficheros de cada partición y su UUID.*

- **Como formatear usb por imagenes**

1. ![Img-Formatear-Usb#1]("")

2. ![Img-Formatear-Usb#2]("")

3. ![Img-Formatear-Usb#3]("")

4. ![Img-Formatear-Usb#4]("")

5. ![Img-Formatear-Usb#5]("")

6. ![Img-Formatear-Usb#6]("")

7. ![Img-Formatear-Usb#7]("")

8. ![Img-Formatear-Usb#8]("")
