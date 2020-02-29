import socket
print("Starting our server")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('192.168.1.64',5004))
s.listen(1)
conn, addr = s.accept()
while 1: 
    data = conn.recv(1024)
    print(data.decode('utf-8'))
    if not data:
        break
conn.close()

