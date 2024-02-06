"""
--workers: Número de procesos de trabajo. Por defecto es 1. Este parámetro es útil si quieres aprovechar múltiples núcleos en tu servidor.

--limit-concurrency: El número máximo de conexiones simultáneas que el servidor aceptará.

--timeout-keep-alive: Tiempo de espera en segundos para mantener las conexiones inactivas abiertas.

--ssl-keyfile, --ssl-certfile: Rutas a los archivos de clave y certificado SSL si quieres servir tu aplicación sobre HTTPS.

--log-level: El nivel de registro. Puede ser uno de critical, error, warning, info, debug, trace.

Por ejemplo, si quieres iniciar el servidor con 4 trabajadores y un nivel de registro de info, puedes usar el siguiente comando:

"""

"""
# Ejecuta uvicorn con:
# - Nombre del módulo: "users"
# - Nombre de la aplicación: "app"
# - Modo de recarga: habilitado (--reload)
# - Puerto: 8000 (--port 8000)
# - Host: 127.0.0.1 (--host 127.0.0.1)
# - Número de trabajadores: 1 (--workers 1)
# - Límite de conexiones simultáneas: 1000 (--limit-concurrency 1000)
# - Tiempo de espera para mantener las conexiones inactivas abiertas: 5 segundos (--timeout-keep-alive 5)
# - Nivel de registro: "info" (--log-level info)
# - Acceso a registros: habilitado (--access-log)
# - Límite de tamaño de solicitud: 1000000 bytes (--limit-max-request 1000000)
# - Tiempo de espera de gracia: 100 segundos (ws-ping-timeout 100)




--proxy-headers: Habilita/Desactiva el soporte para encabezados de proxy HTTP. Valor por defecto: False.

--forwarded-allow-ips: Una cadena de direcciones IP de confianza que pueden enviar encabezados de proxy. Valor por defecto: '127.0.0.1'.

--root-path: Configura la ruta raíz de la aplicación. Valor por defecto: ''.

--ssl-keyfile: Ruta al archivo de clave SSL para habilitar HTTPS. Valor por defecto: None.

--ssl-certfile: Ruta al archivo de certificado SSL para habilitar HTTPS. Valor por defecto: None.

--ssl-version: Versión de SSL a utilizar para HTTPS. Valor por defecto: 2.

--ssl-cert-reqs: Si se requiere o no un certificado de cliente para HTTPS. Valor por defecto: None.

--ssl-ca-certs: Ruta al archivo de certificados CA para habilitar HTTPS. Valor por defecto: None.

--ssl-ciphers: Cifrado a utilizar para HTTPS. Valor por defecto: None.

Por favor, ten en cuenta que estos son los valores por defecto y pueden no ser adecuados para tu caso de uso. Deberías ajustarlos según tus necesidades. Además, algunos de estos parámetros, como --ssl-keyfile y --ssl-certfile, requieren que proporciones tus propios archivos de certificado y clave SSL para habilitar HTTPS.





uvicorn users:app --reload --port 8000 --host 127.0.0.1 --workers 1 --limit-concurrency 1000 --timeout-keep-alive 5 --log-level info --access-log --limit-max-requests 1000000 --ws-ping-timeout 100



"""
