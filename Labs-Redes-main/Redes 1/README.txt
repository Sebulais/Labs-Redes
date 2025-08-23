Integrantes:
Sebastián Canales 202273640-2
Giselle Gómez 202273591-0
Rafael Baeza 202204598-1

Instrucciones:
El zip a descargar contiene 4 archivos llamados Servidor(TCP, TCP2, UDP y HTTP) los cuales deberán ser ejecutados cada uno en una terminal distinta, por ejemplo para abrir el ServidorTCP debe ser: Python ServidorTCP.py
Una vez estén los cuatro servidores abiertos, se debe ejecutar en otra terminal aparte el archivo main.py (el cual contiene la lógica de los clientes) para iniciar el mecanismo de envió de mensajes.
En la terminal de main, se le pedirá al usuario ingresar el largo mínimo del mensaje para después pedir la primera palabra que contenga el mensaje.
Acto seguido se le seguirá pidiendo por la misma terminal la nueva palabra que desea agregar. En el caso que el usuario no alcance el largo mínimo se le seguirá pidiendo nuevas palabras hasta alcanzar
el servidor 4 nuevamente.
Cuando se alcance el largo mínimo en el servidor de HTTP, los servidores comenzaran a terminar para cerrar todo. También el mensaje final se escribirá en un .txt dentro de la carpeta del código.

Aclaraciones:
Los archivos clientes.py solo contienen sus respectivas clases con sus funciones que son llamadas por el main.py
Solo se admiten palabras en minúsculas y mayúsculas, sin caracteres especiales o espacios.

Algoritmo:
El main inicia con pedir el largo mínimo y palabra inicial para comenzar, se llama primero al cliente 1 (TCP) para pedir una palabra extra y este se envia al servidor 2 (TCP).
Luego el servidor lo envía mediante UDP al Cliente UDP para nuevamente pedir una palabra extra al mensaje. Este cliente envia mediante UDP al servidor 3 (UDP).
El servidor 3 envía el mensaje al Cliente HTTP el cual pide una palabra nueva para el mensaje. Luego este lo envia al servidor 4 (HTTP)
El servidor 4 compara los largos, sucediendo dos casos:
Si el largo mínimo es superado, entonces al Cliente 4 (TCP) le envía la palabra "Close" el cual hará que inicie una cadena de apagado para los servidores.
Si el largo mínimo no es superado, entonces al Cliente 4 le envía el mensaje que contiene para luego pedir una palabra extra y volver a empezar el loop en el cliente 1 (TCP).

Bibliografia:
https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842 Tutorial de HTTP
https://www.youtube.com/watch?v=FTdii0o5vBM Video de TCP
https://docs.python.org/es/3.13/library/http.server.html Documentación de HTTP.server
https://realpython.com/python-sockets/ Documentación de Sockets
https://www.youtube.com/watch?v=jQmlJQiznks Video de conexiones TCP y UDP