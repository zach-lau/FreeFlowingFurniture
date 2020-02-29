import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.13.152.108', 50000))
s.sendall("Hello world")
data = s.recv(1024)
print("Received %s", data)
