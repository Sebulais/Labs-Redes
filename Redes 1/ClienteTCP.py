import socket
from datetime import datetime

HOST = "127.0.0.1" 
PORT = 65432

largo_final = input("Ingresa el largo mínimo del mensaje final: ")
mensaje = input("Mensaje: ")
current_dt = datetime.now()

final = str(f"[{current_dt}]-[{largo_final}]-[{len(mensaje)}]-[{mensaje}]")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(final.encode())
    data = s.recv(1024).decode()

print(f"Received {data!r}")