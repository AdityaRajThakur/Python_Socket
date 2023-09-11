from pydoc import cli
import socket 

ADDRESS =  socket.gethostbyname(socket.gethostname()) 
PORT = 8000 
HEADER = 64 
FORMATE = 'utf-8' 
ADDR = (ADDRESS ,PORT) 
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 
client.connect(ADDR)

client.send("hello server".encode('utf-8')) 
try:
    data = client.recv(HEADER) 
    print(bytes(data).decode('utf-8'))
except Exception as e : 
    print(e)

count = 0  
while(True):
    if count==5:
        break;
    str = input("enter sms").encode('utf-8')
    count+=1 
    client.send(str) 
    
client.close()