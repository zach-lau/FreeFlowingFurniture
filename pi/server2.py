#!/usr/bin/python3
import sys
sys.path.insert(1, '../common')
from motorcommands import *
import socket
import RF24
import RPi.GPIO as GPIO
import time
import struct

# User libraries 
from controller import *

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
con = controller(conn, radio)

con.run()
print("Shutting down server")
s.close()
conn.close()
