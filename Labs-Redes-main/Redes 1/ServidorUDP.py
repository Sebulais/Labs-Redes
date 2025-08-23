import socket

HOST = "127.0.0.1"  
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    
    print(f"Servidor UDP {HOST}:{PORT}")
    print("Esperando conexión...\n")
    
    while True:
        # Conexion Cliente 2 UDP
        data, addr = s.recvfrom(1024)
        print(f"Connected by {addr}")
        print(f"Cliente {addr} dice: {data.decode('utf-8')}")
        
        # Conexion Cliente 3 HTTP
        conf, n_addr = s.recvfrom(1024)
        print(f"Connected by {n_addr}")
        s.sendto(data,n_addr)
        
        if data.decode('utf-8') == "Close":
            break
    
    print("Servidor cerrado")
    s.close()
