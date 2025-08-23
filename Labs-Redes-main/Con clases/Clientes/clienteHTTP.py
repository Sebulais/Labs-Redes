from socket import *
from datetime import datetime
import json

class ClienteHTTP:
    
    def __init__(self, servicio):
        self.servicio = servicio
        
    def actualizar_mensaje(self, _mensaje, _largo_final):
        a = input("Ingrese nueva palabra: ")
        current_dt = datetime.now()
        self.mensaje = str(f"[{current_dt}]-[{_largo_final}]-[{len(_mensaje+a)}]-[{_mensaje+a}]")

        http_request = f"POST / HTTP/1.1\r\nContent-Type: application/json\r\nContent-Length: {len(json.dumps(self.mensaje))}\r\n\r\n"
        http_request += json.dumps(self.mensaje)

        self.mensaje = http_request

        
    
    def enviar_por_HTTP(self, host, port):
        with socket(AF_INET, SOCK_STREAM) as c:
            c.connect((host, port))
            print(f"Cliente TCP del {self.servicio} conectado a {host} : {port}")

            c.send(self.mensaje.encode())
            print(f"Mensaje enviado: {self.mensaje}\n")
            c.close()
            
    def recibir_por_UDP(self, host, port):    
        with socket(AF_INET, SOCK_STREAM) as c:
            c.connect(host, port)
            print(f"Cliente HTTP del {self.servicio} conectado a {host} : {port}")
            
            self.mensaje =  c.recvfrom(host, port).decode()
            print(f"Mensaje recibido: {self.mensaje}\n")
            c.close()
