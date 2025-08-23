import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import json

HOST = "127.0.0.1"  
PORT = 8000

HOST_c = "127.0.0.1"
PORT_c = 5000

class ServidorHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Servidor HTTP funcionando", 'utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length == 0:
            self.send_response(400)
            self.end_headers()
            return
            
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        try:
            json_data = json.loads(post_data)
            formatted_message = json_data['message']
        except:
            formatted_message = post_data
        
        if(formatted_message == "Close"):
            print("Cerrando servidor http...")
            mensaje = "Terminar"
            self.server.shutdown()
            #Contactamos mensaje = terminar
            
        else:
            timestamp = formatted_message.split("]-[")[0][1:]
            largo_minimo_str = formatted_message.split("]-[")[1]
            largo_actual_str = formatted_message.split("]-[")[2]
            mensaje = formatted_message.split("]-[")[-1][:-1]
            
            largo_minimo = int(largo_minimo_str)
            largo_actual = int(largo_actual_str)
            flag = False
            if largo_actual >= largo_minimo:
                # Finalizar
                with open("mensajes.txt", "a") as archivo:
                    archivo.write(f"{timestamp}-{mensaje}\n")
                    archivo.close()
                    mensaje = "Close"
                    flag = True
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((HOST_c, PORT_c))
                s.listen(1)
                conn, addr = s.accept()  # bloquea hasta que el cliente se conecte
                with conn:
                    print(f"Cliente TCP conectado desde {addr}")
                    conn.sendall(mensaje.encode('utf-8'))
                    print(f"Mensaje enviado al cliente TCP: {mensaje}")
        
        if flag:
            self.server.shutdown()
            server.server_close()


server = HTTPServer((HOST, PORT), ServidorHTTP)
print("Servidor iniciado... ")

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

finally:
    server.server_close()
    print("Servidor finalizado")