**_Detalles de sistemas linux_**

> _El fichero `/etc/passwd` es un fichero de sistema en Unix y Linux que contiene información sobre todos los usuarios del sistema. Cada línea del fichero representa un usuario y está dividida en siete campos separados por dos puntos (`:`). Aquí está lo que significa cada campo:_

1. **\*Nombre de usuario**: El nombre que los usuarios introducen cuando inician sesión en el sistema.\*

2. **\*Contraseña**: En la mayoría de los sistemas modernos, este campo contiene una `x`, lo que significa que la contraseña está almacenada en el fichero `/etc/shadow`, que es más seguro.\*

3. **\*UID (User ID)**: El identificador numérico único del usuario. El root tiene siempre el UID 0.\*

4. **\*GID (Group ID)**: El identificador numérico único del grupo principal del usuario.\*

5. **\*Información del usuario**: Un campo que puede contener información adicional sobre el usuario, como su nombre completo.\*

6. **\*Directorio de inicio**: La ruta al directorio que se convierte en el directorio de trabajo actual cuando el usuario inicia sesión.\*

7. **\*Shell de inicio de sesión**: La ruta al programa que se ejecuta cuando el usuario inicia sesión. Normalmente es un intérprete de comandos como `/bin/bash`, pero también puede ser `/usr/sbin/nologin` para usuarios que no deben iniciar sesión.\*

**La línea `root:x:0:0:root:/root:/bin/bash`:**

- _`root` es el nombre de usuario._

- _`x` indica que la contraseña está en `/etc/shadow`._

- _`0` es el UID._

- _El segundo `0` es el GID._

- _El segundo `root` es la información del usuario._

- _`/root` es el directorio de inicio._

- _`/bin/bash` es la shell de inicio de sesión._

1. **Contraseña encriptada**: _En sistemas Unix y Linux modernos, las contraseñas de los usuarios no se almacenan en texto plano por razones de seguridad. En su lugar, se almacenan en una forma encriptada en el fichero `/etc/shadow`, que solo puede ser leído por el usuario root. En el fichero `/etc/passwd`, este campo se reemplaza generalmente por una 'x' o un '_'.\*

2. **Shells**: _Un shell es un programa que proporciona la interfaz de línea de comandos para interactuar con el sistema operativo. Hay muchos shells disponibles, como bash (Bourne Again SHell), sh (Bourne SHell), csh (C SHell), ksh (Korn SHell), zsh (Z SHell), fish (Friendly Interactive SHell), etc. El shell predeterminado para la mayoría de los sistemas Linux es bash._

3. **Daemon**: _En Unix y Linux, un daemon es un programa que se ejecuta en segundo plano y proporciona servicios que no están directamente controlados por un usuario. Estas tareas pueden incluir servicios como la gestión de redes, la programación de tareas, la auditoría de seguridad y muchas otras funciones del sistema operativo. En el fichero `/etc/passwd`, 'daemon' es un usuario del sistema que se utiliza para ejecutar estos programas. Este usuario tiene permisos muy limitados y no puede iniciar sesión en el sistema, lo que ayuda a mejorar la seguridad. En la mayoría de los casos, los programas de daemon se ejecutan con los permisos mínimos necesarios para realizar su tarea. Puedes pensar en 'daemon' como un tipo de "usuario bot" en sistemas Unix y Linux._

4. **daniel:x:1000:1000:daniel,,,:/home/daniel:/bin/bash**: Esta es la entrada para el usuario 'daniel'. Aquí está lo que significa cada campo:

   - _`daniel`: nombre de usuario._
   - _`x`: indica que la contraseña está en `/etc/shadow`._
   - _`1000`: UID del usuario._
   - _`1000`: GID del grupo principal del usuario._
   - _`daniel,,,`: información del usuario._
   - _`/home/daniel`: directorio de inicio del usuario._
   - _`/bin/bash`: shell de inicio de sesión del usuario._

- _`cat /etc/group`: Este comando muestra el contenido del fichero `/etc/group`, que es un fichero de sistema en Unix y Linux que contiene información sobre los grupos del sistema. Cada línea del fichero representa un grupo y está dividida en cuatro campos separados por dos puntos (`:`): el nombre del grupo, la contraseña del grupo (generalmente está vacía o es una 'x'), el GID (Group ID) y una lista de los nombres de usuario que son miembros del grupo._

- _`cat /etc/sudoers`: Este comando muestra el contenido del fichero `/etc/sudoers`, que es un fichero de configuración para el comando `sudo`. Este fichero define qué usuarios pueden ejecutar qué comandos como root (o como otro usuario) y con qué restricciones. Por razones de seguridad, este fichero solo debe editarse con el comando `visudo`, que bloquea el fichero para otros usuarios y realiza una comprobación de sintaxis antes de guardar._

- **Servicios en segundo plano**

- *`systemctl` es una utilidad de línea de comandos en sistemas Linux que interactúa con el sistema `systemd` para gestionar servicios y unidades del sistema.*

- *`sudo systemctl enable mongodb`: Este comando habilita el servicio `mongodb` para que se inicie automáticamente en el arranque del sistema. `sudo` se utiliza para ejecutar el comando con privilegios de root.*

- *`sudo systemctl disable mongodb`: Este comando deshabilita el servicio `mongodb` para que no se inicie automáticamente en el arranque del sistema.*

- `sudo`: Es una abreviatura de "SuperUser DO". En español, podría traducirse como "Hacer Como SuperUsuario". Se utiliza para ejecutar comandos con privilegios de superusuario o root.

- *`systemctl`: Es una abreviatura de "System Control". En español, podría traducirse como "Control del Sistema". Es una herramienta para interactuar con el sistema `systemd`.*

- *`systemd`: Es una abreviatura de "System Daemon". En español, podría traducirse como "Demonio del Sistema". Es un sistema de inicio y un gestor de servicios para Linux. Se utiliza para arrancar el sistema y gestionar servicios del sistema.*

- *`enable`: En inglés significa "habilitar". En este contexto, se utiliza para habilitar un servicio para que se inicie automáticamente en el arranque del sistema.*

- *`disable`: En inglés significa "deshabilitar". En este contexto, se utiliza para deshabilitar un servicio para que no se inicie automáticamente en el arranque del sistema.*

- *`mongodb`: Es el nombre de un servicio, en este caso, el servicio de la base de datos MongoDB.*
