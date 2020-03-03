import socket
import RF24
import RPi.GPIO as GPIO
import time 

#Set up wifi stuff
IPADDRESS = '192.168.1.65'
print("Starting our server")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((IPADDRESS,5005))
s.listen(1)
conn, addr = s.accept()

#Set up transceiver stuff
radio = RF24.RF24(25, 0)
pipe = bytes("1Node","ASCII")
radio.begin()
radio.setRetries(5,15)
#Set up as transmitter
radio.openWritingPipe(pipe)

while 1: 
    try:
        #Receive from laptop
        data = conn.recv(1024)
        received = data.decode('utf-8')
        print(received)
        if not data:
            break
        #Send to arduino nano
        output = bytes(received, "ASCII")
        radio.write(output)
    except: 
        print("\nError")
        break
    
conn.close()

