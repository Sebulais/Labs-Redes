from socket import *
from datetime import datetime
import json
import re

class ClienteHTTP:
    
    def __init__(self, _servicio):
        self.servicio = _servicio
    
    def actualizar_mensaje(self, _largo_final):
        _mensaje = self.mensaje.split("]-[")[-1][:-1]
        a = input("Ingrese nueva palabra: ")

        while not re.match(r'^[a-zA-Z]+$', a):
            a = input("Ingrese de nuevo la palabra (solo se admiten letras mayúsculas y minúsculas): ")
            
        current_dt = datetime.now()
        self.mensaje = str(f"[{current_dt}]-[{_largo_final}]-[{len(_mensaje+a)}]-[{_mensaje+a}]")

        http_request = f"POST / HTTP/1.1\r\nContent-Type: application/json\r\nContent-Length: {len(json.dumps(self.mensaje))}\r\n\r\n"
        http_request += json.dumps(self.mensaje)

        self.mensaje = http_request
        
    
    def enviar_por_HTTP(self, host, port):
        with socket(AF_INET, SOCK_STREAM) as c:
            c.connect((host, port))
            print(f"Cliente HTTP del {self.servicio} conectado a {host} : {port}")

            c.send(self.mensaje.encode('utf-8'))
            print(f"Mensaje enviado: {self.mensaje}\n")
            c.close()
            
    def recibir_por_UDP(self, host, port):    
        with socket(AF_INET, SOCK_DGRAM) as c:
            print(f"Cliente HTTP del {self.servicio} conectado a {host} : {port}")
            c.sendto("conectado".encode('utf-8'),(host,port))
            
            self.mensaje, addr =  c.recvfrom(1024)
            self.mensaje = self.mensaje.decode('utf-8')
            
            print(f"Mensaje recibido: {self.mensaje}\n")
            c.close()

