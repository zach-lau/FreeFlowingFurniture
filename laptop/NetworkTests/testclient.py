import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.67', 5005))
s.sendall("Hello, world")
data = s.recv(1024) #receives 1024 bytes
s.close()
print("Received %s" % data)