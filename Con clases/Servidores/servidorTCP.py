from socket import *

class ServidorTCP:
    def __init__(self, _host, _port, _servicio):
        self.host = _host
        self.port = _port
        self.servicio = _servicio
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        
        with self.server_socket as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Servidor TCP del {self.servicio} ({self.host}:{self.port})")
            print("Esperando conexión...\n")
    
    def recibir_mensaje_cliente(self):
        conn, addr = self.server_socket.accept()
        
        print(f"Conectado por {addr} | conn {conn} \n")
        self.mensaje = conn.recv(1024).decode()
        print(f"Mensaje recibido: {self.mensaje}\n")
        
        conn.close()
    
    def enviar_mensaje_cliente(self):
        conn, addr = self.server_socket.accept()
        with conn:
            print(f"Conectado por {addr} | conn {conn} \n")
            conn.sendall(self.mensaje.encode())
            print("Mensaje enviado")
            conn.close()
            
    def get_mensaje(self):
        print(self.mensaje)
        
    def cerrar_servidor():
        self.server_socket.close()
