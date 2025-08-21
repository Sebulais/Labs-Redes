import socket

HOST = "127.0.0.1"  
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("Servido UDP conectado a localhost")
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Connected by {addr}")
        print(f"Cliente {addr} dice: {data.decode()}")

        s.sendto(f"Mensaje recibido".encode(), addr)