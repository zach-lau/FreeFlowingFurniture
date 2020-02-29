import socket 


print("Staring our server...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.67',50000)) 
#binds to this computer on a 50000 port
s.listen(1) #Eanable the server to accept new connections
conn, addr = s.accept() 
#connn -> new socket object to send and receive data on the connection
#adress -> address bound to the socket on the other end? 
while 1: 
	data = conn.recv(1024)
	if not data:
		break
	conn.sendall(data)
conn.close()
