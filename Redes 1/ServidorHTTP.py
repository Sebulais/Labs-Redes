import socket
import datetime
import json

HOST = "127.0.0.1"  
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Servicio 4 escuchando en {HOST}:{PORT} ...')
    
    while True:    
        client_connection, client_address = s.accept()
        request = client_connection.recv(4096).decode('utf-8')
        
        json_start = request.find('{')
        json_str = request[json_start:]
        json_data = json.loads(json_str)
        print("JSON extraído:", json_data)
        
        client_connection.close()
