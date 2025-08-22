import socket
import datetime
import json


HOST = "127.0.0.1"  
PORT = 8000

message_data = {
        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
        'min_length': 20, # Faltaría alterar esto para recibirlo del mensaje anterior
        'current_length': 15,
        'message': "Hola mundo ejemplo"
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    formatted_message = f"{message_data['timestamp']}-{message_data['min_length']}-{message_data['current_length']}-{message_data['message']}"
    
    json_data = {
        "message": formatted_message
    }
    http_request = f"POST / HTTP/1.1\r\nHost: {HOST}:{PORT}\r\nContent-Length: {len(json.dumps(json_data))}\r\n\r\n"
    http_request += json.dumps(json_data)
    
    s.sendall(http_request.encode('utf-8'))
    
    print(f"Mensaje enviado a servicio 4: {formatted_message}")
