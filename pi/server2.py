#!/usr/bin/python3
import sys
sys.path.insert(1, '../common')
from motorcommands import *
import socket
import RF24
import RPi.GPIO as GPIO
import time
import struct

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
        data = conn.recv(32)
        #print(data)
        try:
            received = struct.unpack("!BBBBBB",data)
            print(received)
            if not data:
                break
        except:
            print("Couldn't parse data")
            break
        try:
            #Send to arduino nano
            #output = bytes(received, "ASCII")
            output = []
            for i in range(1,6):
                output.append(received[i])
            radio.write(bytes(output))
            print(output)
        except:
            print("Couldn't send to nano")
    except:
        print("\nError")
        break

s.close()
conn.close()
