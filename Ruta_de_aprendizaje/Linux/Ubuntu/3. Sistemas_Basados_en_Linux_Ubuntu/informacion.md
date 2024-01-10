_Sistemas basados en Linux Ubuntu_

**Indice**

- [**_Usuarios en linux_**](#usuarios-en-linux)
- [**_Configurando GRUB en Ubuntu_**](#configurando-grub-en-ubuntu)
- [**_Atajo\_Linux_!!\_**](#atajo_linux_)

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

   2. ![img-grup#1]("")

2. _Para editarlo_

   1. ```bash
      sudo nano /etc/default/grup
      ```

   2. ![img-grup#2]("")

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

3. ![img-grup#3]("")

   1. _La línea GRUB_DEFAULT=0 es una configuración en el archivo de configuración de GRUB, que normalmente se encuentra en /etc/default/grub en sistemas Linux._

      - _GRUB_DEFAULT controla qué entrada del menú de GRUB se selecciona por defecto cuando el sistema arranca. Las entradas del menú se cuentan desde 0, por lo que GRUB_DEFAULT=0 significa que se seleccionará la primera entrada del menú._

      - _Por ejemplo, si tu menú de GRUB tiene las siguientes entradas:_

        - **Ubuntu**
        - **Advanced options for Ubuntu**
        - **Windows Boot Manager**

      - > _Entonces GRUB_DEFAULT=0 seleccionará "Ubuntu" por defecto._

4. ![img-grup#4]("")

   1. _La línea GRUB_TIMEOUT=10 es una configuración en el archivo de configuración de GRUB, que normalmente se encuentra en /etc/default/grub en sistemas Linux._

      - _GRUB_TIMEOUT controla cuánto tiempo (en segundos) GRUB espera antes de arrancar automáticamente la entrada del menú por defecto. En este caso, GRUB_TIMEOUT=10 significa que GRUB esperará 10 segundos antes de arrancar la entrada por defecto._

      - _Si durante ese tiempo seleccionas manualmente otra entrada del menú, GRUB arrancará esa entrada en lugar de la entrada por defecto._

---

# **_Atajo_Linux_!!\_**

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

   1. ![img-grup#5]("")
