import socket
print("Starting our server")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('192.168.1.67',5005))
s.listen(1)
conn, addr = s.accept()
while 1: 
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(bytes("Hello from the raspberry pi", 'utf-8'))
conn.close()
