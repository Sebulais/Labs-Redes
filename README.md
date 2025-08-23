Integrantes:
Sebastián Canales 202273640-2
Giselle Gómez 202273591-0
Rafael Baeza 202204598-1

Instrucciones:
El zip a descargar contiene 4 archivos llamados Servidor(TCP, TCP2, UDP y HTTP) los cuales deberán ser ejecutados cada uno en una terminal distinta, por ejemplo para abrir el ServidorTCP debe ser: python ServidorTCP.py
Una vez esten los cuatro servidores abiertos, se debe ejecutar en otra terminal aparte el archivo main.py (el cual contiene la logica de los clientes) para iniciar el mecanismo de envio de mensajes.
En la terminal de main, se le pedira al usuario ingresar el largo minimo del mensaje para despues pedir la primera palabra que contenga el mensaje.
Acto seguido se le seguira pidiendo por la misma terminal la nueva palabra que desea agregar. En el caso que el usuario no alcanze el largo minimo se le seguira pidiendo nuevas palabras hasta alcanzar
el servidor 4 nuevamente.
Cuando se alcance el largo minimo en el servidor de HTTP, los servidores comenzaran a terminar para cerrar todo. Tambien el mensaje final se escribira en un .txt dentro de la carpeta del codigo.

Aclaraciones:
Los archivos clientes.py solo contienen sus respectivas clases con sus funciones que son llamadas por el main.py

Bibliografia:
https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842 Tutorial de HTTP
https://www.youtube.com/watch?v=FTdii0o5vBM Video de TCP
https://docs.python.org/es/3.13/library/http.server.html Documentacion de HTTP.server
https://realpython.com/python-sockets/ Documentacion de Sockets
https://www.youtube.com/watch?v=jQmlJQiznks Video de conexiones TCP y UDP
