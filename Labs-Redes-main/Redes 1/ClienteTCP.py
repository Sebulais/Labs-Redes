from socket import *
from datetime import datetime
import re

class ClienteTCP:
    
    def __init__(self, _servicio):
        self.servicio = _servicio
        
    def ingresar_mensaje(self, _mensaje, _largo_final):
        a = input("Ingrese nueva palabra: ")
        current_dt = datetime.now()
        self.mensaje = str(f"[{current_dt}]-[{_largo_final}]-[{len(_mensaje+a)}]-[{_mensaje+a}]")
        
    def actualizar_mensaje(self, _largo_final):
        _mensaje = self.mensaje.split("]-[")[-1][:-1]
        a = input("Ingrese nueva palabra: ")

        while not re.match(r'^[a-zA-Z]+$', a):
            a = input("Ingrese de nuevo la palabra (solo se admiten letras mayúsculas y minúsculas): ")

        current_dt = datetime.now()
        self.mensaje = str(f"[{current_dt}]-[{_largo_final}]-[{len(_mensaje+a)}]-[{_mensaje+a}]")
        
    def enviar_por_TCP(self, host, port):
        with socket(AF_INET, SOCK_STREAM) as c:
            c.connect((host, port))
            print(f"Cliente TCP del {self.servicio} conectado a {host} : {port}")
            
            c.send(self.mensaje.encode('utf-8'))
            print(f"Mensaje enviado: {self.mensaje}\n")
            c.close()
            
    def recibir_por_TCP(self, host, port):    
        with socket(AF_INET, SOCK_STREAM) as c:
            c.connect((host, port))
            print(f"Cliente TCP del {self.servicio} conectado a {host} : {port}")
            
            self.mensaje = c.recv(1024).decode('utf-8')
            print(f"Mensaje recibido: {self.mensaje}\n")
            c.close()
    
    def recibir_por_UDP(self, host, port):    
        with socket(AF_INET, SOCK_DGRAM) as c:
            c.connect(host, port)
            print(f"Cliente TCP del {self.servicio} conectado a {host} : {port}")
            
            self.mensaje =  c.recvfrom(1024)
            print(f"Mensaje recibido: {self.mensaje}\n")
            c.close()

    def recibir_por_HTTP(self, host,port):
        with socket(AF_INET, SOCK_STREAM) as c:
            c.connect((host, port))
            print(f"Cliente TCP del {self.servicio} conectado a {host} : {port}")
            
            self.mensaje = c.recv(1024).decode('utf-8')
            print(f"Mensaje recibido: {self.mensaje}\n")
            c.close()
            
    def get_mensaje(self):
        return self.mensaje