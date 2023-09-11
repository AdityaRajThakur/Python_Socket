import socket
import threading
HEADER = 64
PORT  = 8000
# SERVER = "47.247.209.253"
SERVER  = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER , PORT) 
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECTED'
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
server.bind(ADDR) 


def connectClient(conn , addr):
    print(f"[NEW CONNECTION] {addr} connected. ") 
    connected = True 
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"[{addr}] {msg}")
            if msg==DISCONNECT_MSG:
                connected = False 
    print("Your are [DISCONNECTED] ")  
    conn.close()    


def start():
    server.listen()
    print(f"[Listening] on {SERVER}")
    while(True):
        conn , addr =server.accept()
        thread = threading.Thread(target = connectClient,args = (conn ,addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count() - 1 }")
print(f"server has started ") 
start()