import socket			 

s = socket.socket()		 
port = 12345				

# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

def receive():
    return s.recv(1024).decode();

def send(msg):
    s.send(msg.encode())

while True:
    print(receive())
    string = input()
    send(string)
    if string == "/exit":
        break

s.close()

