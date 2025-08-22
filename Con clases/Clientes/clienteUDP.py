from socket import *
from datetime import datetime

class ClienteUDP:
    
    def __init__(self, _servicio):
        self.servicio = _servicio
        
    def actualizar_mensaje(self, _mensaje, _largo_final):
        a = input("Ingrese nueva palabra: ")
        current_dt = datetime.now()
        self.mensaje = str(f"[{current_dt}]-[{_largo_final}]-[{len(_mensaje+a)}]-[{_mensaje+a}]")
        
        
    def enviar_por_UDP(self, host, port):
        with socket(AF_INET, SOCK_DGRAM) as c:
            print(f"Cliente UDP del {self.servicio} conectado a {host} : {port}")
            
            c.sendto(self.mensaje.encode(), (host, port))
            print(f"Mensaje enviado: {self.mensaje}\n")
            c.close()
            
    def recibir_por_TCP(self, host, port):    
        with socket(AF_INET, SOCK_STREAM) as c:
            c.connect((host, port))
            print(f"Cliente UDP del {self.servicio} conectado a {host} : {port}")
            
            self.mensaje = c.recv(1024).decode()
            print(f"Mensaje recibido: {self.mensaje}\n")
            c.close()