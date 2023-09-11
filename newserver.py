import socket
ADDRESS = socket.gethostbyname(socket.gethostname()) 
PORT = 8000
ADDR = (ADDRESS , PORT) 
HEADER = 64

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 
server.bind(ADDR) 

server.listen(5) 

while(True):
    print("server is waiting for connection") 
    conn , addr = server.accept()
    print(f"Client is connected {conn} ") 
    while(True):
        data = conn.recv(HEADER).decode('utf-8') 
        if data:
            print(data)
        else:
            break; 
        try:
            conn.send("hey client".encode('utf_8'))  
        except Exception as e:
            print(e) 
    conn.close()


