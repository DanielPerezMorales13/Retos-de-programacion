**_Ciberataques mas comunes_**

**Indice**

- [**_APTs-Cosas_**](#apts-cosas)
- [**_APTs-Personas_**](#apts-personas)
- [**_Phishing y sus tipos_**](#phishing-y-sus-tipos)
- [**_Ataque Man in the middle (hombre en el medio)_**](#ataque-man-in-the-middle-hombre-en-el-medio)
- [**_Ransomware (Rescate software)_**](#ransomware-rescate-software)
- [**_Spyware (software espia)_**](#spyware-software-espia)
- [**_Botnet_**](#botnet)
- [***Denegación de Servicio (DoS) y Ataque Distribuido de Denegación de Servicio (DDoS)***](#denegación-de-servicio-dos-y-ataque-distribuido-de-denegación-de-servicio-ddos)
- [***Cross-Site Scripting (XSS) y Inyección de SQL***](#cross-site-scripting-xss-y-inyección-de-sql)
- [***Top Ciberataques de la historia***](#top-ciberataques-de-la-historia)

# **_APTs-Cosas_**

**_"Advanced Persistent Threats" (Amenazas Persistentes Avanzadas)._**

**Actores**:

> _Estados Nacionales o Grupos Organizados: Los APTs a menudo son respaldados por estados nacionales, como agencias de inteligencia o fuerzas militares. También pueden ser llevados a cabo por grupos organizados con recursos significativos._

**Objetivos**:

> _Espionaje o Sabotaje a Largo Plazo: Los APTs buscan acceder y mantenerse en sistemas durante un período prolongado sin ser detectados. Los objetivos pueden incluir el robo de información sensible, el sabotaje de infraestructuras críticas, etc._

**Sofisticación**:

> _Altamente Sofisticados: Los APTs suelen utilizar técnicas avanzadas de ingeniería social, exploits y malware personalizado. Pueden adaptarse y evolucionar para evadir la detección._

---

# **_APTs-Personas_**

**Actores**:

> _Individuos o Grupos del Crimen Organizado: Los criminales comunes pueden ser individuos o grupos que buscan obtener beneficios financieros a través de actividades ilícitas en línea._

**Objetivos**:

> _Robo de Datos, Fraude Financiero, Extorsión: Los criminales comunes suelen centrarse en actividades delictivas tradicionales en línea, como el robo de información personal para el fraude financiero, la extorsión o la venta de información en el mercado negro._

**Sofisticación**:

> _Varía en Sofisticación: Aunque algunos criminales comunes pueden utilizar tácticas avanzadas, muchos dependen de métodos más comunes, como phishing, ransomware o ataques más oportunistas._

---

# **_Phishing y sus tipos_**

> _El phishing (pesca de datos) es una forma de ciberataque en la que un atacante intenta engañar a las personas para que revelen información confidencial, como nombres de usuario, contraseñas y detalles de tarjetas de crédito. Esto se hace comúnmente a través de correos electrónicos, mensajes de texto, o sitios web falsos que imitan a entidades legítimas._

**_Tipos_**

1. **Smishing - "SMS" y "phishing"**:

   1. > _Definición: Es una variante de phishing que utiliza mensajes de texto (SMS) para engañar a las víctimas._

   2. **Ejemplo**: _Un mensaje de texto falso que solicita hacer clic en un enlace o proporcionar información personal._

2. **Vishing - "voice" (voz) y "phishing"**:

   1. > _Definición: Es el phishing que se realiza a través de llamadas telefónicas._

   2. **Ejemplo**: _Una llamada telefónica automática que simula ser de un banco y pide al receptor que marque un número para "resolver un problema"._

3. **Spear Phishing - phishing dirigido" o "phishing personalizado"**:

   1. > _Definición: Es un ataque dirigido a individuos o empresas específicas, personalizando los mensajes para aumentar la probabilidad de éxito._

   2. **Ejemplo**: _Un correo electrónico dirigido a un empleado de una empresa con información específica sobre proyectos internos._

4. **QRishing - "QR" y "phishing"**:
   1. > _Definición: Implica el uso de códigos QR para dirigir a las víctimas a sitios web maliciosos._
   2. **Ejemplo**: _Un código QR en un póster que, cuando se escanea, lleva a una página falsa de inicio de sesión._

---

# **_Ataque Man in the middle (hombre en el medio)_**

> _Un ataque Man-in-the-Middle (MitM) es una técnica en la que un atacante intercepta y potencialmente modifica la comunicación entre dos partes sin que ninguna de ellas sea consciente de la intervención. Este tipo de ataque puede ocurrir en varios contextos, como redes Wi-Fi, conexiones Bluetooth, redes cableadas, etc._

1. **Intercepción de Tráfico:**

> _El atacante intercepta el tráfico de datos entre dos partes que están intentando comunicarse. Esto puede hacerse de varias maneras, como mediante el acceso no autorizado a una red, la utilización de software malicioso o la manipulación de la configuración de red._

2. **Reenvío de Tráfico:**

> _Una vez que el atacante ha interceptado el tráfico, lo reenvía a su destino original para que las partes afectadas no noten la intercepción. El atacante actúa como un intermediario entre las partes legítimas._

3. **Posible Modificación de Datos:**

> _Dependiendo de los objetivos del atacante, puede modificar los datos transmitidos entre las partes.Por ejemplo, podría alterar información en formularios web, mensajes de correo electrónico o solicitudes HTTP._

4. **Suplantación de Identidad:**

> _El atacante puede hacerse pasar por una de las partes originales para engañar a la otra. Esto puede incluir la falsificación de certificados SSL/TLS para hacer que una conexión parezca segura cuando no lo es._

5. **Ataques SSL/TLS:**

> _En conexiones seguras (HTTPS), el atacante puede intentar desencriptar el tráfico o realizar ataques específicos contra el protocolo SSL/TLS._

6. **Ataques DNS:**

> _Los atacantes pueden modificar las consultas DNS para redirigir el tráfico a servidores controlados por ellos._

7. **Ataques Wi-Fi:**

> _En redes Wi-Fi, un atacante puede realizar un ataque MitM configurando un punto de acceso falso (evil twin) o explotando vulnerabilidades en el protocolo de seguridad._

8. **Sniffing de Paquetes:**

> El atacante puede utilizar herramientas de sniffing para capturar y analizar los paquetes de datos que pasan a través de la red.

---

# **_Ransomware (Rescate software)_**

> _El ransomware es un tipo de software malicioso (malware) diseñado para cifrar archivos en el sistema de un usuario y luego exigir un pago (un "rescate") a cambio de proporcionar la clave de descifrado o desbloquear los archivos. En esencia, es un tipo de ataque cibernético que tiene como objetivo extorsionar a las víctimas._

1. **Cifrado de Archivos:**

> _El ransomware cifra archivos en la computadora de la víctima, utilizando algoritmos de cifrado fuertes. Los archivos se vuelven inaccesibles para el usuario sin la clave de descifrado correspondiente._

2. **Mensaje de Rescate:**

> _Después de cifrar los archivos, el ransomware generalmente muestra un mensaje de rescate en la pantalla de la víctima. Este mensaje contiene instrucciones sobre cómo realizar el pago y obtener la clave de descifrado._

3. **Extorsión:**

> _Los atacantes exigen un pago generalmente en criptomonedas, como Bitcoin, ya que estas transacciones son más difíciles de rastrear. El pago suele ser la única forma de recuperar los archivos._

4. **Métodos de Distribución:**

> _El ransomware se propaga a menudo a través de correos electrónicos de phishing, descargas de archivos maliciosos, sitios web comprometidos o mediante la explotación de vulnerabilidades en sistemas no actualizados._

---

# **_Spyware (software espia)_**

> _El spyware es un tipo de software malicioso que se instala en un dispositivo sin el conocimiento o el consentimiento del usuario y tiene la capacidad de recopilar información sobre las actividades del usuario. Esta información puede incluir datos de navegación, hábitos de búsqueda, contraseñas, mensajes de texto y más. Los objetivos suelen ser el robo de información personal y la monitorización no autorizada._

1. **Keylogger (Registrador de pulsaciones):**

> _Un keylogger es un tipo específico de spyware diseñado para registrar las pulsaciones del teclado de un usuario. Captura y registra cada tecla presionada, lo que significa que puede registrar contraseñas, mensajes y otra información confidencial. Los keyloggers pueden ser tanto de software como de hardware. Algunos keyloggers son utilizados de manera legítima para monitoreo parental o por empresas para la supervisión de empleados, pero también pueden ser abusados con fines maliciosos._

1. **Adware:**

> _El adware, o software publicitario, es un tipo de software que muestra anuncios no deseados en el dispositivo del usuario. Por lo general, se instala sin el conocimiento del usuario, a menudo como parte de la instalación de otro software. El propósito principal del adware es generar ingresos para el creador mostrando anuncios, pero también puede afectar el rendimiento del dispositivo y la experiencia del usuario al inundar la pantalla con publicidad no deseada._

1. **Command and Control (C2 o C&C):**

> _El término "Command and Control" (Comando y Control, en español) se refiere a una infraestructura utilizada por atacantes para comunicarse y controlar malware instalado en sistemas comprometidos. El C2 permite a los atacantes enviar comandos a las máquinas infectadas, recibir datos robados y coordinar actividades maliciosas. En un ataque, el malware infecta un dispositivo y se conecta al servidor de Comando y Control para recibir instrucciones._

---

# **_Botnet_**

> _Una botnet es una red de dispositivos informáticos comprometidos que son controlados de manera remota por un atacante, conocido como botmaster. Los dispositivos comprometidos en una botnet se llaman bots, y pueden incluir computadoras personales, servidores, enrutadores y otros dispositivos conectados a Internet._

1. **Botmaster (Bot herder):**

   > _Es el individuo o grupo de individuos que controla la botnet. El botmaster utiliza un software especializado para enviar comandos a los bots y coordinar sus acciones._

2. **Bot (Robot):**

   > _Un bot es un dispositivo comprometido que forma parte de la botnet. Puede ser una computadora personal, un servidor o cualquier otro dispositivo conectado a Internet que haya sido infectado con un malware específico. Los bots son controlados de manera remota por el botmaster._

3. **Backdoor (Puerta trasera):**
   > _Es una vulnerabilidad o una puerta secreta en el software de un sistema que permite a un atacante eludir la autenticación normal y obtener acceso no autorizado. En el contexto de una botnet, el backdoor es el método a través del cual el malware se instala en un dispositivo y establece una conexión con el botmaster._

**Infección:**

> _El malware se propaga a través de diversos métodos, como correos electrónicos maliciosos, descargas de software infectado, sitios web comprometidos, etc. Una vez que el malware se instala en un dispositivo, establece una conexión con el botmaster a través de la puerta trasera._

**Control:**

> _Una vez que un dispositivo está infectado, el botmaster puede enviar comandos a través de la conexión establecida. Estos comandos pueden incluir instrucciones para realizar ataques distribuidos de denegación de servicio (DDoS), robo de información, envío de spam, o cualquier otra actividad maliciosa._

**Amplificación:**

> _A medida que se agregan más dispositivos a la botnet, la capacidad del atacante para llevar a cabo acciones maliciosas aumenta. Las botnets a menudo se utilizan para realizar ataques coordinados a gran escala._
---

# ***Denegación de Servicio (DoS) y Ataque Distribuido de Denegación de Servicio (DDoS)***

1. > *La **Denegación de Servicio (DoS)** es un tipo de ataque cibernético diseñado para hacer que un servicio o recurso en línea sea inaccesible para los usuarios legítimos, saturando o agotando los recursos del sistema objetivo. Este ataque se realiza inundando el objetivo con un tráfico falso o manipulado, sobrecargando sus capacidades y provocando la interrupción del servicio.*

   1. *El acrónimo **DoS** se refiere a la "Denegación de Servicio", donde el atacante busca negar el acceso al servicio o recurso afectado.*

2. **Ataque Distribuido de Denegación de Servicio (DDoS):** *Por otro lado, el **Ataque Distribuido de Denegación de Servicio (DDoS)** es una variante del ataque DoS, pero implica la utilización de múltiples sistemas distribuidos para coordinar y ejecutar el ataque. En lugar de depender de un solo origen, un ataque DDoS involucra una red de dispositivos comprometidos (a menudo una botnet) para generar un volumen masivo de tráfico malicioso hacia el objetivo.*

   1. El acrónimo **DDoS** significa "Ataque Distribuido de Denegación de Servicio", donde la distribución de los atacantes hace que sea más difícil mitigar el ataque y dificulta la identificación del origen.

**Características Técnicas**

1. **DoS:**
   - **Atacante Único:** *Un solo atacante intenta sobrecargar los recursos del objetivo.*
   - **Tráfico Manipulado:** *Se utiliza tráfico falso o manipulado para consumir recursos.*
   - **Menor Escala:** *Puede ser efectivo contra sistemas menos protegidos.*

2. **DDoS:**
   - **Atacantes Distribuidos:** *Múltiples dispositivos coordinados participan en el ataque.*
   - **Amplificación:** *Mayor capacidad de generación de tráfico malicioso.*
   - **Mayor Escala:** *Puede abrumar incluso sistemas robustos con medidas de seguridad.*

**Métodos Comunes de Ataque**

1. **DoS:**
   - **Ataque de Consumo de Ancho de Banda:** *Saturación de la conexión con tráfico masivo.*
   - **Ataque de Consumo de Recursos:** *Agotamiento de recursos como CPU o memoria.*

2. **DDoS:**
   - **Ataques de Amplificación:** Uso de servicios mal configurados para amplificar el tráfico.
   - **Ataques de Reflejo:** *Engañar a los servidores para que respondan a solicitudes no solicitadas.*

**Mitigación**

1. **DoS:**
   - **Filtrado de Tráfico:** *Identificación y bloqueo de patrones maliciosos.*
   - **Aumento de Recursos:** *Mejora de la capacidad para resistir ataques.*

2. **DDoS:**
   - **Detección de Patrones:** *Identificación de comportamientos anómalos en el tráfico.*
   - **Balanceo de Carga:** *Distribución del tráfico para mitigar la carga en puntos específicos.*

---

# ***Cross-Site Scripting (XSS) y Inyección de SQL***

**Cross-Site Scripting (XSS)**

> *El **Cross-Site Scripting (XSS)** es una vulnerabilidad de seguridad en aplicaciones web que permite a un atacante ejecutar scripts maliciosos en el navegador de un usuario final. Esta vulnerabilidad se produce cuando una aplicación web no valida o filtra adecuadamente la entrada del usuario antes de mostrarla en el navegador. Un atacante puede insertar scripts maliciosos, generalmente en forma de código JavaScript, que luego se ejecutan en el contexto del navegador del usuario afectado.*

**Tipos de XSS:**

1. **Reflejado (Reflected XSS):**
   - *Los datos del usuario se reflejan directamente en la respuesta HTTP.*
   - *El atacante engaña al usuario para que haga clic en un enlace malicioso que contiene el código XSS.*

2. **Persistente (Stored XSS):**
   - *Los datos maliciosos se almacenan en la aplicación y se sirven a otros usuarios.*
   - *Ejemplos incluyen comentarios o perfiles de usuario que muestran contenido no validado.*

**Mitigación de XSS:**

- **Validación de Entrada:** *Filtrar y validar la entrada del usuario para prevenir la ejecución de scripts maliciosos.*
- **Codificación de Salida:** *Codificar datos antes de mostrarlos en el navegador para evitar la interpretación incorrecta como código.*

**Inyección de SQL**

> *La **Inyección de SQL** es una vulnerabilidad que ocurre cuando los atacantes insertan instrucciones SQL maliciosas en las consultas de una aplicación web. Esto suele ocurrir cuando la entrada del usuario no se valida adecuadamente antes de ser utilizada en una consulta SQL. Los atacantes pueden manipular las consultas para acceder, modificar o eliminar datos en la base de datos.*

**Ejemplo de Inyección de SQL:**

```sql
SELECT * FROM usuarios WHERE nombre_usuario = 'usuario' AND contraseña = 'contraseña';
```

Un atacante podría ingresar como nombre de usuario: `' OR '1'='1'; --`, haciendo que la consulta sea:

```sql
SELECT * FROM usuarios WHERE nombre_usuario = '' OR '1'='1'; --' AND contraseña = 'contraseña';
```

*Esto podría permitir al atacante eludir la autenticación, ya que la condición `'1'='1'` siempre es verdadera.*

**Mitigación de Inyección de SQL**

- **Sentencias Preparadas:** *Utilizar sentencias SQL preparadas para separar datos y consultas.*
- **Validación de Entrada:** *Validar y filtrar la entrada del usuario para evitar caracteres maliciosos.*
- **Principio de Menor Privilegio:** *Limitar los permisos de la cuenta de base de datos utilizada por la aplicación.*

---

# ***Top Ciberataques de la historia***
>
> *[_Artículo Deloitte_](https://www2.deloitte.com/es/es/pages/risk/articles/los-cinco-mayores-ciberataques-de-la-historia.html "https://www2.deloitte.com/es/es/pages/risk/articles/los-cinco-mayores-ciberataques-de-la-historia.html").*
