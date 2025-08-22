import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import json

HOST = "127.0.0.1"  
PORT = 8000

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
        
        partes = formatted_message.split('-', 3)
            
        timestamp, largo_minimo_str, largo_actual_str, mensaje = partes
        
        largo_minimo = int(largo_minimo_str)
        largo_actual = int(largo_actual_str)
        
        if largo_actual >= largo_minimo:
            with open("mensajes.txt", "a") as archivo:
                archivo.write(f"{timestamp}-{mensaje}\n")
        else:
            palabra = input("Ingresa una palabra para agregar al mensaje: ")
            mensaje_completo = mensaje + " " + palabra
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_tcp:
                cliente_tcp.connect(("127.0.0.1", 65432))
                cliente_tcp.sendall(mensaje_completo.encode('utf-8'))
                cliente_tcp.close()

server = HTTPServer((HOST, PORT), ServidorHTTP)
print("Servidor iniciado... ")

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
    print("Servidor finalizado")
