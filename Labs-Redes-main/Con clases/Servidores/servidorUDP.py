from socket import *

class ServidorUDP:
    def __init__(self, _host, _port, _servicio):
        self.host = _host
        self.port = _port
        self.servicio = _servicio
        self.server_socket = socket(AF_INET, SOCK_DGRAM)
        
        with self.server_socket as s:
            s.bind((self.host, self.port))
            
            print(f"Servidor UDP {self.host}:{self.port}")
            print("Esperando conexión...\n")
    
    def recibir_mensaje_cliente(self):
        self.mensaje, addr = self.server_socket.recvfrom(1024)
        self.mensaje = self.mensaje.decode()
        print(f"Mensaje recibido de {addr}: {self.mensaje}")
    
    def enviar_mensaje_cliente(self, dir_cliente):
        self.server_socket.sendto(1024, dir_cliente)
        print(f"Mensaje enviado: {self.mensaje}")
    
    def get_mensaje(self):
        print(self.mensaje)
        
    def cerrar_servidor(self):
        self.server_socket.close()