import socket

HOST = "127.0.0.1" 
PORT = 65432 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024).decode()

print(f"Received {data!r}")


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(data.encode(), ("127.0.0.1", 65432))
    data, addr = s.recvfrom(1024)
    print(f"Servidor: {data.decode()}")

    s.close()