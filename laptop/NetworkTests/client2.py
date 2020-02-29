import socket
SERVER_ADDRESS = "192.168.1.65"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_ADDRESS, 5005))
line = input()
while line:
	s.sendall(bytes(line, 'utf-8'))
	line = str(input())
s.close()
print("Closing client");
