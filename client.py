import socket


HEADER = 64
PORT  = 8000
# SERVER = "192.168.56.1"
SERVER  = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER , PORT) 
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECTED'
client= socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT) 
    msg_length  = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length +=b' ' * (HEADER - len(send_length)) 
    client.send(send_length)
    client.send(message) 

while(True):
    st = str(input("textME : ")) 
    if st=="yes":
        break
    send(st) 