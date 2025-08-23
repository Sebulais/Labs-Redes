import socket
HOST = "127.0.0.1"  
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
        
    while True:
        # Conexion Cliente 1 TCP
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024).decode('utf-8')
            print(f"{data}")
            message = data
        
            conn.sendall("Mensaje recibido".encode('utf-8'))
            conn.close()
            
        # Conexion Cliente 2 TCP
        conn, addr = s.accept()    
        with conn:
            print(f"Conectado por {addr} | conn {conn} \n")
            conn.sendall(message.encode('utf-8'))
            print("Mensaje enviado")
            conn.close()
            
        if data == "Close":
            break
    
    print("Servidor cerrado")
    s.close()