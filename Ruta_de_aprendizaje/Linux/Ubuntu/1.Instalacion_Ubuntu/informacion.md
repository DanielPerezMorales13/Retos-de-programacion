**Instalacion de Ubuntu**

- [**_VirtualBox_**](#virtualbox)
- [**_Instalar Ubuntu_**](#instalar-ubuntu)
- [**_Instalacion en Maquina Virtual_**](#instalacion-en-maquina-virtual)
- [**_Instalacion del sistema operativo en Hardware_**](#instalacion-del-sistema-operativo-en-hardware)

---

# **_VirtualBox_**

> _Una máquina virtual (VM, por sus siglas en inglés) es un entorno virtualizado que emula un sistema informático físico y permite ejecutar sistemas operativos y aplicaciones como si estuvieran instalados en hardware físico. Esto es útil para probar software, realizar pruebas de seguridad, ejecutar sistemas operativos múltiples en un mismo hardware, entre otros usos._

- **Para instalar VirtualBox**

  - _Instalar desde su pagina oficial_

    - [_**VirtualBox**_](https://www.virtualbox.org/ "https://www.virtualbox.org/")

  - _Actualizar el sistema_

    - ```bash
        sudo apt-get install update
      ```

    - ```bash
        sudo apt-get install upgrade
      ```

  - _Instalar VirtualBox_

    - ```bash
        sudo apt-get install virtualbox
      ```

    - ```bash
        vboxmanage --version
      ```

# **_Instalar Ubuntu_**

> _Ubuntu es un sistema operativo de código abierto basado en el kernel de Linux. Es conocido por su enfoque en la facilidad de uso, la estabilidad y la seguridad. Ubuntu se distribuye gratuitamente y está respaldado por una comunidad activa de desarrolladores y usuarios._

1. **Versiones principales**

   1. **Ubuntu Desktop:**

      1. > _La versión de escritorio estándar, diseñada para usuarios de computadoras personales._

   2. **Xubuntu:**

      1. _Utiliza el entorno de escritorio Xfce, siendo una opción más ligera y eficiente para sistemas con recursos limitados._

   3. **Lubuntu:**

      1. > _Ofrece un entorno de escritorio LXQt, diseñado para ser liviano y adecuado para hardware más antiguo o menos potente._

   4. Ubuntu Cloud:

      1. > _Orientado a la implementación y gestión de servicios en la nube, utiliza herramientas como OpenStack._

   5. Ubuntu IoT:
      1. > _Diseñado para dispositivos de Internet de las cosas (IoT), proporciona un entorno de desarrollo para aplicaciones IoT._

2. **Empresa detrás**

   1. > _Canonical Ltd. es la empresa que respalda y desarrolla Ubuntu. Fue fundada por Mark Shuttleworth y tiene como objetivo promover el uso de software de código abierto._

3. **Características principales**

   1. **Entorno de escritorio:**

      1. Utiliza el entorno de escritorio GNOME por defecto en la versión estándar, pero ofrece variantes con otros entornos más ligeros.

   2. **Ciclo de lanzamiento:**

      1. _Ubuntu sigue un ciclo de lanzamiento regular con versiones de soporte a largo plazo (LTS-Long Term Support) y versiones regulares._

   3. **Centro de Software:**

      1. _Proporciona un fácil acceso a la instalación y gestión de aplicaciones._

   4. **Seguridad:**
      1. _Ubuntu se enorgullece de su seguridad y ofrece actualizaciones regulares para mantener el sistema protegido._

---

# **_Instalacion en Maquina Virtual_**

1. _Ejecutamos el siguiente comando para abrir virtualbox_

   1. ```bash
      virtualbox
      ```

      1. ![_virtualbox#1_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox1.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox1.png?raw=true")

      2. ![_virtualbox#2_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox2.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox2.png?raw=true")

      3. ![_virtualbox#3_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox3.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox3.png?raw=true")

      4. ![_virtualbox#4_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox4.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox4.png?raw=true")

      5. ![_virtualbox#5_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox5.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox5.png?raw=true")

      6. ![_virtualbox#6_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox6.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox6.png?raw=true")

      7. ![_virtualbox#7_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox7.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox7.png?raw=true")

      8. ![_virtualbox#8_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox8.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox8.png?raw=true")

      9. ![_virtualbox#9_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox9.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox9.png?raw=true")

      10. ![_virtualbox#10_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox10.png?raw=true   "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox10.png?raw=true")

      11. ![_virtualbox#11_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox11.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox11.png?raw=true")

      12. ![_virtualbox#12_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox12.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox12.png?raw=true")

      13. ![_virtualbox#13_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox13.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox13.png?raw=true")

      14. ![_virtualbox#14_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox14.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox14.png?raw=true")

      15. ![_virtualbox#15_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox15.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox15.png?raw=true")

      16. ![_virtualbox#16_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox16.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox16.png?raw=true")

      17. ![_virtualbox#17_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox17.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox17.png?raw=true")

      18. ![_virtualbox#18_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox18.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox18.png?raw=true")

      19. ![_virtualbox#19_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox19.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox19.png?raw=true")

      20. ![_virtualbox#20_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox20.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox20.png?raw=true")

      21. ![_virtualbox#21_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox21.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox21.png?raw=true")

      22. ![_virtualbox#22_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox22.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox22.png?raw=true")

      23. ![_virtualbox#23_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox23.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox23.png?raw=true")

      24. ![_virtualbox#24_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox24.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox24.png?raw=true")

      25. ![_virtualbox#25_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox25.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox25.png?raw=true")

      26. ![_virtualbox#26_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox26.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox26.png?raw=true")

      27. ![_virtualbox#27_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox27.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox27.png?raw=true")

      28. ![_virtualbox#28_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox28.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox28.png?raw=true")

      29. ![_virtualbox#29_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox29.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox29.png?raw=true")

      30. ![_virtualbox#30_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox30.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox30.png?raw=true")

      31. ![_virtualbox#31_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox31.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox31.png?raw=true")

      32. ![_virtualbox#32_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox32.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox32.png?raw=true")

      33. ![_virtualbox#33_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox33.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox33.png?raw=true")

      34. ![_virtualbox#34_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox34.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox34.png?raw=true")

      35. ![_virtualbox#35_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox35.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox35.png?raw=true")

      36. ![_virtualbox#36_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox36.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox36.png?raw=true")

      37. ![_virtualbox#37_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox37.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox37.png?raw=true")

      38. ![_virtualbox#38_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox38.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox38.png?raw=true")

      39. ![_virtualbox#39_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox39.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox39.png?raw=true")

      40. ![_virtualbox#40_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox40.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox40.png?raw=true")

      41. ![_virtualbox#41_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox41.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox41.png?raw=true")

      42. ![_virtualbox#42_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox42.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox42.png?raw=true")

      43. ![_virtualbox#43_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox43.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox43.png?raw=true")

      44. ![_virtualbox#44_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox44.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox44.png?raw=true")

      45. ![_virtualbox#45_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox45.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox45.png?raw=true")

      46. ![_virtualbox#46_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox46.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox46.png?raw=true")

      47. ![_virtualbox#47_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox47.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox47.png?raw=true")

      48. ![_virtualbox#48_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox48.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox48.png?raw=true")

      49. ![_virtualbox#49_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox49.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox49.png?raw=true")

      50. ![_virtualbox#50_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox50.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox50.png?raw=true")

      51. ![_virtualbox#51_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox51.png?raw=true  "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox51.png?raw=true")

      52. ![_virtualbox#52_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox52.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox52.png?raw=true")

> _Las particiones son divisiones lógicas en el disco duro de tu computadora que permiten organizar y gestionar el espacio de almacenamiento. Estas divisiones son esenciales por varias razones:_

1. **Gestión del sistema de archivos:**

   1. > _Las particiones ayudan a organizar y gestionar el sistema de archivos del sistema operativo. Cada partición puede tener su propio sistema de archivos y configuración._

2. **Aislamiento de datos:**

   1. > _Si una partición falla, las demás pueden seguir funcionando. Esto significa que, por ejemplo, si tienes tus archivos personales en una partición separada, es menos probable que se vean afectados en caso de problemas en otras áreas del sistema._

3. **Múltiples sistemas operativos:**

   1. > _Si deseas tener varios sistemas operativos en una misma máquina, necesitarás particiones separadas para cada uno._

4. **Mejora del rendimiento:**
   1. > _Al separar áreas del disco, es posible mejorar el rendimiento de ciertos aspectos del sistema, como la velocidad de acceso a datos._

> **Un disco puede tener 4 Particiones Primarias es decir un disco puede almacenar 5 sistemas operativos y los discos puede tener varias particiones logicas**

1. **/ (raíz):**

   1. > _Contiene los archivos del sistema y directorios principales. Es la partición principal._

2. **/boot:**

   1. > _Almacena los archivos del kernel y otros archivos de inicio del sistema._

3. **/home:**

   1. > _Contiene los directorios personales de los usuarios, incluyendo documentos, música, imágenes, etc._

4. **/swap:**

   1. > _Esta es la partición de intercambio y se utiliza como espacio adicional cuando la memoria RAM está llena. Puede mejorar el rendimiento del sistema en situaciones de baja memoria._

5. **/tmp:**

   1. > _Almacena archivos temporales._

6. **/var:**

   1. > _Contiene datos variables, como registros del sistema y archivos de spool._

7. **/usr:**

   1. > _Almacena programas y archivos de sistema que no cambian con frecuencia._

8. **/opt:**
   1. > _Utilizado para instalar software adicional de terceros._

> En general, se recomienda crear tres particiones al instalar un sistema operativo, siguiendo una estructura que incluya una partición primaria para el sistema operativo y dos particiones lógicas. Estas dos particiones lógicas suelen ser /Swap y /Home. Veamos el propósito de cada una:

**Partición primaria para el sistema operativo (/):**

1. _Esta partición es donde se instala el sistema operativo. Contiene los archivos del sistema, el kernel y otros componentes esenciales para el funcionamiento del sistema._

2. _Mantener el sistema operativo en una partición separada facilita la gestión y las actualizaciones sin afectar los datos personales._

**Partición lógica de intercambio (/Swap):**

1. _La partición de intercambio (Swap) actúa como un espacio adicional cuando la memoria RAM está llena. Permite que el sistema operativo transfiera datos temporales al disco duro para evitar problemas de falta de memoria._

2. _Mejora el rendimiento del sistema en situaciones de uso intensivo de memoria._

**Partición lógica para archivos personales (/Home):**

1. _La partición /Home almacena los directorios personales de los usuarios, que incluyen documentos, música, imágenes y configuraciones personales._

2. _Al tener /Home en una partición separada, los archivos personales están aislados del sistema operativo. Esto significa que si decides reinstalar o actualizar el sistema operativo, los archivos personales permanecerán intactos, facilitando la migración y la protección de tus datos._

**Designaciones de Disco en Linux**

> _En sistemas operativos basados en Linux, los discos duros y otros dispositivos de almacenamiento son representados en el sistema de archivos como archivos en el directorio `/dev`. La designación de disco base suele seguir el patrón `/dev/sda`, donde "sda" podría ser reemplazado por otras letras según la cantidad de discos presentes en el sistema (por ejemplo, `/dev/sdb`, `/dev/sdc`, etc.)._

**Particiones Primarias y Lógicas**

_Cuando se crean particiones en un disco, las designaciones de disco cambian para reflejar estas divisiones. A continuación, se describen las convenciones comunes:_

- **Disco Completo:** _`/dev/sda` representa todo el disco._

- **Particiones Primarias:** _Las particiones primarias se numeran secuencialmente, por ejemplo, `/dev/sda1`, `/dev/sda2`, `/dev/sda3`, etc. Cada número indica una partición primaria diferente en el mismo disco._

- **Particiones Lógicas:** _Cuando se utilizan particiones lógicas (generalmente dentro de una partición extendida), las designaciones cambian a `/dev/sda5`, `/dev/sda6`, `/dev/sda7`, etc. La numeración comienza desde 5 para indicar particiones lógicas._

**Diferencia entre Particiones Primarias y Lógicas**

_La principal diferencia entre particiones primarias y lógicas radica en cómo se utilizan y cómo interactúan con la tabla de particiones:_

- **Particiones Primarias:** _Están limitadas a un máximo de cuatro por disco. Son independientes y pueden contener sistemas de archivos o actuar como contenedores para sistemas de archivos adicionales (por ejemplo, contenedor de una partición extendida)._

- **Particiones Lógicas:** _Se utilizan cuando se necesitan más de cuatro particiones en un disco. Se crean dentro de una partición extendida, que es una partición primaria especial. La partición extendida actúa como un contenedor para varias particiones lógicas. Esto permite superar la limitación de cuatro particiones primarias._

**Ejemplo Práctico**

_Supongamos que tenemos un disco `/dev/sda` con tres particiones primarias y una partición extendida con dos particiones lógicas:_

- `/dev/sda1` - _Partición Primaria_
- `/dev/sda2` - _Partición Primaria_
- `/dev/sda3` - _Partición Primaria_
- `/dev/sda4` - _Partición Extendida_
  - `/dev/sda5` - _Partición Lógica_
  - `/dev/sda6` - _Partición Lógica_

_En este ejemplo, `/dev/sda1`, `/dev/sda2`, y `/dev/sda3` son particiones primarias, mientras que `/dev/sda5` y `/dev/sda6` son particiones lógicas dentro de la partición extendida `/dev/sda4`._

**Guest Additions en VirtualBox**

**¿Qué son las Guest Additions?**

> _Las Guest Additions son controladores y utilidades que mejoran la integración y el rendimiento de una máquina virtual en VirtualBox._

**Funcionalidades Comunes de Guest Additions:**

- **Mejora de Resolución de Pantalla:** _Ajusta automáticamente la resolución de pantalla de la máquina virtual._
- **Integración del Ratón:** _Permite una transición más fluida entre el sistema anfitrión y el sistema invitado._
- **Compartición de Carpetas:** _Facilita la transferencia de archivos entre ambos sistemas._

**Instalación de Guest Additions:**

1. **Iniciar la Máquina Virtual:** _Asegúrate de que tu máquina virtual esté en ejecución._

2. **Insertar el CD de Guest Additions:**

   - _Desde el menú de VirtualBox, selecciona "Dispositivos" -> "Insertar imagen de CD de Guest Additions..."_
   - ![_virtualbox#53_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox53.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox53.png?raw=true")

3. **Acceder al Terminal en el Sistema Invitado:**

   - _En la máquina virtual, abre la terminal._

   - Es posible que necesites tener instalados los "build-essential" y los "linux-headers" antes de ejecutar el script de instalación.

     - ```bash
         sudo apt-get install build-essential linux-headers-$(uname -r)
       ```

     - ![_virtualbox#58_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox58.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox58.png?raw=true")

4. **Ejecutar el script de instalacion:**

   1. _Ir al directorio y ejecutarlo_

      1. ![_virtualbox#54_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox54.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox54.png?raw=true")

      2. ```bash
         cd /media/daniel/VBox_Gas_6.1.38
         ```

      3. _Remplazar daniel por tu usuario y VBox_Gas_6.1.38 con el directorio que te aparece_

      4. ```bash
         ls
         ```

         1. ![_virtualbox#55_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox55.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox55.png?raw=true")

         2. _Actualizamos el sistema_

            1. ```bash
               sudo apt-get install update
               ```

         3. _Terminamos de actualizar el sistema_

            1. ```bash
               sudo apt-get install upgrade
               ```

      5. ![_virtualbox#56_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox56.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox56.png?raw=true")
      6. ![_virtualbox#57_](https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox57.png?raw=true "https://github.com/Danitrix13/Retos-de-programacion/blob/master/Ruta_de_aprendizaje/Linux/Ubuntu/Images/Png/Img_virtualbox/virtualbox57.png?raw=true")

5. **Reiniciar la Máquina Virtual:**

   1. ```bash
      sudo reboot
      ```

6. _Desde el menú de VirtualBox, selecciona "Dispositivos" -> "Papeles compartidos...", Seleccionar Bidireccional_

7. _Desde el menú de VirtualBox, selecciona "Dispositivos" -> "Arrastrar y soltar...", Seleccionar Bidireccional_

8. **Estos comandos y pasos son específicos para sistemas basados en Debian o Ubuntu. Si estás utilizando una distribución diferente, es posible que necesites adaptar los comandos según los requisitos del sistema operativo invitado.**

---

# **_Instalacion del sistema operativo en Hardware_**

**_Recomendacion al hacer las particiones para intalar el sistema operativo en hardware_**

**Un solo SSD o HDD:**

> _Solo hay que particionar el disco dejando el espacio que puedas, mi recomendación es mitad para Windows mitad para Linux, aunque si tienes un HDD con mucho espacio puedes dejar 200-300 GB para Linux y el resto para Windows si lo usas para juegos o similar._

**SSD + HDD:**

> _Tienes que particionar el SSD para instalar ahí el sistema operativo, y tienes que particionar el HDD para montar ahí el /home y almacenar tus archivos. En cuando al SSD recomiendo si es posible mitad para Windows mitad para Linux. El HDD va a tu criterio, deja el espacio que consideres necesario._

**Un solo disco en el PC (SSD o HDD) pero con disco externo para archivos:**

> _Se tiene que particionar el disco que tienes en el PC, ya sea SSD o HDD, debes hacer espacio para instalar el Sistema, tus archivos los almacenas en el disco externo._

[Etcher](https://etcher.balena.io/ "https://etcher.balena.io/")

> _Balena Etcher es una herramienta de código abierto que se utiliza para escribir imágenes de sistemas operativos en tarjetas SD, unidades flash USB u otros dispositivos de almacenamiento masivo. Su principal función es facilitar la creación de medios de arranque para sistemas operativos, especialmente en el contexto de sistemas basados en Linux y otras plataformas embebidas._

**Algunas características clave de Balena Etcher incluyen:**

1. **Interfaz Gráfica de Usuario (GUI):** _Balena Etcher ofrece una interfaz gráfica intuitiva y fácil de usar que simplifica el proceso de escritura de imágenes en dispositivos de almacenamiento._

2. **Multiplataforma:** _Está disponible para sistemas operativos Windows, macOS y Linux, lo que permite a los usuarios de diferentes plataformas utilizar la herramienta de manera consistente._

3. **Soporte para Formatos** _de Imagen Comunes: Puede escribir imágenes en varios formatos comunes, como ISO, IMG y ZIP, lo que facilita la creación de medios de instalación para sistemas operativos._

> **Modo de uso**

1. _Necesitaremos una **USB** de almenos 8 GB para arrancar el ordenador desde la **USB**_

   1. _Se recomienda que la **USB** este vacia_

2. _Ejecutar el programa_
   1. _Te pedira que seleccione la iso del sistema operativo_
   2. *Segunda cosa que te pedira es la unidad extraible osea el **USB***
   3. _De ultimo simplemente lo finalizaremos_
   4. _Y ya con esa **USB** podremos instalar Linux en cualquier ordenador_

> **Primeramente hay que crear las particiones desde windows por que en la maquina virtual no habia ningun sistema operativo instalado**

**Buscar en la barra de busqueda en windows** _Crear y formatear particiones del disco o administracion de discos_

1. *Seleccionar el disco que queremos particionar y luego darle reducir volumen*
2. *Tendremos un limite de espacio para particionar el disco windows no los dira*
3. *Poner la cantidad de espacio que queremos particionar siempre y cuando no sobre pase el limite establecido por windows y listo*

_*Luego tenemos que configurar la BIOS para arrancar el ordenador desde la USB*_

> _La BIOS, que significa "Basic Input/Output System" (Sistema Básico de Entrada/Salida), es un software esencial almacenado en un chip de memoria flash en la placa base de una computadora. La BIOS es fundamental para el inicio y la operación básica del sistema antes de que el sistema operativo se cargue desde el disco duro o cualquier otro dispositivo de almacenamiento._

1. _Para entrar ala bios hay muchas formas. Mantener presionada la tecla <kbd>Shift</kbd> y reiniciar el sistema operativo en windows. O apagar el ordenador y presionar las teclas especiales como <kbd>f11</kbd>,<kbd>f12</kbd> para abrir la bios_

2. _Cuando entremos ala Bios ir ala opcion modo avanzado y luego ir a **BOOT** y luego colocar la USB de primero para que arranque el sistema operativo desde el usb de primero_

**Si tenemos problema al particionar el disco se puede deber a muchas razones** 

1. [*Guía partition wizard*](https://www.partitionwizard.com/partitionmanager/cannot-shrink-volume-win10.html "https://www.partitionwizard.com/partitionmanager/cannot-shrink-volume-win10.html")