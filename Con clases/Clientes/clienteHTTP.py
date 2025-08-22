from socket import *

class ClienteHTTP:
    
    def __init__(self, servicio):
        self.servicio = servicio
        
    def actualizar_mensaje(self, _mensaje, _largo_final):
        a = input("Ingrese nueva palabra: ")
        current_dt = datetime.now()
        self.mensaje = str(f"[{current_dt}]-[{_largo_final}]-[{len(_mensaje+a)}]-[{_mensaje+a}]")
        
    
    #def enviar_por_HTTP(self, host, port):
            
    def recibir_por_UDP(self, host, port):    
        with socket(AF_INET, SOCK_STREAM) as c:
            c.connect(host, port)
            print(f"Cliente HTTP del {self.servicio} conectado a {host} : {port}")
            
            self.mensaje =  c.recvfrom(host, port)
            print(f"Mensaje recibido: {self.mensaje}\n")
            c.close()
