import socket

IPADDRESS = '192.168.1.65'
print("Starting our server")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((IPADDRESS,5005))
s.listen(1)
conn, addr = s.accept()
while 1: 
    data = conn.recv(1024)
    print(data.decode('utf-8'))
    if not data:
        break
conn.close()

